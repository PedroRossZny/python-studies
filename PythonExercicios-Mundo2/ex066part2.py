c = s = 0
while True:
    n = int(input('\033[1;34mDigite um número inteiro \033[33m(999 para parar)\033[34m: \033[m'))
    if n == 999:
        break
    else:
        c += 1
        s += n
print(f'\033[1;34;40mForam digitados \033[33m{c}\033[34m números e a soma entre eles vale: \033[33m{s}\033[m')