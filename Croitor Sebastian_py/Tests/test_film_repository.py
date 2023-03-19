from Domain.film import Film
from Repository.json_repository import RepositoryJson
from utils import clear_file


def test_film_repository():
    filename = 'test_films.json'
    clear_file(filename)
    film_repository = RepositoryJson(filename)
    added = Film('1', 'Fast and Furious', '2010', 10, 'Yes')
    film_repository.create(added)
    assert film_repository.read(added.id_entity) == added


test_film_repository()
