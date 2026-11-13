print("===== CAMPEONATO DE JOGO DA VELHA =====")

vitorias_jogador = 0
vitorias_adversario = 0
jogador1 = ""
jogador2 = ""

executando_programa = True
while executando_programa:
    print("\n1 - Jogar")
    print("2 - Ver regras")
    print("3 - Ver placar")
    print("4 - Sair")
    
    opcao_valida = False
    opcao = ""
    while opcao_valida == False:
        opcao = input("Escolha uma opção: ")
        for n in range(1, 5):
            if opcao == str(n):
                opcao_valida = True
        if opcao_valida == False:
            print("Opção inválida! Escolha uma opção entre 1 e 4.")

    if opcao == "4":
        print("\nObrigado por jogar!")
        print("Programa encerrado!")
        executando_programa = False

    elif opcao == "1":
        print("\n===== INICIAR CAMPEONATO =====")
        print("1 - Melhor de 3")
        print("2 - Melhor de 5")
        print("3 - Personalizado")

        modo_valido = False
        modo = ""
        while modo_valido == False:
            modo = input("Escolha o tipo de campeonato: ")
            for n in range(1, 4):
                if modo == str(n):
                    modo_valido = True
            if modo_valido == False:
                print("Opção inválida! Digite 1, 2 ou 3.")

        n_partidas = 0

        if modo == "1":
            n_partidas = 3
        elif modo == "2":
            n_partidas = 5
        elif modo == "3":
    
            numero_valido = False
            while numero_valido == False:
                entrada_impar = input("Digite o número ímpar de partidas (ex: 7, 9): ")
    
                eh_numero = False
                for n in range(1, 100, 2):
                    if entrada_impar == str(n):
                        eh_numero = True
                
                if eh_numero:
                    n_partidas = int(entrada_impar)
                    numero_valido = True
                else:
                    print("Por favor, digite um número ímpar maior que zero!")

        if n_partidas > 0:
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

                print("\n===== PARTIDA", partida_atual, "=====")
                print(jogador1, "é X")
                print(jogador2, "é O")

                while jogando:
                    print("\n 1 | 2 | 3")
                    print("---|---|---")
                    print(" 4 | 5 | 6")
                    print("---|---|---")
                    print(" 7 | 8 | 9")

                    print("\nTabuleiro atual:")
            
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
                        print("\nVez de", jogador1, "(X)")
                    else:
                        print("\nVez de", jogador2, "(O)")

                    posicao_valida = False
                    posicao_str = ""
                    while posicao_valida == False:
                        posicao_str = input("Escolha uma posição (1-9): ")
                        for n in range(1, 10):
                            if posicao_str == str(n):
                                posicao_valida = True
                        if posicao_valida == False:
                            print("Entrada inválida! Digite um número de 1 a 9.")

                    posicao = int(posicao_str)
                    linha = (posicao - 1) // 3
                    coluna = (posicao - 1) % 3

                
                    if tabuleiro[linha][coluna] != " ":
                        print("Posição ocupada! Escolha outra.")
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

                            if (
                                tabuleiro[0][i] != " "
                                and tabuleiro[0][i] == tabuleiro[1][i]
                                and tabuleiro[1][i] == tabuleiro[2][i]
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
                                print("\nEmpate! Ninguém pontuou nesta rodada.")
                                jogando = False
                            else:
                                jogador_atual = "O" if jogador_atual == "X" else "X"

                print("\n===== PLACAR DO CAMPEONATO =====")
                print(jogador1, ":", vitorias_jogador)
                print(jogador2, ":", vitorias_adversario)

                partida_atual += 1

            print("\n===== FIM DO CAMPEONATO =====")
            if vitorias_jogador > vitorias_adversario:
                print("CAMPEÃO:", jogador1)
            else:
                print("CAMPEÃO:", jogador2)

            print("Placar final:")
            print(jogador1, vitorias_jogador, "x", vitorias_adversario, jogador2)

    elif opcao == "2":
        print("\n===== REGRAS DO CAMPEONATO =====")
        print("1. Tipos de Campeonato:")
        print("   - Melhor de 3: Vence quem ganhar 2 partidas.")
        print("   - Melhor de 5: Vence quem ganhar 3 partidas.")
        print("   - Personalizado: Vence quem alcançar a maioria dos pontos necessários.")
        print("\n2. Dinâmica do Jogo:")
        print("   - O Jogador 1 joga sempre com o 'X' e começa a partida.")
        print("   - O Jogador 2 joga com o 'O'.")
        print("   - O tabuleiro possui posições numeradas de 1 a 9.")
        print("\n3. Pontuação e Empates:")
        print("   - Cada vitória vale 1 ponto para o placar da rodada.")
        print("   - Caso dê velha (empate no tabuleiro), a partida termina sem pontuação para ninguém.")
        print("\n4. Objetivo:")
        print("   - Alinhar 3 símbolos iguais (horizontal, vertical ou diagonal) antes do adversário.")

    elif opcao == "3":
        print("\n===== PLACAR =====")
        print("Vitórias de", jogador1 or "Jogador 1", ":", vitorias_jogador)
        print("Vitórias de", jogador2 or "Jogador 2", ":", vitorias_adversario)
