f = str(input('\033[1;34mDigite uma frase: \033[m')).strip().upper()
print(f'\033[1;40mQuantas vezes aparece a letra "A"? \033[33m{f.count('A')}\033[m')
print(f'\033[1;40mEm que posição ele aparece a primeira vez? \033[33m{f.find('A')}\033[m')
print(f'\033[1;40mEm que posição ela aparece a última vez? \033[33m{f.rfind('A')}\033[m')