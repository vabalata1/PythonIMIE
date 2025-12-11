import json
import sqlite3
from pathlib import Path

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

def migrer_json_vers_sqlite(fichier_json=Path("todos.json"), fichier_sqlite="todo.db"):
    if not fichier_json.exists():
        print(f"Je trouve pas le fichier {fichier_json}")
        return
    
    with fichier_json.open("r", encoding="utf-8") as f:
        taches_json = json.load(f)
    
    creer_base_todo(fichier_sqlite)
    
    conn = sqlite3.connect(fichier_sqlite)
    cur = conn.cursor()
    
    cur.execute("SELECT COUNT(*) FROM taches")
    nb_existant = cur.fetchone()[0]
    
    if nb_existant > 0:
        print(f"Tu as déjà {nb_existant} tâche{'s' if nb_existant > 1 else ''} dans ta base. Tu veux continuer quand même ? (o/n)")
        reponse = input().lower()
        if reponse != "o":
            print("Ok, j'annule")
            conn.close()
            return
        cur.execute("DELETE FROM taches")
    
    for tache in taches_json:
        id_tache = tache.get("id")
        titre = tache.get("titre")
        fait = 1 if tache.get("fait", False) else 0
        
        if id_tache:
            cur.execute("INSERT INTO taches (id, titre, fait) VALUES (?, ?, ?)", (id_tache, titre, fait))
        else:
            cur.execute("INSERT INTO taches (titre, fait) VALUES (?, ?)", (titre, fait))
    
    conn.commit()
    conn.close()
    
    print(f"Parfait j'ai migré {len(taches_json)} tâche{'s' if len(taches_json) > 1 else ''} depuis le JSON vers SQLite")

if __name__ == "__main__":
    migrer_json_vers_sqlite()

