import csv
import json
import shutil
from pathlib import Path

def nettoyer_logs(chemin_log):
    if not chemin_log.exists():
        print(f"Je trouve pas le fichier {chemin_log}")
        return
    
    total = 0
    conservees = 0
    
    chemin_cible = chemin_log.parent / f"{chemin_log.stem}_sans_debug{chemin_log.suffix}"
    
    with chemin_log.open("r", encoding="utf-8") as fin, \
         chemin_cible.open("w", encoding="utf-8") as fout:
        for ligne in fin:
            total += 1
            if "[DEBUG]" not in ligne:
                fout.write(ligne)
                conservees += 1
    
    print(f"J'ai trouvé {total} lignes au total")
    print(f"J'ai conservé {conservees} lignes")
    print(f"J'ai créé le fichier {chemin_cible}")

def nettoyer_clients_csv(chemin_csv):
    if not chemin_csv.exists():
        print(f"Je trouve pas le fichier {chemin_csv}")
        return
    
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
    
    with chemin_csv.open("r", encoding="utf-8", newline="") as f:
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
    
    chemin_propre = chemin_csv.parent / f"{chemin_csv.stem}_propre{chemin_csv.suffix}"
    with chemin_propre.open("w", encoding="utf-8", newline="") as f:
        champs = ["nom", "age", "ville"]
        ecrivain = csv.DictWriter(f, fieldnames=champs, delimiter=";")
        ecrivain.writeheader()
        for ligne in lignes_valides:
            ecrivain.writerow({"nom": ligne["nom"], "age": ligne["age"], "ville": ligne["ville"]})
    
    chemin_erreurs = chemin_csv.parent / f"{chemin_csv.stem}_erreurs{chemin_csv.suffix}"
    with chemin_erreurs.open("w", encoding="utf-8", newline="") as f:
        champs = ["nom", "age", "ville", "raison"]
        ecrivain = csv.DictWriter(f, fieldnames=champs, delimiter=";")
        ecrivain.writeheader()
        for ligne in lignes_invalides:
            ecrivain.writerow(ligne)
    
    print(f"J'ai trouvé {len(lignes_valides)} lignes valides")
    print(f"J'ai trouvé {len(lignes_invalides)} lignes invalides")
    print(f"J'ai créé les fichiers {chemin_propre} et {chemin_erreurs}")

def mettre_a_jour_config_json(chemin_config):
    if not chemin_config.exists():
        print(f"Je trouve pas le fichier {chemin_config}")
        return
    
    try:
        with chemin_config.open("r", encoding="utf-8") as f:
            config = json.load(f)
    except json.JSONDecodeError as e:
        print(f"Oups, le fichier JSON est invalide : {e}")
        return
    
    config["debug"] = False
    
    version_parts = config["version"].split(".")
    version_parts[2] = str(int(version_parts[2]) + 1)
    config["version"] = ".".join(version_parts)
    
    config["max_connexions"] += 10
    
    if "admin" not in config["services"]:
        config["services"].append("admin")
    
    config["theme"] = "dark"
    
    fichier_backup = chemin_config.parent / f"{chemin_config.stem}_backup{chemin_config.suffix}"
    shutil.copy(chemin_config, fichier_backup)
    print(f"J'ai créé une sauvegarde {fichier_backup}")
    
    fichier_temp = chemin_config.parent / f"{chemin_config.stem}.tmp"
    with fichier_temp.open("w", encoding="utf-8") as f:
        json.dump(config, f, ensure_ascii=False, indent=2)
    
    fichier_temp.replace(chemin_config)
    print(f"La configuration a été mise à jour dans {chemin_config}")

if __name__ == "__main__":
    print("1) Nettoyer les logs")
    print("2) Nettoyer le CSV clients")
    print("3) Mettre à jour config")
    choix = input("Alors, qu'est-ce que tu veux faire ? ")
    
    if choix == "1":
        chemin = Path("logs") / "app.log"
        nettoyer_logs(chemin)
    elif choix == "2":
        chemin = Path("donnees") / "clients_brut.csv"
        nettoyer_clients_csv(chemin)
    elif choix == "3":
        chemin = Path("config_app.json")
        mettre_a_jour_config_json(chemin)
    else:
            print("Je comprends pas choisis un numéro du menu")

