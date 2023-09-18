'''Excercício JO-KEN-PO o jogador escolherá pedra
papel ou tesoura e o computador também atraves de
um número aleatório de 1 a 3
@author alunos de python data 18/09/2023
version 1.0
'''
from random import randint
from time import sleep
#escolha do computador

print('#'*50)
print('''Bem vindo ao jogo do JO-KEN-PO 👊 🤚 ✌''')
#fazendo um contador ganhar pontos
acumularPonto = 0      
#escolha player
escolhaPlayer = int(input('''
Digite [1] - 👊 - PEDRA
Digite [2] - 🤚 - PAPEL
Digite [3] - ✌ - TESOURA
Faça a escolha: '''))
sleep(1)
print("JO-👊")
sleep(1)
print("KEN-🤚")
sleep(1)
print("PO-✌")
if (escolhaPlayer == 1):
    print(f'A sua escolha foi 👊')
elif(escolhaPlayer == 2):
    print(f'A sua escolha foi 🤚')
elif(escolhaPlayer == 3):
    print(f'A sua escolha foi ✌')
else:
    print('Digite uma opção entre 1 e 3 e reinicie o jogo')

#escolha do computador
escolhaComputador = randint(1,3)
if (escolhaComputador == 1):
    print(f'O computador escolheu: 👊')
elif(escolhaComputador == 2):
    print(f'O computador escolheu: 🤚')
else:
    print(f'O computador escolheu: ✌')
if(escolhaPlayer == escolhaComputador):
    print(f'''Empate''')
# pedra ganha de tesoura 1 ganha de 3
# papel ganha de pedra 2 ganha de 1
# tesoura ganha de papel 3 ganha de 2
elif((escolhaPlayer == 1 and escolhaComputador == 3) or 
   (escolhaPlayer == 2 and escolhaComputador == 1) or
   (escolhaPlayer == 3 and escolhaComputador == 2)):
    print('''Parabéns você ganhou!!!''')
    acumularPonto = acumularPonto + 1
    print(f'''Sua pontuação é {acumularPonto}''')
else:
    print('''Você perdeu playboy Game Over''')

escolhaPlayer = int(input('''
Digite [1] - 👊 - PEDRA
Digite [2] - 🤚 - PAPEL
Digite [3] - ✌ - TESOURA
Faça a escolha: '''))
sleep(1)
print("JO-👊")
sleep(1)
print("KEN-🤚")
sleep(1)
print("PO-✌")
if (escolhaPlayer == 1):
    print(f'A sua escolha foi 👊')
elif(escolhaPlayer == 2):
    print(f'A sua escolha foi 🤚')
elif(escolhaPlayer == 3):
    print(f'A sua escolha foi ✌')
else:
    print('Digite uma opção entre 1 e 3 e reinicie o jogo')

#escolha do computador
escolhaComputador = randint(1,3)
if (escolhaComputador == 1):
    print(f'O computador escolheu: 👊')
elif(escolhaComputador == 2):
    print(f'O computador escolheu: 🤚')
else:
    print(f'O computador escolheu: ✌')
if(escolhaPlayer == escolhaComputador):
    print(f'''Empate''')
# pedra ganha de tesoura 1 ganha de 3
# papel ganha de pedra 2 ganha de 1
# tesoura ganha de papel 3 ganha de 2
elif((escolhaPlayer == 1 and escolhaComputador == 3) or 
   (escolhaPlayer == 2 and escolhaComputador == 1) or
   (escolhaPlayer == 3 and escolhaComputador == 2)):
    print('''Parabéns você ganhou!!!''')
    acumularPonto = acumularPonto + 1
    print(f'''Sua pontuação é {acumularPonto}''')
else:
    print('''Você perdeu playboy Game Over''')

escolhaPlayer = int(input('''
Digite [1] - 👊 - PEDRA
Digite [2] - 🤚 - PAPEL
Digite [3] - ✌ - TESOURA
Faça a escolha: '''))
sleep(1)
print("JO-👊")
sleep(1)
print("KEN-🤚")
sleep(1)
print("PO-✌")
if (escolhaPlayer == 1):
    print(f'A sua escolha foi 👊')
elif(escolhaPlayer == 2):
    print(f'A sua escolha foi 🤚')
elif(escolhaPlayer == 3):
    print(f'A sua escolha foi ✌')
else:
    print('Digite uma opção entre 1 e 3 e reinicie o jogo')

#escolha do computador
escolhaComputador = randint(1,3)
if (escolhaComputador == 1):
    print(f'O computador escolheu: 👊')
elif(escolhaComputador == 2):
    print(f'O computador escolheu: 🤚')
else:
    print(f'O computador escolheu: ✌')
if(escolhaPlayer == escolhaComputador):
    print(f'''Empate''')
# pedra ganha de tesoura 1 ganha de 3
# papel ganha de pedra 2 ganha de 1
# tesoura ganha de papel 3 ganha de 2
elif((escolhaPlayer == 1 and escolhaComputador == 3) or 
   (escolhaPlayer == 2 and escolhaComputador == 1) or
   (escolhaPlayer == 3 and escolhaComputador == 2)):
    print('''Parabéns você ganhou!!!''')
    acumularPonto +=  1
    print(f'''Sua pontuação é {acumularPonto}''')
else:
    print('''Você perdeu playboy Game Over''')
print(f'''Sua pontuação Total {acumularPonto} fim de jogo''')
    



