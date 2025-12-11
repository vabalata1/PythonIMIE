import outils_chaine

phrase = input("Entre une phrase : ")

nb_mots = outils_chaine.compter_mots(phrase)
print(f"Il y a {nb_mots} mot{'s' if nb_mots > 1 else ''} dans ta phrase")

print(outils_chaine.SEPARATEUR)

if outils_chaine.est_palindrome(phrase):
    print("La phrase est un palindrome")
else:
    print("La phrase est pas un palindrome")

