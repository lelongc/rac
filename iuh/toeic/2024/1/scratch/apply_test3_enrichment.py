# scratch/apply_test3_enrichment.py: Master application of all enriched educational data to web/data/test3.json
import json
import os
import sys

sys.stdout.reconfigure(encoding='utf-8')

# 1. Load official answer keys for verification
with open('scratch/test3_official_answers.json', encoding='utf-8') as f:
    official_answers = json.load(f)

# 2. Load all enrichment components
all_enriched = {}

# P2: Q7 - Q31
sys.path.append('scratch')
from enrich_t3_p2 import p2_enrichment
for qid, data in p2_enrichment.items():
    all_enriched[int(qid)] = data

# P3: Q32 - Q43
with open('scratch/enrich_p3_p4.json', encoding='utf-8') as f:
    p3_early = json.load(f)
for qid, data in p3_early.items():
    all_enriched[int(qid)] = data

# P3: Q44 - Q70
with open('scratch/p3_q44_q70_part.json', encoding='utf-8') as f:
    p3_late = json.load(f)
for qid, data in p3_late.items():
    all_enriched[int(qid)] = data

# P4: Q71 - Q100
with open('scratch/p4_q71_q100_part.json', encoding='utf-8') as f:
    p4_all = json.load(f)
for qid, data in p4_all.items():
    all_enriched[int(qid)] = data

# P5: Q101 - Q110
with open('scratch/p5_q101_q110_part.json', encoding='utf-8') as f:
    p5_early = json.load(f)
for qid, data in p5_early.items():
    all_enriched[int(qid)] = data

# P5: Q111 - Q130
with open('scratch/p5_q111_q130_part.json', encoding='utf-8') as f:
    p5_late = json.load(f)
for qid, data in p5_late.items():
    all_enriched[int(qid)] = data

# P6: Q131 - Q146
with open('scratch/p6_q131_q146_part.json', encoding='utf-8') as f:
    p6_all = json.load(f)
for qid, data in p6_all.items():
    all_enriched[int(qid)] = data

# P7: Q147 - Q175
with open('scratch/p7_q147_q175_part.json', encoding='utf-8') as f:
    p7_early = json.load(f)
for qid, data in p7_early.items():
    all_enriched[int(qid)] = data

# P7: Q176 - Q200
with open('scratch/p7_q176_q200_part.json', encoding='utf-8') as f:
    p7_late = json.load(f)
for qid, data in p7_late.items():
    all_enriched[int(qid)] = data

print(f"Total enriched questions loaded: {len(all_enriched)}")

# Load base test3.json
with open('web/data/test3.json', encoding='utf-8') as f:
    t3 = json.load(f)

# Load page 18 text for Q172-175 passage
with open('scratch/ocr_rc_test3.json', encoding='utf-8') as f:
    ocr_rc = json.load(f)
p18_passage = "Questions 172-175 refer to the following online chat discussion.\n\n" + ocr_rc['18'][:ocr_rc['18'].find('172.')].strip() if '172.' in ocr_rc['18'] else ocr_rc['18'][:950].strip()

# Stem & Options fixes for corrupted LC items
lc_fixes = {
    38: {
        "questionText": "What most likely is the woman's job?",
        "options": {"A": "Professional chef", "B": "Bank executive", "C": "Administrative assistant", "D": "Web designer"},
        "correctAnswer": "D"
    },
    43: {
        "questionText": "What will the man most likely do next?",
        "options": {"A": "Purchase a snack", "B": "Take a shuttle bus", "C": "File a complaint", "D": "Download a map"},
        "correctAnswer": "B"
    },
    48: {
        "questionText": "What is the woman concerned about?",
        "options": {"A": "A lighting issue", "B": "A script mistake", "C": "A material shortage", "D": "A revenue decrease"},
        "correctAnswer": "A"
    },
    56: {
        "questionText": "Where does the conversation most likely take place?",
        "options": {"A": "At a restaurant", "B": "At a shipping dock", "C": "At a farm", "D": "At a supermarket"},
        "correctAnswer": "D"
    },
    57: {
        "questionText": "What does the man say is popular?",
        "options": {"A": "A colorful package design", "B": "A self-service machine", "C": "A same-day delivery service", "D": "A television advertisement"},
        "correctAnswer": "B"
    },
    62: {
        "questionText": "Who will the man give some gifts to?",
        "options": {"A": "Conference participants", "B": "Employees", "C": "Contest winners", "D": "Visitors"},
        "correctAnswer": "B"
    },
    65: {
        "questionText": "What industry do the speakers most likely work in?",
        "options": {"A": "Tourism", "B": "Film", "C": "Engineering", "D": "Transportation"},
        "correctAnswer": "B"
    },
    66: {
        "questionText": "Why does the woman want to make a change?",
        "options": {"A": "Some equipment is not available.", "B": "A new business is opening.", "C": "A process will be easier.", "D": "Costs will be lower."},
        "correctAnswer": "C"
    },
    67: {
        "questionText": "Look at the graphic. Which road should be closed?",
        "options": {"A": "Bangalore Avenue", "B": "Dublin Avenue", "C": "Polly Street", "D": "Elm Lane"},
        "correctAnswer": "A"
    },
    68: {
        "questionText": "What are the speakers preparing for?",
        "options": {"A": "A video-game convention", "B": "An in-store demonstration", "C": "A product launch", "D": "A focus-group session"},
        "correctAnswer": "C"
    },
    69: {
        "questionText": "Look at the graphic. Which level is the woman concerned about?",
        "options": {"A": "Level 1", "B": "Level 2", "C": "Level 3", "D": "Level 4"},
        "correctAnswer": "B"
    },
    70: {
        "questionText": "What does the woman suggest doing?",
        "options": {"A": "Contacting a colleague", "B": "Postponing an event", "C": "Working over the weekend", "D": "Making travel arrangements"},
        "correctAnswer": "C"
    },
    79: {
        "questionText": "According to the speaker, what is available in the staff room?",
        "options": {"A": "A product catalog", "B": "Coffee makers", "C": "Work schedules", "D": "Office supplies"},
        "correctAnswer": "A"
    },
    80: {
        "questionText": "According to the speaker, what happened three years ago?",
        "options": {"A": "A council member was elected.", "B": "A local tax law changed.", "C": "A train station opened.", "D": "A business relocated."},
        "correctAnswer": "D"
    },
    81: {
        "questionText": "Who is Matthew Hughes?",
        "options": {"A": "A store owner", "B": "A real estate developer", "C": "A city architect", "D": "A government official"},
        "correctAnswer": "B"
    },
    82: {
        "questionText": "What will the listeners hear about next?",
        "options": {"A": "A sporting event", "B": "Street closures", "C": "The weather", "D": "Parking fines"},
        "correctAnswer": "C"
    },
    83: {
        "questionText": "What is the speaker discussing?",
        "options": {"A": "The renovation of a train station", "B": "The construction of a tunnel", "C": "The replacement of a bridge", "D": "The repaving of a bicycle trail"},
        "correctAnswer": "C"
    },
    84: {
        "questionText": "Why does the speaker say, “this is just one of our many projects”?",
        "options": {"A": "To propose a change of topic", "B": "To explain a delay", "C": "To praise some employees", "D": "To ask for help"},
        "correctAnswer": "B"
    },
    85: {
        "questionText": "What does the speaker suggest doing?",
        "options": {"A": "Organizing an opening ceremony", "B": "Scheduling a television interview", "C": "Revising a design", "D": "Meeting with the press"},
        "correctAnswer": "D"
    },
    86: {
        "questionText": "According to the speaker, what will be different about today’s session?",
        "options": {"A": "It will take place outside.", "B": "It will be recorded.", "C": "Participants will work in pairs.", "D": "Participants will deliver presentations."},
        "correctAnswer": "C"
    },
    87: {
        "questionText": "What is the topic of today’s session?",
        "options": {"A": "Improving communication skills", "B": "Updating accounting practices", "C": "Managing company finances", "D": "Recruiting qualified job candidates"},
        "correctAnswer": "A"
    },
    90: {
        "questionText": "What does the speaker imply when he says, “we’ll have to take a look”?",
        "options": {"A": "A schedule may be changed.", "B": "A supervisor should be consulted.", "C": "A cost cannot be determined yet.", "D": "A new policy must be followed."},
        "correctAnswer": "C"
    },
    91: {
        "questionText": "What does the speaker say about tomorrow?",
        "options": {"A": "Some machinery will be serviced.", "B": "The business will close early.", "C": "Some new employees will start work.", "D": "An appointment will probably become available."},
        "correctAnswer": "B"
    },
    92: {
        "questionText": "What type of business does the speaker most likely work at?",
        "options": {"A": "A car dealership", "B": "An electronics store", "C": "A clothing boutique", "D": "A furniture store"},
        "correctAnswer": "D"
    },
    93: {
        "questionText": "What does the speaker imply when he says, “that day will probably not be a profitable day for us anyway”?",
        "options": {"A": "Reduced profits have prevented salary increases.", "B": "A new sales strategy will have to be developed.", "C": "The listeners will be able to attend an event.", "D": "The listeners have been keeping accurate records."},
        "correctAnswer": "C"
    },
    94: {
        "questionText": "What does the speaker expect the listeners to do?",
        "options": {"A": "Submit an order form", "B": "Provide some feedback", "C": "Sign a contract", "D": "Check a display area"},
        "correctAnswer": "A"
    },
    96: {
        "questionText": "Look at the graphic. Where does the speaker want to meet?",
        "options": {"A": "On Market Street", "B": "On Twelfth Street", "C": "On Central Avenue", "D": "On Tenth Street"},
        "correctAnswer": "A"
    }
}

# Apply updates to each question
for q in t3['questions']:
    qid = q['id']
    
    # Apply stem/options/answers fixes if any
    if qid in lc_fixes:
        for k, v in lc_fixes[qid].items():
            q[k] = v
            
    # Add passageText for Q172-175 if missing
    if 172 <= qid <= 175:
        q['passageText'] = p18_passage

    # Ensure answer matches official key
    if str(qid) in official_answers:
        q['correctAnswer'] = official_answers[str(qid)]

    # Apply enrichment if available
    if qid in all_enriched:
        e = all_enriched[qid]
        if 'exp' in e:
            q['explanation'] = e['exp']
        if 'vocab' in e:
            q['vocabulary'] = e['vocab']
            q['vocab'] = e['vocab']
        if 'collocations' in e:
            q['collocations'] = e['collocations']
        if 'grammar' in e:
            q['grammar'] = e['grammar']
            q['grammarPoints'] = e['grammar']

# Save updated test3.json
with open('web/data/test3.json', 'w', encoding='utf-8') as f:
    json.dump(t3, f, ensure_ascii=False, indent=2)

print("Saved enriched web/data/test3.json successfully!")

# Run strict quality audit
dummy_vocab = 0
zero_vocab = 0
zero_grammar = 0
zero_colloc = 0
answer_mismatches = 0

for q in t3['questions']:
    qid = q['id']
    vocs = q.get('vocabulary', [])
    if len(vocs) == 0:
        zero_vocab += 1
    for v in vocs:
        if v.get('meaning') == 'xác nhận, khẳng định' or v.get('ipa') == '/kənˈfɜːm/' or v.get('word') in ['what', 'there', 'which', 'will']:
            dummy_vocab += 1
            break
            
    if len(q.get('collocations', [])) == 0:
        zero_colloc += 1
        
    if len(q.get('grammar', []) or q.get('grammarPoints', [])) == 0:
        zero_grammar += 1
        
    if str(qid) in official_answers:
        if q['correctAnswer'] != official_answers[str(qid)]:
            answer_mismatches += 1

print("\n=== STRICT AUDIT RESULTS FOR TEST 3 ===")
print(f"Total Questions: {len(t3['questions'])}")
print(f"Dummy confirm vocab: {dummy_vocab}")
print(f"Zero vocab questions: {zero_vocab}")
print(f"Zero grammar questions: {zero_grammar}")
print(f"Zero collocation questions: {zero_colloc}")
print(f"Answer mismatches vs official keys: {answer_mismatches}")
