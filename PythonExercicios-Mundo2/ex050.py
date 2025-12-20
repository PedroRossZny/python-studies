s = 0
for c in range(0, 6):
    n = int(input('\033[1;34mDigite um número inteiro: \033[m'))
    if n % 2 == 0:
        s += n
print(f'\033[1;34mSoma dos números pares: \033[33m{s}\033[m')