import time
from typing import List

from Domain.add_operations import AddOperation
from Domain.card_client import CardClient
from Domain.card_client_validator import CardClientValidator
from Domain.delete_operations import DeleteOperation
from Domain.increase import IncrementOperation
from Domain.modelview import ResView
from Domain.update_operations import UpdateOperation
from Repository.exceptions import DuplicateIdError
from Repository.exceptions import NoSouchIdError
from Repository.repository import Repository
from Service.undo_redo_service import UndoRedoService
from utils import my_sorted


class CardClientService:
    def __init__(self,
                 card_client_repository: Repository,
                 card_client_validator: CardClientValidator,
                 undo_redo_service: UndoRedoService
                 ):
        self.card_client_repository = card_client_repository
        self.card_client_validator = card_client_validator
        self.undo_redo_service = undo_redo_service

    def get_idcard(self, id_card):
        """
        Returns the client card with the id card
        :return: client card with the specified id
        """
        return self.card_client_repository.read(id_card)

    def search(self, text):
        """
        Searchs the introduced text
        :param text: The text which will be searched
        :return: A list with the film which has the introduced text
        """
        result = []
        client_cards = self.card_client_repository.read()
        if check2(text) is False:
            for card in client_cards:
                if (text in card.id_name) or (
                        text in card.name) or (
                        text in card.sur_name) or (
                        text in card.date_of_birth) or (
                        text in card.registration_data):
                    result.append(card)
            return result
        else:
            for card in client_cards:
                if str(text) in str(card.accumulated_point) or str(
                        text) in str(card.id_card_client) or \
                        str(text) in str(card.cnp):
                    result.append(card)
            return result

    def add_card_client(self,
                        id_card_client: str,
                        id_name: str,
                        name: str,
                        sur_name: str,
                        cnp: str,
                        date_of_birth: str,
                        registration_data: str,
                        accumulated_points: float):
        """
        Adds a new client card
        :param id_card_client: The id of the card client
        :param id_name: The id name of the card client
        :param name: The name of the card client
        :param sur_name: The surname of the card client
        :param cnp: cnp of the card client
        :param date_of_birth: date of birth of the card client
        :param registration_data: registration data of the card client
        :param accumulated_points: accumulated points of the card client
        :return:
        """
        cards_client = self.get_all()
        if self.card_client_repository.read(id_card_client) is not None:
            raise DuplicateIdError(
                "There is already a card_client with the id {0}".format(
                    id_card_client))
        lista = []
        for i in cards_client:
            lista.append(getattr(i, "cnp"))
        if len(cnp) != 13:
            raise KeyError("CNP must contain 13 figures.")
        if cnp in lista:
            raise DuplicateIdError(f"Cnp {cnp} already exist.")
        card_client = CardClient(id_card_client, id_name, name, sur_name,
                                 cnp, date_of_birth, registration_data,
                                 accumulated_points)
        self.card_client_validator.validate(card_client)
        self.card_client_repository.create(card_client)
        self.undo_redo_service.clear_redo()
        add_operation = AddOperation(self.card_client_repository, card_client)
        self.undo_redo_service.add_to_undo(add_operation)

    def update_card_client(self,
                           id_card_client: str,
                           id_name: str,
                           name: str,
                           sur_name,
                           cnp: str,
                           date_of_birth: str,
                           registration_data: str,
                           accumulated_point: float):
        """
                Update a  client card
                :param id_card_client: The id of the card client
                :param id_name: The id name of the card client
                :param name: The name of the card client
                :param sur_name: The surname of the card client
                :param cnp: cnp of the card client
                :param date_of_birth: date of birth of the card client
                :param registration_data: registration data of the card client
                :param accumulated_point: accumulated points of the card client
                :return:
                """
        if len(cnp) != 13:
            raise KeyError("CNP must contain 13 figures.")
        if self.card_client_repository.read(id_card_client) is None:
            raise NoSouchIdError(
                f"There isn't any card_client "
                f"with {id_card_client} id to update"
            )
        else:
            before_update = self.card_client_repository.read(id_card_client)

        card_client = CardClient(id_card_client, id_name, name, sur_name,
                                 cnp, date_of_birth, registration_data,
                                 accumulated_point)
        self.card_client_validator.validate(card_client)
        self.card_client_repository.update(card_client)

        self.undo_redo_service.clear_redo()
        update_operation = UpdateOperation(self.card_client_repository,
                                           before_update,
                                           card_client)
        self.undo_redo_service.add_to_undo(update_operation)

    def delete_card(self, id_card_client: str):
        """
        Delete a card client
        :param id_card_client: The id of the card client which will be deleted
        :return: Returns client cards without the card with de id card client
        """
        card_client_del = self.card_client_repository.read(id_card_client)

        if self.card_client_repository.read(id_card_client) is None:
            raise NoSouchIdError(
                f"There isn't any card_client "
                f"with {id_card_client} id to delete"
            )
        self.card_client_repository.delete(id_card_client)
        self.undo_redo_service.clear_redo()
        delete_operation = DeleteOperation(self.card_client_repository,
                                           card_client_del)

        self.undo_redo_service.add_to_undo(delete_operation)

    def get_all(self) -> List[CardClient]:
        return self.card_client_repository.read()

    def card_client_orderd(self):
        """
        Oreder the card clients by the accumulated points
        :return: cards client ordered descending by the accumulated points
        """

        def inner(reservations):
            if not reservations:
                return []

            res = reservations[0]
            return [ResView(res.name, res.accumulated_point)] + inner(
                reservations[1:])

        reservations = self.get_all()
        res_lens = inner(reservations)
        return my_sorted(res_lens,
                         key=lambda x: x.accumulated_points,
                         reverse=True)

    def card_incrementation(self, value: float, start_day: str,
                            final_day: str):
        """
        Increases by a given value the points on all cards whose birthday
        is in a given range.
        :param value:
        :param start_day:
        :param final_day:
        :return:
        """
        before = []
        after = []
        cards = self.card_client_repository.read()
        formatted_date1 = time.strptime(start_day, "%d-%m-%Y")
        formatted_date2 = time.strptime(final_day, "%d-%m-%Y")
        for card in cards:
            formatted_date3 = time.strptime(
                card.date_of_birth, "%d-%m-%Y")
            if formatted_date1 <= formatted_date3 <= formatted_date2:
                before.append(card)
                self.update_card_client(card.id_entity, card.id_name,
                                        card.name, card.sur_name, card.cnp,
                                        card.date_of_birth,
                                        card.registration_data,
                                        card.accumulated_point+value)
        for card in self.card_client_repository.read():
            after.append(card)
        self.undo_redo_service.clear_redo()
        increment_operation = IncrementOperation(self.card_client_repository,
                                                 before,
                                                 after)
        self.undo_redo_service.add_to_undo(increment_operation)


def check2(number):
    """
    Chech if a number is float
    :param number: The number to verify
    :return: True if it is float otherwise False
    """
    try:
        float(number)
        return True
    except ValueError:
        return False
