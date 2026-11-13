# timetable.py
from datetime import date
from config import data, DAYS, XP_CLASS
from utils import header, get_int, get_text, get_time, GREEN, YELLOW, GREY, RED, RESET
from profile import award_xp

today = date.today()
today_iso = today.isoformat()
today_name = today.strftime("%A")

def show_timetable():
    header("TIMETABLE")
    if not data["timetable"]:
        print("  No classes yet. Use the menu to add one.")
        return
    for day in DAYS:
        entries = [r for r in data["timetable"] if r["day"] == day]
        entries.sort(key=lambda r: r["time"])
        if not entries:
            continue
        marker = "  <-- today" if day == today_name else ""
        print(YELLOW + day + marker + RESET)
        for r in entries:
            status = ""
            if day == today_name:
                if [today_iso, r["day"], r["time"], r["subject"]] in data["completed"]:
                    status = GREEN + "  [DONE]" + RESET
                else:
                    status = GREY + "  [pending]" + RESET
            print(f"   {r['time']}  {r['subject']}{status}")

def add_timetable_entry():
    header("ADD NEW TIMETABLE ENTRY")
    for i, d in enumerate(DAYS, 1):
        print(f"  {GREEN}{i}.{RESET} {d}")
    day = DAYS[get_int("Day (1-7): ", 1, 7) - 1]
    time = get_time("Time (HH:MM, 24-hour): ")
    subject = get_text("Subject / class name: ")
    data["timetable"].append({"day": day, "time": time, "subject": subject})
    print(GREEN + f"  Added: {day} {time} - {subject}" + RESET)

def remove_timetable_entry():
    header("REMOVE TIMETABLE ENTRY")
    if not data["timetable"]:
        print("  No timetable entries to remove.")
        return
    for i, r in enumerate(data["timetable"], 1):
        print(f"  {GREEN}{i}.{RESET} {r['day']} {r['time']} - {r['subject']}")
    print(f"  {GREEN}0.{RESET} Back")
    choice = get_int("Choose entry to remove: ", 0, len(data["timetable"]))
    if choice == 0:
        return
    removed = data["timetable"].pop(choice - 1)
    print(RED + f"  Removed: {removed['day']} {removed['time']} - {removed['subject']}" + RESET)

def complete_class():
    header("COMPLETE A CLASS")
    pending = []
    for r in sorted(data["timetable"], key=lambda r: r["time"]):
        item = [today_iso, r["day"], r["time"], r["subject"]]
        if r["day"] == today_name and item not in data["completed"]:
            pending.append(r)
    if not pending:
        print("  No pending classes for today. Nice work!")
        return
    for i, r in enumerate(pending, 1):
        print(f"  {GREEN}{i}.{RESET} {r['time']}  {r['subject']}")
    print(f"  {GREEN}0.{RESET} Back")
    choice = get_int("Which class did you attend? ", 0, len(pending))
    if choice == 0:
        return
    picked = pending[choice - 1]
    data["completed"].append([today_iso, picked["day"], picked["time"], picked["subject"]])
    print(f"  Class cleared: {picked['subject']}")
    award_xp(XP_CLASS)