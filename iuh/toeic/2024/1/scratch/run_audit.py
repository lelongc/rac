import json
import os

BASE_DIR = r"d:\folder\rac\iuh\toeic\2024\1"
total_audio_clips = 0
audit_results = {}

for t in range(1, 11):
    json_path = os.path.join(BASE_DIR, "web", "data", f"test{t}.json")
    with open(json_path, "r", encoding="utf-8") as f:
        data = json.load(f)
    
    qs = data.get("questions", [])
    errs = []
    
    if len(qs) != 200:
        errs.append(f"Expected 200 questions, got {len(qs)}")
        
    for q in qs:
        qid = q["id"]
        ans = q.get("correctAnswer")
        opts = q.get("options", {})
        clip = q.get("audioClip")
        
        # Audio check for LC (1-100)
        if qid <= 100:
            if not clip:
                errs.append(f"Q{qid}: missing audioClip")
            else:
                disk_path = os.path.join(BASE_DIR, "web", clip.replace("/", os.sep))
                if not os.path.exists(disk_path):
                    errs.append(f"Q{qid}: audioClip missing on disk ({clip})")
                elif os.path.getsize(disk_path) < 1000:
                    errs.append(f"Q{qid}: audioClip too small ({clip})")
                else:
                    total_audio_clips += 1
                    
        # Option check for all
        if ans not in opts:
            errs.append(f"Q{qid}: answer {ans} not in options {list(opts.keys())}")
            
    audit_results[f"Test {t}"] = {
        "questions": len(qs),
        "errors": len(errs),
        "sample_errs": errs[:3]
    }

print("=== FINAL MASTER AUDIT REPORT ===")
all_passed = True
for test_name, res in audit_results.items():
    err_cnt = res["errors"]
    q_cnt = res["questions"]
    status = "PASSED (100% OK)" if err_cnt == 0 else f"FAILED ({err_cnt} errors)"
    print(f"{test_name:8s}: {status} | Questions: {q_cnt}")
    if err_cnt > 0:
        all_passed = False
        for e in res["sample_errs"]:
            print(f"   -> {e}")

print(f"\nTotal verified audio clips linked across all tests: {total_audio_clips}")
if all_passed:
    print("ALL 10 TESTS PASSED COMPLETE VERIFICATION (100% READY)!")
