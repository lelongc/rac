import os

base = r"d:\folder\rac\iuh\toeic\2024\1\web\assets\images"
print("Root images dir files:", [f for f in os.listdir(base) if os.path.isfile(os.path.join(base, f))])

for t in range(1, 11):
    tdir = os.path.join(base, f"test{t}")
    if os.path.exists(tdir):
        files = os.listdir(tdir)
        q_imgs = [f for f in files if f.startswith("q")]
        lc_imgs = [f for f in files if f.startswith("lc")]
        rc_imgs = [f for f in files if f.startswith("rc")]
        print(f"test{t}: {len(q_imgs)} q-images, {len(lc_imgs)} lc-images ({lc_imgs}), {len(rc_imgs)} rc-images")
    else:
        print(f"test{t}: NOT FOUND")
