import sqlite3
import os

DB_DIR = os.path.join(os.path.dirname(os.path.dirname(__file__)), "database")
DB_PATH = os.path.join(DB_DIR, "tasks.db")

def get_db_connection():
    os.makedirs(DB_DIR, exist_ok=True)
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn

def init_db():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS tasks (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            done BOOLEAN NOT NULL DEFAULT 0
        )
    ''')
    
    # Check if empty
    cursor.execute('SELECT COUNT(*) FROM tasks')
    if cursor.fetchone()[0] == 0:
        sample_tasks = [
            ("Learn FastAPI", 1),
            ("Setup SQLite", 0),
            ("Build CRUD", 0)
        ]
        cursor.executemany("INSERT INTO tasks (title, done) VALUES (?, ?)", sample_tasks)
        
    conn.commit()
    conn.close()

if __name__ == "__main__":
    init_db()
