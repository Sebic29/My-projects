import datetime

from Domain.card_client import CardClient


class CardClienValidationError(Exception):
    pass


class CardClientValidator:
    def validate(self, card_client: CardClient):
        date_format = "%d-%m-%Y"
        if datetime.datetime.strptime(card_client.date_of_birth,
                                      date_format) is None:
            raise CardClienValidationError("It is not good the format")

        if datetime.datetime.strptime(card_client.registration_data,
                                      date_format) is None:
            raise CardClienValidationError("It is not good the format")
