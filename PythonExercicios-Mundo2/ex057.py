s = 'A'
while s not in 'MF':
    s = str(input('\033[1;33mM:\033[34m (Masculino)\n\033[33mF:\033[34m (Feminino)\nQual o seu sexo? \033[m')).upper().strip()
    if s not in 'MF':
        print('\033[1;31;40mOpcão inválida! Tente novamente.\033[m')
if s == 'M':
    print('\033[1;32;40mOK! O seu sexo é Masculino.\033[m')
else:
    print('\033[1;32;40mOK! O seu sexo é Feminino.\033[m')