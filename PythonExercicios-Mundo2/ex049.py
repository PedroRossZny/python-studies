n = int(input('\033[1;34mDigite um número inteiro: \033[m'))
print(f'\033[1;32mTABUADA\033[m')
for c in range(1, 11):
    print(f'\033[34m{n}\033[0m x \033[35m{c:2}\033[0m = \033[33m{n*c}\033[0m')