import matplotlib.pyplot as plt

categories = ["Électronique", "Mode", "Maison", "Sport", "Livres", "Jouets"]
ca = [12000, 8000, 6000, 4000, 3000, 2500]

plt.bar(categories, ca)
plt.title("Chiffre d'affaires par catégorie")
plt.xlabel("Catégorie")
plt.ylabel("CA (€)")
plt.xticks(rotation=45)

for i, valeur in enumerate(ca):
    plt.text(i, valeur + 200, str(valeur) + "€", ha="center")

plt.tight_layout()
plt.show()

