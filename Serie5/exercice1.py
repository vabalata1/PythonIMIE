def get_age_lbyl(utilisateur):
    if "age" in utilisateur:
        return utilisateur["age"]
    else:
        print("Clé 'age' absente valeur par défaut utilisée")
        return None

def get_age_eafp(utilisateur):
    try:
        return utilisateur["age"]
    except KeyError:
        print("Clé 'age' absente valeur par défaut utilisée")
        return None

if __name__ == "__main__":
    utilisateur1 = {
        "nom": "Alice",
        "email": "alice@example.com",
        "age": 30
    }
    
    utilisateur2 = {
        "nom": "Bob",
        "email": "bob@example.com"
    }
    
    print("Test avec un dictionnaire qui contient 'age'")
    print("LBYL:", get_age_lbyl(utilisateur1))
    print("EAFP:", get_age_eafp(utilisateur1))
    
    print("\nTest avec un dictionnaire sans 'age'")
    print("LBYL:", get_age_lbyl(utilisateur2))
    print("EAFP:", get_age_eafp(utilisateur2))

