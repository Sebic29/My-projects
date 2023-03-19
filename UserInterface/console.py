from Domain.card_client_validator import CardClienValidationError
from Domain.film_validator import FilmValidationError
from Domain.reservation_validator import ReservationValidationError
from Repository.exceptions import DuplicateIdError
from Service.RandomEntityGenerate import Generate
from Service.card_client_service import CardClientService
from Service.film_service import FilmService
from Service.reservation_service import ReservationService
from Service.undo_redo_service import UndoRedoService
from Service.waterfall import WaterfallDelete


class Console:
    def __init__(self,
                 film_service: FilmService,
                 card_client_service: CardClientService,
                 reservation_service: ReservationService,
                 generate_service: Generate,
                 waterfall_service: WaterfallDelete,
                 undo_redo_service: UndoRedoService):

        self.film_service = film_service
        self.card_client_service = card_client_service
        self.reservation_service = reservation_service
        self.generate_service = generate_service
        self.waterfall_service = waterfall_service
        self.undo_redo_service = undo_redo_service

    def show_menu(self):
        print('a[film|card|res] - add film or card '
              'client or reservation.')
        print('u[film|card|res] - update film or card '
              'client or reservation.')
        print('d[film|card|res] - delete film or card '
              'client or reservation.')
        print('s[film|card|res] - showall film or card '
              'client or reservation.')
        print('1)Searchfilm - search full text in films')
        print('2)searchcard - search full text in cards')
        print('3)Generate   - generate n entity ')
        print('4)Range      - reservations from a given range')
        print('5)Shownrres  - films ordered by numbers of reservations')
        print('6)Showordcard - cards ordered by acccumulated points')
        print('7)Delresrange(/) - delete reservation from a given day interval')
        print('8)Incr(-)    - increments accumulated points with a value given')
        print('9)Deletewt   - waterfall delete(client card/film)')
        print('Undo')
        print('Redo')
        print('x. Exit')

    def run_console(self):
        while True:
            self.show_menu()
            opt = input('Choose an option: ')

            if opt == 'afilm':
                self.handle_add_film()
            elif opt == 'acard':
                self.handle_add_card_client()
            elif opt == 'ares':
                self.handle_add_reservation()
            elif opt == 'sfilm':
                self.handle_show_all(self.film_service.get_all())
            elif opt == 'scard':
                self.handle_show_all(self.card_client_service.get_all())
            elif opt == 'sres':
                self.handle_show_all(self.reservation_service.get_all())
            elif opt == 'dfilm':
                self.handle_del_film()
            elif opt == 'dcard':
                self.handle_delete_card_client()
            elif opt == 'dres':
                self.handle_delete_reservation()
            elif opt == 'ufilm':
                self.handle_update_film()
            elif opt == 'ucard':
                self.handle_update_card_client()
            elif opt == 'ures':
                self.handle_update_reservation()
            elif opt == 'Searchfilm':
                self.handle_searchfilm()
            elif opt == 'Searchcard':
                self.handle_serchcard()
            elif opt == 'Generate':
                self.handle_generate_entity()
            elif opt == 'Range':
                self.handle_range()
            elif opt == 'Shownrres':
                self.handle_film_order()
            elif opt == 'Showordcard':
                self.handle_card_order()
            elif opt == 'Delresrange':
                self.handle_del_res()
            elif opt == 'Incr':
                self.handle_incr()
            elif opt == 'Deletewt':
                self.handle_waterfall()
            elif opt == 'Undo':
                self.undo_redo_service.do_undo()
            elif opt == 'Redo':
                self.undo_redo_service.do_redo()
            elif opt == 'x':
                break
            else:
                print('Invalid command,retry.')

    def handle_add_film(self):
        try:
            id_film = input('Give the id of the film: ')
            title = input('Give the title of the film: ')
            year_apperance = input('Give the year '
                                   'apperance of the film: ')
            price_ticket = float(input('Give the price '
                                       'ticket of the film: '))
            in_program = input(
                'Yes if the film is in program or Not otherwise: ')
            self.film_service.add_film(id_film, title,
                                       year_apperance, price_ticket,
                                       in_program)
        except FilmValidationError as ve:
            print('Eror validation:', ve)
        except DuplicateIdError as ke:
            print('Duplicate ID:', ke)
        except Exception as ex:
            print('Eror:', ex)

    def handle_show_all(self, objects):
        for obj in objects:
            print(obj)

    def handle_add_card_client(self):
        try:
            id_card_client = input('Give the id of the card '
                                   'client: ')
            id_name = input('Give the id name: ')
            name = input('Give the first name: ')
            sur_name = input('Give the surname: ')
            cnp = input('Give the cnp: ')
            date_of_birth = input('Give the date of birth: ')
            registration_data = input('Give the registration data: ')

            accumulated_points = 0
            self.card_client_service.add_card_client(id_card_client,
                                                     id_name,
                                                     name,
                                                     sur_name,
                                                     cnp,
                                                     date_of_birth,
                                                     registration_data,
                                                     accumulated_points)

        except CardClienValidationError as ve:
            print('Eror validation:', ve)
        except DuplicateIdError as ke:
            print('Eror ID:', ke)
        except Exception as ex:
            print('Eror:', ex)

    def handle_add_reservation(self):
        try:
            id_reservation = input('Give the id of reservation: ')
            id_film = input('Give the id of the film: ')
            id_card_client = input('Give the id of the card client: ')
            date_and_hour = input('Give the date and hour of the '
                                  'reservation: ')
            if self.film_service.film_repository.read(id_film) is None:
                raise KeyError('Eror ID')
            self.reservation_service.add_reservation(id_reservation,
                                                     id_film,
                                                     id_card_client,
                                                     date_and_hour)
            short = self.card_client_service.get_idcard(id_card_client)
            print(f"On the card {id_card_client} has been added "
                  f"{self.reservation_service.acumulate_points(id_film)}"
                  f" points. "
                  f"Total points are "
                  f"{short.accumulated_point}.")

        except ReservationValidationError as ve:
            print('Eror validation:', ve)
        except DuplicateIdError as ke:
            print('Eror ID:', ke)
        except Exception as ex:
            print('Eror:', ex)

    def handle_update_film(self):
        try:
            to_update = input('Give the id of the film which '
                              'need to be updated: ')
            title = input('Give the title of the film: ')
            year_apperance = input('Give the year apperance '
                                   'of the film: ')
            price_ticket = float(input('Give the price ticket '
                                       'of the film: '))
            in_program = input(
                'Yes if the film is in program or Not otherwise: ')

            self.film_service.update_film(to_update, title,
                                          year_apperance, price_ticket,
                                          in_program)

        except FilmValidationError as ve:
            print('Eror validation:', ve)
        except DuplicateIdError as ke:
            print('Eror ID:', ke)
        except Exception as ex:
            print('Eror:', ex)

    def handle_del_film(self):
        try:
            id_film = input('Give the id of the film which will be deleted: ')
            self.film_service.delete_film(id_film)
        except FilmValidationError as ve:
            print('Eror validation:', ve)
        except DuplicateIdError as ke:
            print('Eror ID:', ke)
        except Exception as ex:
            print('Eror:', ex)

    def handle_update_card_client(self):
        try:
            id_card_client = input('Give the id of the card '
                                   'client: ')
            id_name = input('Give the id name: ')
            name = input('Give the first name: ')
            sur_name = input('Give the surname: ')
            cnp = input('Give the cnp: ')
            date_of_birth = input('Give the date of birth: ')
            registration_data = input('Give the registration data: ')
            accumulated_point = float(input('Give the accumulated points: '))

            self.card_client_service.update_card_client(
                id_card_client,
                id_name,
                name,
                sur_name,
                cnp,
                date_of_birth,
                registration_data,
                accumulated_point)

        except CardClienValidationError as ve:
            print('Eror validation:', ve)
        except DuplicateIdError as ke:
            print('Eror ID:', ke)
        except Exception as ex:
            print('Eror:', ex)

    def handle_delete_card_client(self):
        try:
            id_card_client = input(
                'Give the id of the client card which will be deleted: ')
            self.card_client_service.delete_card(id_card_client)
        except CardClienValidationError as ve:
            print('Eror validation:', ve)
        except DuplicateIdError as ke:
            print('Eror ID:', ke)
        except Exception as ex:
            print('Eror:', ex)

    def handle_update_reservation(self):
        try:
            id_reservation = input('Give the id of reservation:')
            id_film = input('Give the id of the film: ')
            id_card_client = input('Give the id of the card client:')
            date_and_hour = input('Give the date and hour of the '
                                  'reservation: ')
            self.reservation_service.update_reservation(id_reservation,
                                                        id_film,
                                                        id_card_client,
                                                        date_and_hour)
        except ReservationValidationError as ve:
            print('Eror validation:', ve)
        except DuplicateIdError as ke:
            print('Eror ID:', ke)
        except Exception as ex:
            print('Eror:', ex)

    def handle_delete_reservation(self):
        try:
            id_reservation = input('Give the id of the reservetion'
                                   ' which will be deleted: ')
            self.reservation_service.delete_reservation(id_reservation)
        except ReservationValidationError as ve:
            print('Eror validation:', ve)
        except DuplicateIdError as ke:
            print('Eror ID:', ke)
        except Exception as ex:
            print('Eror:', ex)

    def handle_generate_entity(self):
        n = int(input('Give the number of entity you want to generate:  '))
        self.generate_service.generate(n)

    def handle_searchfilm(self):
        text = input('Give the text you want to search in films: ')
        print(self.film_service.search_text(text))

    def handle_serchcard(self):
        text = input('Give the text you want to search in client cards: ')
        print(self.card_client_service.search(text))

    def handle_film_order(self):
        print(self.reservation_service.film_order_by_reservations_number())

    def handle_card_order(self):
        a = self.card_client_service.card_client_orderd()
        for i in a:
            print(i)

    def handle_range(self):
        try:
            start_hour = input('Give the start hour: ')
            end_hour = input('Give the final hour: ')
            for a in self.reservation_service.res_ors_in_range(start_hour,
                                                               end_hour):
                print(a)
        except ReservationValidationError as ve:
            print('Eror validation:', ve)
        except DuplicateIdError as ke:
            print('Eror ID:', ke)
        except Exception as ex:
            print('Eror:', ex)

    def handle_del_res(self):
        try:
            start_hour = input('Give the start day: ')
            end_hour = input('Give the final day: ')
            print(self.reservation_service.del_res(start_hour, end_hour))
        except ReservationValidationError as ve:
            print('Eror validation:', ve)
        except DuplicateIdError as ke:
            print('Eror ID:', ke)
        except Exception as ex:
            print('Eror:', ex)

    def handle_incr(self):
        try:
            start_hour = input('Give the start day: ')
            end_hour = input('Give the final day: ')
            value = float(input('Give the value: '))
            self.card_client_service.card_incrementation(value, start_hour,
                                                         end_hour)
        except ReservationValidationError as ve:
            print('Eror validation:', ve)
        except DuplicateIdError as ke:
            print('Eror ID:', ke)
        except Exception as ex:
            print('Eror:', ex)

    def handle_waterfall(self):
        try:
            id_entity = input(
                'Give the id of the entity which will be deleted: ')
            entity = input('Give the entity which will be deleted: ')
            self.waterfall_service.delete(id_entity, entity)
        except ReservationValidationError as ve:
            print('Eror validation:', ve)
        except DuplicateIdError as ke:
            print('Eror ID:', ke)
        except Exception as ex:
            print('Eror:', ex)
