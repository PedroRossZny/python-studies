nota1 = float(input('\033[1;34mPrimeira nota: \033[m'))
nota2 = float(input('\033[1;34mSegunda nota: \033[m'))
media = (nota1 + nota2) / 2
if media < 5:
    print(f'\033[1;34;40mMédia: \033[33m{media:.1f}\033[m\n\033[1;31;40mREPROVADO!!!\033[m')
elif media <= 6.9:
    print(f'\033[1;34;40mMédia: \033[33m{media:.1f}\033[m\n\033[1;35;40mRECUPERAÇÃO!!!\033[m')
else:
    print(f'\033[1;34;40mMédia: \033[33m{media:.1f}\033[m\n\033[1;32;40mAPROVADO!!!\033[m')