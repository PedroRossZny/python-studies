dados = dict()
gols = list()
total = 0
dados['nome'] = str(input('\033[1;34mNome do Jogador: \033[m'))
partidas = int(input(f'\033[1;34mQuantas partidas \033[33m{dados["nome"]}\033[34m jogou? \033[m'))
for p in range(1, partidas+1):
    gol = int(input(f'\033[1;34mQuantos gols na \033[33m{p}ª\033[34m partida? \033[m'))
    gols.append(gol)
    total += gol
dados['gols'] = gols
dados['total'] = total
print('\033[1;35;40m-\033[m' * 36)
print(f'\033[1;34;40mNome do Jogador: \033[33m{dados["nome"]}              \033[m')
print(f'\033[1;35;40m--O jogador {dados["nome"]} jogou {partidas} partidas--\033[m')
for p in range(0, partidas):
    print(f'\033[1;34;40mNa \033[33m{p+1}ª\033[34m partida, fez \033[35m{gols[p]}\033[34m gol(s).        \033[m')
print(f'\033[1;34;40mFoi um Total de \033[33m{dados["total"]}\033[34m gols.             \033[m')
print('\033[1;35;40m-\033[m' * 36)