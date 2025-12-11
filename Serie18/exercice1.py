from pathlib import Path

fichier_log = Path("logs") / "app.log"

if not fichier_log.exists():
    print(f"Je trouve pas le fichier {fichier_log}")
    exit(1)

total_lignes = 0
lignes_error = 0
lignes_warning = 0

with fichier_log.open("r", encoding="utf-8") as f:
    for ligne in f:
        total_lignes += 1
        if "[ERROR]" in ligne:
            lignes_error += 1
        if "[WARNING]" in ligne:
            lignes_warning += 1

print(f"J'ai trouvé {total_lignes} lignes au total")
print(f"J'ai trouvé {lignes_warning} lignes WARNING")
print(f"J'ai trouvé {lignes_error} lignes ERROR")

fichier_cible = Path("logs") / "app_sans_debug.log"

with fichier_log.open("r", encoding="utf-8") as fin, \
     fichier_cible.open("w", encoding="utf-8") as fout:
    for ligne in fin:
        if "[DEBUG]" not in ligne:
            fout.write(ligne)

print(f"\nJ'ai créé le fichier filtré {fichier_cible}")

