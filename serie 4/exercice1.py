while True:
    try:
        age = int(input("Votre âge:"))
        break
    except ValueError:
        print("Veuillez entrer un entier valide (ex: 25).")

print("Vous avez", age, "ans.")

