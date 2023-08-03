'''Orientação a objeto como já foi criado a classe Animais
Agora iremos chamar a classe Animais em Pyhton'''
from Animais.Tigre import Tigre
tigreObjeto = Tigre("Tigrão")
nomeT = tigreObjeto.get_nome()
print(nomeT)
print(f'''O nome é {tigreObjeto.get_nome()}''')