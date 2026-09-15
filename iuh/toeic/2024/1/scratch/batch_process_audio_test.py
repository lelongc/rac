import os
import sys
BASE_DIR = r"d:\folder\rac\iuh\toeic\2024\1"
if BASE_DIR not in sys.path:
    sys.path.insert(0, BASE_DIR)

import json
import subprocess
from faster_whisper import WhisperModel
from scratch.audio_slice_helper import parse_number_timestamps, parse_triplet_timestamps

BASE_DIR = r"d:\folder\rac\iuh\toeic\2024\1"

def cut_clip(src, dest, start, end):
    start = max(0.0, float(start))
    end = float(end)
    if end <= start + 2.0:
        start = max(0.0, end - 60.0)
    cmd = [
        "ffmpeg", "-y", "-v", "quiet",
        "-ss", f"{start:.2f}",
        "-to", f"{end:.2f}",
        "-i", src,
        "-c:a", "libmp3lame",
        "-b:a", "128k",
        dest
    ]
    subprocess.run(cmd, check=True)

def process_test(test_id, model):
    print(f"\n==========================================")
    print(f"   PROCESSING AUDIO FOR TEST {test_id}    ")
    print(f"==========================================")
    
    src_dir = os.path.join(BASE_DIR, "web", "assets", "audio", f"test{test_id}")
    dest_dir = os.path.join(src_dir, "cuts")
    os.makedirs(dest_dir, exist_ok=True)
    
    # --- PART 1 ---
    print(f"Test {test_id}: Transcribing Part 1...", flush=True)
    p1_src = os.path.join(src_dir, "part1.mp3")
    s1, _ = model.transcribe(p1_src, beam_size=1, vad_filter=True)
    segs1 = [{"start": round(s.start, 2), "end": round(s.end, 2), "text": s.text.strip()} for s in s1]
    p1_ts = parse_number_timestamps(segs1, 1, 6)
    
    # Part 1 cuts: from Number X to Number X+1
    p1_total_dur = segs1[-1]["end"] if segs1 else 180.0
    for i in range(len(p1_ts)):
        qid, st = p1_ts[i]
        et = p1_ts[i+1][1] if i+1 < len(p1_ts) else p1_total_dur
        dest_file = os.path.join(dest_dir, f"q{qid}.mp3")
        cut_clip(p1_src, dest_file, max(0.0, st - 1.0), et)
        print(f"  P1 cut q{qid}.mp3 ({st:.2f} -> {et:.2f})", flush=True)

    # --- PART 2 ---
    print(f"Test {test_id}: Transcribing Part 2...", flush=True)
    p2_src = os.path.join(src_dir, "part2.mp3")
    s2, _ = model.transcribe(p2_src, beam_size=1, vad_filter=True)
    segs2 = [{"start": round(s.start, 2), "end": round(s.end, 2), "text": s.text.strip()} for s in s2]
    p2_ts = parse_number_timestamps(segs2, 7, 31)
    
    p2_total_dur = segs2[-1]["end"] if segs2 else 540.0
    for i in range(len(p2_ts)):
        qid, st = p2_ts[i]
        et = p2_ts[i+1][1] if i+1 < len(p2_ts) else p2_total_dur
        dest_file = os.path.join(dest_dir, f"q{qid}.mp3")
        cut_clip(p2_src, dest_file, max(0.0, st - 1.0), et)
        print(f"  P2 cut q{qid}.mp3 ({st:.2f} -> {et:.2f})", flush=True)

    # --- PART 3 ---
    print(f"Test {test_id}: Transcribing Part 3...", flush=True)
    p3_src = os.path.join(src_dir, "part3.mp3")
    s3, _ = model.transcribe(p3_src, beam_size=1, vad_filter=True)
    segs3 = [{"start": round(s.start, 2), "end": round(s.end, 2), "text": s.text.strip()} for s in s3]
    p3_ts = parse_triplet_timestamps(segs3, 32, 70)
    
    p3_total_dur = segs3[-1]["end"] if segs3 else 1100.0
    for i in range(len(p3_ts)):
        qs, qe, st = p3_ts[i]
        et = p3_ts[i+1][2] if i+1 < len(p3_ts) else p3_total_dur
        fname = f"q{qs}_{qe}.mp3"
        dest_file = os.path.join(dest_dir, fname)
        cut_clip(p3_src, dest_file, max(0.0, st - 1.0), et)
        print(f"  P3 cut {fname} ({st:.2f} -> {et:.2f})", flush=True)

    # --- PART 4 ---
    print(f"Test {test_id}: Transcribing Part 4...", flush=True)
    p4_src = os.path.join(src_dir, "part4.mp3")
    s4, _ = model.transcribe(p4_src, beam_size=1, vad_filter=True)
    segs4 = [{"start": round(s.start, 2), "end": round(s.end, 2), "text": s.text.strip()} for s in s4]
    p4_ts = parse_triplet_timestamps(segs4, 71, 100)
    
    p4_total_dur = segs4[-1]["end"] if segs4 else 880.0
    for i in range(len(p4_ts)):
        qs, qe, st = p4_ts[i]
        et = p4_ts[i+1][2] if i+1 < len(p4_ts) else p4_total_dur
        fname = f"q{qs}_{qe}.mp3"
        dest_file = os.path.join(dest_dir, fname)
        cut_clip(p4_src, dest_file, max(0.0, st - 1.0), et)
        print(f"  P4 cut {fname} ({st:.2f} -> {et:.2f})", flush=True)

    # --- UPDATE TEST JSON ---
    json_path = os.path.join(BASE_DIR, "web", "data", f"test{test_id}.json")
    with open(json_path, "r", encoding="utf-8") as f:
        t_data = json.load(f)

    for q in t_data.get("questions", []):
        qid = q["id"]
        if 1 <= qid <= 6:
            q["audioClip"] = f"assets/audio/test{test_id}/cuts/q{qid}.mp3"
            q["audioLabel"] = f"Nghe câu {qid}"
        elif 7 <= qid <= 31:
            q["audioClip"] = f"assets/audio/test{test_id}/cuts/q{qid}.mp3"
            q["audioLabel"] = f"Nghe câu {qid}"
        elif 32 <= qid <= 70:
            # find which triplet
            for qs in range(32, 71, 3):
                qe = qs + 2
                if qs <= qid <= qe:
                    q["audioClip"] = f"assets/audio/test{test_id}/cuts/q{qs}_{qe}.mp3"
                    q["audioLabel"] = f"Nghe bài hội thoại (Câu {qs} - {qe})"
                    break
        elif 71 <= qid <= 100:
            for qs in range(71, 101, 3):
                qe = qs + 2
                if qs <= qid <= qe:
                    q["audioClip"] = f"assets/audio/test{test_id}/cuts/q{qs}_{qe}.mp3"
                    q["audioLabel"] = f"Nghe bài nói (Câu {qs} - {qe})"
                    break

    with open(json_path, "w", encoding="utf-8") as f:
        json.dump(t_data, f, ensure_ascii=False, indent=2)

    print(f"Successfully updated test{test_id}.json with all 100 audio clips!")

if __name__ == "__main__":
    t_id = int(sys.argv[1]) if len(sys.argv) > 1 else 3
    model = WhisperModel('tiny', device='cpu', compute_type='int8', cpu_threads=2)
    process_test(t_id, model)
