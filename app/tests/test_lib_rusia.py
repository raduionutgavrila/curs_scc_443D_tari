import logging
from app.lib.biblioteca_rusia import descriere_tara, descriere_capitala, descriere_limbi, descriere_populatie

logger = logging.getLogger(__name__)


def test_functie_descriere_tara():
    expected_result = "Rusia este cea mai întinsă țară din lume, situată în Europa de Est și Asia de Nord, cunoscută pentru capitala Moscova, patrimoniul cultural impresionant și diversitatea peisajelor naturale. Pentru acest proiect, accentul este pus pe atracțiile istorice și culturale, precum Kremlinul din Moscova, Piața Roșie, Muzeul Ermitaj din Sankt Petersburg și lacul Baikal, unul dintre cele mai adânci lacuri din lume. Rusia este recunoscută și pentru literatura, baletul și arhitectura sa, dar și pentru bucătăria tradițională, cu preparate precum borșul, pelmeni și blini."
    result = descriere_tara()
    assert result == expected_result, f"Test eșuat! Rezultatul funcției descriere_tara() este: {result}"
    logger.info("Merge functia descriere_tara")


def test_functie_populatie():
    expected_result = "Aproximativ 146 de milioane de locuitori"
    result = descriere_populatie()
    assert result == expected_result, f"Test eșuat! Rezultatul funcției descriere_populatie() este: {result}"
    logger.info("Merge functia descriere_populatie")


def test_functie_capitala():
    expected_result = "Moscova"
    result = descriere_capitala()
    assert result == expected_result, f"Test eșuat! Rezultatul funcției descriere_capitala() este: {result}"
    logger.info("Merge functia descriere_capitala")


def test_functie_limbi():
    expected_result = "Rusa"
    result = descriere_limbi()
    assert result == expected_result, f"Test eșuat! Rezultatul funcției descriere_limbi() este: {result}"
    logger.info("Merge functia descriere_limbi")


if __name__ == "__main__":
    test_functie_descriere_tara()
    test_functie_populatie()
    test_functie_capitala()
    test_functie_limbi()
