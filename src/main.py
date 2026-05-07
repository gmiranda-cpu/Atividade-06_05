from model.filme import Filme
from repository.filme_repository import FilmeRepository
from service.filme_service import FilmeService
from controller.filme_controller import FilmeController

repository = FilmeRepository()
service = FilmeService(repository)
controller = FilmeController(service)

filme = Filme(
    "Vingadores",
    "Ação",
    "Marvel"
)

controller.cadastrar(filme)

print("Filme cadastrado com sucesso!")
