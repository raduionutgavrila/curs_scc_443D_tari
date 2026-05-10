import unittest
from app.lib.biblioteca_scotia import descriere_tara, descriere_limbi, descriere_populatie, descriere_capitala, descriere_steag

class TestLibScotia(unittest.TestCase):

    def test_descriere_tara(self):
        result = descriere_tara()
        expected_result = "Scotia este o tara parte a Regatului Unit, renumita pentru peisajele sale muntoase, castelele istorice si cultura sa bogata."
        self.assertEqual(result, expected_result)

    def test_descriere_limbi(self):
        result = descriere_limbi()
        expected_result = "Limbile oficiale sunt engleza si scotiana (Gaelic)."
        self.assertEqual(result, expected_result)

    def test_descriere_populatie(self):
        result = descriere_populatie()
        expected_result = "Populația Scotiei este de aproximativ 5.4 milioane de locuitori."
        self.assertEqual(result, expected_result)

    def test_descriere_capitala(self):
        result = descriere_capitala()
        expected_result = "Capitala Scotiei este Edinburgh."
        self.assertEqual(result, expected_result)

    def test_descriere_steag(self):
        result = descriere_steag()
        expected_result = "<img src='/static/steag_scotia.png' alt='Steag Scotia' style='max-width: 500px;'>"
        self.assertEqual(result, expected_result)

if __name__ == '__main__':
    unittest.main()
