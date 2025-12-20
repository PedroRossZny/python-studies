def ar(l, c):
    area = l * c
    print(f'\033[1;34mA área do terreno de \033[33m{l:.2f}m\033[34m por \033[33m{c:.2f}m\033[34m equivale a \033[33m{area}m²\033[m')


largura = float(input('\033[1;34mLargura em metros: \033[m'))
comprimento = float(input('\033[1;34mComprimento em metros: \033[m'))
ar(largura, comprimento)