n = int(input("Entrez un nombre entier: "))

for i in range(1, 11):
    resultat = n * i
    print(n, "x", i, "=", resultat)

compteur = 1
somme = 0
while compteur <= n:
    somme = somme + compteur
    compteur = compteur + 1

print("Valeur des entiers de 1 a", n, ":", somme)

