import logging
from app.lib.biblioteca_finlanda import descriere_tara, descriere_capitala, descriere_limbi, descriere_populatie

logger = logging.getLogger(__name__)


def test_functie_descriere_tara():
    expected_result = "Finlanda, denumita oficial Republica Finlanda, este o tara nordica situata in regiunea finoscandica a Europei de Nord, fiind cunoscuta pentru lacuri, paduri, aurora boreala si sistemul educational performant."
    result = descriere_tara()
    assert result == expected_result, f"Test esuat! Rezultatul functiei descriere_tara() este: {result}"
    logger.info("Merge functia descriere_tara")


def test_functie_populatie():
    expected_result = "5.6 milioane de locuitori"
    result = descriere_populatie()
    assert result == expected_result, f"Test esuat! Rezultatul functiei descriere_populatie() este: {result}"
    logger.info("Merge functia descriere_populatie")


def test_functie_capitala():
    expected_result = "Helsinki"
    result = descriere_capitala()
    assert result == expected_result, f"Test esuat! Rezultatul functiei descriere_capitala() este: {result}"
    logger.info("Merge functia descriere_capitala")


def test_functie_limbi():
    expected_result = "Finlandeza, Suedeza"
    result = descriere_limbi()
    assert result == expected_result, f"Test esuat! Rezultatul functiei descriere_limbi() este: {result}"
    logger.info("Merge functia descriere_limbi")


if __name__ == "__main__":
    test_functie_descriere_tara()
    test_functie_populatie()
    test_functie_capitala()
    test_functie_limbi()
