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

commandes = []

with open("commandes.txt", "r", encoding="utf-8") as f:
    for ligne in f:
        ligne = ligne.strip()
        if ligne:
            champs = ligne.split(";")
            commande = {
                "id": int(champs[0]),
                "client": champs[1],
                "montant": float(champs[2]),
                "statut": champs[3]
            }
            commandes.append(commande)

ca = calculer_ca(commandes)
print("Chiffre d'affaires total:", ca)

stats = compter_commandes_par_statut(commandes)
print("Nombre de commandes par statut:", stats)

totaux = totaux_par_client(commandes)
print("Montant total par client:", totaux)

