num1 = int(input('\033[1;34mDigite um número inteiro: \033[m'))
num2 = int(input('\033[1;34mDigite outro número inteiro: \033[m'))
if num1 > num2:
    print(f'\033[34;40mO \033[1;33mprimeiro\033[0;34;40m valor é \033[1;33mMAIOR\033[0;34;40m.\033[m')
elif num2 > num1:
    print(f'\033[34;40mO \033[1;33msegundo\033[0;34;40m valor é \033[1;33mMAIOR\033[0;34;40m.\033[m')
else:
    print('\033[1;34;40mOs dois valores são iguais.\033[m')