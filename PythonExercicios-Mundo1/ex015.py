d = int(input('\033[1;34mDias alugados: \033[m'))
km = float(input('\033[1;34mQuilômetros rodados: \033[m'))
dp = d * 60
kmp = km * 0.15
t = dp + kmp
print(f'\033[1;34;40mO preço a pagar considerando os dias alugados e os km rodados: \033[32mR${t:.2f}\033[m')