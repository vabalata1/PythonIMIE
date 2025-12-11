import unittest
from service_remise_log import appliquer_remise

class TestAppliquerRemise(unittest.TestCase):
    def test_remise_valide(self):
        resultat = appliquer_remise(100, 0.1)
        self.assertAlmostEqual(resultat, 90.0, places=2)
    
    def test_remise_invalide_negative(self):
        with self.assertRaises(ValueError):
            appliquer_remise(100, -0.1)
    
    def test_remise_invalide_superieure_un(self):
        with self.assertRaises(ValueError):
            appliquer_remise(100, 1.5)

if __name__ == "__main__":
    unittest.main()

