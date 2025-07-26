#Tabuada de um número
## Peça ao usuário um número e exiba a tabuada dele (1 a 10).
usuario = int(input('Informe um NUMERO:'))
for conte in range(0,11):
    print(f'{usuario} x {conte} = {usuario * conte}')
print('Aqui esta sua tabuada !!!')    