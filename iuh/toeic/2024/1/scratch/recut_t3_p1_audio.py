import subprocess, os

p1_src = "web/assets/audio/test3/part1.mp3"
dest_dir = "web/assets/audio/test3/cuts"

cuts = [
    (1, 4.0, 26.0),
    (2, 26.0, 58.0),
    (3, 58.0, 84.0),
    (4, 84.0, 108.5),
    (5, 108.5, 136.0),
    (6, 136.0, 165.2)
]

for qid, st, et in cuts:
    dest_path = os.path.join(dest_dir, f"q{qid}.mp3")
    dur = et - st
    cmd = [
        "ffmpeg", "-y", "-ss", str(st), "-i", p1_src,
        "-t", str(dur), "-c:a", "libmp3lame", "-b:a", "128k", dest_path
    ]
    subprocess.run(cmd, check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    print(f"Cut Q{qid}: {st:.1f}s -> {et:.1f}s ({dur:.1f}s) -> {dest_path}")
