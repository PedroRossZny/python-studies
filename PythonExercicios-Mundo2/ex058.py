from random import randint
t = 0
p = 11
c = randint(0, 10)
while p != c:
    if t == 0:
        p = int(input('\033[1;34mTente adivinhar um número de 0 a 10: \033[m'))
        t = 1
    else:
        p = int(input('\033[31mAinda não acertou! Escolha outro número: \033[m'))
        t += 1
    if p == c:
        print(f'\033[1;32mPARABÉNS! Você acertou!\nForam \033[33m{t}\033[32m tentativas!\033[m')
