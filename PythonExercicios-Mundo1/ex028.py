from random import randint
n = randint(0, 5)
nad = int(input('\033[1;34mTente adivinhar o número de 0 a 5: \033[m'))
if nad == n:
    print('\033[1;32mPARABÉNS! Você acertou!\033[m')
else:
    print('\033[1;31mNão foi dessa vez :(\033[m')
print(f'\033[1;40mO número sorteado foi: \033[33m{n}\033[m')