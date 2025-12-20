c = ''
con = tv = ma = me = 0
while c != 'N':
    v = int(input('\033[1;34mDigite um valor: \033[m'))
    con += 1
    tv += v
    if con == 1:
        ma = me = v
    if v > ma:
        ma = v
    elif v < me:
        me = v
    c = str(input('\033[1;33m[S]:\033[34m Sim\n'
                  '\033[33m[N]:\033[34m Não\n'
                  'Quer continuar? \033[m')).upper().strip()
    while c not in 'SN':
        print('\033[1;31mOpção inválida! Tente novamente\033[m')
        c = str(input('\033[1;33m[S]:\033[34m Sim\n'
                      '\033[33m[N]:\033[34m Não\n'
                      'Quer continuar? \033[m')).upper().strip()
print(f'\033[1;34;40mMédia dos valores: \033[33m{tv/con:.2f}\033[m')
if ma != me:
    print(f'\033[1;34;40mMaior: \033[33m{ma}\033[m\n'
          f'\033[1;34;40mMenor: \033[33m{me}\033[m')
else:
    print('\033[1;34;40mOs valores são iguais.\033[m')
print('\033[1;32mVOLTE SEMPRE!\033[m')