pt = int(input('\033[1;34mDigite o primeiro termo de uma PA: \033[m'))
r = int(input('\033[1;34mDigite a razão dessa PA: \033[m'))
d = pt + (10 - 1) * r
while pt < d+r:
    print(f'\033[1;40m{pt} \033[m', end='')
    pt += r