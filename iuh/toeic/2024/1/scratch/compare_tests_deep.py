import json
import sys
sys.stdout.reconfigure(encoding='utf-8')

with open('web/data/test1.json', encoding='utf-8') as f:
    t1 = json.load(f)
with open('web/data/test2.json', encoding='utf-8') as f:
    t2 = json.load(f)
with open('web/data/test3.json', encoding='utf-8') as f:
    t3 = json.load(f)

print("=== COMPARING KEYS AND FIELDS BY PART ===")

for part in range(1, 8):
    q1 = next((q for q in t1['questions'] if q.get('part') == part), None)
    q2 = next((q for q in t2['questions'] if q.get('part') == part), None)
    q3 = next((q for q in t3['questions'] if q.get('part') == part), None)
    
    print(f"\n--- PART {part} ---")
    keys1 = set(q1.keys()) if q1 else set()
    keys2 = set(q2.keys()) if q2 else set()
    keys3 = set(q3.keys()) if q3 else set()
    
    print("Keys only in T1:", sorted(list(keys1 - keys2 - keys3)))
    print("Keys missing in T2 vs T1:", sorted(list(keys1 - keys2)))
    print("Keys missing in T3 vs T1:", sorted(list(keys1 - keys3)))
    
    # Check transcript and transcriptVi in Listening parts (1-4)
    if part <= 4:
        for t_name, t_data in [('T1', t1), ('T2', t2), ('T3', t3)]:
            qs = [q for q in t_data['questions'] if q.get('part') == part]
            has_tr = sum(1 for q in qs if q.get('transcript'))
            has_tr_vi = sum(1 for q in qs if q.get('transcriptVi') and len(q.get('transcriptVi', '')) > 20)
            sample_tr = qs[0].get('transcript', '')[:80].replace('\n', ' ') if qs else ''
            sample_tr_vi = qs[0].get('transcriptVi', '')[:80].replace('\n', ' ') if qs else ''
            print(f"  {t_name} Part {part}: transcript={has_tr}/{len(qs)}, transcriptVi (>20 chars)={has_tr_vi}/{len(qs)}")
            print(f"    sample tr: {sample_tr}")
            print(f"    sample trVi: {sample_tr_vi}")
