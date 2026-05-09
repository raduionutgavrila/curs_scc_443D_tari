import logging
from app.lib.biblioteca_mexic import descriere_tara, descriere_capitala, descriere_limbi, descriere_populatie

logger = logging.getLogger(__name__)

def test_functie_descriere_tara():
    expected_result = "Mexic, denumita oficial Statele Unite Mexicane, este o tara situata in America de Nord, cunoscuta pentru cultura sa vibranta, istoria antica a civilizatiilor precolumbiene si bucataria traditionala faimoasa in intreaga lume."
    result = descriere_tara()
    assert result == expected_result, f"Test esuat! Rezultatul functiei descriere_tara() este: {result}"
    logger.info("Merge functia descriere_tara")

def test_functie_populatie():
    expected_result = "Aproximativ 128 milioane de locuitori"
    result = descriere_populatie()
    assert result == expected_result, f"Test esuat! Rezultatul functiei descriere_populatie() este: {result}"
    logger.info("Merge functia descriere_populatie")

def test_functie_capitala():
    expected_result = "Ciudad de Mexico"
    result = descriere_capitala()
    assert result == expected_result, f"Test esuat! Rezultatul functiei descriere_capitala() este: {result}"
    logger.info("Merge functia descriere_capitala")

def test_functie_limbi():
    expected_result = "Spaniola (majoritara) si 68 de limbi indigene recunoscute"
    result = descriere_limbi()
    assert result == expected_result, f"Test esuat! Rezultatul functiei descriere_limbi() este: {result}"
    logger.info("Merge functia descriere_limbi")

if __name__ == "__main__":
    test_functie_descriere_tara()
    test_functie_populatie()
    test_functie_capitala()
    test_functie_limbi()