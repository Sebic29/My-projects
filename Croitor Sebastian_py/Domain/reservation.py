from dataclasses import dataclass

from Domain.entity import Entity


@dataclass
class Reservation(Entity):
    """
    Create a reservation:
    -id_film: the id of the film
    -id_card_client: the id of the card client
    -date_and_hour: the hour and the date of the reservation
    """
    id_film: str
    id_card_client: str
    date_and_hour: str
