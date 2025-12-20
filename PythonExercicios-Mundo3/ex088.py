from random import randint
quantidade = int(input('\033[1;34mQuantos jogos você quer que eu sorteie? \033[m'))
dados = []
jogos = []
for j in range(0, quantidade):
    cont = 0
    while True:
        num = randint(1, 60)
        if num not in dados:
            dados.append(num)
            cont += 1
        if cont == 6:
            break
    jogos.append(dados[:])
    dados.clear()
for n, j in enumerate(jogos):
    print(f'\033[1;33mJogo {n+1}:\033[35m {sorted(j)}\033[m')