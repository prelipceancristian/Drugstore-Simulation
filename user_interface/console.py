from domain.medicament_validator import MedicamentValidatorError
from repository.repository_error import RepositoryError
import datetime

from service.service_errors import MedicamentError, ClientCardError, TransactionError


class Console:

    def __init__(self, medicament_service, client_card_service, transaction_service):
        """
        Initialises the services for the console
        :param medicament_service: the medicament service
        :param client_card_service: the client card service
        :param transaction_service: the transaction service
        """
        self.__medicament_service = medicament_service
        self.__client_card_service = client_card_service
        self.__transaction_service = transaction_service

    def __show_menu_meds(self):
        """
        Prints the menu for the medicament submenu
        :return: -
        """
        print("---- Meds menu ----")
        print("1. Add medicament")
        print("2. Update medicament")
        print("3. Delete medicament")
        print("4. Search medicament database")
        print("5. Show meds in the descending order based on the no. of sales")
        print("6. Populate")
        print("7. Increase meds price")
        print("8. Permutari")
        print("a. Show meds")
        print("b. Back")

    def __show_menu_client_cards(self):
        """
        Prints the menu for the client card submenu
        :return: -
        """
        print("---- Client cards menu ----")
        print("1. Add client card")
        print("2. Update client card")
        print("3. Delete client card")
        print("4. Search client card database")
        print("5. Show client cards in the ascending order based on the no. of sales received")
        print("a. Show client cards")
        print("b. Back")

    def __show_menu_transactions(self):
        """
        Prints the menu for the transaction submenu
        :return: -
        """
        print("---- Transactions menu ----")
        print("1. Add transaction")
        print("2. Update transaction")
        print("3. Delete transaction")
        print("4. Show all transactions in an interval of days")
        print("5. Delete all transactions in an interval of days")
        print("a. Show transactions")
        print("b. Back")

    def __show_menu_client_card_search(self):
        """
        Prints the menu for the client card search submenu
        :return: -
        """
        print("---- Client card search menu-----")
        print("1.Surname")
        print("2.First name")
        print("3.CNP")
        print("4.Birthday(dd.mm.yyyy)")
        print("5.Registration day(dd.mm.yyyy)")

    def __show_menu(self):
        """
        Shows the main menu.
        :return: -
        """
        print("---- Main menu ----")
        print("1.Meds")
        print("2.Client cards")
        print("3.Transactions")
        print("x.Exit")

    def __show_menu_medicament_search(self):
        print("---- Medicament search menu ----")
        print("1.Name")
        print("2.Manufacturer")
        print("3.Price")
        print("4.Prescription requirement")

    def run_console(self):
        """
        Coordinates the user input in the main menu
        :return:
        """
        while True:
            self.__show_menu()
            op = input("Option: ")
            if op == "1":
                self.__show_meds()
            elif op == "2":
                self.__show_client_cards()
            elif op == "3":
                self.__show_transactions()
            elif op == "x":
                break
            else:
                print("Invalid character!")
        print("Thanks for trying out my database! :)")

    def __show_client_cards(self):
        """
        Coordinates the user input in client card menu
        :return:
        """
        while True:
            self.__show_menu_client_cards()
            op = input("Option: ")
            if op == "1":
                self.__handle_client_card_add()
            elif op == "2":
                self.__handle_client_card_update()
            elif op == "3":
                self.__handle_client_card_delete()
            elif op == "4":
                self.__handle_client_card_search()
            elif op == "5":
                self.__handle_client_card_sorted_by_discounts()
            elif op == "a":
                self.__show_list(self.__client_card_service.get_all())
            elif op == "b":
                break
            else:
                print("Inavlid character!")

    def __show_meds(self):
        """
        Coordonates the user input in the medicament menu
        :return:
        """
        while True:
            self.__show_menu_meds()
            op = input("Option: ")
            if op == "1":
                self.__handle_medicament_add()
            elif op == "2":
                self.__handle_medicament_update()
            elif op == "3":
                self.__handle_medicament_delete()
            elif op == "4":
                self.__handle_medicament_search()
            elif op == "5":
                self.__handle_medicament_sorted_by_sales()
            elif op == "6":
                self.__handle_medicament_populate()
            elif op == "7":
                self.__handle_medicament_increase_price()
            elif op == "8":
                self.__handle_medicament_permutari()
            elif op == "a":
                self.__show_list(self.__medicament_service.get_all())
            elif op == "b":
                break
            else:
                print("Invalid character!")

    def __show_transactions(self):
        """
        Coordonates the user input in the transaction menu
        :return:
        """
        while True:
            self.__show_menu_transactions()
            op = input("Option: ")
            if op == "1":
                self.__handle_transaction_add()
            elif op == "2":
                self.__handle_transaction_update()
            elif op == "3":
                self.__handle_transaction_delete()
            elif op == "4":
                self.__handle_transaction_between_dates()
            elif op == "5":
                self.__handle_transaction_delete_between_dates()
            elif op == "a":
                self.__show_list(self.__transaction_service.get_all())
            elif op == "b":
                break
            else:
                print("Invalid character!")

    def __handle_medicament_add(self):
        """
        Handles the medicament addition.
        :return: -
        """
        try:
            id_medicament = int(input("Medicament ID: "))
            name = input("Name: ")
            manufacturer = input("Manufacturer: ")
            price = float(input("Price: "))
            requires_prescription = input("Requires prescription(yes/no): ")
            self.__medicament_service.add_medicament(id_medicament, name, manufacturer, price, requires_prescription)
            print("The medicament was added!")
        except MedicamentValidatorError as mve:
            print("Errors:")
            for error in mve.args[0]:
                print(error)
        except MedicamentError as me:
            print("Error: ", me)
        except RepositoryError as re:
            print("Error:", re)
        except ValueError as ve:
            print("Error:", ve)

    def __handle_medicament_update(self):
        """
        Handles the medicament update.
        :return: -
        """
        try:
            id_medicament = int(input("Medicament ID: "))
            name = input("Name: ")
            manufacturer = input("Manufacturer: ")
            price = float(input("Price: "))
            requires_prescription = input("Requires prescription(yes/no): ")
            self.__medicament_service.update_medicament_binary_search(id_medicament, name, manufacturer, price, requires_prescription)
            print("The medicament with the ID {} was updated!".format(id_medicament))
        except MedicamentValidatorError as mve:
            print("Errors:")
            for error in mve.args[0]:
                print(error)
        except MedicamentError as me:
            print("Error: ", me)
        except RepositoryError as ke:
            print("Error: ", ke)
        except ValueError as ve:
            print("Error: ", ve)

    def __handle_medicament_delete(self):
        """
        Handles the medicament deletion.
        :return: -
        """
        try:
            id_medicament = int(input("Medicament ID: "))
            self.__medicament_service.delete_medicament(id_medicament)
            self.__transaction_service.cascade_delete_medicament(id_medicament)
            print("The medicament with the id {} wad successfully deleted!".format(id_medicament))
        except RepositoryError as re:
            print("Error:", re)
        except ValueError as ve:
            print("Error:", ve)

    def __handle_client_card_add(self):
        """
        Handles the client card addition.
        :return: -
        """
        try:
            id_client_card = int(input("Client card ID: "))
            surname = input("Surname: ")
            first_name = input("First name: ")
            CNP = int(input("CNP: "))

            print("Birthday details:")
            day_birth = int(input("Day(1-31): "))
            month_birth = int(input("Month(1-12): "))
            year_birth = int(input("Year: "))
            birth_date = datetime.date(year_birth, month_birth, day_birth)

            print("Registration date details:")
            day_register = int(input("Day(1-31): "))
            month_register = int(input("Month(1-12): "))
            year_register = int(input("Year: "))
            register_date = datetime.date(year_register, month_register, day_register)

            self.__client_card_service.add_client_card(id_client_card, surname, first_name, CNP, birth_date,
                                                       register_date)
            print("Client card added successfully!")
        except RepositoryError as ke:
            print("Error:", ke)
        except ValueError as ve:
            print("Error:", ve)
        except ClientCardError as cle:
            print("Error", cle)

    def __handle_client_card_delete(self):
        """
        Handles the client card deletion.
        :return: -
        """
        try:
            id_client_card = int(input("Client card ID: "))
            self.__client_card_service.delete_client_card(id_client_card)
            self.__transaction_service.cascade_delete_client_card(id_client_card)
            print("Client card successfully deleted!")
        except KeyError as ke:
            print("Errors", ke)
        except ValueError as ve:
            print("Error:", ve)
        except RepositoryError as re:
            print("Error:", re)


    def __handle_client_card_update(self):
        """
        Handles the client card update.
        :return: -
        """
        try:
            id_client_card = int(input("Client card ID: "))
            surname = input("Surname: ")
            first_name = input("First name: ")
            CNP = int(input("CNP: "))

            print("Birthday details:")
            day_birth = int(input("Day(1-31): "))
            month_birth = int(input("Month(1-12): "))
            year_birth = int(input("Year: "))
            birth_date = datetime.date(year_birth, month_birth, day_birth)

            print("Registration date details:")
            day_register = int(input("Day(1-31): "))
            month_register = int(input("Month(1-12): "))
            year_register = int(input("Year: "))
            register_date = datetime.date(year_register, month_register, day_register)

            self.__client_card_service.update_client_card(id_client_card, surname, first_name, CNP, birth_date,
                                                          register_date)
            print("Client card updated successfully!")
        except KeyError as ke:
            print("Error:", ke)
        except ValueError as ve:
            print("Error:", ve)
        except RepositoryError as re:
            print("Error:", re)
        except ClientCardError as cle:
            print("Error", cle)

    def __show_list(self, objects):
        """
        Prints all objects in an iterable entity.
        :param objects: the iterable entity
        :return: -
        """
        for obj in objects:
            print(obj)

    def __handle_transaction_add(self):
        """
        Handles the transaction addition.
        :return: -
        """
        try:
            id_transaction = int(input("Transaction ID: "))
            id_medicament = int(input("Medicament ID: "))
            id_client_card = input("Client card ID: ")
            number_of_meds = int(input("Number of meds: "))

            print("Transaction time details:")
            day_transaction = int(input("Day(1-31): "))
            month_transaction = int(input("Month(1-12): "))
            year_transaction = int(input("Year: "))
            hour_transaction = int(input("Hour(0-23): "))
            minutes_transaction = int(input("Minute(0-59): "))
            date_of_transaction = datetime.datetime(year_transaction, month_transaction, day_transaction,
                                                    hour_transaction, minutes_transaction)
            self.__transaction_service.add_transaction(id_transaction, id_medicament, id_client_card,
                                                       number_of_meds, date_of_transaction)
            print("Transaction added successfully!")
        except KeyError as ke:
            print("Error:", ke)
        except ValueError as ve:
            print("Error:", ve)
        except RepositoryError as re:
            print("Error:", re)
        except TransactionError as te:
            print("Error:", te)

    def __handle_transaction_update(self):
        """
        Handles the transaction update.
        :return: -
        """
        try:
            id_transaction = int(input("Transaction ID: "))
            id_medicament = int(input("Medicament ID: "))
            id_client_card = int(input("Client card ID: "))
            number_of_meds = int(input("Number of meds: "))
            print("Transaction time details:")
            day_transaction = int(input("Day(1-31): "))
            month_transaction = int(input("Month(1-12): "))
            year_transaction = int(input("Year: "))
            hour_transaction = int(input("Hour(0-23): "))
            minutes_transaction = int(input("Minute(0-59): "))
            date_of_transaction = datetime.datetime(year_transaction, month_transaction, day_transaction,
                                                    hour_transaction, minutes_transaction)
            self.__transaction_service.update_transaction(id_transaction, id_medicament, id_client_card,
                                                          number_of_meds,
                                                          date_of_transaction)
            print("Transaction updated successfully!")
        except KeyError as ke:
            print("Error:", ke)
        except ValueError as ve:
            print("Error:", ve)
        except RepositoryError as re:
            print("Error:", re)
        except TransactionError as te:
            print("Error:", te)

    def __handle_transaction_delete(self):
        """
        Deletes a transaction from a given ID.
        :return:
        """
        try:
            transaction_id = int(input("Transaction ID: "))
            self.__transaction_service.delete_transaction(transaction_id)
            print("Transcation deleted successfully!")
        except RepositoryError as re:
            print("Error", re)
        except ValueError as ve:
            print("Error", ve)


    def __handle_client_card_search(self):
        try:
            self.__show_menu_client_card_search()
            op = input("Option: ")
            criteria = input("Criteria: ")
            result = self.__client_card_service.client_card_search(op, criteria)
            ok = 0
            for ent in result:
                print(ent)
                ok = 1
            if ok == 0:
                print("No client cards with the given criteria were found!")
        except ValueError as ve:
            print("Error", ve)
        except ClientCardError as cle:
            print("Error:", cle)

    def __handle_medicament_populate(self):
        """
        Populates the repository with randomly generated meds.
        :return: -
        """
        try:
            n = int(input("How many entities do you want to randomly generate?: "))
            self.__medicament_service.populate_meds(n)
            print("{} medicament entities were added!".format(n))
        except KeyError as ke:
            print("Error", ke)
        except ValueError as ve:
            print("Error", ve)

    def __handle_medicament_search(self):
        try:
            self.__show_menu_medicament_search()
            op = input("Option: ")
            criteria = input("Criteria: ")
            result = self.__medicament_service.medicament_search(op, criteria)
            ok = 0
            for ent in result:
                print(ent)
                ok = 1
            if ok == 0:
                print("No meds with the given criteria were found!")
        except ValueError as ve:
            print("Error", ve)
        except MedicamentError as me:
            print("Error", me)

    def __handle_medicament_sorted_by_sales(self):

        result = self.__transaction_service.medicament_sorted_by_sales()
        sorted_result = sorted(result.items(), key=lambda c: (c[1], c[0]), reverse=True)
        for ent in sorted_result:
            print(self.__medicament_service.get_all(ent[0]), "sold {} times.".format(ent[1]))

    def __handle_client_card_sorted_by_discounts(self):
        result = self.__transaction_service.client_card_sorted_by_discounts()
        sorted_result = sorted(result.items(), key=lambda c: (c[1], c[0]), reverse=True)
        for ent in sorted_result:
            if ent[1] != 0:
                print(self.__client_card_service.get_all(ent[0]), "saved {} in discounts.".format(ent[1]))

    def __handle_medicament_increase_price(self):
        percentage = float(input("By how much would you like to increase the prices?(number in interval [0,1]): "))
        bound_value = float(input("What is the bottom value for the increment?: "))
        self.__medicament_service.medicament_increase_price(percentage, bound_value)
        print("The prices lower than {} were increased by {}% successfully!".format(bound_value, percentage * 100))

    def __handle_transaction_between_dates(self):
        try:
            print("Day 1 details:")
            day1 = int(input("Day(1-31): "))
            month1 = int(input("Month(1-12): "))
            year1 = int(input("Year: "))
            first_date = datetime.datetime(year1, month1, day1)

            print("Day 2 details:")
            day2 = int(input("Day(1-31): "))
            month2 = int(input("Month(1-12): "))
            year2 = int(input("Year: "))
            second_date = datetime.datetime(year2, month2, day2)

            result = self.__transaction_service.transaction_between_dates(first_date, second_date)
            ok = 0
            for tran in result:
                print(tran)
                ok = 1
            if ok == 0:
                print("No transactions between these dates were found!")
        except ValueError as ve:
            print("Error:", ve)

    def __handle_transaction_delete_between_dates(self):
        try:
            print("Day 1 details:")
            day1 = int(input("Day(1-31): "))
            month1 = int(input("Month(1-12): "))
            year1 = int(input("Year: "))
            first_date = datetime.datetime(year1, month1, day1)

            print("Day 2 details:")
            day2 = int(input("Day(1-31): "))
            month2 = int(input("Month(1-12): "))
            year2 = int(input("Year: "))
            second_date = datetime.datetime(year2, month2, day2)

            self.__transaction_service.transaction_delete_between_dates(first_date, second_date)
            print("Transactions between {} and {} were deleted!".format(first_date, second_date))
        except ValueError as ve:
            print("Error:", ve)

    def __handle_medicament_permutari(self):
        result = self.__medicament_service.permutari()
        for perm in result:
            for ent in perm:
                print(ent.id_entity, end=" ")
            print("")
