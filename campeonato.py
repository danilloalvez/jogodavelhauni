Python
print("========================================")
print("   SISTEMA DE CAMPEONATO: MELHOR DE N   ")
print("========================================\n")

n_partidas = int(input("Digite o número total de partidas da série (ex: 3, 5, 7): ")
                 
vitorias_necessarias = (n_partidas // 2) + 1

print(f"\nRegra da Série: Quem atingir {vitorias_necessarias} vitórias primeiro é o campeão!")
print("-" * 40)

jogador1 = input("Nome do Jogador 1: ")
jogador2 = input("Nome do Jogador 2: ")

vitorias_j1 = 0
vitorias_j2 = 0
partida_atual = 1

while vitorias_j1 < vitorias_necessarias and vitorias_j2 < vitorias_necessarias and partida_atual <= n_partidas:
    print(f"\n--- Partida {partida_atual} de {n_partidas} ---")
    print(f"Placar atual da série -> {jogador1}: {vitorias_j1} | {jogador2}: {vitorias_j2}")
    
    vencedor = input(f"Quem venceu a partida {partida_atual}? (Digite 1 para {jogador1} / 2 para {jogador2}): ")
    
    if vencedor == "1":
        vitorias_j1 += 1
        print(f"-> Ponto para {jogador1}!")
        partida_atual += 1
    elif vencedor == "2":
        vitorias_j2 += 1
        print(f"-> Ponto para {jogador2}!")
        partida_atual += 1
    else:
        print("[Erro] Entrada inválida! Digite apenas 1 ou 2. A partida será repetida.")

print("\n" + "=" * 40)
print("          FIM DA SÉRIE!          ")
print("=" * 40)
print(f"Placar Final: {jogador1} {vitorias_j1} x {vitorias_j2} {jogador2}\n")

if vitorias_j1 >= vitorias_necessarias:
    print(f"O GRANDE CAMPEÃO É: {jogador1.upper()}!")
elif vitorias_j2 >= vitorias_necessarias:
    print(f"O GRANDE CAMPEÃO É: {jogador2.upper()}!")
else:
    print("A série terminou sem um vencedor definido.")
