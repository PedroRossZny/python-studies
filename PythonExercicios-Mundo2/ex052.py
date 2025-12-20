cd = 0
n = int(input('\033[1;34mDigite um número: \033[m'))
for c in range(1, n+1):
    if n % c == 0:
        cd += 1
if cd == 2:
    print(f'\033[32mO número é \033[1mPRIMO\033[m')
else:
    print(f'\033[31mO número \033[1mNÃO\033[0;31m é \033[1mPRIMO\033[m')