# ============================================================
# TRABALHO DE ADS - JOGO DA VELHA
# MÓDULO: MECÂNICA E REGRAS DO JOGO
# RESPONSÁVEL: [Seu Nome]
# ============================================================

def criar_tabuleiro():
    """Cria e retorna um tabuleiro vazio com 9 posições."""
    return [" "] * 9

def desenhar_tabuleiro(tabuleiro):
    """Exibe o tabuleiro formatado no terminal."""
    print("\n")
    print(f" {tabuleiro[0]} | {tabuleiro[1]} | {tabuleiro[2]} ")
    print("---|---|---")
    print(f" {tabuleiro[3]} | {tabuleiro[4]} | {tabuleiro[5]} ")
    print("---|---|---")
    print(f" {tabuleiro[6]} | {tabuleiro[7]} | {tabuleiro[8]} ")
    print("\n")

def verificar_vitoria(tabuleiro, jogador):
    """
    Verifica se o jogador venceu.
    Mapeia as 8 combinações possíveis (3 linhas, 3 colunas, 2 diagonais).
    """
    combinacoes = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Linhas
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Colunas
        [0, 4, 8], [2, 4, 6]               # Diagonais
    ]
    for c in combinacoes:
        if tabuleiro[c[0]] == tabuleiro[c[1]] == tabuleiro[c[2]] == jogador:
            return True
    return False

def verificar_empate(tabuleiro):
    """Retorna True se todas as posições estiverem preenchidas sem vencedor."""
    return " " not in tabuleiro

def jogar_partida():
    """
    Executa uma partida completa de Jogo da Velha entre 'X' e 'O'.
    Retorna o vencedor ('X' ou 'O') ou 'Empate'.
    """
    tabuleiro = criar_tabuleiro()
    jogador_atual = "X"

    print("\n--- INÍCIO DA PARTIDA ---")
    print("Mapa de posições do tabuleiro:")
    print(" 1 | 2 | 3 \n---|---|---\n 4 | 5 | 6 \n---|---|---\n 7 | 8 | 9 ")

    while True:
        desenhar_tabuleiro(tabuleiro)
        print(f"Vez do Jogador '{jogador_atual}'.")

        # Tratamento de exceções e validação de jogada
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

        # Aplica a jogada
        tabuleiro[posicao] = jogador_atual

        # Checa se o jogador atual venceu
        if verificar_vitoria(tabuleiro, jogador_atual):
            desenhar_tabuleiro(tabuleiro)
            print(f"🎉 O Jogador '{jogador_atual}' venceu esta partida!")
            return jogador_atual

        # Checa se deu empate
        if verificar_empate(tabuleiro):
            desenhar_tabuleiro(tabuleiro)
            print("🤝 Partida empatada (Deu Velha)!")
            return "Empate"

        # Alterna a vez entre X e O
        jogador_atual = "O" if jogador_atual == "X" else "X"
```