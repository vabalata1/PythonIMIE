import csv
import matplotlib.pyplot as plt

dates = []
trafic = []
revenus = []

with open("ventes_journalieres.csv", "r", encoding="utf-8") as f:
    lecteur = csv.reader(f)
    next(lecteur)
    for ligne in lecteur:
        date = ligne[0]
        t = int(ligne[1])
        revenu = float(ligne[3])
        dates.append(date)
        trafic.append(t)
        revenus.append(revenu)

plt.figure(figsize=(8, 6))

plt.subplot(2, 1, 1)
plt.plot(dates, trafic, marker="o")
plt.title("Trafic")
plt.ylabel("Visites")
plt.xticks(rotation=45)

plt.subplot(2, 1, 2)
plt.plot(dates, revenus, marker="o")
plt.title("Revenu")
plt.xlabel("Date")
plt.ylabel("Revenu (€)")
plt.xticks(rotation=45)

plt.tight_layout()
plt.show()

