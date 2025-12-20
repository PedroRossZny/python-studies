n = input('\033[1;34mDigite um número entre 0 a 9999: \033[m').strip()
nc = '0000' + n
print(f'\033[1;34mUnidade: \033[33m{nc[-1]}\033[m\n'
      f'\033[1;34mDezena: \033[33m{nc[-2]}\033[m\n'
      f'\033[1;34mCentena: \033[33m{nc[-3]}\033[m\n'
      f'\033[1;34mMilhar: \033[33m{nc[-4]}\033[m')