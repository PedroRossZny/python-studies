n = int(input('\033[1;34mDigite um número inteiro: \033[m'))
if n % 2 == 0:
    print(f'\033[1;40mO número \033[35m{n}\033[1;38;40m é \033[34mPAR\033[1;38;40m.\033[m')
else:
    print(f'\033[1;40mO número \033[35m{n}\033[1;38;40m é \033[33mÍMPAR\033[1;38;40m.\033[m')