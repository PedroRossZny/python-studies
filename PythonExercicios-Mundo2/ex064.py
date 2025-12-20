n = c = s = 0
while n != 999:
    n = int(input('\033[1;34mDigite um número inteiro \033[33m(999 para parar)\033[34m: \033[m'))
    if n != 999:
        c += 1
        s += n
print(f'\033[1;34mForam digitados \033[33m{c}\033[34m números\nA soma entre eles vale: \033[33m{s}\033[m')