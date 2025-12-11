class Employe:
    def __init__(self, nom, salaire_base):
        self.nom = nom
        self.salaire_base = salaire_base
    
    def calculer_salaire(self):
        return self.salaire_base
    
    def afficher(self):
        print(f"L'employé {self.nom} a un salaire de {self.calculer_salaire()}€")

class Developpeur(Employe):
    def __init__(self, nom, salaire_base, prime_technique):
        super().__init__(nom, salaire_base)
        self.prime_technique = prime_technique
    
    def calculer_salaire(self):
        return self.salaire_base + self.prime_technique

class Manager(Employe):
    def __init__(self, nom, salaire_base, prime_management):
        super().__init__(nom, salaire_base)
        self.prime_management = prime_management
    
    def calculer_salaire(self):
        return self.salaire_base + self.prime_management

if __name__ == "__main__":
    e1 = Developpeur("Alice", 3000, 500)
    e2 = Developpeur("Bob", 3200, 600)
    e3 = Manager("Charlie", 4000, 1000)
    e4 = Manager("Diana", 4500, 1200)
    
    employes = [e1, e2, e3, e4]
    
    print("Voici la liste des employés")
    for emp in employes:
        if isinstance(emp, Developpeur):
            type_emp = "Développeur"
        elif isinstance(emp, Manager):
            type_emp = "Manager"
        else:
            type_emp = "Employé"
        
        print(f"{type_emp} {emp.nom} a un salaire de {emp.calculer_salaire()}€")

