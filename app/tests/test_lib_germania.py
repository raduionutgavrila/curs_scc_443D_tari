import logging
from app.lib.biblioteca_germania import (
    descriere_tara,
    descriere_capitala,
    descriere_limbi,
    descriere_populatie,
)

logger = logging.getLogger(__name__)


def test_functie_descriere_tara():
    result = descriere_tara()
    assert "Germania" in result
    assert "BMW Museum" in result
    assert "Mercedes-Benz Museum" in result
    assert "Porsche Museum" in result
    assert "Hofbräuhaus" in result
    assert "Paulaner" in result
    logger.info("Merge functia descriere_tara")


def test_functie_populatie():
    expected_result = "Aproximativ 83 de milioane de locuitori"
    result = descriere_populatie()
    assert result == expected_result, (
        f"Test eșuat! Rezultatul funcției descriere_populatie() este: {result}"
    )
    logger.info("Merge functia descriere_populatie")


def test_functie_capitala():
    expected_result = "Berlin"
    result = descriere_capitala()
    assert result == expected_result, (
        f"Test eșuat! Rezultatul funcției descriere_capitala() este: {result}"
    )
    logger.info("Merge functia descriere_capitala")


def test_functie_limbi():
    expected_result = "Germana"
    result = descriere_limbi()
    assert result == expected_result, (
        f"Test eșuat! Rezultatul funcției descriere_limbi() este: {result}"
    )
    logger.info("Merge functia descriere_limbi")


if __name__ == "__main__":
    test_functie_descriere_tara()
    test_functie_populatie()
    test_functie_capitala()
    test_functie_limbi()
