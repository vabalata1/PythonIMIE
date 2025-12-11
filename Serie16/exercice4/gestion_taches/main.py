from todo import Tache, ajouter_tache, marquer_terminee, afficher_toutes

def main():
    liste_taches = []
    
    tache1 = Tache("Faire les courses", "Acheter du pain et du lait")
    tache2 = Tache("Réviser Python", "Relire les chapitres sur les modules")
    tache3 = Tache("Appeler le médecin", "")
    
    ajouter_tache(liste_taches, tache1)
    ajouter_tache(liste_taches, tache2)
    ajouter_tache(liste_taches, tache3)
    
    print("Voici toutes tes tâches")
    afficher_toutes(liste_taches)
    
    print("\nJe marque 'Faire les courses' comme terminée")
    marquer_terminee(liste_taches, "Faire les courses")
    
    print("\nVoici tes tâches après la modification")
    afficher_toutes(liste_taches)

if __name__ == "__main__":
    main()

