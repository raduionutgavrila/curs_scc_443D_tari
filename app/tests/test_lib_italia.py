import logging
from app.lib.biblioteca_italia import descriere_tara, descriere_capitala, descriere_limbi, descriere_populatie

logger = logging.getLogger(__name__)


def test_functie_descriere_tara():
    expected_result = "Italia, denumita oficial Republica Italiana, este o tara situata in sudul Europei, pe Peninsula Italica, fiind cunoscuta pentru arta, arhitectura, moda, gastronomia si istoria sa bogata."
    result = descriere_tara()
    assert result == expected_result, f"Test esuat! Rezultatul functiei descriere_tara() este: {result}"
    logger.info("Merge functia descriere_tara")


def test_functie_populatie():
    expected_result = "59 milioane de locuitori"
    result = descriere_populatie()
    assert result == expected_result, f"Test esuat! Rezultatul functiei descriere_populatie() este: {result}"
    logger.info("Merge functia descriere_populatie")


def test_functie_capitala():
    expected_result = "Roma"
    result = descriere_capitala()
    assert result == expected_result, f"Test esuat! Rezultatul functiei descriere_capitala() este: {result}"
    logger.info("Merge functia descriere_capitala")


def test_functie_limbi():
    expected_result = "Italiana"
    result = descriere_limbi()
    assert result == expected_result, f"Test esuat! Rezultatul functiei descriere_limbi() este: {result}"
    logger.info("Merge functia descriere_limbi")


if __name__ == "__main__":
    test_functie_descriere_tara()
    test_functie_populatie()
    test_functie_capitala()
    test_functie_limbi()
