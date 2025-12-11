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

def afficher_menu():
    print("\nVoici ton menu")
    print("1) Voir mes tâches")
    print("2) Ajouter une tâche")
    print("3) Cocher une tâche")
    print("4) Supprimer une tâche")
    print("0) Quitter")

def boucle_principale():
    creer_base_todo()
    
    taches = lister_taches()
    print("Salut ! Bienvenue dans ton gestionnaire de tâches")
    print(f"Tu as {len(taches)} tâche{'s' if len(taches) != 1 else ''} enregistrée{'s' if len(taches) != 1 else ''}")
    
    while True:
        afficher_menu()
        choix = input("Alors, qu'est-ce que tu veux faire ? ")
        
        if choix == "0":
            print("À bientôt")
            break
        elif choix == "1":
            afficher_taches()
        elif choix == "2":
            titre = input("Quelle tâche veux-tu ajouter ? ")
            if titre.strip():
                ajouter_tache(titre.strip())
                print("Ok c'est ajouté")
            else:
                print("Il faut mettre un titre à ta tâche")
        elif choix == "3":
            try:
                id_tache = int(input("Quelle tâche veux-tu cocher ? (donne son numéro) "))
                if marquer_tache_faite(id_tache):
                    print("Parfait c'est coché")
                else:
                    print(f"Je trouve pas la tâche {id_tache}")
            except ValueError:
                print("Il faut mettre un numéro")
        elif choix == "4":
            try:
                id_tache = int(input("Quelle tâche veux-tu supprimer ? (donne son numéro) "))
                if supprimer_tache(id_tache):
                    print("C'est supprimé")
                else:
                    print(f"Je trouve pas la tâche {id_tache}")
            except ValueError:
                print("Il faut mettre un numéro")
        else:
            print("Je comprends pas choisis un numéro du menu")

if __name__ == "__main__":
    boucle_principale()

