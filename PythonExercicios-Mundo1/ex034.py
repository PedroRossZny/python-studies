s = float(input('\033[1;34mSalário: \033[m'))
if s > 1250:
    a = s + (s * 10 / 100)
else:
    a = s + (s * 15 / 100)
print(f'\033[1;40mO salário teve um aumento de \033[32mR${a:.2f}\033[m')