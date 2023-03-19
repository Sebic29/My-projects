from Domain.film import Film


class FilmValidationError(Exception):
    pass


class FilmValidator:
    def validate(self, film: Film):
        if film.price_ticket < 0:
            raise FilmValidationError('The price of the ticket '
                                      'need to be only pozitive')
