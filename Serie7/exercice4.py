import matplotlib.pyplot as plt

revenus = [2000, 2500, 3000, 2800, 5000, 6000, 2200, 2700, 4500, 5200,
           3200, 3800, 2900, 4100, 4800, 3500, 3900, 4400, 3600, 4300,
           5100, 4700, 3300, 4000, 4600, 3400, 4200, 3700, 4900, 5500]

plt.hist(revenus, bins=7)
plt.title("Distribution des revenus journaliers")
plt.xlabel("Revenu (€)")
plt.ylabel("Fréquence")
plt.show()

