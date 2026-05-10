import logging
from app.lib.biblioteca_nepal import descriere_tara, descriere_capitala, descriere_limbi, descriere_populatie

#from app.lib.biblioteca_<tara_mea> import descriere_tara, descriere_capitala, descriere_limbi, descriere_populatie

logger = logging.getLogger(__name__)


def test_functie_descriere_tara():
    expected_result = "Republica Federala Democratica Nepal este un stat muntos situat in Asia de Sud, organizat ca republica parlamentara federala. Tara este impartita in 7 provincii fiind un centru cultural si spiritual major in regiunea Himalaya."
    result = descriere_tara()
    assert result == expected_result, f"Test eșuat! Rezultatul funcției descriere_tara() este: {result}"
    logger.info("Merge functia descriere_tara")

def test_functie_populatie():
    expected_result = "30.5 milioane de locuitori"
    result = descriere_populatie()
    assert result == expected_result, f"Test eșuat! Rezultatul funcției descriere_populatie() este: {result}"
    logger.info("Merge functia descriere_populatie")


def test_functie_capitala():
    expected_result = "Kathmandu"
    result = descriere_capitala()
    assert result == expected_result, f"Test eșuat! Rezultatul funcției descriere_capitala() este: {result}"
    logger.info("Merge functia descriere_capitala")


def test_functie_limbi():
    expected_result = "Nepaleza, Maithili, Bhojpuri, Tharu, Tamang."
    result = descriere_limbi()
    assert result == expected_result, f"Test eșuat! Rezultatul funcției descriere_limbi() este: {result}"
    logger.info("Merge functia descriere_limbi")


if __name__ == "__main__":
    test_functie_descriere_tara()
    test_functie_populatie()
    test_functie_capitala()
    test_functie_limbi()
