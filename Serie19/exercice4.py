from pathlib import Path
import json
from typing import Any

FICHIER_TODOS = Path("todos.json")

def charger_donnees_securise(chemin_fichier):
    if not chemin_fichier.exists():
        return {
            "utilisateur": "utilisateur",
            "derniere_id": 0,
            "taches": []
        }
    
    try:
        with chemin_fichier.open("r", encoding="utf-8") as f:
            donnees = json.load(f)
        return donnees
    except json.JSONDecodeError as e:
        print(f"Oups, le fichier JSON est invalide : {e}")
        return {
            "utilisateur": "utilisateur",
            "derniere_id": 0,
            "taches": []
        }

def sauvegarder_donnees(chemin_fichier, donnees):
    with chemin_fichier.open("w", encoding="utf-8") as f:
        json.dump(donnees, f, ensure_ascii=False, indent=2)

def ajouter_tache(donnees, titre):
    donnees["derniere_id"] += 1
    nouvelle_tache = {
        "id": donnees["derniere_id"],
        "titre": titre,
        "fait": False
    }
    donnees["taches"].append(nouvelle_tache)

def marquer_tache_faite(donnees, id_tache):
    for tache in donnees["taches"]:
        if tache["id"] == id_tache:
            tache["fait"] = True
            return True
    return False

def supprimer_tache(donnees, id_tache):
    for i, tache in enumerate(donnees["taches"]):
        if tache["id"] == id_tache:
            donnees["taches"].pop(i)
            return True
    return False

def afficher_taches(donnees):
    taches_triees = sorted(donnees["taches"], key=lambda t: t["id"])
    print(f"\nVoici les tâches de {donnees['utilisateur']}")
    if not taches_triees:
        print("  Aucune tâche")
    else:
        for tache in taches_triees:
            statut = "✓" if tache["fait"] else " "
            print(f"  [{tache['id']}] {statut} {tache['titre']}")

def afficher_taches_a_faire(donnees):
    taches_a_faire = [t for t in donnees["taches"] if not t["fait"]]
    taches_triees = sorted(taches_a_faire, key=lambda t: t["id"])
    print("\nTâches à faire")
    if not taches_triees:
        print("  Aucune tâche à faire")
    else:
        for tache in taches_triees:
            print(f"  [{tache['id']}] {tache['titre']}")

def afficher_taches_faites(donnees):
    taches_faites = [t for t in donnees["taches"] if t["fait"]]
    taches_triees = sorted(taches_faites, key=lambda t: t["id"])
    print("\nTâches faites")
    if not taches_triees:
        print("  Aucune tâche faite")
    else:
        for tache in taches_triees:
            print(f"  [{tache['id']}] {tache['titre']}")

def menu():
    print("\nVoici ton menu")
    print("1) Afficher les tâches")
    print("2) Ajouter une tâche")
    print("3) Marquer une tâche comme faite")
    print("4) Supprimer une tâche")
    print("5) Afficher les tâches à faire")
    print("6) Afficher les tâches faites")
    print("0) Quitter")
    choix = input("Alors, qu'est-ce que tu veux faire ? ")
    return choix

def boucle_principale():
    donnees = charger_donnees_securise(FICHIER_TODOS)
    print("Salut ! Bienvenue dans ton gestionnaire de tâches")
    print(f"Tu as {len(donnees['taches'])} tâche{'s' if len(donnees['taches']) != 1 else ''} enregistrée{'s' if len(donnees['taches']) != 1 else ''}")
    
    while True:
        choix = menu()
        
        if choix == "0":
            print("À bientôt")
            break
        elif choix == "1":
            afficher_taches(donnees)
        elif choix == "2":
            titre = input("Quel est le titre de la nouvelle tâche ? ")
            ajouter_tache(donnees, titre)
            sauvegarder_donnees(FICHIER_TODOS, donnees)
            print("Ok c'est ajouté et sauvegardé")
        elif choix == "3":
            try:
                id_tache = int(input("Quel est l'ID de la tâche à marquer comme faite ? "))
                if marquer_tache_faite(donnees, id_tache):
                    sauvegarder_donnees(FICHIER_TODOS, donnees)
                    print("Parfait c'est coché")
                else:
                    print(f"Désolé j'ai pas trouvé de tâche avec l'ID {id_tache}")
            except ValueError:
                print("Hmm l'ID doit être un nombre entier")
        elif choix == "4":
            try:
                id_tache = int(input("Quel est l'ID de la tâche à supprimer ? "))
                if supprimer_tache(donnees, id_tache):
                    sauvegarder_donnees(FICHIER_TODOS, donnees)
                    print("C'est supprimé")
                else:
                    print(f"Désolé j'ai pas trouvé de tâche avec l'ID {id_tache}")
            except ValueError:
                print("Hmm l'ID doit être un nombre entier")
        elif choix == "5":
            afficher_taches_a_faire(donnees)
        elif choix == "6":
            afficher_taches_faites(donnees)
        else:
            print("J'ai pas compris ton choix Essaie encore")

if __name__ == "__main__":
    boucle_principale()

