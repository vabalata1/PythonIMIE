def est_pair(n):
    if n % 2 == 0:
        return True
    else:
        return False

def calculer_tva(prix_ht, taux):
    tva = prix_ht * taux / 100
    prix_ttc = prix_ht + tva
    return prix_ttc

def moyenne(liste_nombres):
    total = 0
    for nombre in liste_nombres:
        total = total + nombre
    return total / len(liste_nombres)

print("Test est_pair:")
print("8 est pair ?", est_pair(8))
print("7 est pair ?", est_pair(7))

print("\nTest calculer_tva:")
print("Prix TTC pour 100€ HT avec 20% TVA :", calculer_tva(100, 20))
print("Prix TTC pour 50€ HT avec 10% TVA :", calculer_tva(50, 10))

print("\nTest moyenne:")
notes = [12, 15, 9, 18]
print("Moyenne de", notes, ":", moyenne(notes))

