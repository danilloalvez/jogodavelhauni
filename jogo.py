
tabuleiro = [
    [" ", " ", " "],
    [" ", " ", " "],
    [" ", " ", " "]
]

jogador_atual = "X"
jogando = True

print("--- INÍCIO DA PARTIDA DE JOGO DA VELHA ---")
print("Esquema de posições do tabuleiro:")
print(" 1 | 2 | 3 ")
print("---|---|---")
print(" 4 | 5 | 6 ")
print("---|---|---")
print(" 7 | 8 | 9 ")


while jogando:
    
    print()
    for i in range(3):
        linha_str = " "
        for j in range(3):
            linha_str = linha_str + tabuleiro[i][j]
            if j < 2:
                linha_str = linha_str + " | "
        print(linha_str)
        if i < 2:
            print("---|---|---")
    print()

    print("Vez do jogador: " + jogador_atual)
    posicao = int(input("Escolha uma posição livre (1-9): "))

    
    if posicao < 1 or posicao > 9:
        print(">> Posição inválida! Digite um número entre 1 e 9.")
    else:
        
        linha = (posicao - 1) // 3
        coluna = (posicao - 1) % 3

        
        if tabuleiro[linha][coluna] != " ":
            print(">> Posição já ocupada! Escolha outro local.")
        else:
            
            tabuleiro[linha][coluna] = jogador_atual

            
            vitoria = False

            
            for i in range(3):
                if tabuleiro[i][0] != " " and tabuleiro[i][0] == tabuleiro[i][1] and tabuleiro[i][1] == tabuleiro[i][2]:
                    vitoria = True

            
            for j in range(3):
                if tabuleiro[0][j] != " " and tabuleiro[0][j] == tabuleiro[1][j] and tabuleiro[1][j] == tabuleiro[2][j]:
                    vitoria = True

            
            if tabuleiro[0][0] != " " and tabuleiro[0][0] == tabuleiro[1][1] and tabuleiro[1][1] == tabuleiro[2][2]:
                vitoria = True
            if tabuleiro[0][2] != " " and tabuleiro[0][2] == tabuleiro[1][1] and tabuleiro[1][1] == tabuleiro[2][0]:
                vitoria = True

            
            if vitoria:
                
                print()
                for i in range(3):
                    linha_str = " "
                    for j in range(3):
                        linha_str = linha_str + tabuleiro[i][j]
                        if j < 2:
                            linha_str = linha_str + " | "
                    print(linha_str)
                    if i < 2:
                        print("---|---|---")
                print()
                print("🎉 PARABÉNS! O jogador " + jogador_atual + " venceu a partida!")
                jogando = False

            else:
                
                espacos_vazios = 0
                for i in range(3):
                    for j in range(3):
                        if tabuleiro[i][j] == " ":
                            espacos_vazios = espacos_vazios + 1

                if espacos_vazios == 0:
                    
                    print()
                    for i in range(3):
                        linha_str = " "
                        for j in range(3):
                            linha_str = linha_str + tabuleiro[i][j]
                            if j < 2:
                                linha_str = linha_str + " | "
                        print(linha_str)
                        if i < 2:
                            print("---|---|---")
                    print()
                    print("🤝 EMPATE! O tabuleiro está cheio (Deu Velha).")
                    jogando = False
                else:
                    
                    if jogador_atual == "X":
                        jogador_atual = "O"
                    else:
                        jogador_atual = "X"
```
