import sqlite3
from contextlib import closing
from pathlib import Path

DB_PATH = Path(__file__).resolve().parent.parent / "data" / "football.db"


def get_connection():
    """بتفتح اتصال بقاعدة البيانات (وبتعمل مجلد data لو مش موجود)"""
    DB_PATH.parent.mkdir(exist_ok=True)
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn


def init_db():
    """بتعمل جدول matches لو مش موجود"""
    with closing(get_connection()) as conn:
        with conn:
            conn.execute(
                """
                CREATE TABLE IF NOT EXISTS matches (
                    id INTEGER PRIMARY KEY,
                    date TEXT NOT NULL,
                    matchday INTEGER,
                    home TEXT,
                    away TEXT,
                    home_goals INTEGER,
                    away_goals INTEGER
                )
                """
            )


def save_matches(matches):
    """بتحفظ قايمة المباريات في الجدول، ولو المباراة موجودة بتتحدّث"""
    with closing(get_connection()) as conn:
        with conn:
            for match in matches:
                conn.execute(
                    """
                    INSERT OR REPLACE INTO matches
                    (id, date, matchday, home, away, home_goals, away_goals)
                    VALUES (?, ?, ?, ?, ?, ?, ?)
                    """,
                    (
                        match["id"],
                        match["date"],
                        match["matchday"],
                        match["home"],
                        match["away"],
                        match["home_goals"],
                        match["away_goals"],
                    ),
                )


if __name__ == "__main__":
    init_db()
    print("Database ready")