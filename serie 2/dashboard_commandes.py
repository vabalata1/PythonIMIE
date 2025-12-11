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
    commandes = json.load(f)

ca = calculer_ca(commandes)
stats = compter_commandes_par_statut(commandes)
totaux = totaux_par_client(commandes)

print("Tableau de bord commandes")
print()
print("Chiffre d'affaires (commandes payées):", ca, "€")
print()
print("Nombre de commandes par statut:")
print("- payee:", stats["payee"])
print("- annulee:", stats["annulee"])
print("- en_attente:", stats["en_attente"])
print()
print("Top clients:")

clients_tries = sorted(totaux.items(), key=lambda x: x[1], reverse=True)
for client, montant in clients_tries:
    print("  -", client, ":", montant, "€")

