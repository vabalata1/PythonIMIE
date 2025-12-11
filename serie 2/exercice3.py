commandes = [
    {"id": 1, "client": "alice@example.com",  "montant": 49.90, "statut": "payee"},
    {"id": 2, "client": "bob@example.com",    "montant": 15.00, "statut": "annulee"},
    {"id": 3, "client": "alice@example.com",  "montant": 19.90, "statut": "payee"},
    {"id": 4, "client": "charlie@example.com","montant": 120.0, "statut": "en_attente"},
    {"id": 5, "client": "bob@example.com",    "montant": 35.0,  "statut": "payee"},
]

chiffre_affaires = 0
for cmd in commandes:
    if cmd["statut"] == "payee":
        chiffre_affaires = chiffre_affaires + cmd["montant"]
print("Chiffre d'affaires total:", chiffre_affaires)

statuts = {"payee": 0, "annulee": 0, "en_attente": 0}
for cmd in commandes:
    statut = cmd["statut"]
    statuts[statut] = statuts[statut] + 1
print("Nombre de commandes par statut:", statuts)

totaux_clients = {}
for cmd in commandes:
    client = cmd["client"]
    montant = cmd["montant"]
    if client in totaux_clients:
        totaux_clients[client] = totaux_clients[client] + montant
    else:
        totaux_clients[client] = montant
print("Montant total par client:", totaux_clients)

