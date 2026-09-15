import os
import subprocess

BASE_DIR = r"d:\folder\rac\iuh\toeic\2024\1"
SRC_AUDIO_DIR = os.path.join(BASE_DIR, "web", "assets", "audio", "test2")
DEST_AUDIO_DIR = os.path.join(SRC_AUDIO_DIR, "cuts")
os.makedirs(DEST_AUDIO_DIR, exist_ok=True)

cuts_p1 = [
    (1, 3.0, 25.0),
    (2, 25.0, 63.0),
    (3, 63.0, 90.0),
    (4, 90.0, 113.0),
    (5, 113.0, 143.0),
    (6, 143.0, 168.8),
]

cuts_p2 = [
    (7, 25.0, 50.0),
    (8, 50.0, 69.0),
    (9, 69.0, 84.0),
    (10, 84.0, 103.0),
    (11, 103.0, 127.0),
    (12, 127.0, 141.0),
    (13, 141.0, 159.0),
    (14, 159.0, 190.0),
    (15, 190.0, 211.0),
    (16, 211.0, 226.0),
    (17, 226.0, 242.0),
    (18, 242.0, 272.0),
    (19, 272.0, 293.0),
    (20, 293.0, 308.0),
    (21, 308.0, 326.0),
    (22, 326.0, 353.0),
    (23, 353.0, 372.0),
    (24, 372.0, 392.0),
    (25, 392.0, 414.0),
    (26, 414.0, 434.0),
    (27, 434.0, 454.0),
    (28, 454.0, 474.0),
    (29, 474.0, 495.0),
    (30, 495.0, 517.0),
    (31, 517.0, 534.1),
]

cuts_p3 = [
    ("q32_34.mp3", 33.12, 102.20),
    ("q35_37.mp3", 102.20, 166.88),
    ("q38_40.mp3", 166.88, 242.32),
    ("q41_43.mp3", 242.32, 331.12),
    ("q44_46.mp3", 331.12, 419.12),
    ("q47_49.mp3", 419.12, 505.12),
    ("q50_52.mp3", 505.12, 591.12),
    ("q53_55.mp3", 591.12, 677.12),
    ("q56_58.mp3", 677.12, 760.12),
    ("q59_61.mp3", 760.12, 833.12),
    ("q62_64.mp3", 833.12, 921.12),
    ("q65_67.mp3", 921.12, 1014.12),
    ("q68_70.mp3", 1014.12, 1092.00),
]

cuts_p4 = [
    ("q71_73.mp3", 34.04, 102.76),
    ("q74_76.mp3", 102.76, 183.44),
    ("q77_79.mp3", 183.44, 262.52),
    ("q80_82.mp3", 262.52, 350.20),
    ("q83_85.mp3", 350.20, 426.04),
    ("q86_88.mp3", 426.04, 510.60),
    ("q89_91.mp3", 510.60, 584.64),
    ("q92_94.mp3", 584.64, 681.12),
    ("q95_97.mp3", 681.12, 771.44),
    ("q98_100.mp3", 771.44, 862.00),
]

def cut_clip(src, dest, start, end):
    cmd = [
        "ffmpeg", "-y", "-v", "quiet",
        "-ss", str(start),
        "-to", str(end),
        "-i", src,
        "-c:a", "libmp3lame",
        "-b:a", "128k",
        dest
    ]
    subprocess.run(cmd, check=True)

print("Cutting Part 1...")
p1_src = os.path.join(SRC_AUDIO_DIR, "part1.mp3")
for qid, s, e in cuts_p1:
    dest = os.path.join(DEST_AUDIO_DIR, f"q{qid}.mp3")
    cut_clip(p1_src, dest, s, e)
    print(f"Cut q{qid}.mp3 ({s} -> {e})")

print("Cutting Part 2...")
p2_src = os.path.join(SRC_AUDIO_DIR, "part2.mp3")
for qid, s, e in cuts_p2:
    dest = os.path.join(DEST_AUDIO_DIR, f"q{qid}.mp3")
    cut_clip(p2_src, dest, s, e)
    print(f"Cut q{qid}.mp3 ({s} -> {e})")

print("Cutting Part 3...")
p3_src = os.path.join(SRC_AUDIO_DIR, "part3.mp3")
for fname, s, e in cuts_p3:
    dest = os.path.join(DEST_AUDIO_DIR, fname)
    cut_clip(p3_src, dest, s, e)
    print(f"Cut {fname} ({s} -> {e})")

print("Cutting Part 4...")
p4_src = os.path.join(SRC_AUDIO_DIR, "part4.mp3")
for fname, s, e in cuts_p4:
    dest = os.path.join(DEST_AUDIO_DIR, fname)
    cut_clip(p4_src, dest, s, e)
    print(f"Cut {fname} ({s} -> {e})")

print("All Test 2 clips cut successfully!")
