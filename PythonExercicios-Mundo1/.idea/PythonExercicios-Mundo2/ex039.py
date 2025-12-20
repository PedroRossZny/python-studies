import datetime
nascimento = int(input('\033[1;34mAno que nasceu: \033[m'))
ano = datetime.date.today().year
idade = ano - nascimento
if idade < 18:
    print(f'\033[1;34;40mFalta\033[33m{18-idade}\033[34m ano(s) para se alistar ao serviço militar.\033[m')
elif idade == 18:
    print('\033[1;32;40mEstá na hora de se alistar ao serviço militar!!!\033[m')
else:
    print(f'\033[1;31;40mPassou \033[33m{idade-18}\033[31m ano(s) do tempo de se alistar.\033[m')