import json
import shutil
from pathlib import Path

fichier_config = Path("config_app.json")

try:
    with fichier_config.open("r", encoding="utf-8") as f:
        config = json.load(f)
except json.JSONDecodeError as e:
    print(f"Oups, le fichier JSON est invalide : {e}")
    exit(1)

config_ancienne = config.copy()

def mettre_a_jour_config(config):
    config["debug"] = False
    
    version_parts = config["version"].split(".")
    version_parts[2] = str(int(version_parts[2]) + 1)
    config["version"] = ".".join(version_parts)
    
    config["max_connexions"] += 10
    
    if "admin" not in config["services"]:
        config["services"].append("admin")
    
    config["theme"] = "dark"
    
    return config

config = mettre_a_jour_config(config)

fichier_backup = Path("config_app_backup.json")
shutil.copy(fichier_config, fichier_backup)
print(f"J'ai créé une sauvegarde {fichier_backup}")

fichier_temp = Path("config_app.json.tmp")
with fichier_temp.open("w", encoding="utf-8") as f:
    json.dump(config, f, ensure_ascii=False, indent=2)

fichier_temp.replace(fichier_config)
print(f"La configuration a été mise à jour dans {fichier_config}")

print("\nVoici les changements")
print(f"L'ancienne version était {config_ancienne['version']}")
print(f"La nouvelle version est {config['version']}")
print(f"L'ancien debug était {config_ancienne['debug']}")
print(f"Le nouveau debug est {config['debug']}")

