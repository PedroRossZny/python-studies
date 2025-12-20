from datetime import date
ma = me = 0
atual = date.today().year
for c in range(0, 7):
    ano = int(input('\033[1;34mAno de nascimento: \033[m'))
    if (atual - ano) < 18:
        me += 1
    else:
        ma += 1
print(f'\033[1;34m{me}\033[0m pessoas ainda \033[1;31mNÃO\033[0m atingiram a maioridade.\n'
      f'E \033[1;34m{ma} \033[m\033[1;32mJÁ\033[0m são maiores de idade.')