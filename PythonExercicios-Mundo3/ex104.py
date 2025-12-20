def leiaint(valor):
    """
    → Mostra o valor apenas se for um número inteiro.
    :param valor: Valor digitado como em um "input".
    :return: Número inteiro.
    """
    valor = input(valor)
    while not valor.isnumeric():
        print('\033[1;31mERRO!\033[0;31m Digite um número válido.\033[m')
        valor = input('\033[1;34mDigite um número inteiro: \033[m')
    return valor


n = leiaint('\033[1;34mDigite um número inteiro: \033[m')
print(f'\033[1;34mVocê acabou de digitar o número \033[33m{n}\033[m')
help(leiaint)