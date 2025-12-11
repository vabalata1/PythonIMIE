import json

def charger_taches(chemin_fichier):
    with open(chemin_fichier, "r", encoding="utf-8") as f:
        taches = json.load(f)
    return taches

def sauvegarder_taches(chemin_fichier, taches):
    with open(chemin_fichier, "w", encoding="utf-8") as f:
        json.dump(taches, f, ensure_ascii=False, indent=2)

if __name__ == "__main__":
    taches = charger_taches("todos.json")
    
    for tache in taches:
        print(f"[{tache['id']}] {tache['titre']} (fait={tache['fait']})")
    
    nouvelle_tache = {"id": 3, "titre": "Terminer l'exercice 1", "fait": False}
    taches.append(nouvelle_tache)
    
    sauvegarder_taches("todos.json", taches)
    print(f"\nJ'ai ajouté une nouvelle tâche. Tu as maintenant {len(taches)} tâche{'s' if len(taches) > 1 else ''} au total")

