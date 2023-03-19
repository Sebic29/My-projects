from Domain.waterfall_undo_redo import DeleteCascadeOperation
from Repository.repository import Repository
from Service.card_client_service import CardClientService
from Service.film_service import FilmService
from Service.reservation_service import ReservationService
from Service.undo_redo_service import UndoRedoService


class WaterfallDelete:
    def __init__(self, film_repository: Repository,
                 client_card_repository: Repository,
                 reservation_repository: Repository,
                 film_service: FilmService,
                 card_client_service: CardClientService,
                 reservation_service: ReservationService,
                 undo_redo_service: UndoRedoService):
        self.film_repository = film_repository
        self.client_card_repository = client_card_repository
        self.reservation_repository = reservation_repository
        self.film_service = film_service
        self.card_client_service = card_client_service
        self.reservation_service = reservation_service
        self.undo_redo_service = undo_redo_service

    def delete(self, id_entity: str, entity: str):
        """
        Deletes in cascade
        :param id_entity: id entity
        :param entity: entity type entity/client card
        :return:
        """
        film_list = []
        reservation_list = []
        client_card_list = []
        if entity == 'film':
            if self.film_repository.read(id_entity):
                film = self.film_repository.read(id_entity)
                film_list.append(film)
                self.film_repository.delete(id_entity)
            for reservation in self.reservation_service.get_all():
                if reservation.id_film == id_entity:
                    reservation_list.append(reservation)
                    self.reservation_service.delete_reservation(
                        reservation.id_entity)
            self.undo_redo_service.clear_redo()
            delete_operation = DeleteCascadeOperation(
                self.film_repository,
                self.reservation_repository,
                film_list,
                reservation_list)
            self.undo_redo_service.add_to_undo(delete_operation)

        elif entity == 'client card':
            if self.client_card_repository.read(id_entity):
                client_card = self.client_card_repository.read(id_entity)
                client_card_list.append(client_card)
                self.client_card_repository.delete(id_entity)
            for reservation in self.reservation_service.get_all():
                if reservation.id_card_client == id_entity:
                    reservation_list.append(reservation)
                    self.reservation_service.delete_reservation(
                        reservation.id_entity)
            self.undo_redo_service.clear_redo()
            delete_operation = DeleteCascadeOperation(
                self.client_card_repository, self.reservation_repository,
                client_card_list, reservation_list)
            self.undo_redo_service.add_to_undo(delete_operation)
