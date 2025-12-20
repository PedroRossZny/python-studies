r1 = float(input('\033[1;34mPrimeira reta: \033[m'))
r2 = float(input('\033[1;34mSegunda reta: \033[m'))
r3 = float(input('\033[1;34mTerceira reta: \033[m'))
if r1 + r2 > r3 and r1 + r3 > r2 and r2 + r3 > r1:
    print('\033[1;32mElas podem formar um triângulo!')
else:
    print('\033[31mElas \033[1mNÃO\033[0;31m podem formar um triângulo :(\033[m')