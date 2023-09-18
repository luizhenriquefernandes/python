i = 1
while(i<11):
    print(i, end = ' ')
    i += 2
    
print('fim while')

for i in range (1,11,2):
    print(i,end=" ")
print('fim')
soma = 0
for i in range (1,5):
    nota = float(input(f'Digite a nota {i}: ')
                 .replace(',','.'))
    soma += nota
print(f'A soma de tudo é {soma}')