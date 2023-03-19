import datetime
import time
from typing import List

from Domain.add_operations import AddOperation
from Domain.delete_operations import DeleteOperation
from Domain.interval_Del import DeleteIntervalOperation
from Domain.reservation import Reservation
from Domain.reservation_validator import ReservationValidator
from Domain.update_operations import UpdateOperation
from Repository.exceptions import DuplicateIdError, NoSouchIdError
from Repository.repository import Repository
from Service.undo_redo_service import UndoRedoService


class ReservationService:
    def __init__(self,
                 reservation_repository: Repository,
                 film_repository: Repository,
                 card_client_repository: Repository,
                 resevartion_validator: ReservationValidator,
                 undo_redo_service: UndoRedoService
                 ):

        self.reservation_repository = reservation_repository
        self.film_repository = film_repository
        self.card_client_repository = card_client_repository
        self.reservation_validator = resevartion_validator
        self.undo_redo_service = undo_redo_service

    def get_inprogram(self, id_entity: str):
        film = self.film_repository.read(id_entity)
        if film is not None:
            if film.in_program == 'Yes':
                return True
        return False

    def acumulate_points(self, id_film: str):
        """
        Returns the accumulated points
        :param id_film: The id of the film for which we are returning the price
        :return: The numbers of the accumulated points.
        """
        film = self.film_repository.read(id_film)
        accumulated_points = 0
        if id_film == '':
            for fl in self.film_repository.read():
                if fl.id_entity == id_film:
                    accumulated_points = -1
                    return accumulated_points
        if film is not None:
            accumulated_points = accumulated_points \
                                 + 10 / 100 * film.price_ticket
        return accumulated_points

    def add_reservation(self,
                        id_reservation: str,
                        id_film: str,
                        id_card_client: str,
                        date_and_hour: str):
        """
        Add a reservation
        :param id_reservation: the id of the reservatin
        :param id_film: the id of the film
        :param id_card_client: the id of the card client
        :param date_and_hour: date and hour of the reservation
        :return:
        """
        card = self.card_client_repository.read(id_card_client)
        accumulated_points = self.acumulate_points(id_film)
        if card is not None and accumulated_points != -1:
            card.accumulated_point += accumulated_points
            self.card_client_repository.update(card)
        if self.reservation_repository.read(id_reservation):
            raise DuplicateIdError(
                f'The reservation with id {id_reservation} already'
                f' exists ')
        if self.get_inprogram(id_film) is not True:
            raise NoSouchIdError(f'The film with id {id_film} is not'
                                 f' in program ')

        if self.film_repository.read(id_film) is None:
            raise NoSouchIdError(f'There is no film with id'
                                 f' {id_film}')
        if self.card_client_repository.read(id_card_client) \
                is None:
            raise NoSouchIdError(f'There is no client card with id '
                                 f'{id_card_client}')

        reservation = Reservation(id_reservation, id_film,
                                  id_card_client, date_and_hour)

        self.reservation_validator.validate(reservation)
        self.reservation_repository.create(reservation)
        self.undo_redo_service.clear_redo()
        add_operation = AddOperation(self.reservation_repository, reservation)
        self.undo_redo_service.add_to_undo(add_operation)

    def update_reservation(self,
                           id_reservation: str,
                           id_film: str,
                           id_card_client: str,
                           date_and_hour: str):
        """
        Update a reservation
        :param id_reservation: the id of the reservatin
        :param id_film: the id of the film
        :param id_card_client: the id of the card client
        :param date_and_hour: date and hour of the reservation
        :return:
        """
        film = self.film_repository.read(id_film)
        card = self.card_client_repository.read(id_card_client)
        if film.in_program == 'Not':
            raise NoSouchIdError('The reservantion can not be made because '
                                 'the film is not in program')
        if self.film_repository.read(id_film) is None:
            raise NoSouchIdError(f'There is no film with the id'
                                 f'{id_film}')
        if self.card_client_repository.read(id_card_client) \
                is None:
            raise NoSouchIdError(f'There is no card client with the id '
                                 f'{id_card_client}')
        if self.reservation_repository.read(id_reservation) is None:
            msg = f"There is no reservation to update " \
                  f"with {id_reservation} id."
            raise NoSouchIdError(msg)
        else:
            before_update = self.reservation_repository.read(id_reservation)
        accumulated_points = self.acumulate_points(id_film)
        if card is not None:
            card.accumulated_point += accumulated_points
            self.card_client_repository.update(card)

        reservation = Reservation(id_reservation, id_film,
                                  id_card_client, date_and_hour)

        self.reservation_validator.validate(reservation)
        self.reservation_repository.update(reservation)
        self.undo_redo_service.clear_redo()
        update_operation = UpdateOperation(self.reservation_repository,
                                           before_update,
                                           reservation)
        self.undo_redo_service.add_to_undo(update_operation)

    def delete_reservation(self, id_reservation: str):
        """
        Delete reservation
        :param id_reservation: Id of the reservattion which will be deleted
        :return: The reservations without reservation with id reservation
        """
        reservation_del = self.reservation_repository.read(id_reservation)
        if self.reservation_repository.read(id_reservation) is None:
            raise NoSouchIdError(
                f'There is not any reservation with {id_reservation}')
        self.reservation_repository.delete(id_reservation)
        self.undo_redo_service.clear_redo()
        delete_operation = DeleteOperation(self.reservation_repository,
                                           reservation_del)
        self.undo_redo_service.add_to_undo(delete_operation)

    def get_all(self) -> List[Reservation]:
        return self.reservation_repository.read()

    def film_order_by_reservations_number(self):
        """
        Order films by booking numbers
        :return:
        """

        result = []
        numberres = {}
        for film in self.film_repository.read():
            numberres[film.id_entity] = 0
        for reservation in self.reservation_repository.read():
            numberres[reservation.id_film] += 1

        numberres = sorted(numberres.items(), key=lambda x: x[1],
                           reverse=True)

        for id_film, value in numberres:
            result.append({'Film': self.film_repository.read(id_film),
                           'NrRes': value})

        return result

    def res_ors_in_range(self, star_hour: str, final_hour: str):
        """
        Show all reservation from a given hour interval
        :param star_hour: start hour of the interval
        :param final_hour: final hour of the interval
        :return: a list with all reservation from a given hour interval
        """
        result = []
        try:
            hour_format = "%H:%M"
            datetime.datetime.strptime(star_hour, hour_format)
            datetime.datetime.strptime(final_hour, hour_format)
        except ValueError:
            raise ValueError("Date hour format is invalid. ")
        formatted_date1 = time.strptime(star_hour, "%H:%M")
        formatted_date2 = time.strptime(final_hour, "%H:%M")
        for reservation in self.reservation_repository.read():
            formatted_date3 = time.strptime(
                reservation.date_and_hour.split(' ')[1], "%H:%M")
            if formatted_date1 <= formatted_date3 <= formatted_date2:
                result.append(reservation)
        return result

    def del_res(self, start_day: str, final_day: str):
        """
        Delete de reservation from a given day interval
        :param start_day: first parameter of the interval
        :param final_day: second parameter of the interval
        :return:
        """
        del_res = []
        formatted_date1 = time.strptime(start_day, "%d/%m/%Y")
        formatted_date2 = time.strptime(final_day, "%d/%m/%Y")
        for reservation in self.reservation_repository.read():
            formatted_date3 = time.strptime(
                reservation.date_and_hour.split(' ')[0], "%d/%m/%Y")
            if formatted_date1 <= formatted_date3 <= formatted_date2:
                del_res.append(reservation)
                self.delete_reservation(reservation.id_entity)
        self.undo_redo_service.clear_redo()
        delete_operation = DeleteIntervalOperation(self.reservation_repository,
                                                   del_res)
        self.undo_redo_service.add_to_undo(delete_operation)
