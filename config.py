# config.py
import json
import os

BASE = os.path.dirname(os.path.abspath(__file__))
DATA_FILE = os.path.join(BASE, "semester_quest.json")

DAYS = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
TITLES = ["Fresher Rookie", "Class Explorer", "Deadline Dodger",
          "Assignment Slayer", "Exam Hunter", "Semester Legend"]

XP_CLASS = 10
XP_ASSIGN_PART = 20
XP_ASSIGN_KILL = 50
XP_STUDY_HOUR = 10
XP_EXAM_KILL = 100
DAMAGE_PER_HOUR = 10
XP_PER_LEVEL = 100

data = {
    "timetable": [],
    "completed": [],
    "assignments": [],
    "exams": [],
    "profile": {"xp": 0, "level": 1, "streak": 0, "last_played": ""}
}

def load_data():
    global data
    if os.path.exists(DATA_FILE):
        try:
            with open(DATA_FILE, "r", encoding="utf-8") as f:
                loaded = json.load(f)
                for key in data:
                    if key in loaded:
                        data[key] = loaded[key]
        except Exception:
            print("Error loading save file. Starting fresh!")

def save_data():
    try:
        with open(DATA_FILE, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=4)
    except Exception:
        print("Error saving game data!")