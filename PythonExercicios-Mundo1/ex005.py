n = int(input('\033[1;34mDigite um número inteiro: \033[m'))
s = n + 1
a = n - 1
print(f'\033[1;40mO antecessor de \033[34m{n}\033[1;38;40m é \033[33m{a}\033[m\n'
      f'\033[1;40mO sucessor de \033[34m{n}\033[1;38;40m é \033[33m{s}\033[m')