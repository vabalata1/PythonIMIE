class Tache:
    def __init__(self, titre, description="", statut="à faire"):
        self.titre = titre
        self.description = description
        self.statut = statut
    
    def afficher(self):
        print(f"[{self.statut}] {self.titre}")
        if self.description:
            print(f"  {self.description}")

