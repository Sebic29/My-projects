from Domain.card_client_validator import CardClientValidator
from Domain.film_validator import FilmValidator
from Domain.reservation_validator import ReservationValidator
from Repository.json_repository import RepositoryJson
from Service.RandomEntityGenerate import Generate
from Service.card_client_service import CardClientService
from Service.film_service import FilmService
from Service.reservation_service import ReservationService
from Service.undo_redo_service import UndoRedoService
from Service.waterfall import WaterfallDelete
from Tests.test_card_client_repository import test_card_client_repository
from Tests.test_card_client_service import test_card_client_service
from Tests.test_film_repository import test_film_repository
from Tests.test_film_service import test_film_service
from Tests.test_functions import tests_functions
from Tests.test_reservation_repository import test_reservation_repository
from Tests.test_reservation_service import test_reservation_service
from Tests.waterfall_test import test_waterfall_service
from UserInterface.console import Console


def main():
    undo_redo_service = UndoRedoService()

    film_repository = RepositoryJson('films.json')
    film_validator = FilmValidator()
    film_service = FilmService(film_repository, film_validator,
                               undo_redo_service)

    generate_service = Generate(film_repository, film_validator,
                                undo_redo_service)

    card_client_repository = RepositoryJson('card_client.json')
    card_client_validator = CardClientValidator()
    card_client_service = CardClientService(card_client_repository,
                                            card_client_validator,
                                            undo_redo_service)

    reservation_repository = RepositoryJson('reservation.json')
    reservation_validator = ReservationValidator()
    reservation_service = ReservationService(reservation_repository,
                                             film_repository,
                                             card_client_repository,
                                             reservation_validator,
                                             undo_redo_service)
    waterfall_service = WaterfallDelete(film_repository,
                                        card_client_repository,
                                        reservation_repository, film_service,
                                        card_client_service,
                                        reservation_service, undo_redo_service)
    console = Console(film_service, card_client_service, reservation_service,
                      generate_service, waterfall_service, undo_redo_service)
    console.run_console()


if __name__ == '__main__':
    test_film_repository()
    test_film_service()
    test_card_client_repository()
    test_card_client_service()
    test_reservation_repository()
    test_reservation_service()
    tests_functions()
    test_waterfall_service()
    main()
