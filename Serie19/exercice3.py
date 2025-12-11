from pathlib import Path
import json
from typing import Any

def charger_donnees_securise(chemin_fichier):
    if not chemin_fichier.exists():
        print(f"Je trouve pas le fichier {chemin_fichier} je crée une structure par défaut")
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
    print(f"Voici les tâches de {donnees['utilisateur']}")
    for tache in donnees["taches"]:
        statut = "fait=True" if tache["fait"] else "fait=False"
        print(f"[{tache['id']}] {tache['titre']} ({statut})")

if __name__ == "__main__":
    FICHIER_TODOS = Path("todos_ex3.json")
    
    donnees = charger_donnees_securise(FICHIER_TODOS)
    
    print("Voici tes tâches actuelles")
    afficher_taches(donnees)
    
    print("\nJ'ajoute une nouvelle tâche")
    ajouter_tache(donnees, "Nouvelle tâche ajoutée")
    
    print("Je marque la tâche 2 comme faite")
    if marquer_tache_faite(donnees, 2):
        print("C'est fait")
    else:
        print("Je trouve pas la tâche 2")
    
    print("\nJe supprime la tâche 1")
    if supprimer_tache(donnees, 1):
        print("C'est supprimé")
    else:
        print("Je trouve pas la tâche 1")
    
    print("\nVoici tes tâches après les modifications")
    afficher_taches(donnees)
    
    sauvegarder_donnees(FICHIER_TODOS, donnees)
    print("\nTout est sauvegardé")

