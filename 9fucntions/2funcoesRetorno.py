''' Funções com Retorno
São funções sem retorno ideais para otimizar
o trabalho.
Aula elaborada por
@Luiz Henrique de Almeida Fernandes
@version1
#Funções servem para facilitar a vida porque automatizam processos
para declarar uma função em python é necessário usar def
com retorno podemos trabalhar com variáveis, tuplas, listas e dicionários.
'''

def somaDoisNumeros (a,b):
    soma = a + b
    print(type(soma))
    return soma
somar = somaDoisNumeros(3,5)
print(somar)
print(somaDoisNumeros(10,20))

#retornando valores multiplos
def calculo(a,b):
    soma = a + b
    media = float((a+b)/2)
    return soma, media
a = 10
b = 10
print(f'''Cálculo da soma e da média {calculo(a,b)}''')

#trablhando com lista
#extend adiciona uma lista em uma lista já existente
#nesse processo foi obrigatório utilizar o return
def adiconarNome(nomeLista = list()):
    print(type(nomeLista))
    fruta = str(input('Digite a fruta: '))
    nomeLista.append(fruta)
    print(f'''Foi incluido {fruta}''')
    return nomeLista
vetFruta=['maçã', 'goiaba']
print(vetFruta)
vetFruta.extend(adiconarNome())
print(vetFruta)

