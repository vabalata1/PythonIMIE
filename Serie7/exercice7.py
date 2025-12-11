import csv
import matplotlib.pyplot as plt

revenus = []

with open("ventes_journalieres.csv", "r", encoding="utf-8") as f:
    lecteur = csv.reader(f)
    next(lecteur)
    for ligne in lecteur:
        revenu = float(ligne[3])
        revenus.append(revenu)

totaux_semaines = []
taille_semaine = 7

for i in range(0, len(revenus), taille_semaine):
    bloc = revenus[i:i+taille_semaine]
    totaux_semaines.append(sum(bloc))

labels = []
for i in range(len(totaux_semaines)):
    labels.append(f"S{i+1}")

plt.bar(labels, totaux_semaines)
plt.title("Chiffre d'affaires total par semaine")
plt.xlabel("Semaine")
plt.ylabel("CA total (€)")
plt.show()

