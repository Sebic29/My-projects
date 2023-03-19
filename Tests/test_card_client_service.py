from Domain.card_client import CardClient
from Domain.card_client_validator import CardClientValidator

from Repository.json_repository import RepositoryJson
from Service.card_client_service import CardClientService
from Service.undo_redo_service import UndoRedoService
from utils import clear_file


def test_card_client_service():
    undo_redo_service = UndoRedoService()
    filename = 'test_clientcard_service.json'
    card_client_validator = CardClientValidator()
    clear_file(filename)
    card_client_repository = RepositoryJson(filename)
    card_client_service = CardClientService(card_client_repository,
                                            card_client_validator,
                                            undo_redo_service)
    added = CardClient('1', 't1', 'asdf', 'daasda', '1234567890123',
                       '11-11-1111',
                       '11-11-1111', 0)
    card_client_validator.validate(added)
    card_client_service.add_card_client('1', 't1', 'asdf', 'daasda',
                                        '1234567890123',
                                        '11-11-1111',
                                        '11-11-1111', 0)
    assert card_client_repository.read(added.id_entity) == added
    added2 = CardClient('2', 't2', 'asdf', 'daasda', '1234567890126',
                        '11-11-1111',
                        '11-11-1111', 0)
    card_client_validator.validate(added2)
    card_client_service.add_card_client('2', 't2', 'asdf', 'daasda',
                                        '1234567890126',
                                        '11-11-1111',
                                        '11-11-1111', 0)
    before_update = card_client_repository.read()
    card_client_service.update_card_client('2', 't3', 'asdf', 'daasda',
                                           '1234567890126',
                                           '11-11-1111',
                                           '11-11-1111', 0)
    assert card_client_repository.read() != before_update
    card_client_service.delete_card(added2.id_entity)
    assert card_client_repository.read(added.id_entity) == added

    added = CardClient('100', 'aasd', 'asssd', 'asdf', '4567890123456',
                       '11-11-2021', '11-11-1111', 20)
    card_client_repository.create(added)
    card_client_service.card_incrementation(10, '9-11-2021', '12-11-2021')
    assert card_client_repository.read('100') == CardClient('100', 'aasd',
                                                            'asssd', 'asdf',
                                                            '4567890123456',
                                                            '11-11-2021',
                                                            '11-11-1111', 30)


test_card_client_service()
