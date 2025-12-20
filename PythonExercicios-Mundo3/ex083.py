lista = []
expressao = str(input('\033[1;34mDigite uma expressão qualquer: \033[m')).strip()
for e in expressao:
    lista.append(e)
if lista.count('(') == lista.count(')'):
    print('\033[1;32mSua expressão está certa.\033[m')
else:
    print('\033[1;31mSua expressão está errada.\033[m')