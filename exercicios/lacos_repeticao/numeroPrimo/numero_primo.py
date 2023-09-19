print('🎪'*15)
print('''Número Primo''')
contadorPrimo = 0
numero = int(input(f'''Digite um número: '''))
if numero == 1:
    print(f'número: {numero} é primo')
elif numero == 2:
    print(f'número: {numero} é o único primo par')
for i in range(1,numero+1):
    if(numero % i == 0):
        contadorPrimo += 1
if(contadorPrimo <= 2):
    print(f'O número {numero} é primo')
else:
    print(f'O número {numero} não é primo')

    
    


