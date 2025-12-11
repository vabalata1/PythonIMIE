age = int(input("Votre âge: "))

if age < 12:
    tarif = 5
elif age < 18:
    tarif = 7
elif age < 26:
    tarif = 8.5
else:
    tarif = 10

print("Tarif:", tarif, "€")

