import logging
from app.lib.biblioteca_china import descriere_tara, descriere_capitala, descriere_limbi, descriere_populatie

#from app.lib.biblioteca_<tara_mea> import descriere_tara, descriere_capitala, descriere_limbi, descriere_populatie

logger = logging.getLogger(__name__)


def test_functie_descriere_tara():
    expected_result = "China , denumită oficial Republica Populară Chineză, este un stat independent situat în Asia de Est. Este a doua cea mai populată țară din lume, cu o populație de aproximativ 1.409.000.000 de locuitori. China are un sistem unipartid, condus de către Partidul Comunist Chinez, având sediul guvernamental în orașul-capitală Beijing. Acesta exercită jurisdicție peste 22 de provincii, cinci regiuni autonome, patru municipii de subordonare centrală (Beijing, Tianjin, Shanghai și Chongqing) și două regiuni administrative speciale, având în mare parte un sistem de autoguvernare (Hong Kong și Macao)."
    result = descriere_tara()
    assert result == expected_result, f"Test eșuat! Rezultatul funcției descriere_tara() este: {result}"
    logger.info("Merge functia descriere_tara")

def test_functie_populatie():
    expected_result = "1,404,890,000 chinezi"
    result = descriere_populatie()
    assert result == expected_result, f"Test eșuat! Rezultatul funcției descriere_populatie() este: {result}"
    logger.info("Merge functia descriere_populatie")


def test_functie_capitala():
    expected_result = "Beijing"
    result = descriere_capitala()
    assert result == expected_result, f"Test eșuat! Rezultatul funcției descriere_capitala() este: {result}"
    logger.info("Merge functia descriere_capitala")


def test_functie_limbi():
    expected_result = "Chineza"
    result = descriere_limbi()
    assert result == expected_result, f"Test eșuat! Rezultatul funcției descriere_limbi() este: {result}"
    logger.info("Merge functia descriere_limbi")


if __name__ == "__main__":
    test_functie_descriere_tara()
    test_functie_populatie()
    test_functie_capitala()
    test_functie_limbi()
