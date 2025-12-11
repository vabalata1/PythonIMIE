def ajouter_points(scores, nom_joueur, points):
    if nom_joueur not in scores:
        scores[nom_joueur] = 0
    scores[nom_joueur] = scores[nom_joueur] + points
    return scores

def afficher_scores(scores):
    for joueur, score in scores.items():
        print(f"{joueur} a {score} point{'s' if score > 1 else ''}")

scores = {
    "joueur1": 0,
    "joueur2": 0,
}

scores = ajouter_points(scores, "joueur1", 10)
scores = ajouter_points(scores, "joueur2", 5)
scores = ajouter_points(scores, "joueur1", 7)
afficher_scores(scores)

