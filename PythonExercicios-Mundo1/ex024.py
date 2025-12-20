nci = str(input('\033[1;34mNome da cidade: \033[m')).strip().title()
nci = nci.split()
print(f'\033[1;40mO nome da cidade começa com "Santo"? \033[33m{'Santo' in nci[0]}\033[m')