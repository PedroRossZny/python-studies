listatotal = list()
dados = dict()
gols = list()
total = 0
while True:
    dados['nome'] = str(input('\033[1;34mNome do Jogador: \033[m'))
    partidas = int(input(f'\033[1;34mQuantas partidas \033[33m{dados["nome"]}\033[34m jogou? \033[m'))
    for p in range(1, partidas+1):
        gol = int(input(f'\033[1;34mQuantos gols na \033[33m{p}ª\033[34m partida? \033[m'))
        gols.append(gol)
        total += gol
    dados['gols'] = gols
    dados['total'] = total
    dados['totalpartidas'] = partidas
    listatotal.append(dados)
    del gols
    del dados
    total = 0
    gols = list()
    dados = dict()
    continuar = 'A'
    while continuar not in 'SN':
        continuar = str(input('\033[1;34mQuer continuar? \033[33m[S/N] \033[m')).strip().upper()[0]
    if continuar == 'N':
        break
print('\033[1;35m-\033[m' * 36)
print('\033[1;35m|Nº|NOME    |GOLS            |TOTAL|\033[m')
print('\033[1;35m-\033[m' * 36)
for n, p in enumerate(listatotal):
    print(f'\033[1;35m|\033[37m{n:<2}\033[35m|\033[37m{p["nome"]:<8}\033[35m|\033[37m{str(p["gols"]):<16}\033[35m|\033[37m{p["total"]:<5}\033[35m|\033[m')
print('\033[1;35m-\033[m' * 36)
seguir = 'A'
while seguir not in 'SN':
    seguir = str(input('\033[1;34mQuer mostrar os dados de algum jogador? \033[33m[S/N] \033[m')).strip().upper()[0]
if seguir == 'S':
    while True:
        jogador = int(input('\033[1;34mMostrar dados de qual jogador? \033[m'))
        if jogador > (len(listatotal) - 1) or jogador < 0:
            print('\033[1;31mEste jogador não existe. Tente novamente.\033[m')
        else:
            print(f'\033[1;34mNome do Jogador: \033[33m{listatotal[jogador]["nome"]}              \033[m')
            print(f'\033[1;35m--O jogador {listatotal[jogador]["nome"]} jogou {listatotal[jogador]["totalpartidas"]} partidas--\033[m')
            for p in range(0, listatotal[jogador]['totalpartidas']):
                print(f'\033[1;34mNa \033[33m{p + 1}ª\033[34m partida, fez \033[35m{listatotal[jogador]["gols"][p]}\033[34m gol(s).        \033[m')
            print(f'\033[1;34mFoi um Total de \033[33m{listatotal[jogador]["total"]}\033[34m gols.             \033[m')
            print('\033[1;35m-\033[m' * 36)
            continuar = 'A'
            while continuar not in 'SN':
                continuar = str(input('\033[1;34mQuer continuar? \033[33m[S/N] \033[m')).strip().upper()[0]
            if continuar == 'N':
                break
print('\033[1;32mVOLTE SEMPRE!\033[m')
