class Produit:
    def __init__(self, id, nom, categorie, prix, stock):
        self.id = id
        self.nom = nom
        self.categorie = categorie
        self.prix = prix
        self.stock = stock
    
    def est_en_rupture(self):
        return self.stock == 0
    
    def afficher_resume(self):
        print(f"[{self.categorie}] {self.nom} : {self.prix}€ (stock de {self.stock})")

class Catalogue:
    def __init__(self):
        self.produits = []
    
    def produits_par_categorie(self, categorie):
        resultat = []
        for produit in self.produits:
            if produit.categorie == categorie:
                resultat.append(produit)
        return resultat
    
    def prix_moyen(self):
        if len(self.produits) == 0:
            return 0
        total = 0
        for produit in self.produits:
            total = total + produit.prix
        return total / len(self.produits)
    
    def produits_en_rupture(self):
        resultat = []
        for produit in self.produits:
            if produit.est_en_rupture():
                resultat.append(produit)
        return resultat

if __name__ == "__main__":
    donnees_produits = [
        {"id": 1, "nom": "Clavier",  "categorie": "Informatique", "prix": 39.99, "stock": 10},
        {"id": 2, "nom": "Souris",   "categorie": "Informatique", "prix": 19.99, "stock": 0},
        {"id": 3, "nom": "Écran",    "categorie": "Informatique", "prix": 129.90, "stock": 5},
        {"id": 4, "nom": "Chaise",   "categorie": "Bureau",       "prix": 89.90, "stock": 2}
    ]
    
    catalogue = Catalogue()
    
    for donnee in donnees_produits:
        produit = Produit(
            donnee["id"],
            donnee["nom"],
            donnee["categorie"],
            donnee["prix"],
            donnee["stock"]
        )
        catalogue.produits.append(produit)
    
    print(f"Le prix moyen est {catalogue.prix_moyen():.2f}€")
    
    print("\nProduits en rupture")
    for produit in catalogue.produits_en_rupture():
        produit.afficher_resume()
    
    print("\nProduits de catégorie 'Informatique'")
    for produit in catalogue.produits_par_categorie("Informatique"):
        produit.afficher_resume()

