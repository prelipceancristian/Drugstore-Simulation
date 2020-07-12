# from domain.client_card import ClientCard


class ClientCardInMemoryRepository:

    def __init__(self):
        """
        Creates an in memory repository for the client cards.
        """
        self.__storage = {}

    def create(self, client_card):
        """
        Adds a new client card
        :param client_card: the client card to add.
        :return: -
        """
        client_card_id = client_card.id_client_card
        CNP = client_card.CNP
        if client_card_id in self.__storage:
            raise KeyError("There already is a client card with the id {}".format(client_card_id))
        for obj in self.__storage:
            if obj.CNP == CNP:
                raise KeyError("There already is a client card with the CNP {}".format(CNP))
        self.__storage[client_card_id] = client_card

    def read(self, client_card_id=None):
        """
        Returns the client card with the given id, or every client card.
        :param client_card_id: the card id.
        :return: a card or every card.
        """
        if client_card_id is None:
            return self.__storage.values()
        else:
            return self.__storage[client_card_id]

    def update(self, client_card):
        """
        Updates a client card
        :param client_card: the new client card
        :return: -
        """
        client_card_id = client_card.id_client_card
        CNP = client_card.CNP
        if client_card_id not in self.__storage:
            raise KeyError("There is no client card with the id {}".format(client_card_id))
        for obj in self.__storage.values():
            if obj.CNP == CNP:
                raise KeyError("There already is a client card with the CNP {}".format(CNP))
        self.__storage[client_card_id] = client_card

    def delete(self, client_card_id):
        """
        Deletes a client card with the given id.
        :param client_card_id:
        :return: -
        """
        if client_card_id not in self.__storage:
            raise KeyError("There is no client card with the id {}".format(client_card_id))
        del self.__storage[client_card_id]
