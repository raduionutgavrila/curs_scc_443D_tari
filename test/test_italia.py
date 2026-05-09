import unittest
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from tari import app
from app.lib.biblioteca_italia import (
    descriere_tara,
    descriere_capitala,
    descriere_populatie,
    descriere_steag
)


class TestBibliotecaItalia(unittest.TestCase):
    """Teste pentru functiile din biblioteca_italia.py."""

    def test_descriere_tara_returneaza_string(self):
        rezultat = descriere_tara()
        self.assertIsInstance(rezultat, str)

    def test_descriere_tara_contine_italia(self):
        rezultat = descriere_tara()
        self.assertIn('Italia', rezultat)

    def test_descriere_tara_nu_e_gol(self):
        rezultat = descriere_tara()
        self.assertTrue(len(rezultat) > 0)

    def test_descriere_capitala_returneaza_string(self):
        rezultat = descriere_capitala()
        self.assertIsInstance(rezultat, str)

    def test_descriere_capitala_contine_roma(self):
        rezultat = descriere_capitala()
        self.assertIn('Roma', rezultat)

    def test_descriere_populatie_returneaza_string(self):
        rezultat = descriere_populatie()
        self.assertIsInstance(rezultat, str)

    def test_descriere_populatie_contine_milioane(self):
        rezultat = descriere_populatie()
        self.assertIn('milioane', rezultat)

    def test_descriere_steag_returneaza_string(self):
        rezultat = descriere_steag()
        self.assertIsInstance(rezultat, str)

    def test_descriere_steag_contine_tricolor(self):
        rezultat = descriere_steag()
        self.assertIn('tricolor', rezultat)


class TestRuteFlaskItalia(unittest.TestCase):
    """Teste pentru rutele Flask referitoare la Italia."""

    def setUp(self):
        app.config['TESTING'] = True
        self.client = app.test_client()

    def test_ruta_index(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_ruta_index_contine_italia(self):
        response = self.client.get('/')
        self.assertIn(b'Italia', response.data)

    def test_ruta_italia(self):
        response = self.client.get('/italia')
        self.assertEqual(response.status_code, 200)

    def test_ruta_italia_capitala(self):
        response = self.client.get('/italia/capitala')
        self.assertEqual(response.status_code, 200)

    def test_ruta_italia_populatie(self):
        response = self.client.get('/italia/populatie')
        self.assertEqual(response.status_code, 200)

    def test_ruta_italia_steag(self):
        response = self.client.get('/italia/steag')
        self.assertEqual(response.status_code, 200)

    def test_ruta_capitala_contine_roma(self):
        response = self.client.get('/italia/capitala')
        self.assertIn(b'Roma', response.data)

    def test_ruta_inexistenta_404(self):
        response = self.client.get('/franta')
        self.assertEqual(response.status_code, 404)


if __name__ == '__main__':
    unittest.main()
