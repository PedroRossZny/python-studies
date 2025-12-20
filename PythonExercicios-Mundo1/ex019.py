from random import choice
a1 = input('\033[1;34mPrimeiro aluno: \033[m')
a2 = input('\033[1;34mSegundo aluno: \033[m')
a3 = input('\033[1;34mTerceiro aluno: \033[m')
a4 = input('\033[1;34mQuarto aluno: \033[m')
l = (a1, a2, a3, a4)
s = choice(l)
print(f'\033[1;34mO aluno sorteado foi: \033[33m{s}\033[m')