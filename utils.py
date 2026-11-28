# utils.py - Terminal color formatting and input validation helpers
import os
import sys
from datetime import datetime

os.system("")  # enables ANSI colours in Windows cmd terminal
try:
    sys.stdout.reconfigure(encoding="utf-8")
except Exception:
    pass

CYAN = "\033[96m"
YELLOW = "\033[93m"
GREEN = "\033[92m"
RED = "\033[91m"
BLUE = "\033[94m"
GREY = "\033[90m"
RESET = "\033[0m"

def get_int(prompt, low, high):
    while True:
        text = input(prompt).strip()
        if text.isdigit() and low <= int(text) <= high:
            return int(text)
        print(RED + f"  Please enter a number from {low} to {high}." + RESET)

def get_text(prompt):
    while True:
        text = input(prompt).strip()
        if text != "":
            return text
        print(RED + "This cannot be empty!" + RESET)

def get_date(prompt):
    while True:
        text = input(prompt).strip()
        try:
            return datetime.strptime(text, "%d-%m-%Y").date()
        except ValueError:
            print(RED + "Use the format DD-MM-YYYY (like 15-10-2026)" + RESET)

def get_time(prompt):
    while True:
        text = input(prompt).strip()
        try:
            return datetime.strptime(text, "%H:%M").strftime("%H:%M")
        except ValueError:
            print(RED + "Use 24-hour format HH:MM (e.g. 09:30)" + RESET)

def deadline_text(iso_date):
    days_left = (datetime.strptime(iso_date, "%Y-%m-%d").date() - datetime.now().date()).days
    if days_left < 0:
        return RED + f"OVERDUE by {-days_left} day(s)" + RESET
    if days_left == 0:
        return RED + "DUE TODAY!" + RESET
    if days_left <= 2:
        return RED + f"{days_left} day(s) left" + RESET
    if days_left <= 5:
        return YELLOW + f"{days_left} day(s) left" + RESET
    return GREEN + f"{days_left} day(s) left" + RESET

def pause():
    input(GREY + "\nPress Enter to continue..." + RESET)

def hp_bar(current, total, width=20):
    if total <= 0:
        total = 1
    filled = int(width * current / total)
    if current > 0 and filled == 0:
        filled = 1
    return RED + "█" * filled + GREY + "░" * (width - filled) + RESET

def header(title):
    print()
    print(CYAN + "=" * 60 + RESET)
    print(CYAN + f"  {title}" + RESET)
    print(CYAN + "=" * 60 + RESET)

def line():
    print(BLUE + "-" * 60 + RESET)
