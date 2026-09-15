import json
import sys

sys.stdout.reconfigure(encoding='utf-8')

with open("web/data/test1.json", "r", encoding="utf-8") as f:
    t1 = json.load(f)

with open("web/data/test2.json", "r", encoding="utf-8") as f:
    t2 = json.load(f)

print("Test 1 root keys:", list(t1.keys()))
print("Test 2 root keys:", list(t2.keys()))

# Check question keys for each Part in Test 1 vs Test 2
parts = [1, 2, 3, 4, 5, 6, 7]
for p in parts:
    q1 = next((q for q in t1["questions"] if q["part"] == p), None)
    q2 = next((q for q in t2["questions"] if q["part"] == p), None)
    print(f"\n--- PART {p} ---")
    if q1:
        print(f"Test 1 Q{q1['id']} keys: {list(q1.keys())}")
        if "image" in q1 or "pageImage" in q1:
            print(f"  T1 Image fields: image={q1.get('image')}, pageImage={q1.get('pageImage')}")
    if q2:
        print(f"Test 2 Q{q2['id']} keys: {list(q2.keys())}")
        if "image" in q2 or "pageImage" in q2:
            print(f"  T2 Image fields: image={q2.get('image')}, pageImage={q2.get('pageImage')}")

print("\n--- SAMPLE Q1 in T1 vs T2 ---")
print("T1 Q1:", json.dumps(t1["questions"][0], ensure_ascii=False, indent=2)[:400])
print("T2 Q1:", json.dumps(t2["questions"][0], ensure_ascii=False, indent=2)[:400])

print("\n--- SAMPLE Q32 (Part 3) in T1 vs T2 ---")
q32_1 = next(q for q in t1["questions"] if q["id"] == 32)
q32_2 = next(q for q in t2["questions"] if q["id"] == 32)
print("T1 Q32:", json.dumps(q32_1, ensure_ascii=False, indent=2)[:400])
print("T2 Q32:", json.dumps(q32_2, ensure_ascii=False, indent=2)[:400])

print("\n--- SAMPLE Q131 (Part 6) in T1 vs T2 ---")
q131_1 = next(q for q in t1["questions"] if q["id"] == 131)
q131_2 = next(q for q in t2["questions"] if q["id"] == 131)
print("T1 Q131:", json.dumps(q131_1, ensure_ascii=False, indent=2)[:500])
print("T2 Q131:", json.dumps(q131_2, ensure_ascii=False, indent=2)[:500])

print("\n--- SAMPLE Q147 (Part 7) in T1 vs T2 ---")
q147_1 = next(q for q in t1["questions"] if q["id"] == 147)
q147_2 = next(q for q in t2["questions"] if q["id"] == 147)
print("T1 Q147:", json.dumps(q147_1, ensure_ascii=False, indent=2)[:500])
print("T2 Q147:", json.dumps(q147_2, ensure_ascii=False, indent=2)[:500])
