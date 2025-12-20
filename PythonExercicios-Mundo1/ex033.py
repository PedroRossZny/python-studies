n1 = float(input('\033[1;34mPrimeiro número: \033[m'))
n2 = float(input('\033[1;34mSegundo número: \033[m'))
n3 = float(input('\033[1;34mTerceiro número: \033[m'))
if n1 > n2 > n3:
    print(f'\033[1;40mO maior número é \033[35m{n1}\033[38m e o menor é \033[35m{n3}\033[m')
if n1 > n3 > n2:
    print(f'\033[1;40mO maior número é \033[35m{n1}\033[38m e o menor é \033[35m{n2}\033[m')
if n2 > n1 > n3:
    print(f'\033[1;40mO maior número é \033[35m{n2}\033[38m e o menor é \033[35m{n3}\033[m')
if n2 > n3 > n1:
    print(f'\033[1;40mO maior número é \033[35m{n2}\033[38m e o menor é \033[35m{n1}\033[m')
if n3 > n2 > n1:
    print(f'\033[1;40mO maior número é \033[35m{n3}\033[38m e o menor é \033[35m{n1}\033[m')
if n3 > n1 > n2:
    print(f'\033[1;40mO maior número é \033[35m{n3}\033[38m e o menor é \033[35m{n2}\033[m')