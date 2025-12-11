class ScoreBoard:
    def __init__(self):
        self.scores = {}
    
    def ajouter_points(self, nom_joueur, points):
        if nom_joueur not in self.scores:
            self.scores[nom_joueur] = 0
        self.scores[nom_joueur] = self.scores[nom_joueur] + points
    
    def afficher(self):
        for joueur, score in self.scores.items():
            print(f"{joueur} a {score} point{'s' if score > 1 else ''}")

if __name__ == "__main__":
    scoreboard = ScoreBoard()
    
    scoreboard.ajouter_points("joueur1", 10)
    scoreboard.ajouter_points("joueur2", 5)
    scoreboard.ajouter_points("invité", 8)
    
    scoreboard.afficher()

