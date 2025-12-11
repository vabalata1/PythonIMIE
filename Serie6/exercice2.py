class CompteBancaire:
    def __init__(self, titulaire, solde=0):
        self.titulaire = titulaire
        self.solde = solde
    
    def deposer(self, montant):
        if montant > 0:
            self.solde = self.solde + montant
            print(f"J'ai déposé {montant}€. Ton nouveau solde est {self.solde}€")
        else:
            print("Le montant doit être positif")
    
    def retirer(self, montant):
        if montant < 0:
            print("Le montant doit être positif")
        elif montant > self.solde:
            print(f"Solde insuffisant. Tu as actuellement {self.solde}€")
        else:
            self.solde = self.solde - montant
            print(f"J'ai retiré {montant}€. Ton nouveau solde est {self.solde}€")
    
    def afficher(self):
        print(f"Le titulaire est {self.titulaire} et le solde est {self.solde}€")

if __name__ == "__main__":
    compte = CompteBancaire("Alice")
    
    print("Je crée un compte pour Alice")
    compte.afficher()
    
    print("\nJe fais quelques dépôts")
    compte.deposer(100)
    compte.deposer(50)
    
    print("\nJe fais quelques retraits")
    compte.retirer(30)
    compte.retirer(200)
    
    print("\nVoici l'état final du compte")
    compte.afficher()

