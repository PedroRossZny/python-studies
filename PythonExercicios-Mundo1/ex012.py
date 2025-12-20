p = float(input('\033[1;34mPreço do produto: R$\033[m'))
d = p * (95 / 100)
print(f'\033[1;40mNovo preço do produto com \033[33m5%\033[1;38;40m de desconto: \033[32mR${d:.2f}\033[m')