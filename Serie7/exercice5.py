import csv
import matplotlib.pyplot as plt

dates = []
revenus = []

with open("ventes_journalieres.csv", "r", encoding="utf-8") as f:
    lecteur = csv.reader(f)
    next(lecteur)
    for ligne in lecteur:
        date = ligne[0]
        revenu = float(ligne[3])
        dates.append(date)
        revenus.append(revenu)

plt.plot(dates, revenus, marker="o")
plt.title("Revenu quotidien")
plt.xlabel("Date")
plt.ylabel("Revenu (€)")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

