pt = int(input('\033[1;34mDigite o primeiro termo de uma PA: \033[m'))
r = int(input('\033[1;34mDigite a razão dessa PA: \033[m'))
for c in range(0, 10):
    print(f'{pt}', end=' ')
    pt += r