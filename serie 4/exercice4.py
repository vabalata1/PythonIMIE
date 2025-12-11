def lire_fichier_securise(nom_fichier):
    try:
        with open(nom_fichier, "r", encoding="utf-8") as f:
            contenu = f.read()
        return contenu
    except FileNotFoundError:
        print("Le fichier n'existe pas.")
        return None

nom_fichier = input("Nom du fichier à lire:")
contenu = lire_fichier_securise(nom_fichier)

if contenu is not None:
    print(contenu)
else:
    print("Lecture impossible")

