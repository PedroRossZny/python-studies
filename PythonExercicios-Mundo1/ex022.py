n = input('\033[1;34mNome completo: \033[m')
print(f'\033[1;33m{n.upper()}\033[m')
print(f'\033[1;33m{n.lower()}\033[m')
ind = len(n)
esp = n.count(' ')
lt = ind - esp
print(f'\033[1;40mLetras ao todo: \033[33m{lt}\033[m')
ns = n.split()
print(f'\033[1;40mO primeiro nome tem \033[33m{len(ns[0])}\033[1;38;40m letras\033[m')