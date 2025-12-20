aluno = dict()
aluno['Nome'] = str(input('\033[1;34mNome: \033[m'))
aluno['Média'] = float(input(f'\033[1;34mMédia de \033[33m{aluno["Nome"]}\033[34m: \033[m'))
if aluno['Média'] >= 6:
    aluno['Situação'] = '\033[32mAPROVADO\033[m'
else:
    aluno['Situação']  = '\033[31mREPROVADO\033[m'
for i, v in aluno.items():
    print(f'\033[1;34m{i}:\033[1;33m {v}\033[m')