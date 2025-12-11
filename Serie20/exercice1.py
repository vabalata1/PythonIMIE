import sqlite3

def creer_base_todo(nom_fichier="todo.db"):
    conn = sqlite3.connect(nom_fichier)
    cur = conn.cursor()
    
    cur.execute("""
        CREATE TABLE IF NOT EXISTS taches (
            id    INTEGER PRIMARY KEY AUTOINCREMENT,
            titre TEXT NOT NULL,
            fait  INTEGER NOT NULL DEFAULT 0
        )
    """)
    
    conn.commit()
    conn.close()

if __name__ == "__main__":
    creer_base_todo()
    print("Base todo.db initialisée et table taches créée si nécessaire")

