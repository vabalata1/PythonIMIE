import csv
import matplotlib.pyplot as plt

dates = []
trafic = []
nb_commandes = []
revenus = []

with open("ventes_journalieres.csv", "r", encoding="utf-8") as f:
    lecteur = csv.reader(f)
    next(lecteur)
    for ligne in lecteur:
        date = ligne[0]
        t = int(ligne[1])
        nb = int(ligne[2])
        revenu = float(ligne[3])
        dates.append(date)
        trafic.append(t)
        nb_commandes.append(nb)
        revenus.append(revenu)

totaux_semaines = []
taille_semaine = 7
for i in range(0, len(revenus), taille_semaine):
    bloc = revenus[i:i+taille_semaine]
    totaux_semaines.append(sum(bloc))

labels = []
for i in range(len(totaux_semaines)):
    labels.append(f"S{i+1}")

plt.figure(figsize=(12, 8))
plt.suptitle("Tableau de bord e-commerce", fontsize=16)

plt.subplot(2, 2, 1)
plt.plot(dates, trafic, marker="o")
plt.title("Trafic")
plt.ylabel("Visites")
plt.xticks(rotation=45)

plt.subplot(2, 2, 2)
plt.plot(dates, revenus, marker="o")
plt.title("Revenu")
plt.ylabel("Revenu (€)")
plt.xticks(rotation=45)

plt.subplot(2, 2, 3)
plt.hist(revenus, bins=7)
plt.title("Distribution des revenus")
plt.xlabel("Revenu (€)")
plt.ylabel("Fréquence")

plt.subplot(2, 2, 4)
plt.bar(labels, totaux_semaines)
plt.title("CA hebdomadaire")
plt.xlabel("Semaine")
plt.ylabel("CA total (€)")

plt.tight_layout()
plt.savefig("dashboard.png")
plt.show()

