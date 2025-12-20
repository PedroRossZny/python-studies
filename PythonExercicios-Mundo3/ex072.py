numeros = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco',
           'seis', 'sete', 'oito', 'nove', 'dez',
           'onze', 'doze', 'treze', 'quatorze', 'quinze',
           'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')
while True:
    while True:
        escolhido = int(input('\033[1;34mDigite um número entre 0 e 20: \033[m'))
        if 0 <= escolhido <=20:
            break
        print('\033[1;31mTente novamente. \033[m', end='')
    print(f'\033[1;34;40mO número \033[33m{escolhido}\033[34m por extenso é: \033[33m{numeros[escolhido]}\033[m')
    continuar = 'A'
    while continuar not in 'SN':
        continuar = str(input('\033[1;34mQuer continuar? \033[33m[S/N] \033[m')).strip().upper()[0]
        if continuar in 'SN':
            break
    if continuar == 'N':
        break
print('\033[1;33mVOLTE SEMPRE!!!\033[m')