prix = [9.99, 14.5, 3.2, 29.0]

for p in prix:
    print("Prix :", p)

total = 0
for p in prix:
    total = total + p

print("Total :", total)

moyenne = total / len(prix)
print("Prix moyen :", moyenne)

print("Prix supérieurs à 10€ :")
for p in prix:
    if p > 10:
        print(p)

