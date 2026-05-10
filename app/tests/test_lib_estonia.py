import logging
<<<<<<<< HEAD:app/tests/test_lib_estonia.py
from app.lib.biblioteca_estonia import descriere_tara, descriere_capitala, descriere_limbi, descriere_populatie

#from app.lib.biblioteca_<tara_mea> import descriere_tara, descriere_capitala, descriere_limbi, descriere_populatie
========
from app.lib.biblioteca_franta import descriere_tara, descriere_capitala, descriere_limbi, descriere_populatie
>>>>>>>> origin/main_tuturluta_fabian:app/tests/test_lib_franta.py

logger = logging.getLogger(__name__)


def test_functie_descriere_tara():
<<<<<<<< HEAD:app/tests/test_lib_estonia.py
    expected_result = "Estonia se află la Marea Baltică, având câmpii joase, păduri dense, mii de lacuri, întinse zone umede și o coastă cu peste două mii de insule glaciale."
========
    expected_result = "Franța, oficial Republica Franceză, este un stat situat în principal în Europa de Vest. Este o putere globală majoră, având o influență imensă asupra culturii, istoriei, artei și politicii la nivel mondial, fiind și un membru fondator al Uniunii Europene."
>>>>>>>> origin/main_tuturluta_fabian:app/tests/test_lib_franta.py
    result = descriere_tara()
    assert result == expected_result, f"Test eșuat! Rezultatul funcției descriere_tara() este: {result}"
    logger.info("Merge functia descriere_tara")

def test_functie_populatie():
<<<<<<<< HEAD:app/tests/test_lib_estonia.py
    expected_result = "1.36 milioane de locuitori"
========
    expected_result = "Aproximativ 68 de milioane de locuitori"
>>>>>>>> origin/main_tuturluta_fabian:app/tests/test_lib_franta.py
    result = descriere_populatie()
    assert result == expected_result, f"Test eșuat! Rezultatul funcției descriere_populatie() este: {result}"
    logger.info("Merge functia descriere_populatie")


def test_functie_capitala():
<<<<<<<< HEAD:app/tests/test_lib_estonia.py

    expected_result = "Tallinn"
========
    expected_result = "Paris"
>>>>>>>> origin/main_tuturluta_fabian:app/tests/test_lib_franta.py
    result = descriere_capitala()
    assert result == expected_result, f"Test eșuat! Rezultatul funcției descriere_capitala() este: {result}"
    logger.info("Merge functia descriere_capitala")


def test_functie_limbi():
<<<<<<<< HEAD:app/tests/test_lib_estonia.py
    expected_result = "Estona"
========
    expected_result = "Franceza"
>>>>>>>> origin/main_tuturluta_fabian:app/tests/test_lib_franta.py
    result = descriere_limbi()
    assert result == expected_result, f"Test eșuat! Rezultatul funcției descriere_limbi() este: {result}"
    logger.info("Merge functia descriere_limbi")


if __name__ == "__main__":
    test_functie_descriere_tara()
    test_functie_populatie()
    test_functie_capitala()
    test_functie_limbi()