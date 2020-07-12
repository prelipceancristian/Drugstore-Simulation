import datetime

from domain.client_card import ClientCard
from service.service_errors import ClientCardError
# import datetime


class ClientCardService:

    def __init__(self, repository, validator):
        self.__repository = repository
        self.__validator = validator

    def add_client_card(self, id_client_card, surname, first_name, CNP, birth_date, register_date):
        """
        Creates a client card.
        :param id_client_card: int, the client card id.
        :param surname: str, the surname of the client.
        :param first_name: str, the first name of the client.
        :param CNP: int, the CNP of the client.
        :param birth_date: date, the birth date of the client.
        :param register_date: date, the registration dat for the client card.
        :return:
        """
        """
        d1 = 0
        d2 = 0
        if type(birth_date) is not datetime.date:
            print(type(birth_date))
            args_birth = birth_date.split(".")
            d1 = datetime.date(int(args_birth[2]), int(args_birth[1]), int(args_birth[0]))
        else:
            d1 = birth_date
        if type(register_date) is not datetime.date:
            args_reg = register_date.split(".")
            d2 = datetime.date(int(args_reg[2]), int(args_reg[1]), int(args_reg[0]))
        else:
            d2 = register_date

        client_card = ClientCard(id_client_card, surname, first_name, CNP, d1, d2)

        """
        for ent in self.__repository.read():
            if ent.CNP == CNP:
                raise ClientCardError("There alreay is a user with that CNP!")
        client_card = ClientCard(id_client_card, surname, first_name, CNP, birth_date, register_date)
        self.__validator.validate(client_card)
        self.__repository.create(client_card)

    def update_client_card(self, id_client_card, surname, first_name, CNP, birth_date, register_date):
        """
        Updates a client card.
        :param id_client_card: int, the client card id.
        :param surname: str, the surname of the client.
        :param first_name: str, the first name of the client.
        :param CNP: int, the CNP of the client.
        :param birth_date: date, the birth date of the client.
        :param register_date: date, the registration dat for the client card.
        :return:
        """
        for ent in self.__repository.read():
            if ent.CNP == CNP:
                raise ClientCardError("There alreay is a user with that CNP!")
        client_card = ClientCard(id_client_card, surname, first_name, CNP, birth_date, register_date)
        self.__repository.update(client_card)

    def delete_client_card(self, id_client_card):
        """
        Deletes a client card.
        :param id_client_card: the id of the card to be deleted.
        :return: -
        """
        self.__repository.delete(id_client_card)

    def get_all(self, client_card_id=None):
        return self.__repository.read(client_card_id)

    def client_card_search(self, op, criteria):
        """
        Determines all the meds that respect the criteria
        :param op: the option
        :param criteria: the criteria
        :return: the list with all the valid values
        """
        if op == "1":
            result = filter(lambda c : c.surname == criteria, self.__repository.read())
        elif op == "2":
            result = filter(lambda c : c.first_name == criteria, self.__repository.read())
        elif op == "3":
            result = filter(lambda c : c.CNP == int(criteria), self.__repository.read())
        elif op == "4":
            args = criteria.split(".")
            if len(args) != 3:
                raise ClientCardError("The criteria did not respect the date format!")
            search_date = datetime.date(int(args[2]), int(args[1]), int(args[0]))
            result = filter(lambda c : c.birth_date == search_date, self.__repository.read())
        elif op == "5":
            args = criteria.split(".")
            if len(args) != 3:
                raise ClientCardError("The criteria did not respect the date format!")
            search_date = datetime.date(int(args[2]), int(args[1]), int(args[0]))
            result = filter(lambda c: c.register_date == search_date, self.__repository.read())
        else:
            raise ClientCardError("The given option is invalid!")
        return result

    def client_card_sorted_by_discounts(self):
        result = sorted(self.__repository.read(), key=lambda c: c.discounts, reverse=True)
        print(1)
        print(result)
        print(result)

        return result
