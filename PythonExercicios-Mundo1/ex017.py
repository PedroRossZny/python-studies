from math import hypot
co = float(input('\033[1;34mCateto oposto: \033[m'))
ca = float(input('\033[1;34mCateto adjacente: \033[m'))
h = hypot(co, ca)
print(f'\033[1;40mA hipotenusa do cateto oposto \033[33m{co}\033[38m e do cateto adjacente \033[33m{ca}\033[38m é \033[35m{h}\033[m')