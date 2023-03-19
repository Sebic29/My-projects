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


def test_search_film():
    undo_redo_service = UndoRedoService()
    filename = 'test_search_film.json'
    film_validator = FilmValidator()
    clear_file(filename)
    film_repository = RepositoryJson(filename)
    film_service = FilmService(film_repository, film_validator,
                               undo_redo_service)
    added = Film('1', 't1', '1900', 10, 'Not')
    film_validator.validate(added)
    film_service.add_film('1', 't1', '1900', 10, 'Not')
    assert film_service.search_text('1900') == film_service.get_all()


def test_search_card():
    undo_redo_service = UndoRedoService()
    filename = 'test_card_client_search.json'
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
    assert card_client_service.search('t1') == card_client_service.get_all()


def test_res_ors_in_range():
    undo_redo_service = UndoRedoService()
    filename = 'test_res_ors_in_range.json'
    filename2 = 'test_card333.json'
    filename3 = 'test_film333.json'
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
                       '11-11-1111', 10)
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
    added1 = Reservation('1', '1', '1', '11/11/1111 10:11')
    reservation_validator.validate(added1)
    reservation_service.add_reservation('1', '1', '1', '11/11/1111 10:11')
    added3 = Reservation('2', '1', '1', '11/11/1111 12:11')
    reservation_validator.validate(added3)
    reservation_service.add_reservation('2', '1', '1', '11/11/1111 12:11')
    added4 = Reservation('3', '1', '1', '11/11/1111 9:00')
    reservation_validator.validate(added4)
    reservation_service.add_reservation('3', '1', '1', '11/11/1111 9:00')
    added4 = Reservation('4', '1', '1', '11/11/1111 15:00')
    reservation_validator.validate(added4)
    reservation_service.add_reservation('4', '1', '1', '11/11/1111 15:00')
    sortt = reservation_service.res_ors_in_range('10:00', '13:11')
    assert reservation_service.res_ors_in_range('10:00', '13:11') == sortt


def tests_functions():
    test_search_card()
    test_search_film()
    test_res_ors_in_range()
