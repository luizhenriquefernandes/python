n=int(input('Digite o número: '))
primo = False
contPrimo = 0
for i in range (1,n+1):
    if(n == 2):
        print(f'{n} é o único número primo par')
        break
    elif(n%2 == 0):
            print(f'{n} é número par')
            break
    else:
        if(n%i == 0):
            primo=True
            contPrimo += 1
            if(contPrimo>2):
                primo=False
                break
if(primo == True):
    print(f'{n} é primo')
elif(n==2):
    print('')
else:
    print(f'{n} não é primo')

