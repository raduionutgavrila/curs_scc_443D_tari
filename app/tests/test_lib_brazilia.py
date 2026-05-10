import logging
from app.lib.biblioteca_brazilia import descriere_tara, descriere_capitala, descriere_limbi, descriere_populatie

#from app.lib.biblioteca_<tara_mea> import descriere_tara, descriere_capitala, descriere_limbi, descriere_populatie

logger = logging.getLogger(__name__)


def test_functie_descriere_tara():
    expected_result = "Republica Federativă a Braziliei este cel mai mare stat din America de Sud și America Latină, constituind o democrație reprezentativă federală ce adăpostește cea mai mare parte a bazinului Amazonului, fiind totodată o putere economică emergentă de importanță globală și un pilon cultural al emisferei sudice."
    result = descriere_tara()
    assert result == expected_result, f"Test eșuat! Rezultatul funcției descriere_tara() este: {result}"
    logger.info("Merge functia descriere_tara")

def test_functie_populatie():
    expected_result = "Aproximativ 215 milioane de locuitori"
    result = descriere_populatie()
    assert result == expected_result, f"Test eșuat! Rezultatul funcției descriere_populatie() este: {result}"
    logger.info("Merge functia descriere_populatie")


def test_functie_capitala():
    expected_result = "Brasília"
    result = descriere_capitala()
    assert result == expected_result, f"Test eșuat! Rezultatul funcției descriere_capitala() este: {result}"
    logger.info("Merge functia descriere_capitala")


def test_functie_limbi():
    expected_result = "Portugheza (limba oficială)"
    result = descriere_limbi()
    assert result == expected_result, f"Test eșuat! Rezultatul funcției descriere_limbi() este: {result}"
    logger.info("Merge functia descriere_limbi")


if __name__ == "__main__":
    test_functie_descriere_tara()
    test_functie_populatie()
    test_functie_capitala()
    test_functie_limbi()