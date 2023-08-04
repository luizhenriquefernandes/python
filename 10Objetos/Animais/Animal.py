class Animal:
    def __init__(self,nome):
        self._nome = nome
    def get_nome(self):
        return self._nome
    def set_nome(self,novoNome):
        self._nome = novoNome
