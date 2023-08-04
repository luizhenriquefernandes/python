'''Orientação a objeto como já foi criado a classe Animais
Agora iremos chamar a classe Animais em Pyhton'''
from Animais.Tigre import Tigre
from Animais.Animal import Animal
tigreObjeto = Tigre("Tigrão")
nomeT = tigreObjeto.get_nome()
print(nomeT)
print(f'''O nome é {tigreObjeto.get_nome()}''')
leaoObjeto = Animal("Simba", 21)
print(f'''O nome é {leaoObjeto.get_nome()} e a idade é {leaoObjeto.get_idade()}''')