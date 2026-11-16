#  Semester Quest: Gamified Student Companion

> Turn your college grind into an RPG adventure! Manage classes, slay assignment mini-bosses, conquer exam main bosses, and level up your academic career straight from your terminal.

---

##  Features

- **Gamified Progression**: Earn XP, level up your student title (*from "Fresher Rookie" to "Semester Legend"*), and maintain daily login streaks.
- **Timetable Management**: Keep track of your weekly classes and check them off as you attend them.
- **Mini-Bosses (Assignments)**: Treat assignments like boss fights with HP bars that decrease as you complete milestones.
- **Main Bosses (Exams)**: Study for exams to deal damage to their health pools and clear them before the deadline.
- **Terminal Control**: Full ability to add, view, and remove classes, assignments, and exams on the fly.
- **JSON Data Persistence**: Automatically saves your progress locally without the clutter of multiple CSV files.
- **Modular Architecture**: Cleanly separated into multiple Python files for optimal readability and maintainability.

---

## 🛠️ Project Structure

```text
semester-quest/
│
├── main.py          # Entry point and central interactive menu loop
├── config.py        # Central data dictionary and JSON file handlers
├── utils.py         # Terminal color formatting and input validation helpers
├── profile.py       # Player stats, XP progression, level-ups, and streaks
├── timetable.py     # Timetable tracking and class attendance logic
├── assignments.py   # Assignment mini-boss tracking and damage system
└── exams.py         # Exam main boss tracking and study simulation
 How to Run
Make sure you have Python 3 installed on your system.

Clone or download this repository into a local folder:


git clone [https://github.com/arnav912008/semester-quest.git](https://github.com/arnav912008/semester-quest.git)
cd semester-quest
Run the application from your terminal or command prompt:


python main.py


 Game Mechanics & XP System
Attending a Class: +10 XP

Completing Assignment Parts: +20 XP per part

Defeating an Assignment Mini-Boss: +50 XP bonus

Studying for Exams: +10 XP per hour studied (deals damage to boss HP)

Defeating an Exam Main Boss: +100 XP bonus

Leveling Up: Every 100 XP increases your player level and updates your title!
