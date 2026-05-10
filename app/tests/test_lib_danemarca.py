from app.lib.biblioteca_danemarca import descriere_tara, descriere_capitala

def test_descriere_tara():
    assert "Danemarca" in descriere_tara()

def test_descriere_capitala():
    assert "Copenhaga" in descriere_capitala()
