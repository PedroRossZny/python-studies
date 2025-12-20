n = 1
par = ímpar = 0
while n != 0:
    n = int(input('Digite um valor: '))
    if n != 0:
        if n % 2 == 0:
            par += 1
        else:
            ímpar += 1
print(f'Você digitou {par} número pares e {ímpar} números ímpares!')