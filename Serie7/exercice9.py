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

def moyenne_mobile(liste_valeurs, fenetre):
    resultat = []
    for i in range(len(liste_valeurs)):
        if i < fenetre - 1:
            resultat.append(None)
        else:
            bloc = liste_valeurs[i-fenetre+1 : i+1]
            resultat.append(sum(bloc) / fenetre)
    return resultat

moyenne_mob = moyenne_mobile(revenus, 3)

plt.plot(dates, revenus, marker="o", label="Revenus réels")
plt.plot(dates, moyenne_mob, linestyle="--", marker="s", label="Moyenne mobile (3 jours)")
plt.title("Revenus et moyenne mobile")
plt.xlabel("Date")
plt.ylabel("Revenu (€)")
plt.xticks(rotation=45)
plt.legend()
plt.tight_layout()
plt.show()

