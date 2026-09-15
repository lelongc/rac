# generate_p3_p4_data.py: Generates enrich_t3_p3_p4.py containing full details for Q32 - Q100 of Test 3
import json

# Corrections for stems & options in Part 3
fixes_p3 = {
    38: {
        "stem": "What most likely is the woman's job?",
        "options": {
            "A": "Professional chef",
            "B": "Bank executive",
            "C": "Administrative assistant",
            "D": "Web designer"
        },
        "ans": "D"
    },
    43: {
        "stem": "What will the man most likely do next?",
        "options": {
            "A": "Purchase a snack",
            "B": "Take a shuttle bus",
            "C": "File a complaint",
            "D": "Download a map"
        },
        "ans": "B"
    },
    48: {
        "stem": "What is the woman concerned about?",
        "options": {
            "A": "A lighting issue",
            "B": "A script mistake",
            "C": "A material shortage",
            "D": "A revenue decrease"
        },
        "ans": "A"
    },
    56: {
        "stem": "Where does the conversation most likely take place?",
        "options": {
            "A": "At a restaurant",
            "B": "At a shipping dock",
            "C": "At a farm",
            "D": "At a supermarket"
        },
        "ans": "D"
    },
    57: {
        "stem": "What does the man say is popular?",
        "options": {
            "A": "A colorful package design",
            "B": "A self-service machine",
            "C": "A same-day delivery service",
            "D": "A television advertisement"
        },
        "ans": "B"
    },
    62: {
        "stem": "Who will the man give some gifts to?",
        "options": {
            "A": "Conference participants",
            "B": "Employees",
            "C": "Contest winners",
            "D": "Visitors"
        },
        "ans": "B"
    },
    65: {
        "stem": "What industry do the speakers most likely work in?",
        "options": {
            "A": "Tourism",
            "B": "Film",
            "C": "Engineering",
            "D": "Transportation"
        },
        "ans": "B"
    },
    66: {
        "stem": "Why does the woman want to make a change?",
        "options": {
            "A": "Some equipment is not available.",
            "B": "A new business is opening.",
            "C": "A process will be easier.",
            "D": "Costs will be lower."
        },
        "ans": "C"
    },
    67: {
        "stem": "Look at the graphic. Which street will be closed?",
        "options": {
            "A": "Bangalore Avenue",
            "B": "Dublin Avenue",
            "C": "Polly Street",
            "D": "Elm Lane"
        },
        "ans": "A"
    },
    68: {
        "stem": "What event are the speakers preparing for?",
        "options": {
            "A": "A video-game convention",
            "B": "An in-store demonstration",
            "C": "A product launch",
            "D": "A focus-group session"
        },
        "ans": "C"
    },
    69: {
        "stem": "Look at the graphic. Which level has the issue the speakers discuss?",
        "options": {
            "A": "Level 1",
            "B": "Level 2",
            "C": "Level 3",
            "D": "Level 4"
        },
        "ans": "B"
    },
    70: {
        "stem": "What does the woman suggest doing?",
        "options": {
            "A": "Contacting a colleague",
            "B": "Postponing an event",
            "C": "Working over the weekend",
            "D": "Making travel arrangements"
        },
        "ans": "C"
    }
}

print("Fixes loaded:", len(fixes_p3))
