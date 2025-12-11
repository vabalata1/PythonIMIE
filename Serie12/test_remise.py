import unittest
from remise import calculer_prix_ttc

class TestCalculerPrixTTC(unittest.TestCase):
    def test_prix_normal(self):
        resultat = calculer_prix_ttc(100, 0.2)
        self.assertAlmostEqual(resultat, 120.0, places=2)
    
    def test_prix_nul(self):
        resultat = calculer_prix_ttc(0, 0.2)
        self.assertAlmostEqual(resultat, 0.0, places=2)
    
    def test_prix_negatif_erreur(self):
        with self.assertRaises(ValueError):
            calculer_prix_ttc(-10, 0.2)

if __name__ == "__main__":
    unittest.main()

