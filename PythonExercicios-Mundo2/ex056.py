idades = ma = mu = 0
nm = ''
erro = False
for c in range(0, 4):
    nome = str(input('\033[1;34mNome: \033[m')).strip()
    idade = int(input('\033[1;34mIdade: \033[m'))
    sexo = str(input('\033[1;34mSexo: \033[33mM\033[34m(Masculino), '
                     '\033[33mF\033[34m(Feminino): \033[m')).strip().upper()
    idades += idade
    if sexo not in 'MF':
        erro = True
    if sexo[0] == 'M':
        if ma < idade:
            ma = idade
            nm = nome
    elif sexo[0] == 'F':
        if idade < 20:
            mu += 1
if not erro:
    print(f'\033[1;34mA média da idade do grupo: \033[33m{idades/4}\033[m\n'
          f'\033[1;34mO nome do homem mais velho: \033[33m{nm}\033[m\n'
          f'\033[1;33m{mu}\033[34m mulher(es) tem menos de 20 anos.\033[m')
else:
    print('\033[1;31mOpção inválida de sexo. Tente novamente!\033[m')