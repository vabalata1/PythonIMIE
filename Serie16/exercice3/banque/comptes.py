class CompteBancaire:
    def __init__(self, titulaire, solde_initial=0):
        self.titulaire = titulaire
        self.solde = solde_initial

    def deposer(self, montant):
        self.solde += montant

    def afficher(self):
        print(f"{self.titulaire} a un solde de {self.solde:.2f} €")

