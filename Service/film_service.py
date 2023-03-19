from typing import List

from Domain.add_operations import AddOperation
from Domain.delete_operations import DeleteOperation
from Domain.film import Film
from Domain.film_validator import FilmValidator
from Domain.update_operations import UpdateOperation
from Repository.exceptions import DuplicateIdError, NoSouchIdError
from Repository.repository import Repository
from Service.undo_redo_service import UndoRedoService


class FilmService:
    def __init__(self,
                 film_repository: Repository,
                 film_validator: FilmValidator,
                 undo_redo_service: UndoRedoService
                 ):
        self.film_repository = film_repository
        self.film_validator = film_validator
        self.undo_redo_service = undo_redo_service

    def search_text(self, text: str):
        """
                Searchs the introduced text
                :param text: The text which will be searched
                :return: A list with the film which has the introduced text
                """
        result = []
        films = self.film_repository.read()
        if check(text) is False:
            for film in films:
                if (text in film.title) or (
                        text in film.in_program) or (
                        text in film.year_apperance):
                    result.append(film)
            return result
        else:
            for film in films:
                if str(text) in str(film.price_ticket) or str(
                        text) in str(film.id_entity) or \
                        str(text) in str(film.year_apperance):
                    result.append(film)
            return result

    def add_film(self,
                 id_film: str,
                 title: str,
                 year_apperance: str,
                 price_ticket: float,
                 in_program: str):
        """
        Add a film
        id_film: id of the film
        title: title of the film
        year_apperance: the year apperanec
        price_ticket: the price of the film
        in_program: if it is in program or not
        """
        if self.film_repository.read(id_film) is not None:
            raise DuplicateIdError(
                "There is already a film with the id {0}".format(
                    id_film))
        film = Film(id_film, title, year_apperance, price_ticket, in_program)
        self.film_validator.validate(film)
        self.film_repository.create(film)
        self.undo_redo_service.clear_redo()
        add_operation = AddOperation(self.film_repository, film)
        self.undo_redo_service.add_to_undo(add_operation)

    def update_film(self,
                    id_film: str,
                    title: str,
                    year_apperance: str,
                    price_ticket: float,
                    in_program: str):
        """
        Update a film
        id_film: id of the film
        title: title of the film
        year_apperance: the year apperanec
        price_ticket: the price of the film
        in_program: if it is in program or not
        """
        if self.film_repository.read(id_film) is None:
            msg = f"There isn't any film with {id_film} id."
            raise NoSouchIdError(msg)
        else:
            before_update = self.film_repository.read(id_film)

        film = Film(id_film, title, year_apperance, price_ticket, in_program)
        self.film_validator.validate(film)
        self.film_repository.update(film)
        self.undo_redo_service.clear_redo()
        update_operation = UpdateOperation(self.film_repository,
                                           before_update,
                                           film)
        self.undo_redo_service.add_to_undo(update_operation)

    def delete_film(self, id_film: str):
        """
        Delete a film
        :param id_film:the id of the film which will be deleted
        :return:
        """
        film_del = self.film_repository.read(id_film)
        if self.film_repository.read(id_film) is None:
            raise NoSouchIdError(
                f"There isn't any film with {id_film} id to delete"
            )

        self.film_repository.delete(id_film)
        self.undo_redo_service.clear_redo()
        delete_operation = DeleteOperation(self.film_repository,
                                           film_del)
        self.undo_redo_service.add_to_undo(delete_operation)

    def get_all(self) -> List[Film]:
        return self.film_repository.read()


def check(number):
    try:
        float(number)
        return True
    except ValueError:
        return False
