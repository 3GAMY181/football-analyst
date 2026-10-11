from app.client import get_matches
from app.db import init_db, save_matches


def sync():
    """بتجيب المباريات من الـ API وتحفظها في قاعدة البيانات"""
    init_db()
    matches = get_matches()
    save_matches(matches)
    print(f"Saved {len(matches)} matches")


if __name__ == "__main__":
    sync()