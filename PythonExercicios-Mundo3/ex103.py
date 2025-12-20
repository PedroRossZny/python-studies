def ficha(a='<desconhecido>', b=0):
    """
    → Monta a ficha de um jogador e a mostra.
    :param a: Nome do jogador.
    :param b: Quantidade de gols feitos pelo jogador.
    :return: Ficha do jogador.
    """
    print(f'\033[1;34mO jogador \033[33m{a}\033[34m fez \033[33m{b}\033[34m gol(s) no campeonato.\033[m')


nome = str(input('\033[1;34mNome do Jogador: \033[m'))
gols = str(input('\033[1;34mNúmero de gols: \033[m'))
if nome == '' and gols == '':
    ficha()
elif nome == '':
    ficha('<desconhecido>', int(gols))
elif gols == '':
    ficha(nome, 0)
else:
    ficha(nome, int(gols))
help(ficha)