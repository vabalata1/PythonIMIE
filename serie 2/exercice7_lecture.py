import json

def calculer_ca(commandes):
    chiffre_affaires = 0
    for cmd in commandes:
        if cmd["statut"] == "payee":
            chiffre_affaires = chiffre_affaires + cmd["montant"]
    return chiffre_affaires

def compter_commandes_par_statut(commandes):
    statuts = {"payee": 0, "annulee": 0, "en_attente": 0}
    for cmd in commandes:
        statut = cmd["statut"]
        statuts[statut] = statuts[statut] + 1
    return statuts

def totaux_par_client(commandes):
    totaux_clients = {}
    for cmd in commandes:
        client = cmd["client"]
        montant = cmd["montant"]
        if client in totaux_clients:
            totaux_clients[client] = totaux_clients[client] + montant
        else:
            totaux_clients[client] = montant
    return totaux_clients

with open("commandes.json", "r", encoding="utf-8") as f:
    commandes_lues = json.load(f)

ca = calculer_ca(commandes_lues)
print("Chiffre d'affaires total:", ca)

stats = compter_commandes_par_statut(commandes_lues)
print("Nombre de commandes par statut:", stats)

totaux = totaux_par_client(commandes_lues)
print("Montant total par client:", totaux)

