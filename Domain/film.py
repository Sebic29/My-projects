from dataclasses import dataclass

from Domain.entity import Entity


@dataclass
class Film(Entity):
    """
    Create a film:
    -title: the title of the film
    -year_appereance: the year of the film was published
    -price-ticket: the price of the ticket
    -in_program:
    """
    title: str
    year_apperance: str
    price_ticket: float
    in_program: str
