import logging
<<<<<<<< HEAD:app/tests/test_lib_coreea.py
from app.lib.biblioteca_coreea import descriere_tara, descriere_capitala, descriere_limbi, descriere_populatie
========
from app.lib.biblioteca_canada import descriere_tara, descriere_capitala, descriere_limbi, descriere_populatie
>>>>>>>> origin/dev_roseanu_vlad:app/tests/test_lib_canada.py

#from app.lib.biblioteca_<tara_mea> import descriere_tara, descriere_capitala, descriere_limbi, descriere_populatie

logger = logging.getLogger(__name__)


def test_functie_descriere_tara():
<<<<<<<< HEAD:app/tests/test_lib_coreea.py
    expected_result = "Este o țară din Asia de Est, care ocupă partea sudică a Peninsulei Coreene. Coreea de Sud se învecinează la nord cu Coreea de Nord și este înconjurată de Marea Japoniei la est, Marea Galbenă la vest, iar Strâmtoarea Coreei o desparte de Japonia."
========
    expected_result = "Canada este a doua țară ca mărime din lume, ocupând o mare parte din jumătatea nordică a Americii de Nord."
>>>>>>>> origin/dev_roseanu_vlad:app/tests/test_lib_canada.py
    result = descriere_tara()
    assert result == expected_result, f"Test eșuat! Rezultatul funcției descriere_tara() este: {result}"
    logger.info("Merge functia descriere_tara")

def test_functie_populatie():
<<<<<<<< HEAD:app/tests/test_lib_coreea.py
    expected_result = "51.1 milioane de locuitori"
========
    expected_result = "41,5 milioane de locuitori"
>>>>>>>> origin/dev_roseanu_vlad:app/tests/test_lib_canada.py
    result = descriere_populatie()
    assert result == expected_result, f"Test eșuat! Rezultatul funcției descriere_populatie() este: {result}"
    logger.info("Merge functia descriere_populatie")


def test_functie_capitala():
<<<<<<<< HEAD:app/tests/test_lib_coreea.py
    expected_result = "Seul"
========
    expected_result = "Ottawa"
>>>>>>>> origin/dev_roseanu_vlad:app/tests/test_lib_canada.py
    result = descriere_capitala()
    assert result == expected_result, f"Test eșuat! Rezultatul funcției descriere_capitala() este: {result}"
    logger.info("Merge functia descriere_capitala")


def test_functie_limbi():
<<<<<<<< HEAD:app/tests/test_lib_coreea.py
    expected_result = "Coreeana"
========
    expected_result = "Engleză, Franceză"
>>>>>>>> origin/dev_roseanu_vlad:app/tests/test_lib_canada.py
    result = descriere_limbi()
    assert result == expected_result, f"Test eșuat! Rezultatul funcției descriere_limbi() este: {result}"
    logger.info("Merge functia descriere_limbi")


if __name__ == "__main__":
    test_functie_descriere_tara()
    test_functie_populatie()
    test_functie_capitala()
    test_functie_limbi()
