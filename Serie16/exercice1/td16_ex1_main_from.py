from outils_chaine import compter_mots, est_palindrome, SEPARATEUR

phrase = input("Entre une phrase : ")

nb_mots = compter_mots(phrase)
print(f"Il y a {nb_mots} mot{'s' if nb_mots > 1 else ''} dans ta phrase")

print(SEPARATEUR)

if est_palindrome(phrase):
    print("La phrase est un palindrome")
else:
    print("La phrase est pas un palindrome")

