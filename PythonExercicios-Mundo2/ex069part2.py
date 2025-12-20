maior18 = homens = mulheres = 0
while True:
    idade = int(input('\033[1;34mQuantos anos você tem? \033[m'))
    sexo = str(input('\033[1;34mFeminino: \033[33m[F]\n\033[34m'
                     'Masculino: \033[33m[M]\033[34m\n'
                     'Sexo: ')).strip().upper()
    if sexo[0] not in 'FM':
        while sexo[0] not in 'FM':
            print('\033[1;31mOpção inválida, Tente novamente.\033[m')
            sexo = str(input('\033[1;34mFeminino: \033[33m[F]\n\033[34m'
                             'Masculino: \033[33m[M]\033[34m\n'
                             'Sexo: ')).strip().upper()
    if sexo[0] in 'FM':
        if idade > 18:
            maior18 += 1
        if sexo[0] == 'M':
            homens += 1
        if sexo[0] == 'F' and idade < 20:
            mulheres += 1
    continuar = str(input('\033[1;34mQuer continuar? \033[33m[S]\033[34m: Sim \033[33m[N]\033[34m: Não ')).strip().upper()
    if continuar[0] not in 'SN':
        while continuar[0] not in 'SN':
            print('\033[1;31mOpção inválida, Tente novamente.\033[m')
            continuar = str(input('\033[1;34mQuer continuar? \033[33m[S]\033[34m: Sim \033[33m[N]\033[34m: Não ')).strip().upper()
    if continuar[0] == 'N':
        break
print(f'\033[1;33;40m{maior18}\033[34m pessoa(s) tem mais de \033[33m18\033[34m anos\033[m\n'
      f'\033[1;34;40mForam cadastrados \033[33m{homens}\033[34m homem(ns)\033[m\n'
      f'\033[1;33;40m{mulheres}\033[34m mulher(es) tem menos de \033[33m20\033[34m anos\033[m')