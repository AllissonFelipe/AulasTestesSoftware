import pytest 
from forca import Forca


@pytest.fixture
def jogo():
    return Forca()

def test_estado_inicial(jogo):
    """Verifica se o jogo inicia corretamente"""
    assert jogo.tentativas == 6
    assert jogo.letras_corretas == set()