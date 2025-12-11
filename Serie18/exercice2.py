import csv
from pathlib import Path

fichier_source = Path("donnees") / "clients_brut.csv"

def est_ligne_valide(ligne):
    if not ligne.get("nom") or not ligne.get("ville"):
        return False
    try:
        int(ligne.get("age", ""))
        return True
    except (ValueError, TypeError):
        return False

lignes_valides = []
lignes_invalides = []

with fichier_source.open("r", encoding="utf-8", newline="") as f:
    lecteur = csv.DictReader(f, delimiter=";")
    for ligne in lecteur:
        if est_ligne_valide(ligne):
            lignes_valides.append(ligne)
        else:
            raison = []
            if not ligne.get("nom"):
                raison.append("nom vide")
            if not ligne.get("age") or not ligne.get("age").isdigit():
                raison.append("age invalide")
            if not ligne.get("ville"):
                raison.append("ville vide")
            ligne["raison"] = "; ".join(raison)
            lignes_invalides.append(ligne)

fichier_propre = Path("donnees") / "clients_propre.csv"
with fichier_propre.open("w", encoding="utf-8", newline="") as f:
    champs = ["nom", "age", "ville"]
    ecrivain = csv.DictWriter(f, fieldnames=champs, delimiter=";")
    ecrivain.writeheader()
    for ligne in lignes_valides:
        ecrivain.writerow({"nom": ligne["nom"], "age": ligne["age"], "ville": ligne["ville"]})

fichier_erreurs = Path("donnees") / "clients_erreurs.csv"
with fichier_erreurs.open("w", encoding="utf-8", newline="") as f:
    champs = ["nom", "age", "ville", "raison"]
    ecrivain = csv.DictWriter(f, fieldnames=champs, delimiter=";")
    ecrivain.writeheader()
    for ligne in lignes_invalides:
        ecrivain.writerow(ligne)

print(f"J'ai lu {len(lignes_valides) + len(lignes_invalides)} lignes")
print(f"J'ai trouvé {len(lignes_valides)} lignes valides")
print(f"J'ai trouvé {len(lignes_invalides)} lignes invalides")
print("Résultats")
print(f"  {fichier_propre}")
print(f"  {fichier_erreurs}")

