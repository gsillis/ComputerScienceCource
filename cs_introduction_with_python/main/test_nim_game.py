from nim_game import computador_escolhe_jogada

def test_computador_escolhe_jogada ():
    sut = computador_escolhe_jogada(3, 2)
    assert sut == 2