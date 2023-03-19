from dataclasses import dataclass

from Domain.entity import Entity


@dataclass
class CardClient(Entity):
    """
    Create a card client`
    -id_name: the id of the clien with the name
    -first_name: the first name of the client
    -sur_name:
    -cnp: the identification number of the every client
    -date_of_birth: the date of the birth of the every client
    -registration_data: the registration_data of every client
    -accumulated_points: the accumulated poitns of every client
    """
    id_name: str
    name: str
    sur_name: str
    cnp: str
    date_of_birth: str
    registration_data: str
    accumulated_point: float
