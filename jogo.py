def criar_tabuleiro():
    return [" "] * 9

def desenhar_tabuleiro(tabuleiro):
    print("\n")
    print(f" {tabuleiro[0]} | {tabuleiro[1]} | {tabuleiro[2]} ")
    print("---|---|---")
    print(f" {tabuleiro[3]} | {tabuleiro[4]} | {tabuleiro[5]} ")
    print("---|---|---")
    print(f" {tabuleiro[6]} | {tabuleiro[7]} | {tabuleiro[8]} ")
    print("\n")

def verificar_vitoria(tabuleiro, jogador):
    combinacoes = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  
        [0, 4, 8], [2, 4, 6]               
    ]
    for c in combinacoes:
        if tabuleiro[c[0]] == tabuleiro[c[1]] == tabuleiro[c[2]] == jogador:
            return True
    return False

def verificar_empate(tabuleiro):
    return " " not in tabuleiro

def jogar_partida():
    tabuleiro = criar_tabuleiro()
    jogador_atual = "X"

    print("\n--- INÍCIO DA PARTIDA ---")
    print("Mapa de posições do tabuleiro:")
    print(" 1 | 2 | 3 \n---|---|---\n 4 | 5 | 6 \n---|---|---\n 7 | 8 | 9 ")

    while True:
        desenhar_tabuleiro(tabuleiro)
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

        
        if verificar_vitoria(tabuleiro, jogador_atual):
            desenhar_tabuleiro(tabuleiro)
            print(f"🎉 O Jogador '{jogador_atual}' venceu esta partida!")
            return jogador_atual

        
        if verificar_empate(tabuleiro):
            desenhar_tabuleiro(tabuleiro)
            print("🤝 Partida empatada (Deu Velha)!")
            return "Empate"

        
        jogador_atual = "O" if jogador_atual == "X" else "X"
```