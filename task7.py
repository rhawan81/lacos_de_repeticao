num1 = str(input('Digite um numero:'))
digitos = 0
for numeros in num1:
   if numeros.isdigit():
      digitos += 1
print(f'O numero {num1} Possui {digitos} digitos !!')