import pytest
from forca import Forca

@pytest.fixture
def jogo():
    return Forca()
def left(s, amount):
    return s[:amount]

def test_estado_inicial(jogo):
    """Verifica se o jogo inicia corretamente"""
    assert jogo.tentativas == 6, "Testa se tentativa inicia com valor 6"
    assert jogo.letras_corretas == set(), "Testa se as letras corretas inicia vazias"
    assert jogo.jogo_acabou() == False
    assert len(jogo.palavra) != 0

def test_mostrar_palavra(jogo):
    """Testa se a palavra é mostrada corretamente"""
    assert jogo.mostrar_palavra() == left("_ " * len(jogo.palavra), len(jogo.palavra) * 2 - 1), "Testa se a palavra inicial está vazia"


@pytest.mark.parametrize("letra", ["a", "c", "b", "t"])
def test_tentar_variacoes_letra(jogo, letra):
    """Testa letras diferentes que devem constar"""
    jogo.tentar_letra(letra)
    assert letra in jogo.letras_corretas