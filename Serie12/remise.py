def calculer_prix_ttc(prix_ht, taux_tva):
    if prix_ht < 0:
        raise ValueError("Le prix HT doit être positif")
    return prix_ht * (1 + taux_tva)

