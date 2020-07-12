import datetime
# import pickle

from domain.client_card_validator import ClientCardValidator
from domain.medicament_validator import MedicamentValidator

# from repository.client_card_repository import ClientCardInMemoryRepository
# from repository.medicament_repository import MedicamentInMemoryRepository
# from repository.transaction_repository import TransactionInMemoryRepository
from repository.GenericFileRepository import GenericFileRepository
from service.client_card_service import ClientCardService
from service.medicament_service import MedicamentService
from service.transaction_service import TransactionService
from user_interface.console import Console


# medicament_repository = MedicamentInMemoryRepository()
# client_card_repository = ClientCardInMemoryRepository()
# transaction_repository = TransactionInMemoryRepository()


medicament_repository = GenericFileRepository("meds.pkl")
client_card_repository = GenericFileRepository("client_cards.pkl")
transaction_repository = GenericFileRepository("transactions.pkl")

medicament_validator = MedicamentValidator()
client_card_validator = ClientCardValidator()

medicament_service = MedicamentService(medicament_repository, medicament_validator)
client_card_service = ClientCardService(client_card_repository, client_card_validator)
transaction_service = TransactionService(transaction_repository, medicament_repository, client_card_repository)

console = Console(medicament_service, client_card_service, transaction_service)

# medicament_service.add_medicament(1, "Nurofen", "Paduden", 13, "no", 0)
# medicament_service.add_medicament(2, "Aspirin", "Bayer", 10, "no", 0)
# medicament_service.add_medicament(3, "Vicodin", "Abbott", 65, "yes", 0)

date1 = datetime.date(2001, 10, 10)
date2 = datetime.date(1999, 3, 9)
date3 = datetime.date(2000, 1, 10)
date4 = datetime.date(2019, 11, 11)
date5 = datetime.date(2019, 10, 12)
date6 = datetime.date(2019, 12, 21)
date7 = datetime.date(2018, 10, 10)


# client_card_service.add_client_card(1, "Mr", "Poopyhead", 500001, date1, date4, 0)
# client_card_service.add_client_card(2, "Johnson", "John", 500002, date2, date5, 0)
# client_card_service.add_client_card(3, "Smith", "Morty", 500003, date3, date6, 0)
#
# transaction_service.add_transaction(1, 1, 1, 10, date7, "12:34")

console.run_console()

# todo:
# ce se intampla daca se da update la o tranzactie? se modifica numarul de vanzari si discount urile primite?
# weird repository error format
# client_card_update si cerinta 7
