notes = [12, 5.5, 17, 9, 13, 8, 10]

print("Note minimale:", min(notes))
print("Note maximale:", max(notes))

somme = 0
for note in notes:
    somme = somme + note
moyenne = somme / len(notes)
print("Moyenne:", moyenne)

compteur_reussite = 0
for note in notes:
    if note >= 10:
        compteur_reussite = compteur_reussite + 1
print("Nombre de réussites (>= 10):", compteur_reussite)

pourcentage = (compteur_reussite / len(notes)) * 100
print("Pourcentage de réussite:", pourcentage, "%")

