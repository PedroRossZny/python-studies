n1 = int(input('\033[1;34mDigite um número: \033[m'))
n2 = int(input('\033[1;34mDigite mais um número: \033[m'))
s = n1 + n2
print(f'\033[1;40mA soma entre \033[33m{n1}\033[1;38;40m e \033[33m{n2}\033[1;38;40m'
      f' vale: \033[32m{s}\033[m')