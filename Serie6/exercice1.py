class Rectangle:
    def __init__(self, largeur, hauteur):
        self.largeur = largeur
        self.hauteur = hauteur
    
    def surface(self):
        return self.largeur * self.hauteur
    
    def perimetre(self):
        return 2 * (self.largeur + self.hauteur)
    
    def afficher(self):
        print(f"Rectangle : largeur de {self.largeur}, hauteur de {self.hauteur}")
        print(f"La surface est {self.surface()}")
        print(f"Le périmètre est {self.perimetre()}")

if __name__ == "__main__":
    r1 = Rectangle(4, 5)
    r2 = Rectangle(10, 2)
    
    print("Voici le rectangle 1")
    r1.afficher()
    
    print("\nVoici le rectangle 2")
    r2.afficher()

