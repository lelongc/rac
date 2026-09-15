# build_audio_cuts.py: Parse segments and cut individual question MP3s using ffmpeg
import json
import os
import re
import subprocess

os.makedirs("web/assets/audio/cuts", exist_ok=True)

# Cut helper
def cut_audio(src, start, end, dest):
    dur = max(1.0, end - start)
    cmd = [
        "ffmpeg", "-y",
        "-ss", str(start),
        "-t", str(dur),
        "-i", src,
        "-c:a", "libmp3lame",
        "-b:a", "128k",
        dest
    ]
    subprocess.run(cmd, capture_output=True)

# Part 1 predefined precise timestamps
PART1_TIMESTAMPS = {
    1: (5.7, 27.0),
    2: (31.0, 54.0),
    3: (64.0, 87.0),
    4: (87.4, 116.5),
    5: (117.4, 147.0),
    6: (147.4, 172.5)
}

def process_part1():
    print("Cutting Part 1 audio...")
    for q_id, (st, en) in PART1_TIMESTAMPS.items():
        out_file = f"web/assets/audio/cuts/q{q_id}.mp3"
        cut_audio("web/assets/audio/part1.mp3", st, en, out_file)
        print(f"  Q{q_id}: {st} -> {en} -> {out_file}")

if __name__ == "__main__":
    process_part1()
