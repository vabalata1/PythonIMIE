import csv
import matplotlib.pyplot as plt

revenus = []

with open("ventes_journalieres.csv", "r", encoding="utf-8") as f:
    lecteur = csv.reader(f)
    next(lecteur)
    for ligne in lecteur:
        revenu = float(ligne[3])
        revenus.append(revenu)

plt.boxplot(revenus)
plt.title("Distribution des revenus journaliers")
plt.ylabel("Revenu (€)")
plt.show()

