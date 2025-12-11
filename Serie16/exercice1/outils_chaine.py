SEPARATEUR = "-" * 40

def compter_mots(texte):
    return len(texte.split())

def est_palindrome(texte):
    texte_nettoye = texte.replace(" ", "").lower()
    return texte_nettoye == texte_nettoye[::-1]

