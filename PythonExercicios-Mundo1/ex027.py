n = str(input('\033[1;34mNome completo: \033[m')).strip()
n = n.split()
print(f'\033[1;40mPrimeiro nome: \033[33m{n[0]}\033[m')
print(f'\033[1;40mÚltimo nome: \033[33m{n[-1]}\033[m')