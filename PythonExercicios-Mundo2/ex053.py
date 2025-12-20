frase = str(input('\033[1;34mEscreva uma frase: \033[m')).strip().upper()
frase = frase.split()
frase = ''.join(frase)
comprimento = len(frase)
iguais = 0
comprimento -= 1
for c in range(0, comprimento+1):
    if frase[c] == frase[comprimento]:
        iguais += 1
    comprimento -= 1
if iguais == len(frase):
    print(f'\033[32mA frase é um \033[1mPALÍNDROMO\033[0;32m!!!\033[m')
else:
    print(f'\033[31mA frase \033[1mNÃO\033[0;31m é um \033[1mPALÍNDROMO\033[0;31m!!!\033[m')