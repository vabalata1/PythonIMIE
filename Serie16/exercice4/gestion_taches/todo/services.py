def ajouter_tache(liste_taches, tache):
    liste_taches.append(tache)

def marquer_terminee(liste_taches, titre):
    for tache in liste_taches:
        if tache.titre == titre:
            tache.statut = "terminée"
            return True
    return False

def afficher_toutes(liste_taches):
    if not liste_taches:
        print("Aucune tâche")
    else:
        for tache in liste_taches:
            tache.afficher()

