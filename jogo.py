tabuleiro = [" "] * 9
jogador_atual = "X"
vencedor = None
partida_em_andamento = True

print("\n--- INÍCIO DA PARTIDA ---")
print("Mapa de posições do tabuleiro:")
print(" 1 | 2 | 3 \n---|---|---\n 4 | 5 | 6 \n---|---|---\n 7 | 8 | 9 ")


while partida_em_andamento:
    
    print("\n")
    print(f" {tabuleiro[0]} | {tabuleiro[1]} | {tabuleiro[2]} ")
    print("---|---|---")
    print(f" {tabuleiro[3]} | {tabuleiro[4]} | {tabuleiro[5]} ")
    print("---|---|---")
    print(f" {tabuleiro[6]} | {tabuleiro[7]} | {tabuleiro[8]} ")
    print("\n")

    print(f"Vez do Jogador '{jogador_atual}'.")

    
    try:
        posicao = int(input("Escolha uma posição livre (1-9): ")) - 1
        if posicao < 0 or posicao > 8:
            print("\n>> Posição inválida! Escolha um número de 1 a 9.")
            continue
        if tabuleiro[posicao] != " ":
            print("\n>> Posição já ocupada! Escolha outro local.")
            continue
    except ValueError:
        print("\n>> Entrada inválida! Digite apenas números inteiros.")
        continue

    
    tabuleiro[posicao] = jogador_atual

    
    combinacoes = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  
        [0, 4, 8], [2, 4, 6]               
    ]

    houve_vitoria = False
    for c in combinacoes:
        if tabuleiro[c[0]] == tabuleiro[c[1]] == tabuleiro[c[2]] == jogador_atual:
            houve_vitoria = True
            break

    
    if houve_vitoria:
        print("\n")
        print(f" {tabuleiro[0]} | {tabuleiro[1]} | {tabuleiro[2]} ")
        print("---|---|---")
        print(f" {tabuleiro[3]} | {tabuleiro[4]} | {tabuleiro[5]} ")
        print("---|---|---")
        print(f" {tabuleiro[6]} | {tabuleiro[7]} | {tabuleiro[8]} ")
        print("\n")
        print(f"🎉 O Jogador '{jogador_atual}' venceu esta partida!")
        vencedor = jogador_atual
        partida_em_andamento = False

    
    elif " " not in tabuleiro:
        print("\n")
        print(f" {tabuleiro[0]} | {tabuleiro[1]} | {tabuleiro[2]} ")
        print("---|---|---")
        print(f" {tabuleiro[3]} | {tabuleiro[4]} | {tabuleiro[5]} ")
        print("---|---|---")
        print(f" {tabuleiro[6]} | {tabuleiro[7]} | {tabuleiro[8]} ")
        print("\n")
        print("🤝 Partida empatada (Deu Velha)!")
        vencedor = "Empate"
        partida_em_andamento = False

    
    else:
        if jogador_atual == "X":
            jogador_atual = "O"
        else:
            jogador_atual = "X"
```