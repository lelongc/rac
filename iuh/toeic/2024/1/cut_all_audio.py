# cut_all_audio.py: Cut audio for all questions in Part 1, 2, 3, 4 and update test1.json
import json
import os
import subprocess

os.makedirs("web/assets/audio/cuts", exist_ok=True)

def cut_clip(src, start, end, dest):
    dur = max(1.0, end - start)
    cmd = [
        "ffmpeg", "-y",
        "-ss", f"{start:.2f}",
        "-t", f"{dur:.2f}",
        "-i", src,
        "-c:a", "libmp3lame",
        "-b:a", "128k",
        dest
    ]
    subprocess.run(cmd, capture_output=True)

# 1. Part 1
PART1_MAP = {
    1: (5.7, 27.0),
    2: (31.0, 54.0),
    3: (64.0, 87.0),
    4: (87.4, 116.5),
    5: (117.4, 147.0),
    6: (147.4, 172.5)
}

# 2. Part 2
PART2_MAP = {
    7: (23.0, 47.0),
    8: (47.0, 67.0),
    9: (67.0, 85.0),
    10: (85.0, 105.0),
    11: (105.0, 129.0),
    12: (129.0, 150.0),
    13: (150.0, 171.0),
    14: (171.0, 192.0),
    15: (192.0, 213.0),
    16: (213.0, 226.0),
    17: (226.0, 251.0),
    18: (251.0, 267.0),
    19: (267.0, 291.0),
    20: (291.0, 309.0),
    21: (309.0, 328.0),
    22: (328.0, 351.0),
    23: (351.0, 372.0),
    24: (372.0, 392.0),
    25: (392.0, 414.0),
    26: (414.0, 435.0),
    27: (435.0, 453.0),
    28: (453.0, 477.0),
    29: (477.0, 499.0),
    30: (499.0, 520.0),
    31: (520.0, 536.0)
}

# 3. Part 3
PART3_MAP = [
    (32, 34, 34.6, 109.4),
    (35, 37, 109.4, 190.4),
    (38, 40, 190.4, 261.4),
    (41, 43, 261.4, 352.4),
    (44, 46, 352.4, 430.4),
    (47, 49, 430.4, 516.4),
    (50, 52, 516.4, 593.4),
    (53, 55, 593.4, 673.4),
    (56, 58, 673.4, 751.4),
    (59, 61, 751.4, 827.4),
    (62, 64, 827.4, 926.4),
    (65, 67, 926.4, 1013.4),
    (68, 70, 1013.4, 1105.8)
]

# 4. Part 4
PART4_MAP = [
    (71, 73, 35.0, 113.0),
    (74, 76, 113.0, 199.0),
    (77, 79, 199.0, 279.0),
    (80, 82, 279.0, 359.0),
    (83, 85, 359.0, 435.0),
    (86, 88, 435.0, 519.0),
    (89, 91, 519.0, 586.0),
    (92, 94, 586.0, 673.0),
    (95, 97, 673.0, 757.0),
    (98, 100, 757.0, 836.2)
]

print("Cutting Part 1 clips...")
for q, (st, en) in PART1_MAP.items():
    cut_clip("web/assets/audio/part1.mp3", st, en, f"web/assets/audio/cuts/q{q}.mp3")

print("Cutting Part 2 clips...")
for q, (st, en) in PART2_MAP.items():
    cut_clip("web/assets/audio/part2.mp3", st, en, f"web/assets/audio/cuts/q{q}.mp3")

print("Cutting Part 3 clips...")
for q_st, q_en, st, en in PART3_MAP:
    clip_name = f"q{q_st}_{q_en}.mp3"
    cut_clip("web/assets/audio/part3.mp3", st, en, f"web/assets/audio/cuts/{clip_name}")

print("Cutting Part 4 clips...")
for q_st, q_en, st, en in PART4_MAP:
    clip_name = f"q{q_st}_{q_en}.mp3"
    cut_clip("web/assets/audio/part4.mp3", st, en, f"web/assets/audio/cuts/{clip_name}")

print("All audio clips cut successfully!")

# Update test1.json
with open("web/data/test1.json", "r", encoding="utf-8") as f:
    data = json.load(f)

for q in data["questions"]:
    qid = q["id"]
    if qid in PART1_MAP:
        q["audioClip"] = f"assets/audio/cuts/q{qid}.mp3"
        q["audioLabel"] = f"Nghe câu {qid}"
    elif qid in PART2_MAP:
        q["audioClip"] = f"assets/audio/cuts/q{qid}.mp3"
        q["audioLabel"] = f"Nghe câu {qid}"
    else:
        for q_st, q_en, st, en in PART3_MAP:
            if q_st <= qid <= q_en:
                q["audioClip"] = f"assets/audio/cuts/q{q_st}_{q_en}.mp3"
                q["audioLabel"] = f"Nghe bài hội thoại (Câu {q_st} - {q_en})"
                break
        for q_st, q_en, st, en in PART4_MAP:
            if q_st <= qid <= q_en:
                q["audioClip"] = f"assets/audio/cuts/q{q_st}_{q_en}.mp3"
                q["audioLabel"] = f"Nghe bài nói (Câu {q_st} - {q_en})"
                break

with open("web/data/test1.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print("Updated web/data/test1.json with individual question audio clips!")
