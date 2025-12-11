def virement(source, cible, montant):
    if montant <= 0:
        raise ValueError("Montant de virement incorrect")
    if source.solde < montant:
        raise ValueError("Solde insuffisant pour le virement")
    source.solde -= montant
    cible.solde += montant

