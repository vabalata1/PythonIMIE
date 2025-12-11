import matplotlib.pyplot as plt

trafic = [800, 1000, 1200, 1500, 1800, 2000, 2200, 2400]
revenu = [2000, 2500, 3000, 3800, 4200, 4800, 5200, 5800]

plt.scatter(trafic, revenu, alpha=0.7)
plt.title("Relation entre trafic et revenu")
plt.xlabel("Trafic (visites)")
plt.ylabel("Revenu (€)")
plt.grid(True)
plt.show()

