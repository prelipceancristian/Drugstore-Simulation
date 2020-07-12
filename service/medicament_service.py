from domain.medicament import Medicament
from service.service_errors import MedicamentError
# from domain.medicament_validator import MedicamentValidator
# from repository.medicament_repository import MedicamentInMemoryRepository
import random
import string


def randomString(stringLength=10):
    """Generate a random string of fixed length """
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for _ in range(stringLength))


class MedicamentService:

    """
    Manages medicament service.
    """
    def __init__(self, repository, validator):
        """
        Creates a medicament service.
        :param repository: the medicament repository.
        :param validator: the medicament validator.
        """
        self.__repository = repository
        self.__validator = validator

    def add_medicament(self, id_medicament, name, manufacturer, price, requires_prescription):
        """
        Creates a medicament.
        :param id_medicament:int, the id of the medicament.
        :param name:char, the name of the medicament.
        :param manufacturer:char, the name of the manufacturer.
        :param price:float, the price of the medicament, must be positive.
        :param requires_prescription:bool, True if the medicament requires a prescription, False otherwise.
        :return:
        """
        medicament = Medicament(id_medicament, name, manufacturer, price, requires_prescription)
        self.__validator.validate(medicament)
        if requires_prescription == "yes":
            requires_prescription = True
        else:
            requires_prescription = False
        medicament = Medicament(id_medicament, name, manufacturer, price, requires_prescription)
        self.__repository.create(medicament)

    def update_medicament(self, id_medicament, name, manufacturer, price, requires_prescription):
        """
        Updates a medicament.
        :param id_medicament:int, the id of the medicament.
        :param name:char, the name of the medicament.
        :param manufacturer:char, the name of the manufacturer.
        :param price:float, the price of the medicament, must be positive.
        :param requires_prescription:bool, True if the medicament requires a prescription, False otherwise.
        :return:
        """
        medicament = Medicament(id_medicament, name, manufacturer, price, requires_prescription)
        self.__validator.validate(medicament)
        if requires_prescription == "yes":
            requires_prescription = True
        else:
            requires_prescription = False
        medicament = Medicament(id_medicament, name, manufacturer, price, requires_prescription)
        self.__repository.update(medicament)

    def delete_medicament(self, id_medicament):
        """
        Deletes a medicament.
        :param id_medicament: the id of the medicament to be deleted.
        :return: -
        """
        self.__repository.delete(id_medicament)

    def populate_meds(self, n):
        """
        Adds random meds to the repository.
        :param n: the number of meds
        :return: -
        """
        counter = 0
        while counter < n:
            id_medicament = random.randrange(1000)
            name = randomString()
            manufacturer = randomString()
            price = round(random.uniform(0, 40), 2)
            requires_prescription = random.choice(["yes", "no"])
            if self.__repository.read(id_medicament) is None:
                self.add_medicament(id_medicament, name, manufacturer, price, requires_prescription)
                counter = counter + 1

    def get_all(self, med_id=None):
        """
        :return: a list of all meds.
        """
        return self.__repository.read(med_id)

    def medicament_search(self, op, criteria):
        """
        Determines all the meds that respect the criteria
        :param op: the option
        :param criteria: the criteria
        :return: the list with all the valid values
        """
        if op == "1":
            result = filter(lambda c : c.name == criteria, self.__repository.read())
        elif op == "2":
            result = filter(lambda c : c.manufacturer == criteria, self.__repository.read())
        elif op == "3":
            result = filter(lambda c : c.price == float(criteria), self.__repository.read())
        elif op == "4":
            if criteria == "yes":
                criteria = True
            elif criteria == "no":
                criteria = False
            else:
                raise MedicamentError("Criteria should have been either yes or no!")
            result = filter(lambda c: c.requires_prescription == criteria, self.__repository.read())
        else:
            raise MedicamentError("The given option is invalid!")
        return result

    # def medicament_sorted_by_sales(self):
    #     result = sorted(self.__repository.read(), key=lambda c:c.sales, reverse= True)
    #     return result

    def medicament_increase_price(self, percentage, bound_value):
        result = map(lambda c: Medicament(c.id_entity, c.name, c.manufacturer, (1 + percentage) * c.price, c.requires_prescription) if c.price < bound_value else c, self.get_all())
        for ent in result:
            self.__repository.update(ent)
        # result = filter(lambda d: d.price < bound_value, self.get_all())
        # for ent in result:
        #     print(ent)
        # for med in self.__repository.read():
        #     if med.price <= bound_value:
        #         if med.requires_prescription is True:
        #             pre = "yes"
        #         else:
        #             pre = "no"
        #         new_price = (1 + percentage) * med.price
        #         self.update_medicament(med.id_entity, med.name, med.manufacturer,
        #                                new_price, pre)


    def permutari(self):
        """
        Calculates every permutation of the meds in the repository
        :return: a list with every permutation
        """
        n = len(self.get_all())
        results = []

        def inner(permutare_curenta):
            if len(permutare_curenta) == n:
                results.append(permutare_curenta)
                return

            for ent in self.get_all():
                if ent not in permutare_curenta:
                    inner(permutare_curenta + [ent])

        inner([])
        return results

    def binary_search(self, needle, haystack):
        """
        searches for needle in haystack
        """

        st = 0
        dr = len(haystack) - 1

        while st <= dr:
            m = (st + dr) // 2  # st + (dr - st) // 2
            # TODO: get rid of the first if
            # hint: modificat un pic conditia din while
            if haystack[m] == needle:
                return True
            if haystack[m] < needle:
                st = m + 1
            else:
                dr = m - 1
        return False

    def update_medicament_binary_search(self, id_medicament, name, manufacturer, price, requires_prescription):
        """
        Updates a medicament.
        :param id_medicament:int, the id of the medicament.
        :param name:char, the name of the medicament.
        :param manufacturer:char, the name of the manufacturer.
        :param price:float, the price of the medicament, must be positive.
        :param requires_prescription:bool, True if the medicament requires a prescription, False otherwise.
        :return:
        """
        medicament = Medicament(id_medicament, name, manufacturer, price, requires_prescription)
        self.__validator.validate(medicament)
        if requires_prescription == "yes":
            requires_prescription = True
        else:
            requires_prescription = False
        medicament = Medicament(id_medicament, name, manufacturer, price, requires_prescription)
        self.__repository.update_binary_search(medicament)




