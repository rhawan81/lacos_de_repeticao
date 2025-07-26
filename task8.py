### Adivinhe o número
### O programa escolhe um número aleatório de 1 a 100 e o usuário tenta adivinhar. Dê dicas se o palpite está acima ou abaixo.
from random import randint
computer = randint(1,10)
user= int(input('Informe um numero:'))
tentativas = 1
while user != computer:
    
    if user < computer:
        print('MAIS ALTO , TENTE NOVAMENTE')        
        
    elif user > computer:
        print('MAIS BAIXO , TENTE NOVAMENTE')

    user = int(input('Informe um numero:'))
    tentativas += 1
print('SEU NUMERO FOI {} , EU PENSEI NO {}'.format(user,computer))    
print('VOCE GANHOU PARABENS, COM  {} TENTATIVAS !!!'.format(tentativas))