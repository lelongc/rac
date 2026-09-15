import json
import re

# Official answers for Test 2 Listening
ALL_ANS = json.load(open("all_tests_answers.json", encoding="utf-8"))["test2"]

# 1. Part 1 (Q1-Q6)
p1_data = {
    1: {
        "stem": "Look at the picture marked No. 1 in your test book and choose the best statement:",
        "options": {
            "A": "She's inserting a cord into an outlet.",
            "B": "She's pressing a button on a machine.",
            "C": "She's gripping the handle of a drawer.",
            "D": "She's tacking a notice onto the wall."
        },
        "audioClip": "assets/audio/test2/cuts/q1.mp3",
        "audioLabel": "Nghe câu 1"
    },
    2: {
        "stem": "Look at the picture marked No. 2 in your test book and choose the best statement:",
        "options": {
            "A": "Some window shutters are being replaced.",
            "B": "A pillow is being arranged on a seat.",
            "C": "An outdoor table is being cleared off.",
            "D": "Some wooden boards are being painted."
        },
        "audioClip": "assets/audio/test2/cuts/q2.mp3",
        "audioLabel": "Nghe câu 2"
    },
    3: {
        "stem": "Look at the picture marked No. 3 in your test book and choose the best statement:",
        "options": {
            "A": "Some utensils have been discarded in a bin.",
            "B": "Some bottles are being emptied into a sink.",
            "C": "A rolling chair has been placed next to a counter.",
            "D": "Some drawers have been left open."
        },
        "audioClip": "assets/audio/test2/cuts/q3.mp3",
        "audioLabel": "Nghe câu 3"
    },
    4: {
        "stem": "Look at the picture marked No. 4 in your test book and choose the best statement:",
        "options": {
            "A": "A man is chopping some wood into pieces.",
            "B": "Leaves are scattered across the grass.",
            "C": "A man is closing a window.",
            "D": "Wood is piled near a fence."
        },
        "audioClip": "assets/audio/test2/cuts/q4.mp3",
        "audioLabel": "Nghe câu 4"
    },
    5: {
        "stem": "Look at the picture marked No. 5 in your test book and choose the best statement:",
        "options": {
            "A": "People are standing in line in a lobby.",
            "B": "Items are being loaded into shopping bags.",
            "C": "Tents have been set up in a parking area.",
            "D": "A worker is putting up a canopy."
        },
        "audioClip": "assets/audio/test2/cuts/q5.mp3",
        "audioLabel": "Nghe câu 5"
    },
    6: {
        "stem": "Look at the picture marked No. 6 in your test book and choose the best statement:",
        "options": {
            "A": "Some luggage is stacked next to an escalator.",
            "B": "A suitcase is being lifted onto a shuttle bus.",
            "C": "Some suitcases are displayed in a shop window.",
            "D": "A luggage rack has two levels."
        },
        "audioClip": "assets/audio/test2/cuts/q6.mp3",
        "audioLabel": "Nghe câu 6"
    }
}

# 2. Part 2 (Q7-Q31)
p2_data = {
    7: {
        "stem": "Have the machines on the factory floor been cleaned?",
        "options": {
            "A": "No, not yet.",
            "B": "It's in the shipping container.",
            "C": "I just put it in the trash bin."
        }
    },
    8: {
        "stem": "How much will the budget increase next year?",
        "options": {
            "A": "About 10 percent.",
            "B": "Three hours, I think.",
            "C": "At the bank's main branch."
        }
    },
    9: {
        "stem": "You're going to water the plants before you leave, aren't you?",
        "options": {
            "A": "I walked the whole way.",
            "B": "Yes, right after lunch.",
            "C": "In the break room."
        }
    },
    10: {
        "stem": "Aren't you going to schedule an eye doctor appointment?",
        "options": {
            "A": "Those glasses look nice on you.",
            "B": "I already scheduled one.",
            "C": "The seminar is three days long."
        }
    },
    11: {
        "stem": "I'm going to try to fix this printer.",
        "options": {
            "A": "It doesn't fit.",
            "B": "Double-sided copies.",
            "C": "Are you sure it can be repaired?"
        }
    },
    12: {
        "stem": "What should we do with these brochures?",
        "options": {
            "A": "A trip to the seashore.",
            "B": "Yes, I found it already.",
            "C": "I'll leave them at the front desk."
        }
    },
    13: {
        "stem": "Has the policy meeting been rescheduled?",
        "options": {
            "A": "We have lots of desk calendar designs.",
            "B": "Yes, it's happening tomorrow instead.",
            "C": "This soup is delicious."
        }
    },
    14: {
        "stem": "Why don't we stop by the office cafeteria on our way to the workshop?",
        "options": {
            "A": "Sure, we have time for that.",
            "B": "A full service buffet.",
            "C": "The topic is professional networking."
        }
    },
    15: {
        "stem": "Have you tried our famous pasta dish?",
        "options": {
            "A": "We need a table for five.",
            "B": "Yes, it was delicious.",
            "C": "I'll try to make it on time."
        }
    },
    16: {
        "stem": "Who's the opening act at tonight's concert?",
        "options": {
            "A": "Could you turn up the volume?",
            "B": "A jazz singer from France.",
            "C": "The position has been filled."
        }
    },
    17: {
        "stem": "When do the product demonstrations start?",
        "options": {
            "A": "The schedule was emailed last Friday.",
            "B": "Some innovative features.",
            "C": "In room 202, I think."
        }
    },
    18: {
        "stem": "I tried updating the website, but it didn't work.",
        "options": {
            "A": "That date works for me.",
            "B": "Usually our online reviews.",
            "C": "Just send me the changes you want."
        }
    },
    19: {
        "stem": "Did you hire a new welding specialist?",
        "options": {
            "A": "The part is back-ordered.",
            "B": "Yes, he starts tomorrow.",
            "C": "No, it should be higher."
        }
    },
    20: {
        "stem": "How was the color palette for the lobby chosen?",
        "options": {
            "A": "Blue and orange.",
            "B": "It was fine, thanks.",
            "C": "I wasn't involved."
        }
    },
    21: {
        "stem": "When are we ordering more supplies for the office?",
        "options": {
            "A": "In the storage closet.",
            "B": "Next week on Monday.",
            "C": "The new desk looks great."
        }
    },
    22: {
        "stem": "The battery for the water pump is going to be solar powered, right?",
        "options": {
            "A": "We're still in the planning stages.",
            "B": "140 dollars per year.",
            "C": "Yes, I'd love a glass of water."
        }
    },
    23: {
        "stem": "Where can I buy a charger for this laptop?",
        "options": {
            "A": "Around three o'clock.",
            "B": "I can order one for you.",
            "C": "A limited return policy."
        }
    },
    24: {
        "stem": "Do I need to reserve a meeting room?",
        "options": {
            "A": "Yes, let me show you how.",
            "B": "The service is good.",
            "C": "My slide presentation."
        }
    },
    25: {
        "stem": "When's the new department director supposed to start?",
        "options": {
            "A": "It's an hour long.",
            "B": "Ms. Pavlova isn't retiring for several weeks.",
            "C": "No, that department's upstairs."
        }
    },
    26: {
        "stem": "Should I deliver these pizzas, or will you?",
        "options": {
            "A": "No thanks, I'm not hungry.",
            "B": "Ten dollars for two.",
            "C": "They're being picked up."
        }
    },
    27: {
        "stem": "This month's shipment schedule has been revised.",
        "options": {
            "A": "I couldn't find them either.",
            "B": "Which dates have been changed?",
            "C": "Two dollars per pound."
        }
    },
    28: {
        "stem": "How much will the repairs cost?",
        "options": {
            "A": "The work is covered under the warranty plan.",
            "B": "Yes, it's also available in red.",
            "C": "In about two weeks."
        }
    },
    29: {
        "stem": "Why don't we provide more samples of the wallpaper patterns?",
        "options": {
            "A": "The newspaper is delivered daily.",
            "B": "An interior design course.",
            "C": "There are plenty in the binders."
        }
    },
    30: {
        "stem": "Can you give me a tour of the property this afternoon?",
        "options": {
            "A": "Sorry, I won't have time until tomorrow.",
            "B": "It has a very modern design.",
            "C": "A house on Maple Street."
        }
    },
    31: {
        "stem": "Who's scheduled to test the product today?",
        "options": {
            "A": "We're waiting for confirmation.",
            "B": "It's a great album, right?",
            "C": "About six weeks ago."
        }
    }
}

for qid in p2_data:
    p2_data[qid]["audioClip"] = f"assets/audio/test2/cuts/q{qid}.mp3"
    p2_data[qid]["audioLabel"] = f"Nghe câu {qid}"

with open("scratch/t2_p1_clean.json", "w", encoding="utf-8") as f:
    json.dump(p1_data, f, ensure_ascii=False, indent=2)

with open("scratch/t2_p2_clean.json", "w", encoding="utf-8") as f:
    json.dump(p2_data, f, ensure_ascii=False, indent=2)

print("Part 1 and Part 2 clean definitions written!")
