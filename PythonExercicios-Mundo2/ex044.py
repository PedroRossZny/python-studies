preco = float(input('\033[1;34mPreço do produto: \033[32mR$\033[m'))
print('')
print(f"\033[1;32m{'-'*15}CONDIÇÃO DE PAGAMENTO{'-'*15}\033[m\n"
      f"\033[1;34mà vista dinheiro/cheque: 10% de desconto.\033[4;33mOpção (1)\033[m\n"
      f"\033[1;34mà vista no cartão: 5% de desconto. \033[4;33mOpção (2)\033[m\n"
      f"\033[1;34mem até 2x no cartão: preço normal. \033[4;33mOpção (3)\033[m\n"
      f"\033[1;34m3x ou mais no cartão: 20% de juros. \033[4;33mOpção (4)\033[m\n")
opcao = int(input('\033[1;33mEscolha uma das opções acima: \033[m'))
if opcao == 1:
    print(f'\033[1;40mValor a ser pago: \033[32mR${preco-(preco*(10/100)):.2f}\033[m')
elif opcao == 2:
    print(f'\033[1;40mValor a ser pago: \033[32mR${preco-(preco*(5/100)):.2f}\033[m')
elif opcao == 3:
    print(f'\033[1;40mValor a ser pago: \033[32mR${preco:.2f}\033[m')
elif opcao == 4:
    print(f'\033[1;40mValor a ser pago: \033[32mR${preco+(preco*(20/100)):.2f}\033[m')
else:
    print('\033[1;31mOpção inválida!\033[m')