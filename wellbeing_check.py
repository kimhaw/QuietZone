import sqlite3
from datetime import datetime

DB_NAME = "quietzone_wellbeing.db"


def create_table():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS checkins (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            time_logged TEXT,
            sleep_hours REAL,
            stress INTEGER,
            mood INTEGER,
            score REAL
        )
    """)
    conn.commit()
    conn.close()


def calculate_score(sleep_hours, stress, mood):
    if sleep_hours > 8:
        sleep_hours = 8
    sleep_points = (sleep_hours / 8) * 40
    stress_points = ((6 - stress) / 5) * 30
    mood_points = (mood / 5) * 30
    return round(sleep_points + stress_points + mood_points, 1)


def save_checkin(sleep_hours, stress, mood):
    score = calculate_score(sleep_hours, stress, mood)
    now = datetime.now().strftime("%Y-%m-%d %H:%M")

    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO checkins (time_logged, sleep_hours, stress, mood, score)
        VALUES (?, ?, ?, ?, ?)
    """, (now, sleep_hours, stress, mood, score))
    conn.commit()
    conn.close()

    print("Saved! Score:", score)


def show_history():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("SELECT time_logged, sleep_hours, stress, mood, score FROM checkins")
    rows = cursor.fetchall()
    conn.close()

    for time_logged, sleep_hours, stress, mood, score in rows:
        print(time_logged, "| Sleep:", sleep_hours, "| Stress:", stress, "| Mood:", mood, "| Score:", score)


create_table()
save_checkin(sleep_hours=7.5, stress=2, mood=4)
show_history()