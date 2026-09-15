import json
import re

ALL_ANS = json.load(open("all_tests_answers.json", encoding="utf-8"))["test2"]

# Load transcribed audio segments
with open("scratch/t2_p3_segments.json", "r", encoding="utf-8") as f:
    p3_segs = json.load(f)
with open("scratch/t2_p4_segments.json", "r", encoding="utf-8") as f:
    p4_segs = json.load(f)

p3_ranges = [
    (32, 34, 33.12, 65.24),
    (35, 37, 102.20, 137.96),
    (38, 40, 166.88, 211.72),
    (41, 43, 242.32, 292.92),
    (44, 46, 331.12, 378.12),
    (47, 49, 419.12, 467.12),
    (50, 52, 505.12, 552.12),
    (53, 55, 591.12, 635.12),
    (56, 58, 677.12, 723.12),
    (59, 61, 760.12, 796.12),
    (62, 64, 833.12, 870.12),
    (65, 67, 921.12, 966.12),
    (68, 70, 1014.12, 1050.12),
]

p4_ranges = [
    (71, 73, 34.04, 64.32),
    (74, 76, 102.76, 144.64),
    (77, 79, 183.44, 223.96),
    (80, 82, 262.52, 304.76),
    (83, 85, 350.20, 386.96),
    (86, 88, 426.04, 469.64),
    (89, 91, 510.60, 546.72),
    (92, 94, 584.64, 637.36),
    (95, 97, 681.12, 724.16),
    (98, 100, 771.44, 817.04),
]

p3_passages = {}
for q1, q2, s, e in p3_ranges:
    words = [seg['text'].strip() for seg in p3_segs if s <= seg['start'] < e and not seg['text'].startswith('Questions') and not seg['text'].startswith('Question') and not seg['text'].startswith('Number')]
    p3_passages[(q1, q2)] = " ".join(words)

p4_passages = {}
for q1, q2, s, e in p4_ranges:
    words = [seg['text'].strip() for seg in p4_segs if s <= seg['start'] < e and not seg['text'].startswith('Questions') and not seg['text'].startswith('Question') and not seg['text'].startswith('Number')]
    p4_passages[(q1, q2)] = " ".join(words)

# Parse OCR question text
all_text = ""
for p in range(6, 13):
    with open(f"scratch/t2_lc_clean_p{p}.txt", "r", encoding="utf-8") as f:
        all_text += "\n" + f.read()

cleaned_lines = []
for line in all_text.splitlines():
    l = line.strip()
    if not l: continue
    if l.startswith("===") or "PART 3" in l or "PART 4" in l or "Directions:" in l:
        continue
    if "You will hear" in l or "Select the best" in l or "answer sheet" in l or "not be printed" in l:
        continue
    if "GO ON TO" in l or "TEST 2" in l:
        continue
    # fix merged 'do 90.'
    if "do 90." in l:
        cleaned_lines.append(l.replace("do 90.", "\n90."))
        continue
    cleaned_lines.append(l)

clean_blob = "\n".join(cleaned_lines)
q_blocks = re.split(r"\n(?=\d{1,3}\.\s+)", "\n" + clean_blob)

parsed_qs = {}
for block in q_blocks:
    block = block.strip()
    if not block: continue
    m = re.match(r"^(\d{1,3})\.\s+(.*?)(?=\([ABCD]\))", block, re.DOTALL)
    if not m:
        continue
    qid = int(m.group(1))
    stem = " ".join(m.group(2).split())
    opts = {}
    opt_matches = list(re.finditer(r"\(([ABCD])\)\s*([^(\n\r]+(?:\n(?!\([ABCD]\)|\d{1,3}\.)[^\n\r]+)*)", block))
    for om in opt_matches:
        ltr = om.group(1)
        otxt = " ".join(om.group(2).split())
        opts[ltr] = otxt
    if len(opts) == 4:
        parsed_qs[qid] = {"stem": stem, "options": opts}

# Manual overrides for Q69 and Q90
parsed_qs[69] = {
    "stem": "Look at the graphic. How much will the man save on his purchase?",
    "options": {
        "A": "5%",
        "B": "3%",
        "C": "7%",
        "D": "2%"
    }
}
parsed_qs[90] = {
    "stem": "What special feature does the speaker emphasize?",
    "options": {
        "A": "It is durable.",
        "B": "It is adjustable.",
        "C": "It is easy to assemble.",
        "D": "It is available in many colors."
    }
}

print(f"Total parsed Qs: {len(parsed_qs)} (target 69: Q32 to Q100)")
for qid in range(32, 101):
    if qid not in parsed_qs:
        print(f"STILL MISSING: Q{qid}")

with open("scratch/t2_p3_p4_parsed.json", "w", encoding="utf-8") as f:
    json.dump(parsed_qs, f, ensure_ascii=False, indent=2)
