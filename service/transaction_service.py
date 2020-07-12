from domain.transaction import Transaction
from domain.medicament import Medicament
from domain.client_card import ClientCard
from service.service_errors import TransactionError


class TransactionService:

    def __init__(self, transaction_repository, medicament_repository, client_card_repository):
        self.__transaction_repository = transaction_repository
        self.__medicament_repository = medicament_repository
        self.__client_card_repository = client_card_repository

    def add_transaction(self, id_transaction, id_medicament, id_client_card, number_of_meds, date_of_transaction):
        """
        Adds a new transaction.
        :param id_transaction: int, the id of the transaction
        :param id_medicament: int, the id of the medicament
        :param id_client_card: string for now, to be int, the id of the client card
        :param number_of_meds: int, the number of purchased meds
        :param date_of_transaction: date, the date of the transaction
        :param hour_of_transaction: date, the hour of the transaction
        """
        if id_client_card == "":
            id_client_card = None
        else:
            id_client_card = int(id_client_card)

        if self.__medicament_repository.read(id_medicament) is None:
            raise TransactionError("There is no medicament with the ID {}".format(id_medicament))

        if self.__client_card_repository.read(id_client_card) is None and id_client_card is not None:
            raise TransactionError("There is no client card with the ID {}".format(id_client_card))

        effective_price = number_of_meds * self.__medicament_repository.read(id_medicament).price

        if self.__client_card_repository.read(id_client_card) is not None:
            if self.__medicament_repository.read(id_medicament).requires_prescription is True:
                total_paid = 0.85 * effective_price
            else:
                total_paid = 0.9 * effective_price

        if id_client_card is None:
            total_paid = effective_price
        disc = effective_price - total_paid

        transaction = Transaction(id_transaction, id_medicament, id_client_card, number_of_meds, date_of_transaction, total_paid, disc)

        medicament = self.__medicament_repository.read(id_medicament)
        new_medicament = Medicament(id_medicament, medicament.name, medicament.manufacturer, medicament.price,
                                    medicament.requires_prescription)
        self.__medicament_repository.update(new_medicament)
        # de ce pisici e asta aici?

        client_card = self.__client_card_repository.read(id_client_card)
        # print(client_card)
        if client_card in self.__client_card_repository.read():
            new_client_card = ClientCard(id_client_card, client_card.surname, client_card.first_name, client_card.CNP,
                                         client_card.birth_date, client_card.register_date)
            self.__client_card_repository.update(new_client_card)

        client_card = self.__client_card_repository.read(id_client_card)
        new_client_card = ClientCard
        # again, de ce pisici e asta aici?

        self.__transaction_repository.create(transaction)

    def update_transaction(self, id_transaction, id_medicament, id_client_card, number_of_meds, date_of_transaction):
        """
        Updates a transaction.
        :param id_transaction: int, the id of the transaction
        :param id_medicament: int, the id of the medicament
        :param id_client_card: int, the id of the client card
        :param number_of_meds: int, the number of purchased meds
        :param date_of_transaction: date, the date of the transaction
        """
        if self.__medicament_repository.read(id_medicament) is None:
            raise TransactionError("There is no medicament with the ID {}".format(id_medicament))
        if self.__client_card_repository.read(id_client_card) is None:
            raise TransactionError("There is no client card with the ID {}".format(id_client_card))

        effective_price = number_of_meds * self.__medicament_repository.read(id_medicament).price
        if self.__client_card_repository.read(id_client_card) is not None:
            if self.__medicament_repository.read(id_medicament).requires_prescription is True:
                total_paid = 0.85 * effective_price
            else:
                total_paid = 0.9 * effective_price
        else:
            total = effective_price
        disc = effective_price - total_paid
        old_total_paid = self.__transaction_repository.read(id_transaction).total_paid
        old_disc = self.__transaction_repository.read(id_transaction).disc
        transaction = Transaction(id_transaction, id_medicament, id_client_card,
                                  number_of_meds, date_of_transaction, old_total_paid, old_disc)
        self.__transaction_repository.update(transaction)

    def delete_transaction(self, id_transaction):
        """
        Deletes a client card.
        :param id_transaction: the id of the transaction to be deleted.
        :return: -
        """
        self.__transaction_repository.delete(id_transaction)

    def get_all(self):
        """
        :return: a list of all meds.
        """
        return self.__transaction_repository.read()

    def transaction_between_dates(self, first_date, second_date):
        result = filter(lambda c:(first_date < c.date_of_transaction < second_date)
                                 or (first_date > c.date_of_transaction > second_date),
                        self.__transaction_repository.read())
        return result

    def transaction_delete_between_dates(self, first_date, second_date):
        for transaction in self.__transaction_repository.read():
            if first_date < transaction.date_of_transaction < second_date or first_date > transaction.date_of_transaction > second_date:
                self.delete_transaction(transaction.id_entity)

    def medicament_sorted_by_sales(self):
        data = {}
        # for med in self.__medicament_repository.read():
        #     if med not in data:
        #         data[med] = 0
        #     else:
        #         data[med] += 1
        # sorted_data = sorted(data, key=lambda c:data[c].value, reverse=True)
        # return sorted_data
        for transaction in self.__transaction_repository.read():
            med_id = transaction.id_medicament
            if med_id in data:
                data[med_id] += 1
            else:
                data[med_id] = 1
            sorted_data = sorted(data, key=lambda c:data[c], reverse=True)
        return sorted_data

    def client_card_sorted_by_discounts(self):
        data = {}
        for transaction in self.__transaction_repository.read():
            card_id = transaction.id_client_card
            if card_id in data:
                data[card_id] += transaction.disc
            else:
                data[card_id] = transaction.disc
        return data

    def cascade_delete_medicament(self, id_med):
        for entity in self.__transaction_repository.read():
            if entity.id_medicament == id_med:
                self.delete_transaction(entity.id_entity)

    def cascade_delete_client_card(self, id_cc):
        for entity in self.__transaction_repository.read():
            if entity.id_client_card == id_cc:
                self.delete_transaction(entity.id_entity)

