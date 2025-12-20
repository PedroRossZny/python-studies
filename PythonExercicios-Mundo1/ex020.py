from random import sample
a1 = input('\033[1;34mPrimeiro aluno: \033[m')
a2 = input('\033[1;34mSegundo aluno: \033[m')
a3 = input('\033[1;34mTerceiro aluno: \033[m')
a4 = input('\033[1;34mQuarto aluno: \033[m')
l = (a1, a2, a3, a4)
s = sample(l, 4)
print(f'\033[1;40mOrdem sorteada da apresentação dos alunoa (do primeiro ao último): \033[35m{s}\033[m')