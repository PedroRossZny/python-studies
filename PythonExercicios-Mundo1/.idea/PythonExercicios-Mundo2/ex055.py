ma = me = 0
for c in range(1, 6):
    p = float(input(f'\033[1;34m{c}°Peso: \033[m'))
    if c == 1:
        ma = me = p
    else:
        if p > ma:
            ma = p
        elif p < me:
            me = p
if ma != me:
    print(f'\033[34mMaior peso: \033[1;33m{ma}Kg\033[m\n'
          f'\033[34mMenor peso: \033[1;33m{me}Kg\033[m')
else:
    print('\033[34mTodos os pesos são \033[1;33mIGUAIS\033[0;34m.\033[m')