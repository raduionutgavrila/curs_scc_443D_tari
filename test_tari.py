import unittest
from app.lib.biblioteca_tari import detalii_scotia, capitala_scotia

class TestScotia(unittest.TestCase):
    def test_capitala(self):
        self.assertEqual(capitala_scotia(), "Capitala Scoției este frumosul oraș istoric Edinburgh.")

if __name__ == '__main__':
    unittest.main()