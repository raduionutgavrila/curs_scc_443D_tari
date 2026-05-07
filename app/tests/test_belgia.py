import logging
from app.lib.biblioteca_belgia import descriere_capitala, descriere_limbi, descriere_populatie
logger = logging.getLogger(__name__)


def test_functie_descriere():
    expected_result = "Bruxelles"
    result = descriere_capitala()
    assert result == expected_result, f"Test eșuat! Rezultatul funcției descriere_capitala() este: {result}"
    logger.info("Merge functia descriere_capitala")


def test_functie_capitala():
    expected_result = "Bruxelles"
    result = descriere_capitala()
    assert result == expected_result, f"Test eșuat! Rezultatul funcției descriere_capitala() este: {result}"
    logger.info("Merge functia descriere_capitala")


def test_functie_limbi():
    expected_result = "Populație:"
    result = descriere_populatie()
    assert result == expected_result, f"Test eșuat! Rezultatul funcției descriere_populatie() este: {result}"
    logger.info("Merge functia descriere_populatie")


if __name__ == "__main__":
    test_functie_descriere()
    test_functie_capitala()
    test_functie_limbi()