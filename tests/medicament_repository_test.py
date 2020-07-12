from domain.medicament import Medicament
from repository.medicament_repository import MedicamentInMemoryRepository

repository = MedicamentInMemoryRepository()

med1 = Medicament(1, "Nurofen", "Paduden", 13, "no")
med2 = Medicament(2, "Aspirin", "Bayer", 10, "no")
med3 = Medicament(3, "Vicodin", "Abbott", 65, "yes")
med4 = Medicament(3, "yesss", "Abbott", 65, "yes")

repository.create(med1)
repository.create(med2)
repository.create(med3)

assert len(repository.read()) == 3
assert repository.read(1) is not None

repository.delete(med1.id_entity)
assert repository.read(1) is None
assert len(repository.read()) == 2

repository.update(med4)
assert repository.read(med4.id_entity) is not None
