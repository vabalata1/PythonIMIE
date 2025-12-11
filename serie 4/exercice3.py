produits = ["PC Portable", "Écran", "Clavier", "Souris", "Casque"]

try:
    indice = int(input("Indice:"))
    produit = produits[indice]
    print("Produit:", produit)
except ValueError:
    print("Veuillez entrer un entier valide.")
except IndexError:
    print("Indice invalide (doit être entre 0 et", len(produits)-1, ").")

