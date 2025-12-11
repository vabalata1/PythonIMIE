import logging

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(name)s - %(message)s",
    filename="commande.log",
    filemode="a",
)
logger = logging.getLogger(__name__)

def traiter_commande(commande):
    logger.debug("commande reçue : %s", commande)
    if not commande:
        logger.error("commande vide")
        return

    logger.info("vérification du stock...")
    if commande.get("quantite", 0) <= 0:
        logger.error("quantité invalide")
        return

    logger.info("commande validée pour le client %s", commande.get("client"))

if __name__ == "__main__":
    traiter_commande({"id": 1, "client": "Alice", "quantite": 3})
    traiter_commande({"id": 2, "client": "Bob", "quantite": -5})

