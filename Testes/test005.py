lanche = ('Hambúrguer', 'Suco', 'Pizza', 'Pudim')
print(lanche)

lanche = 'Hambúrguer', 'Suco', 'Pizza', 'Pudim', 'Batata Frita'
print(lanche)

print(lanche[1])
print(lanche[3])
print(lanche[-2])
print(lanche[1:3])
print(lanche[2:])
print(lanche[:2])
print(lanche[-2:])
print(lanche[-3:])
print(lanche[::-1])
print(lanche[::2])

#lanche[1] = 'Refrigerante'
#print(lanche[1])

for cont in range(0, len(lanche)):
    print(lanche[cont])

for comida in lanche:
    print(f'Eu vou comer {comida}')
print('Comi pra caramba!')

for cont in range(0, len(lanche)):
    print(f'Eu vou comer {lanche[cont]} na posição {cont}')

for pos, comida in enumerate(lanche):
    print(f'Eu vou comer {comida} na posição {pos}')

print(sorted(lanche))
print(lanche)