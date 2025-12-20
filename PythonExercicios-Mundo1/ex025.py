n = str(input('\033[1;34mNome completo: \033[m')).strip().title()
print(f'\033[1;40mA pessoa possue "Silva" no nome? \033[33m{'Silva' in n}\033[m')