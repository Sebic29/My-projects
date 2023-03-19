from typing import List

from Domain.UndoRedoOperations import UndoRedoOperation
from Domain.entity import Entity
from Repository.repository import Repository


class IncrementOperation(UndoRedoOperation):

    def __init__(self, repository1: Repository,
                 before_increase: List[Entity],
                 after_increase: List[Entity]
                 ):
        self.repository1 = repository1
        self.before_increase = before_increase
        self.after_increase = after_increase

    def undo(self):
        for i in self.before_increase:
            self.repository1.update(i)

    def redo(self):
        for i in self.after_increase:
            self.repository1.update(i)
