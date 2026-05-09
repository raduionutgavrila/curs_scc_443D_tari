from app.lib.danemarca import capitala_danemarca

def test_capitala():
    assert "Copenhaga" in capitala_danemarca()
