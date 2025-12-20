continuar = nomemenor = ''
produto = totalgasto = precomaior = menorproduto = 0
while True:
    produto += 1
    print(f'\033[1;32;40m--{produto}º Produto--\033[m')
    nomeproduto = str(input('\033[1;34mNome do produto: \033[m'))
    precoproduto = float(input('\033[1;34mPreço: \033[32mR$\033[m'))
    totalgasto += precoproduto
    if precoproduto > 1000:
        precomaior += 1
    if produto == 1:
        menorproduto = precoproduto
        nomemenor = nomeproduto
    else:
        if menorproduto > precoproduto:
            menorproduto = precoproduto
            nomemenor = nomeproduto
    while True:
        continuar = str(input('\n\033[1;33m[S]:\033[34m Sim\033[m\n'
                              '\033[1;33m[N]:\033[34m Não\033[m\n'
                              '\033[1;34mQuer continuar? \033[m')).strip().upper()
        if continuar in 'SN':
            print('')
            break
        else:
            print('\033[1;31mOpção inválida! Tente novamente.\033[m')
    if continuar == 'N':
        break
print(f'\033[1;34mTotal gasto na compra: \033[32mR${totalgasto:.2f}\033[m\n'
      f'\033[1;34mQuantidade de produtos com preço maior que R$1.000,00: \033[33m{precomaior}\033[m\n'
      f'\033[1;34mNome do produto mais barato: \033[33m{nomemenor}\033[m')