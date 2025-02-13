import sqlite3

DB_PATH = "history.db"

def create_database():
    """Creates SQLite database for storing conversion history."""
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS conversion_history (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            md_file TEXT,
            html_file TEXT,
            timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
        )
    """)
    conn.commit()
    conn.close()

def save_conversion_history(md_file, html_file):
    """Saves conversion details into SQLite."""
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("INSERT INTO conversion_history (md_file, html_file) VALUES (?, ?)", 
                   (md_file, html_file))
    conn.commit()
    conn.close()

def get_conversion_history():
    """Retrieves past conversions."""
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM conversion_history ORDER BY timestamp DESC")
    history = cursor.fetchall()
    conn.close()
    return history

# Initialize database
create_database()
