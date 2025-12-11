mot_de_passe = input("Entrez un mot de passe:")

longueur_ok = len(mot_de_passe) >= 8

a_minuscule = False
a_majuscule = False
a_chiffre = False

for caractere in mot_de_passe:
    if caractere.islower():
        a_minuscule = True
    if caractere.isupper():
        a_majuscule = True
    if caractere.isdigit():
        a_chiffre = True

if longueur_ok and a_minuscule and a_majuscule and a_chiffre:
    print("Mot de passe valide")
else:
    print("Mot de passe invalide:")
    if not longueur_ok:
        print("- longueur minimale de 8 caractères non respectée")
    if not a_minuscule:
        print("- manque une minuscule")
    if not a_majuscule:
        print("- manque une majuscule")
    if not a_chiffre:
        print("- manque un chiffre")

