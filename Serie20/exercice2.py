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

def ajouter_tache(titre):
    conn = sqlite3.connect("todo.db")
    cur = conn.cursor()
    cur.execute("INSERT INTO taches (titre, fait) VALUES (?, ?)", (titre, 0))
    conn.commit()
    conn.close()

def lister_taches():
    conn = sqlite3.connect("todo.db")
    cur = conn.cursor()
    cur.execute("SELECT id, titre, fait FROM taches ORDER BY id")
    lignes = cur.fetchall()
    conn.close()
    
    resultat = []
    for id_, titre, fait in lignes:
        resultat.append((id_, titre, bool(fait)))
    return resultat

def marquer_tache_faite(id_tache):
    conn = sqlite3.connect("todo.db")
    cur = conn.cursor()
    cur.execute("UPDATE taches SET fait = 1 WHERE id = ?", (id_tache,))
    modifie = cur.rowcount > 0
    conn.commit()
    conn.close()
    return modifie

def supprimer_tache(id_tache):
    conn = sqlite3.connect("todo.db")
    cur = conn.cursor()
    cur.execute("DELETE FROM taches WHERE id = ?", (id_tache,))
    supprime = cur.rowcount > 0
    conn.commit()
    conn.close()
    return supprime

def afficher_taches():
    taches = lister_taches()
    if not taches:
        print("Tu as aucune tâche pour le moment")
        return
    for id_, titre, fait in taches:
        etat = "✔" if fait else " "
        print(f"[{id_}] [{etat}] {titre}")

if __name__ == "__main__":
    creer_base_todo()
    
    ajouter_tache("Apprendre SQLite")
    ajouter_tache("Créer une application")
    ajouter_tache("Tester les fonctions CRUD")
    
    print("\nVoici tes tâches")
    afficher_taches()
    
    print("\nJe marque la tâche 1 comme faite")
    marquer_tache_faite(1)
    
    print("Je supprime la tâche 2")
    supprimer_tache(2)
    
    print("\nVoici ta liste finale")
    afficher_taches()

