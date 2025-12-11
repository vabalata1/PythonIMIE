prix_ht_str = input("Prix HT: ")
prix_ht = float(prix_ht_str)

taux_tva_str = input("Taux de TVA en pourcentage: ")
taux_tva = float(taux_tva_str)

tva = prix_ht * taux_tva / 100
prix_ttc = prix_ht + tva

print("Pour un prix HT de", prix_ht, "€ et une TVA de", taux_tva, "%, le prix TTC est de", prix_ttc, "€.")

