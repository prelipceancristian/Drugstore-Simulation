class TransactionInMemoryRepository:

    def __init__(self):
        self.__storage = {}

    def create(self, transaction):
        """
        Adds a transaction object.
        """
        transaction_id = transaction.id_transaction
        if transaction_id in self.__storage:
            raise KeyError("There already is a transaction with the ID {}".format(transaction_id))
        self.__storage[transaction_id] = transaction

    def read(self, id_transaction=None):
        """
        Gets a transaction or every transaction
        :param id_transaction: the id of the transaction
        :return: returns the transaction with that id if id_transaction is None, a list of all transactions otherwise.
        """
        if id_transaction is None:
            return self.__storage.values()
        else:
            if id_transaction not in self.__storage:
                raise KeyError("There is no transaction with the ID {}".format(id_transaction))
            return self.__storage[id_transaction]

    def update(self, transaction):
        """
        Updates a transaction
        :param transaction: the new transaction
        :return: -
        """
        transaction_id = transaction.id_transaction
        if transaction_id not in self.__storage:
            raise KeyError("There is no transaction with the ID {}".format(transaction_id))
        self.__storage[transaction_id] = transaction

    def delete(self, id_transaction):
        """
        Deletes the transaction with the given id.
        :param id_transaction: the given id.
        :return: -
        """
        if id_transaction not in self.__storage:
            raise KeyError("There is no transaction with the ID {}".format(id_transaction))
        del self.__storage[id_transaction]
