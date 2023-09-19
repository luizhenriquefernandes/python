'''
Calc average (Cálculo de média)
@author Luiz Henrique Fernandes date 2023/09/19
version 1.1
'''
#fazer o menu de sair
soma = 0
i=1
while True:
    print("🤣😁"*10)
    print('''Cálculo de Média''')    
    soma += float(input(f'''Digite a Nota {i}: ''').replace(',','.'))
    sair = ""
    while sair != 'S' or sair != 'N':
        sair = str(input('Quer sair do programa [S] ou [N]: ').upper().strip()[0])
        if sair == 'S':            
            break
        elif sair == 'N':            
            break
    if sair == 'S':        
        break
    elif sair == 'N':
        print()
    i += 1
print(f'valor de i é {i}')
media = soma/i
print(f'''A média é {media:.2f}''')
print('FIM')
print("🤣😁"*10)
