def ajouter_bonus(score):
    nouveau_score = score + 5
    print("Nouveau score après bonus", nouveau_score)
    return nouveau_score

def ajouter_malus(score):
    nouveau_score = score - 3
    print("Nouveau score après malus", nouveau_score)
    return nouveau_score

score = 0
score = ajouter_bonus(score)
score = ajouter_bonus(score)
score = ajouter_malus(score)
print("Score final", score)

