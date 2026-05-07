class FilmeController:

    def __init__(self, service):
        self.service = service

    def cadastrar(self, filme):
        self.service.cadastrar_filme(filme)
