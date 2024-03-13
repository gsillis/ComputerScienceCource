def computador_escolhe_jogada (n, m):
    removes = 1

    while removes != m:
        if (n - removes) % (m + 1) == 0:
            return removes
        else:
            removes += 1
    return removes


def usuario_escolhe_jogada(n, m):
    is_valid_move = False

    while not is_valid_move:
        out = int(input("Quantas peças você vai tirar? "))
        if out > m or out < 1:
            print("Oops! Jogada inválida! Tente de novo.")
        else:
            is_valid_move = True

    return out


def campeonato():
    round = 1

    while round <= 3:
        print(f"**** Rodada {round} ****")
        partida()
        round += 1
    print("Placar: Você 0 X 3 Computador")


def partida():
    n = int(input("Quantas peças? "))
    m = int(input("Limite de peças por jogada? "))

    is_computer_round = False

    if n % (m + 1) == 0:
        print("Voce começa!")

    else:
        print("Computador começa!")
        is_computer_round = True

    while n > 0:
        if is_computer_round:
            commputer_round = computador_escolhe_jogada(n, m)
            n -= commputer_round
            if commputer_round == 1:
                print("O computador tirou uma peça")
            else:
                print(f"O computador tirou {commputer_round} peças")
            is_computer_round = False
        else:
            player_round = usuario_escolhe_jogada(n, m)
            n -= player_round
            if player_round == 1:
                print("Você tirou uma peça")
            else:
                print(f"Você tirou {player_round} peças")
            is_computer_round = True

        if n == 1:
            print("Agora resta apenas uma peça no tabuleiro.")
        else:
            if n != 0:
                print(f"Agora restam {n} peças no tabuleiro.")
                print()

    print("Fim do jogo! O computador ganhou!")

print("Bem-vindo ao jogo do NIM! Escolha:")

print("1 - para jogar uma partida isolada")

game_mode = int(input("2 - para jogar um campeonato "))

if game_mode == 2:
    print("Voce escolheu um campeonato!")
    campeonato()
else:
    if game_mode == 1:
        partida()