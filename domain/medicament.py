from domain.entity import Entity


class Medicament(Entity):
    """
    Medicament object.
    """
    def __init__(self, id_medicament, name, manufacturer, price, requires_prescription):
        """
        Creates a medicament.
        :param id_medicament:int, the id of the medicament.
        :param name:char, the name of the medicament.
        :param manufacturer:char, the name of the manufacturer.
        :param price:float, the price of the medicament, must be positive.
        :param requires_prescription:bool, True if the medicament requires a prescription, False otherwise.
        """
        super().__init__(id_medicament)
        self.__name = name
        self.__manufacturer = manufacturer
        self.__price = price
        self.__requires_prescription = requires_prescription

    # @property
    # def id_medicament(self):
    #     return self.__id_medicament

    @property
    def name(self):
        return self.__name

    @property
    def manufacturer(self):
        return self.__manufacturer

    @property
    def price(self):
        return self.__price

    @property
    def requires_prescription(self):
        return self.__requires_prescription


    @price.setter
    def set_price(self, new_price):
        self.__price = new_price

    def __str__(self):
        return "{}. {}: made by {}, price:{}, prescription:{}.".format(self.id_entity,
                                                                      self.name,
                                                                      self.manufacturer,
                                                                      self.price,
                                                                      self.requires_prescription)

    def __eq__(self, other):
        if type(self) != type(other):
            return False
        return self.id_entity == other.id_entity
