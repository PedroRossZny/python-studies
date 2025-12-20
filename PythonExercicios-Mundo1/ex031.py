d = float(input('\033[1;34mDistância da viagem em Km: \033[m'))
if d <= 200:
    p = d * 0.50
else:
    p = d * 0.45
print(f'\033[1;40mO preço da passagem é de \033[32mR${p:.2f}\033[m')