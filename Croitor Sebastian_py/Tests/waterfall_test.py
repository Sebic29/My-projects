from Domain.card_client import CardClient
from Domain.card_client_validator import CardClientValidator
from Domain.film import Film
from Domain.film_validator import FilmValidator
from Domain.reservation import Reservation
from Domain.reservation_validator import ReservationValidator
from Repository.json_repository import RepositoryJson
from Service.card_client_service import CardClientService
from Service.film_service import FilmService
from Service.reservation_service import ReservationService
from Service.undo_redo_service import UndoRedoService
from Service.waterfall import WaterfallDelete
from utils import clear_file


def test_waterfall_service():
    undo_redo_service = UndoRedoService()
    filename = 'test_reservation_service.json'
    filename2 = 'test_card2.json'
    filename3 = 'test_film2,json'
    clear_file(filename)
    clear_file(filename2)
    clear_file(filename3)
    reservation_repository = RepositoryJson(filename)
    card_client_repository = RepositoryJson(filename2)
    film_repository = RepositoryJson(filename3)

    reservation_validator = ReservationValidator()
    film_validator = FilmValidator()
    card_client_validator = CardClientValidator()

    film_service = FilmService(film_repository, film_validator,
                               undo_redo_service)
    film_validator = FilmValidator()
    added = Film('1', 't1', '1900', 10, 'Yes')
    film_validator.validate(added)
    film_service.add_film('1', 't1', '1900', 10, 'Yes')

    card_client_service = CardClientService(card_client_repository,
                                            card_client_validator,
                                            undo_redo_service)
    added = CardClient('2', 't1', 'asdf', 'daasda', '1234567890123',
                       '11-11-1111',
                       '11-11-1111', 0)
    card_client_validator.validate(added)
    card_client_service.add_card_client('2', 't1', 'asdf', 'daasda',
                                        '1234567890123',
                                        '11-11-1111',
                                        '11-11-1111', 10)

    reservation_service = ReservationService(reservation_repository,
                                             film_repository,
                                             card_client_repository,
                                             reservation_validator,
                                             undo_redo_service)
    added = Reservation('1', '1', '1', '11/11/1111 11:11')
    reservation_validator.validate(added)
    waterfall_delete = WaterfallDelete(film_repository, card_client_repository,
                                       reservation_repository, film_service,
                                       card_client_service,
                                       reservation_service, undo_redo_service)
    try:
        assert film_repository.read('1') is not None
        waterfall_delete.delete('1', 'film')
        assert film_repository.read('1') is None
        assert card_client_repository.read('2') is not None
        waterfall_delete.delete('2', 'client card')
        assert card_client_repository.read('2') is None
    except ValueError:
        pass


test_waterfall_service()
