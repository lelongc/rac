import os
import hashlib

def get_hash(path):
    if not os.path.exists(path):
        return None
    with open(path, "rb") as f:
        return hashlib.md5(f.read()).hexdigest()

print("Checking q1.png across tests:")
for t in range(1, 11):
    p = f"web/assets/images/test{t}/q1.png" if t > 1 else "web/assets/images/q1.png"
    p2 = f"web/assets/images/test{t}/q1.png"
    h = get_hash(p)
    h2 = get_hash(p2) if t == 1 else h
    size = os.path.getsize(p) if os.path.exists(p) else 0
    print(f"Test {t:2d}: size={size:7d}, md5={h}")
