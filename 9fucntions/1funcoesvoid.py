''' Funções do tipo void
São funções sem retorno ideais para otimizar
o trabalho.
Aula elaborada por
@Luiz Henrique de Almeida Fernandes
@version1
#Funções servem para facilitar a vida porque automatizam processos
para declarar uma função em python é necessário usar def
'''
import datetime


def somar():
    a = float(input('Digite o valor de a: '))
    b = float(input('Digite o valor de b: '))
    r = float(a+b)
    print(f'''A soma é {r}''')

somar()

#funcoes com parâmetro sao ideais para receber argumentos da classe principal

def somarParametro(a,b):
    a1 = float (a)
    b1 = float (b)
    r = a1 + b1
    print(f'''A soma é {r}''')
n1 = float(input('''Digite o valor 1: '''))
n2 = float(input('''Digite o valor 2: '''))
somarParametro(n1,n2)

#chamada por nome usando a função date para exibir a data autal
def nomeUsuario(nome):
    print(f'''Olá \033[31m {nome} \033[m! Tudo bem? 
A data e hoje é: {datetime.date.today()}''')
nome = str(input('''Olá digite seu nome: '''))
nomeUsuario(nome)


#trabalhando com parâmetros * cria uma tupla
def maiorQue30(*eita):
    print(type(eita))
    print(eita)
    #agora vamos percorrer a tupla
    for num in eita:
        if num > 30:
            print(num)
maiorQue30(10,20,30,40,50,60)
#criando um dicionario com parâmetros
def dadosPessoa(**preula):
    print(type(preula))
    #vamos percorrer o dicionário
    for chave, valor in preula.items():
        print(f'''A chave é {chave}, o valor é {valor}''')
dadosPessoa(nome = "Lion Thunder Cat", idade = "8", carreira = "Chefe dos thunder, Thunder, THUNDERCATS HOOOOOOOWWWWW")














