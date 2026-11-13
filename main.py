# main.py
from datetime import date
from config import data, load_data, save_data
from utils import CYAN, YELLOW, GREEN, GREY, RED, RESET, line, pause
from profile import update_streak, view_profile
from timetable import show_timetable, add_timetable_entry, remove_timetable_entry, complete_class
from assignments import view_assignments, add_assignment, remove_assignment, work_on_assignment
from exams import view_exams, add_exam, remove_exam, study_for_exam

today = date.today()

MENU_OPTIONS = [
    ("Classes", "Complete Today's Class"),
    ("Classes", "View Timetable"),
    ("Assignments", "View Assignments (Mini-Bosses)"),
    ("Assignments", "Work on Assignment"),
    ("Exams", "View Exams (Main Bosses)"),
    ("Exams", "Study for Exam"),
    ("Profile", "View Player Profile"),
    ("Manage", "Add Assignment"),
    ("Manage", "Remove Assignment"),
    ("Manage", "Add Timetable Entry"),
    ("Manage", "Remove Timetable Entry"),
    ("Manage", "Add Exam"),
    ("Manage", "Remove Exam"),
    ("System", "Exit"),
]

def show_menu():
    profile = data["profile"]
    print()
    print(CYAN + "=" * 60 + RESET)
    print(CYAN + "  SEMESTER QUEST - GAMIFIED TIMETABLE" + RESET)
    print(CYAN + "=" * 60 + RESET)
    print()
    print(YELLOW + today.strftime("%A, %B %d, %Y") + RESET +
          GREY + f"   Lv {profile['level']} | {profile['xp']} XP | streak {profile['streak']}" + RESET)
    line()

    border = "+" + "-" * 4 + "+" + "-" * 14 + "+" + "-" * 38 + "+"
    print(CYAN + border + RESET)
    print(CYAN + "| #  | CATEGORY     | ACTION                               |" + RESET)
    print(CYAN + border + RESET)
    for i, (category, action) in enumerate(MENU_OPTIONS, 1):
        print(f"| {GREEN}{i:>2}{RESET} | {category:<12} | {action:<37} |")
    print(CYAN + border + RESET)
    line()

def main():
    load_data()
    update_streak()
    save_data()

    actions = {
        1: complete_class,
        2: show_timetable,
        3: view_assignments,
        4: work_on_assignment,
        5: view_exams,
        6: study_for_exam,
        7: view_profile,
        8: add_assignment,
        9: remove_assignment,
        10: add_timetable_entry,
        11: remove_timetable_entry,
        12: add_exam,
        13: remove_exam
    }

    while True:
        show_menu()
        option_count = len(MENU_OPTIONS)
        text = input(YELLOW + f"Choose an option (1-{option_count}): " + RESET).strip()
        if not text.isdigit() or not (1 <= int(text) <= option_count):
            print(RED + "Invalid option. Try again." + RESET)
            continue
        choice = int(text)
        if choice == option_count:
            save_data()
            print(CYAN + "\nProgress saved. See you next quest, adventurer!" + RESET)
            break
        
        actions[choice]()
        save_data()
        pause()

if __name__ == "__main__":
    main()