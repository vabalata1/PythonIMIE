score_joueur1 = 0
score_joueur2 = 0

def ajouter_points_j1(points):
    global score_joueur1
    score_joueur1 += points

def ajouter_points_j2(points):
    global score_joueur2
    score_joueur2 += points

def afficher_scores():
    print("Joueur 1 :", score_joueur1)
    print("Joueur 2 :", score_joueur2)

ajouter_points_j1(10)
ajouter_points_j2(5)
ajouter_points_j1(7)
afficher_scores()

