import matplotlib.pyplot as plt

jours = [1, 2, 3, 4, 5, 6, 7]
trafic = [1200, 1350, 900, 1500, 1700, 1600, 1800]

plt.plot(jours, trafic, marker="o")
plt.title("Trafic du site sur 7 jours")
plt.xlabel("Jour")
plt.ylabel("Nombre de visites")
plt.grid(True)
plt.show()

