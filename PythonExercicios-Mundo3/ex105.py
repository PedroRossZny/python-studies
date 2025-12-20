def notas(*num, sit=False):
    """
    → Mostra um dicionário sobre informações de notas e médias de alunos.
    :param num: Notas dos alunos.
    :param sit: Situação da média dos alunos.
    :return: Dicionário com as informações de notas e média dos alunos.
    """
    quantidade = len(num)
    maior = max(num)
    menor = min(num)
    soma = 0
    for n in num:
        soma += n
    media = soma / len(num)
    info = {'total': quantidade, 'maior': maior, 'menor': menor, 'média': media}
    if sit:
        if media < 6:
            s = 'RUIM'
        elif media <= 7:
            s = 'RAZOÁVEL'
        else:
            s = 'BOA'
        info = {'total': quantidade, 'maior': maior, 'menor': menor, 'média': media, 'situação': s}
    return info


resp = notas(5.5, 9.5, 10, 6.5, sit=True)
print(resp)
help(notas)