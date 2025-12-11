class Client:
    def __init__(self, nom, email):
        self.nom = nom
        self.email = email

class LigneCommande:
    def __init__(self, description, quantite, prix_unitaire):
        self.description = description
        self.quantite = quantite
        self.prix_unitaire = prix_unitaire
    
    def total_ligne(self):
        return self.quantite * self.prix_unitaire

class Commande:
    def __init__(self, client):
        self.client = client
        self.lignes = []
    
    def ajouter_ligne(self, ligne):
        self.lignes.append(ligne)
    
    def total(self):
        total = 0
        for ligne in self.lignes:
            total = total + ligne.total_ligne()
        return total

if __name__ == "__main__":
    client = Client("Alice", "alice@example.com")
    
    ligne1 = LigneCommande("Pack 10h de support", 1, 500.0)
    ligne2 = LigneCommande("Formation Python", 2, 200.0)
    ligne3 = LigneCommande("Consultation", 3, 150.0)
    
    commande = Commande(client)
    commande.ajouter_ligne(ligne1)
    commande.ajouter_ligne(ligne2)
    commande.ajouter_ligne(ligne3)
    
    print("Récapitulatif de la commande")
    print(f"Le client est {commande.client.nom} ({commande.client.email})")
    print("\nLignes de commande")
    for i, ligne in enumerate(commande.lignes, 1):
        print(f"  {i}. {ligne.description}")
        print(f"     {ligne.quantite} unité{'s' if ligne.quantite > 1 else ''} à {ligne.prix_unitaire}€")
        print(f"     Le total de cette ligne est {ligne.total_ligne()}€")
    
    print(f"\nLe total de la commande est {commande.total()}€")

