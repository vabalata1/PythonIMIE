import os

def lire_fichier_lbyl(nom_fichier):
    if os.path.exists(nom_fichier):
        with open(nom_fichier, "r", encoding="utf-8") as f:
            contenu = f.read()
            return contenu
    else:
        print(f"Je trouve pas le fichier {nom_fichier}")
        return None

def lire_fichier_eafp(nom_fichier):
    try:
        with open(nom_fichier, "r", encoding="utf-8") as f:
            contenu = f.read()
            return contenu
    except FileNotFoundError:
        print(f"Je trouve pas le fichier {nom_fichier}")
        return None

if __name__ == "__main__":
    fichier_existant = "test.txt"
    
    with open(fichier_existant, "w", encoding="utf-8") as f:
        f.write("Contenu du fichier de test")
    
    print("Test avec un fichier qui existe")
    print("LBYL:", lire_fichier_lbyl(fichier_existant))
    print("EAFP:", lire_fichier_eafp(fichier_existant))
    
    print("\nTest avec un fichier qui existe pas")
    fichier_inexistant = "fichier_qui_n_existe_pas.txt"
    print("LBYL:", lire_fichier_lbyl(fichier_inexistant))
    print("EAFP:", lire_fichier_eafp(fichier_inexistant))

