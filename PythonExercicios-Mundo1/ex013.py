s = float(input('\033[1;34mValor do salário: R$\033[m'))
a = s * (115 / 100)
print(f'\033[1;40mO mesmo salário após um aumento de \033[33m15%\033[1;38;40m: \033[32mR${a:.2f}\033[m')