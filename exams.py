# exams.py
from config import data, XP_STUDY_HOUR, XP_EXAM_KILL, DAMAGE_PER_HOUR
from utils import (
    header, get_int, get_text, get_date, hp_bar, deadline_text,
    GREEN, YELLOW, RED, RESET
)
from profile import award_xp

def view_exams():
    header("EXAMS (MAIN BOSSES)")
    if not data["exams"]:
        print("  No main bosses yet. Add one from the menu.")
        return
    for i, e in enumerate(data["exams"], 1):
        total = int(e["total_hp"])
        left = int(e["hp_left"])
        print(YELLOW + f"{i}. {e['name']}" + RESET + f"  ({e['subject']})")
        if left == 0:
            print("   " + GREEN + "DEFEATED!" + RESET)
        else:
            print(f"   HP {hp_bar(left, total)} {left}/{total}   {deadline_text(e['date'])}")

def add_exam():
    header("ADD NEW EXAM")
    name = get_text("Exam name: ")
    subject = get_text("Subject: ")
    exam_date = get_date("Exam date (DD-MM-YYYY): ")
    data["exams"].append({
        "name": name, "subject": subject, "date": exam_date.isoformat(),
        "total_hp": "100", "hp_left": "100"
    })
    print(GREEN + f"  A main boss appeared: {name} (HP 100)" + RESET)

def remove_exam():
    header("REMOVE EXAM")
    if not data["exams"]:
        print("  No exams to remove.")
        return
    for i, e in enumerate(data["exams"], 1):
        print(f"  {GREEN}{i}.{RESET} {e['name']} ({e['subject']})")
    print(f"  {GREEN}0.{RESET} Back")
    choice = get_int("Choose exam to remove: ", 0, len(data["exams"]))
    if choice == 0:
        return
    removed = data["exams"].pop(choice - 1)
    print(RED + f"  Removed main boss: {removed['name']}" + RESET)

def study_for_exam():
    header("STUDY FOR EXAM")
    active = [e for e in data["exams"] if int(e["hp_left"]) > 0]
    if not active:
        print("  No active main bosses.")
        return
    for i, e in enumerate(active, 1):
        print(f"  {GREEN}{i}.{RESET} {e['name']} ({e['subject']}) - HP {e['hp_left']}/{e['total_hp']}")
    print(f"  {GREEN}0.{RESET} Back")
    choice = get_int("Choose a main boss: ", 0, len(active))
    if choice == 0:
        return
    e = active[choice - 1]
    hours = get_int("How many hours did you study (1-4)? ", 1, 4)
    damage = hours * DAMAGE_PER_HOUR
    new_hp = max(0, int(e["hp_left"]) - damage)
    e["hp_left"] = str(new_hp)
    print(f"  You dealt {damage} damage to {e['name']}!")
    award_xp(XP_STUDY_HOUR * hours)
    if new_hp == 0:
        print(YELLOW + f"  *** MAIN BOSS DEFEATED: {e['name']} ***" + RESET)
        award_xp(XP_EXAM_KILL)