from datetime import date
def voto():
    """
    → Calcula qual a situação de votação.
    :return: NEGADO/OBRIGATÓRIO/OPCIONAL.
    """
    global nasc
    idade = date.today().year - nasc
    if idade < 16:
        print(f'\033[1;34mCom \033[33m{idade}\033[34m anos:\033[35m VOTO NEGADO.\033[m')
    elif 18 <= idade <= 65:
        print(f'\033[1;34mCom \033[33m{idade}\033[34m anos:\033[35m VOTO OBRIGATÓRIO.\033[m')
    elif 16 <= idade < 18 or idade > 65:
        print(f'\033[1;34mCom \033[33m{idade}\033[34m anos:\033[35m VOTO OPCIONAL.\033[m')


nasc = int(input('\033[1;34mEm que ano você nasceu? \033[m'))
voto()
help(voto)
