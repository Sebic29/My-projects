from Domain.reservation import Reservation

from Repository.json_repository import RepositoryJson
from utils import clear_file


def test_reservation_repository():
    filename = 'test_reservation_repository.json'
    clear_file(filename)
    reservation_repository = RepositoryJson(filename)
    addeed = Reservation('1', '1', '1', '11/11/1111 11:11')
    reservation_repository.create(addeed)
    assert reservation_repository.read(addeed.id_film)


test_reservation_repository()
