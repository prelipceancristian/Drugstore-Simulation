from domain.entity import Entity


class ClientCard(Entity):
    """
    Client card object.
    """

    def __init__(self, id_client_card, surname, first_name, CNP, birth_date, register_date):
        """
        Creates a new client card.
        :param id_client_card: int, the client card id.
        :param surname: str, the surname of the client.
        :param first_name: str, the first name of the client.
        :param CNP: int, the CNP of the client.
        :param birth_date: date, the birth date of the client.
        :param register_date: date, the registration dat for the client card.
        """
        super().__init__(id_client_card)
        self.__surname = surname
        self.__first_name = first_name
        self.__CNP = CNP
        self.__birth_date = birth_date
        self.__register_date = register_date

    # @property
    # def id_client_card(self):
    #     return self.__id_client_card

    @property
    def surname(self):
        return self.__surname

    @property
    def first_name(self):
        return self.__first_name

    @property
    def birth_date(self):
        return self.__birth_date

    @property
    def register_date(self):
        return self.__register_date

    @property
    def CNP(self):
        return self.__CNP


    def __eq__(self, other):
        if type(self) != type(other):
            return False
        return self.id_entity == other.id_entity and self.CNP == other.CNP

    def __str__(self):
        return "{}. {} {} (CNP = {}) born in {}, registered in {}".format(self.id_entity,
                                                                                                 self.surname,
                                                                                                 self.first_name,
                                                                                                 self.CNP,
                                                                                                 self.birth_date,
                                                                                                 self.register_date)
