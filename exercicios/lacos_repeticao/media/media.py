'''
Calc average (Cálculo de média)
@author Luiz Henrique Fernandes date 2023/09/19
version 1.0
'''
print("🤣😁"*10)
print('''Cálculo de Média''')
vezes = int(input('''Digite a quantidade de notas: '''))
soma = 0
for i in range(1,vezes+1):
    soma += float(input(f'''Digite a Nota {i}: ''').replace(',','.'))
media = soma/i
print(f'''A média é {media:.2f}''')
print('FIM')
print("🤣😁"*10)

    