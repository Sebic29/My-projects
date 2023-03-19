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
from utils import clear_file


def test_reservation_service():
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
    added = CardClient('1', 't1', 'asdf', 'daasda', '1234567890123',
                       '11-11-1111',
                       '11-11-1111', 0)
    card_client_validator.validate(added)
    card_client_service.add_card_client('1', 't1', 'asdf', 'daasda',
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
    card = card_client_repository.read('1')
    accumulated_points = reservation_service.acumulate_points('1')
    if card is not None:
        card.accumulated_point += accumulated_points
        card_client_repository.update(card)
    reservation_service.add_reservation('1', '1', '1', '11/11/1111 11:11')
    assert reservation_repository.read(added.id_entity) == added
    added2 = Reservation('3', '1', '1', '12/12/1211 12:11')
    reservation_validator.validate(added2)
    reservation_service.add_reservation('3', '1', '1', '12/12/1211 12:11')
    before_update = reservation_repository.read()
    reservation_service.update_reservation('3', '1', '1', '13/11/1234 13:11')
    assert reservation_repository.read() != before_update
    reservation_service.delete_reservation(added2.id_entity)
    assert reservation_repository.read(added.id_entity) == added

    reservation_service.add_reservation('100', '1', '1', '12/12/1211 12:11')
    reservation_service.add_reservation('14', '1', '1', '21/11/2020 11:11')
    reservation_service.del_res('10/11/1111', '20/11/1111')
    assert reservation_repository.read('1') is None


test_reservation_service()
