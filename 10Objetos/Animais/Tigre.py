from .Animal import Animal
'''o usar o ponto (.) antes do nome do módulo na importação, 
você indica que está importando um módulo relativo dentro do 
mesmo pacote. Dessa forma, o Python entenderá que a classe 
Tigre está no mesmo pacote Animais e encontrará a definição 
correta.'''
class Tigre(Animal):
    def __init__(self,nome,idade):
        super().__init__(nome)
        self._idade = idade
    def get_idade(self):
        return self._idade
    def set_idade(self,novaIdade):
        self._idade = novaIdade
