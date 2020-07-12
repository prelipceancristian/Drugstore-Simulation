from domain.entity import Entity


class Transaction(Entity):

    def __init__(self, id_transaction, id_medicament, id_client_card, number_of_meds, date_of_transaction, total_paid,
                 disc):
        """
        Creates an transaction object.
        :param id_transaction: int, the id of the transaction
        :param id_medicament: int, the id of the medicament
        :param id_client_card: int, the id of the client card
        :param number_of_meds: int, the number of purchased meds
        """
        super().__init__(id_transaction)
        self.__id_medicament = id_medicament
        self.__id_client_card = id_client_card
        self.__number_of_meds = number_of_meds
        self.__date_of_transaction = date_of_transaction
        self.__total_paid = total_paid
        self.__disc = disc

    # @property
    # def id_transaction(self):
    #     return self.__id_transaction

    @property
    def id_medicament(self):
        return self.__id_medicament

    @property
    def id_client_card(self):
        return self.__id_client_card

    @property
    def number_of_meds(self):
        return self.__number_of_meds

    @property
    def date_of_transaction(self):
        return self.__date_of_transaction

    @property
    def total_paid(self):
        return self.__total_paid

    @property
    def disc(self):
        return self.__disc

    def __eq__(self, other):
        if type(self) != type(other):
            return False
        return self.id_entity == other.id_entity

    def __str__(self):
        return "{}. Med ID: {}, Card ID: {}, quantity:{}, " \
               "date:{}. Paid: {}, discount: {}".format(self.id_entity,
                                                        self.id_medicament,
                                                        self.id_client_card,
                                                        self.number_of_meds,
                                                        self.date_of_transaction,
                                                        self.total_paid,
                                                        self.disc)
