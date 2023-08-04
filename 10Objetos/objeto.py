'''Orientação a objeto como já foi criado a classe Animais
Agora iremos chamar a classe Animais em Pyhton'''
from Animais.Animal import Animal
from Animais.Tigre import Tigre
tigreObjeto = Animal("Tigrão")
nomeT = tigreObjeto.get_nome()
print(nomeT)
print(f'''O nome é {tigreObjeto.get_nome()}''')
leaoObjeto = Tigre("Simba", 41)
print(f'''O nome é {leaoObjeto.get_nome()} e a idade é {leaoObjeto.get_idade()}''')