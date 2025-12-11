score = 0

def ajouter_bonus():
    global score
    score += 5
    print("Nouveau score après bonus :", score)

def ajouter_malus():
    global score
    score -= 3
    print("Nouveau score après malus :", score)

ajouter_bonus()
ajouter_bonus()
ajouter_malus()
print("Score final :", score)

