import datetime
nascimento = int(input('\033[1;34mAno de nascimento: \033[m'))
ano = datetime.date.today().year
idade = ano - nascimento
if idade <= 9:
    print(f'\033[1;34mIdade: \033[33m{idade}\033[m\n\033[1;34mcategoria: \033[33mMIRIM\033[m')
elif idade <= 14:
    print(f'\033[1;34mIdade: \033[33m{idade}\033[m\n\033[1;34mcategoria: \033[33mINFANTIL\033[m')
elif idade <= 19:
    print(f'\033[1;34mIdade: \033[33m{idade}\033[m\n\033[1;34mcategoria: \033[33mJUNIOR\033[m')
elif idade <= 25:
    print(f'\033[1;34mIdade: \033[33m{idade}\033[m\n\033[1;34mcategoria: \033[33mSÊNIOR\033[m')
else:
    print(f'\033[1;34mIdade: \033[33m{idade}\033[m\n\033[1;34mcategoria: \033[33mMASTER\033[m')