def division_securisee():
    try:
        numerateur = int(input("Numérateur:"))
        denominateur = int(input("Dénominateur:"))
        resultat = numerateur / denominateur
        return resultat
    except ValueError:
        print("Veuillez entrer des entiers uniquement.")
        return None
    except ZeroDivisionError:
        print("Le dénominateur ne peut pas être zéro.")
        return None

resultat = division_securisee()
if resultat is not None:
    print("Résultat:", resultat)
else:
    print("La division n'a pas pu être effectuée.")

