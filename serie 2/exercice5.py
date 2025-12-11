notes = []

with open("notes.txt", "r", encoding="utf-8") as f:
    for ligne in f:
        ligne = ligne.strip()
        if ligne:
            note = float(ligne)
            notes.append(note)

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
print("Nombre de notes >= 10:", compteur_reussite)

