import random
import string

from Domain.film import Film
from Domain.film_validator import FilmValidator
from Domain.generate_operation import GenerateOperation
from Repository.repository import Repository
from Service.undo_redo_service import UndoRedoService


class Generate:
    def __init__(self,
                 film_repository: Repository,
                 film_validator: FilmValidator,
                 undo_redo_service: UndoRedoService):
        self.film_repository = film_repository
        self.film_validator = film_validator
        self.undo_redo_service = undo_redo_service

    def generate(self, n: int):
        """
        Generate n entity
        :param n: The numbers of entities
        :return: The entities
        """
        before = []
        for i in range(0, n):
            idd = str(random.randint(200, 100000000) + i)
            title = ''.join(random.choices(string.ascii_lowercase,
                                           k=random.randint(5, 10)))
            year_apperance = str(random.randint(1990, 2021))
            price_ticket = float(random.randint(100, 9000))
            in_program = random.choice(['0', '1'])
            film = Film(idd, title, year_apperance, price_ticket, in_program)
            self.film_repository.create(film)
            before.append(film)

        self.undo_redo_service.clear_redo()
        add_gen = GenerateOperation(self.film_repository, before)
        self.undo_redo_service.add_to_undo(add_gen)
