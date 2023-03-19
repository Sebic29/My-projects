import datetime

from Domain.reservation import Reservation


class ReservationValidationError(Exception):
    pass


class ReservationValidator:
    def validate(self, reservation: Reservation):
        date_format = "%d/%m/%Y %H:%M"
        if datetime.datetime.strptime(reservation.date_and_hour,
                                      date_format) is None:
            raise ReservationValidationError('The format of the '
                                             'reservation date is wrong')
