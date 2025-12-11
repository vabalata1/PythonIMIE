from banque import CompteBancaire, virement

compte1 = CompteBancaire("Alice", 1000)
compte2 = CompteBancaire("Bob", 500)

print("Avant virement")
compte1.afficher()
compte2.afficher()

virement(compte1, compte2, 200)

print("\nAprès virement")
compte1.afficher()
compte2.afficher()

