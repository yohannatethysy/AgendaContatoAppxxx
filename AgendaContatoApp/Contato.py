from Agenda import Agenda
class Contato(Agenda):
    def __init__(self, criacao, pessoa, telefone):
        self.criacao = criacao
        self.pessoa = pessoa
        self.telefone = telefone

    def listarTelefones(self):
        pass
