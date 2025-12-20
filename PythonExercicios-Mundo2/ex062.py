pt = int(input('\033[1;34mDigite o primeiro termo de uma PA: \033[m'))
r = int(input('\033[1;34mDigite a razão dessa PA: \033[m'))
d = pt + (10 - 1) * r
while pt < d+r:
    print(f'\033[1;40m{pt} \033[m', end='')
    pt += r
t = pt
while t != 0:
    t = int(input('\n\033[1;34mDeseja mostrar mais quantos termos? \033[m'))
    for n in range(0, t):
        print(f'\033[1;40m{pt} \033[m', end='')
        pt += r
    if t == 0:
        print('\033[1;32mVOLTE SEMPRE!\033[m')