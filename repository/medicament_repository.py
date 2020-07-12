# from domain.medicament import Medicament


class MedicamentInMemoryRepository:
    """
    Repository for storing data in memory.
    """

    def __init__(self):
        """
        Creates an in memory repository.
        """
        self.__storage = {}

    def create(self, medicament):
        """
        Adds a new medicament
        :param medicament: the new medicament
        :return: -
        :raises: Keyerror if the id already exists.
        """
        medicament_id = medicament.id_entity
        if medicament_id in self.__storage:
            raise KeyError("The medicament id {} already exists!.".format(medicament_id))
        self.__storage[medicament_id] = medicament

    def read(self, medicament_id=None):
        """
        Gets a medicament by id or every medicament.
        :param medicament_id: the id of the medicaments
        :return: the list of meds with the given id.
        """
        if medicament_id is None:
            return self.__storage.values()

        if medicament_id in self.__storage:
            return self.__storage[medicament_id]
        return None

    def update(self, medicament):
        """
        Updates a medicament.
        :param medicament: the medicament to update.
        :return: -
        :raises: KeyError if the medicament doesn't exist.
        """
        id_medicament = medicament.id_medicament
        if id_medicament not in self.__storage:
            raise KeyError("The medicament with the id {} doesn't exist!".format(id_medicament))
        self.__storage[id_medicament] = medicament

    def delete(self, medicament_id):
        """
        Deletes a medicament.
        :param medicament_id:the id of the medicament to be deleted
        :return: -
        :raises: KeyError if the medicament doesn't exist.
        """
        if medicament_id not in self.__storage:
            raise KeyError("The medicament with the id {} doesn't exist!".format(medicament_id))
        del self.__storage[medicament_id]
