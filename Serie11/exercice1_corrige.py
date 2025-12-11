score = 0

def ajouter_points(score_actuel, points):
    nouveau_score = score_actuel + points
    return nouveau_score

score = ajouter_points(score, 10)
print("Score final :", score)

