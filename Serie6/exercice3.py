class Produit:
    def __init__(self, nom, prix_ht, stock):
        self.nom = nom
        self.prix_ht = prix_ht
        self.stock = stock
    
    def prix_ttc(self, taux_tva):
        return self.prix_ht * (1 + taux_tva / 100)
    
    def valeur_stock_ttc(self, taux_tva):
        return self.stock * self.prix_ttc(taux_tva)

if __name__ == "__main__":
    p1 = Produit("Clavier", 49.99, 10)
    p2 = Produit("Souris", 19.99, 25)
    p3 = Produit("Écran", 199.99, 5)
    
    catalogue = [p1, p2, p3]
    taux_tva = 20
    
    print("Voici le catalogue")
    total_stock = 0
    for produit in catalogue:
        prix_ttc = produit.prix_ttc(taux_tva)
        valeur_stock = produit.valeur_stock_ttc(taux_tva)
        total_stock = total_stock + valeur_stock
        
        print(f"Le produit est {produit.nom}")
        print(f"  Le prix HT est {produit.prix_ht}€")
        print(f"  Le prix TTC est {prix_ttc:.2f}€")
        print(f"  Le stock est {produit.stock}")
        print(f"  La valeur du stock TTC est {valeur_stock:.2f}€")
        print()
    
    print(f"La valeur totale du stock TTC est {total_stock:.2f}€")

