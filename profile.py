# profile.py
from datetime import date, timedelta
from config import data, TITLES, XP_PER_LEVEL
from utils import header, GREEN, YELLOW, GREY, RESET

today = date.today()
today_iso = today.isoformat()

def update_streak():
    profile = data["profile"]
    last = profile["last_played"]
    yesterday = (today - timedelta(days=1)).isoformat()
    if last == today_iso:
        return
    if last == yesterday:
        profile["streak"] += 1
    else:
        profile["streak"] = 1
    profile["last_played"] = today_iso

def award_xp(amount):
    profile = data["profile"]
    profile["xp"] += amount
    print(GREEN + f"  +{amount} XP!" + RESET)
    new_level = profile["xp"] // XP_PER_LEVEL + 1
    if new_level > profile["level"]:
        profile["level"] = new_level
        print(YELLOW + f"  *** LEVEL UP! You are now Level {new_level} ***" + RESET)

def get_title(level):
    index = level - 1
    if index >= len(TITLES):
        index = len(TITLES) - 1
    return TITLES[index]

def view_profile():
    header("PLAYER PROFILE")
    profile = data["profile"]
    into_level = profile["xp"] % XP_PER_LEVEL
    bar_filled = into_level * 20 // XP_PER_LEVEL
    bar = GREEN + "█" * bar_filled + GREY + "░" * (20 - bar_filled) + RESET
    print(f"  Title  : {YELLOW}{get_title(profile['level'])}{RESET}")
    print(f"  Level  : {profile['level']}")
    print(f"  XP     : {profile['xp']}  {bar} {into_level}/{XP_PER_LEVEL}")
    print(f"  Streak : {profile['streak']} day(s)")
    
    done_assign = sum(1 for a in data["assignments"] if int(a["done_parts"]) == int(a["total_parts"]))
    done_exams = sum(1 for e in data["exams"] if int(e["hp_left"]) == 0)
    
    print(f"  Mini-bosses defeated : {done_assign}/{len(data['assignments'])}")
    print(f"  Main bosses defeated : {done_exams}/{len(data['exams'])}")
    print(f"  Classes attended     : {len(data['completed'])}")