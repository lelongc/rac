import re
import os
import subprocess
import json
from faster_whisper import WhisperModel

NUM_WORDS = {
    "one": 1, "two": 2, "three": 3, "four": 4, "five": 5, "six": 6, "seven": 7, "eight": 8, "nine": 9, "ten": 10,
    "eleven": 11, "twelve": 12, "thirteen": 13, "fourteen": 14, "fifteen": 15, "sixteen": 16, "seventeen": 17,
    "eighteen": 18, "nineteen": 19, "twenty": 20, "twenty-one": 21, "twenty-two": 22, "twenty-three": 23,
    "twenty-four": 24, "twenty-five": 25, "twenty-six": 26, "twenty-seven": 27, "twenty-eight": 28,
    "twenty-nine": 29, "thirty": 30, "thirty-one": 31
}

def parse_number_timestamps(segs, expected_start, expected_end):
    # Returns list of (qid, timestamp)
    found = {}
    for s in segs:
        t = s["text"].lower()
        st = s["start"]
        
        # Check digit
        m = re.search(r'\bnumber\s+(\d+)\b', t)
        if m:
            num = int(m.group(1))
            if expected_start <= num <= expected_end and num not in found:
                found[num] = st
                continue
                
        # Check word
        for word, val in NUM_WORDS.items():
            if expected_start <= val <= expected_end and val not in found:
                if f"number {word}" in t:
                    found[val] = st
                    break
                    
    # Interpolate any missing
    timestamps = []
    last_t = 0.0
    for q in range(expected_start, expected_end + 1):
        if q in found:
            timestamps.append((q, found[q]))
            last_t = found[q]
        else:
            # find next known
            next_known = None
            for nq in range(q + 1, expected_end + 1):
                if nq in found:
                    next_known = (nq, found[nq])
                    break
            if next_known:
                steps = next_known[0] - (q - 1)
                est_t = last_t + (next_known[1] - last_t) / steps
                timestamps.append((q, round(est_t, 2)))
                last_t = est_t
            else:
                est_t = last_t + 20.0
                timestamps.append((q, round(est_t, 2)))
                last_t = est_t
    return timestamps

def parse_triplet_timestamps(segs, start_q, end_q):
    # triplets: (32, 34), (35, 37), etc.
    expected = []
    for q in range(start_q, end_q + 1, 3):
        expected.append((q, q + 2))
        
    found = {}
    pattern = re.compile(r'Question[s]?\s+(\d+)\s+(?:through|to|-)\s+(\d+)', re.IGNORECASE)
    
    for s in segs:
        t = s["text"]
        m = pattern.search(t)
        if m:
            q_s = int(m.group(1))
            for exp_s, exp_e in expected:
                if exp_s == q_s and (exp_s, exp_e) not in found:
                    found[(exp_s, exp_e)] = s["start"]
                    break
        elif "refer to the following" in t.lower():
            # sometimes whisper transcribes 'refer to the following conversation' without question numbers
            for exp_s, exp_e in expected:
                if (exp_s, exp_e) not in found:
                    found[(exp_s, exp_e)] = s["start"]
                    break
                    
    # Fill any missing
    res = []
    last_t = 30.0
    for exp in expected:
        if exp in found:
            res.append((exp[0], exp[1], found[exp]))
            last_t = found[exp]
        else:
            next_known = None
            for nexp in expected[expected.index(exp) + 1:]:
                if nexp in found:
                    next_known = (nexp, found[nexp])
                    break
            if next_known:
                idx_diff = expected.index(next_known[0]) - expected.index(exp) + 1
                est_t = last_t + (next_known[1] - last_t) / idx_diff
                res.append((exp[0], exp[1], round(est_t, 2)))
                last_t = est_t
            else:
                est_t = last_t + 80.0
                res.append((exp[0], exp[1], round(est_t, 2)))
                last_t = est_t
    return res

print("Parser functions defined.")
