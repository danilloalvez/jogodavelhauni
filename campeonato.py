
print("===== CAMPEONATO DE JOGO DA VELHA =====")
print("1 - Jogar")
print("2 - Ver regras")
print("3 - Ver placar")
print("4 - Sair")

vitorias_jogador = 0
vitorias_adversario = 0
jogador1 = ""
jogador2 = ""

opcao = input("Escolha uma opção:")

while opcao != "4":

    if opcao == "1":

        print("\n===== INICIAR CAMPEONATO =====")
        print("1 - Melhor de 3")
        print("2 - Melhor de 5")
        print("3 - Personalizado")

        modo = input("Escolha o tipo de campeonato:")

        if modo == "1":
            n_partidas = 3
        elif modo == "2":
            n_partidas = 5
        elif modo == "3":
            n_partidas = int(input("Digite o número ímpar de partidas: "))
        else:
            print("Opção inválida!")
            n_partidas = 0

        if n_partidas > 0:

            if n_partidas % 2 == 0:
                print("Digite um número ímpar de partidas!")

            else:

                jogador1 = input("Nome do Jogador 1: ")
                jogador2 = input("Nome do Jogador 2: ")

                vitorias_jogador = 0
                vitorias_adversario = 0

                vitorias_necessarias = (n_partidas // 2) + 1
                partida_atual = 1

                print("\nCampeonato iniciado!")
                print("Vitórias necessárias:", vitorias_necessarias)

                while (
                    vitorias_jogador < vitorias_necessarias
                    and vitorias_adversario < vitorias_necessarias
                ):

                    tabuleiro = [
                        [" ", " ", " "],
                        [" ", " ", " "],
                        [" ", " ", " "]
                    ]

                    jogador_atual = "X"
                    jogando = True
                    vitoria = False

                    print("\n===== PARTIDA", partida_atual, "=====")
                    print(jogador1, "é X")
                    print(jogador2, "é O")

                    while jogando:

                        print("\n 1 | 2 | 3")
                        print("---|---|---")
                        print(" 4 | 5 | 6")
                        print("---|---|---")
                        print(" 7 | 8 | 9")

                        print("\nTabuleiro:")

                        for i in range(3):
                            linha_str = " "
                            for j in range(3):
                                linha_str = linha_str + tabuleiro[i][j]
                                if j < 2:
                                    linha_str = linha_str + " | "
                            print(linha_str)
                            if i < 2:
                                print("---|---|---")

                        if jogador_atual == "X":
                            print("\nVez de", jogador1)
                        else:
                            print("\nVez de", jogador2)

                        posicao = int(input("Escolha uma posição (1-9): "))

                        if posicao < 1 or posicao > 9:
                            print("Posição inválida!")

                        else:

                            linha = (posicao - 1) // 3
                            coluna = (posicao - 1) % 3

                            if tabuleiro[linha][coluna] != " ":
                                print("Posição ocupada!")

                            else:

                                tabuleiro[linha][coluna] = jogador_atual

                                vitoria = False

                                for i in range(3):
                                    if (
                                        tabuleiro[i][0] != " "
                                        and tabuleiro[i][0] == tabuleiro[i][1]
                                        and tabuleiro[i][1] == tabuleiro[i][2]
                                    ):
                                        vitoria = True

                                for j in range(3):
                                    if (
                                        tabuleiro[0][j] != " "
                                        and tabuleiro[0][j] == tabuleiro[1][j]
                                        and tabuleiro[1][j] == tabuleiro[2][j]
                                    ):
                                        vitoria = True

                                if (
                                    tabuleiro[0][0] != " "
                                    and tabuleiro[0][0] == tabuleiro[1][1]
                                    and tabuleiro[1][1] == tabuleiro[2][2]
                                ):
                                    vitoria = True

                                if (
                                    tabuleiro[0][2] != " "
                                    and tabuleiro[0][2] == tabuleiro[1][1]
                                    and tabuleiro[1][1] == tabuleiro[2][0]
                                ):
                                    vitoria = True

                                if vitoria:

                                    print("\n===== RESULTADO DA PARTIDA =====")

                                    for i in range(3):
                                        linha_str = " "
                                        for j in range(3):
                                            linha_str = linha_str + tabuleiro[i][j]
                                            if j < 2:
                                                linha_str = linha_str + " | "
                                        print(linha_str)
                                        if i < 2:
                                            print("---|---|---")

                                    if jogador_atual == "X":
                                        print("Vitória de", jogador1)
                                        vitorias_jogador += 1
                                    else:
                                        print("Vitória de", jogador2)
                                        vitorias_adversario += 1

                                    jogando = False

                                else:

                                    espacos_vazios = 0

                                    for i in range(3):
                                        for j in range(3):
                                            if tabuleiro[i][j] == " ":
                                                espacos_vazios += 1

                                    if espacos_vazios == 0:
                                        print("\nEmpate! Ninguém pontuou.")
                                        jogando = False

                                    else:

                                        if jogador_atual == "X":
                                            jogador_atual = "O"
                                        else:
                                            jogador_atual = "X"

                    print("\n===== PLACAR DO CAMPEONATO =====")
                    print(jogador1, ":", vitorias_jogador)
                    print(jogador2, ":", vitorias_adversario)

                    partida_atual += 1

                print("\n===== FIM DO CAMPEONATO =====")

                if vitorias_jogador > vitorias_adversario:
                    print("CAMPEÃO:", jogador1.upper())
                else:
                    print("CAMPEÃO:", jogador2.upper())

                print("Placar final:")
                print(jogador1, vitorias_jogador, "x",
                      vitorias_adversario, jogador2)

    elif opcao == "2":

        print("\n===== REGRAS =====")
        print("Melhor de 3: vence quem ganhar 2 partidas.")
        print("Melhor de 5: vence quem ganhar 3 partidas.")
        print("Personalizado: vence quem ganhar a maioria.")
        print("O jogador X começa a partida.")
        print("Cada vitória vale um ponto.")
        print("Empate não conta ponto.")

    elif opcao == "3":

        print("\n===== PLACAR =====")
        print("Vitórias de", jogador1 or "Jogador 1", ":", vitorias_jogador)
        print("Vitórias de", jogador2 or "Jogador 2", ":", vitorias_adversario)

    else:
        print("Opção inválida!")

    print("\n===== CAMPEONATO DE JOGO DA VELHA =====")
    print("1 - Jogar")
    print("2 - Ver regras")
    print("3 - Ver placar")
    print("4 - Sair")

    opcao = input("Escolha uma opção:")

print("\nObrigado por jogar!")
print("Programa encerrado!")
