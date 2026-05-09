import logging
from app.lib.biblioteca_germania import descriere_tara, descriere_capitala, descriere_limbi, descriere_populatie

logger = logging.getLogger(__name__)


def test_functie_descriere_tara():
    expected_result = "Germania este o țară din Europa Centrală, cunoscută pentru capitala Berlin, economia puternică și industria auto. Pentru acest proiect, accentul este pus pe muzeele auto și pe restaurantele/berăriile tradiționale. Printre muzeele auto cunoscute se află BMW Museum din München, Mercedes-Benz Museum și Porsche Museum din Stuttgart, Audi Forum din Ingolstadt și Autostadt Volkswagen din Wolfsburg. La partea de restaurante și bere, Germania este cunoscută pentru Hofbräuhaus, Augustiner, Paulaner și alte berării tradiționale."
    result = descriere_tara()
    assert result == expected_result, f"Test eșuat! Rezultatul funcției descriere_tara() este: {result}"
    logger.info("Merge functia descriere_tara")


def test_functie_populatie():
    expected_result = "Aproximativ 83 de milioane de locuitori"
    result = descriere_populatie()
    assert result == expected_result, f"Test eșuat! Rezultatul funcției descriere_populatie() este: {result}"
    logger.info("Merge functia descriere_populatie")


def test_functie_capitala():
    expected_result = "Berlin"
    result = descriere_capitala()
    assert result == expected_result, f"Test eșuat! Rezultatul funcției descriere_capitala() este: {result}"
    logger.info("Merge functia descriere_capitala")


def test_functie_limbi():
    expected_result = "Germana"
    result = descriere_limbi()
    assert result == expected_result, f"Test eșuat! Rezultatul funcției descriere_limbi() este: {result}"
    logger.info("Merge functia descriere_limbi")


if __name__ == "__main__":
    test_functie_descriere_tara()
    test_functie_populatie()
    test_functie_capitala()
    test_functie_limbi()
