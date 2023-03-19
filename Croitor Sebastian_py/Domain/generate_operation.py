from typing import List

from Domain.UndoRedoOperations import UndoRedoOperation
from Domain.entity import Entity
from Repository.repository import Repository


class GenerateOperation(UndoRedoOperation):

    def __init__(self, repository: Repository,
                 added_entity: List[Entity]):
        self.repository = repository
        self.added_entity = added_entity

    def undo(self):
        for i in self.added_entity:
            self.repository.delete(i.id_entity)

    def redo(self):
        for i in self.added_entity:
            self.repository.create(i)
