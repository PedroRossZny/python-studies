p = 1
idademaior = homem = mulhermenor = 0
c = 'S'
while True:
    print(f'\033[1;32;40m--{p}ª Pessoa--\033[m')
    i = int(input('\033[1;34mIdade: \033[m'))
    s = str(input('\033[1;33m[M]: \033[34mMasculino\033[m\n'
                  '\033[1;33m[F]: \033[34mFeminino\033[m\n'
                  '\033[1;34mSexo: \033[m')).strip().upper()

    if s not in 'MF':
        print('\033[1;31mOpção inválida! Tente novamente.\033[m')
    else:

        p += 1
        if i > 18:
            idademaior += 1
        if s == 'M':
            homem += 1
        if s == 'F' and i < 20:
            mulhermenor += 1

        while True:
            c = str(input('\n\033[1;33m[S]:\033[34m Sim\033[m\n'
                          '\033[1;33m[N]:\033[34m Não\033[m\n'
                          '\033[1;34mQuer continuar? \033[m')).strip().upper()
            if c not in 'SN':
                print('\033[1;31mOpção inválida! Tente novamente.\033[m')
            else:
                break
    print('')
    if c == 'N':
        break

print(f'\033[1;33m{idademaior}\033[34m pessoa(s) tem mais de 18 anos\033[m\n'
      f'\033[1;34mForam cadastrados \033[33m{homem}\033[34m home(m/ns)\033[m\n'
      f'\033[1;33m{mulhermenor}\033[34m mulher(es) tem menos de 20 anos\033[m')