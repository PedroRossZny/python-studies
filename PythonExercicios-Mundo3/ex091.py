from random import randint
numero = []
jogadas = {}
ordenado = {}
jogada = con = 0
while con < 4:
    jogada = randint(1, 6)
    if jogada not in numero:
        numero.append(jogada)
        jogadas[f'jogador{con+1}'] = numero[con]
        con += 1
numero.sort(reverse=True)
j = 0
n = 0
while n < 4:
    if numero[n] == jogadas[f'jogador{j+1}']:
        ordenado[f'jogador{j+1}'] = numero[n]
        n += 1
        j = 0
    else:
        j += 1
print('\033[1;35;40m---- VALORES SORTEADOS ----\033[m')
for i, v in jogadas.items():
    print(f'\033[1;34;40m    O \033[37m{i}\033[34m tirou \033[35m{v}\033[34m     \033[m')
print('\n\033[1;35;40m-- RANKING DOS JOGADORES --\033[m')
lugar = 1
for i, v in ordenado.items():
    print(f'\033[1;33;40m  {lugar}ºlugar: \033[37m{i}\033[34m com \033[35m{v}  \033[m')
    lugar += 1