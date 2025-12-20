r1 = float(input('\033[1;34mPrimeira reta: \033[m'))
r2 = float(input('\033[1;34mSegunda reta: \033[m'))
r3 = float(input('\033[1;34mTerceira reta: \033[m'))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    if r1 == r2 == r3:
        t = 'EQUILÁTERO'
    elif r1 == r2 or r1 == r3 or r2 == r3:
        t = 'ISÓSCELES'
    else:
        t = 'ESCALENO'
    print(f'\033[1;32;40mElas podem formar um triângulo \033[33m{t}\033[32m!\033[m')
else:
    print('\033[31;40mElas \033[1mNÃO\033[0;31;40m podem formar um triângulo :(\033[m')