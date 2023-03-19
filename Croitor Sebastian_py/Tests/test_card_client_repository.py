from Domain.card_client import CardClient
from Repository.json_repository import RepositoryJson
from utils import clear_file


def test_card_client_repository():
    filename = 'test_card_client.json'
    clear_file(filename)
    card_client_repository = \
        RepositoryJson(filename)
    added = CardClient('1', 'a', 'john', 'fdsf',
                       '1234567890098', '11-11-1111', '11-11-1111', 2.5)
    card_client_repository.create(added)
    assert card_client_repository.read(added.id_entity) == added


test_card_client_repository()
