def appliquer_remise(prix: float, remise: float) -> float:
    """
    Calcule le prix final après application d'une remise.

    :param prix: prix initial en euros
    :param remise: taux de remise (entre 0 et 1, ex: 0.1 pour 10%)
    :return: prix final après remise en euros
    """
    prix_final = prix * (1 - remise)
    return prix_final

def compter_commandes_superieures(commandes: list[float], seuil: float) -> int:
    """
    Compte le nombre de commandes dont le montant est supérieur ou égal au seuil.

    :param commandes: liste des montants de commandes en euros
    :param seuil: montant minimum en euros
    :return: nombre de commandes supérieures ou égales au seuil
    """
    compteur = 0
    for montant in commandes:
        if montant >= seuil:
            compteur += 1
    return compteur

def normaliser_email(email: str) -> str:
    """
    Normalise un email en supprimant les espaces et en convertissant en minuscules.

    :param email: adresse email à normaliser
    :return: adresse email normalisée (minuscules, sans espaces)
    """
    return email.strip().lower()

if __name__ == "__main__":
    prix_initial = 100.0
    prix_avec_remise = appliquer_remise(prix_initial, 0.15)
    print(f"Le prix initial est {prix_initial}€, avec une remise de 15% ça fait {prix_avec_remise}€")
    
    commandes = [45.0, 120.0, 80.0, 200.0, 50.0]
    nombre = compter_commandes_superieures(commandes, 100.0)
    print(f"Il y a {nombre} commande{'s' if nombre > 1 else ''} supérieure{'s' if nombre > 1 else ''} ou égale{'s' if nombre > 1 else ''} à 100€")
    
    email = "  ALICE@EXAMPLE.COM  "
    email_normalise = normaliser_email(email)
    print(f"L'email normalisé est '{email_normalise}'")
    
    print("\nTest de help()")
    help(appliquer_remise)

