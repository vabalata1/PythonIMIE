from pathlib import Path
import json

def charger_taches_securise(chemin_fichier):
    if not chemin_fichier.exists():
        print(f"Je trouve pas le fichier {chemin_fichier} je crée une liste vide")
        return []
    
    try:
        with chemin_fichier.open("r", encoding="utf-8") as f:
            taches = json.load(f)
        return taches
    except json.JSONDecodeError as e:
        print(f"Oups, le fichier JSON est invalide : {e}")
        print("Je retourne une liste vide")
        return []

def sauvegarder_taches(chemin_fichier, taches):
    with chemin_fichier.open("w", encoding="utf-8") as f:
        json.dump(taches, f, ensure_ascii=False, indent=2)

if __name__ == "__main__":
    FICHIER_TODOS = Path("todos.json")
    
    taches = charger_taches_securise(FICHIER_TODOS)
    nb_avant = len(taches)
    
    if len(taches) == 0:
        nouvelle_tache = {"id": 1, "titre": "Première tâche", "fait": False}
        taches.append(nouvelle_tache)
    
    sauvegarder_taches(FICHIER_TODOS, taches)
    
    print(f"Tu avais {nb_avant} tâche{'s' if nb_avant != 1 else ''} avant")
    print(f"Tu as maintenant {len(taches)} tâche{'s' if len(taches) != 1 else ''}")

