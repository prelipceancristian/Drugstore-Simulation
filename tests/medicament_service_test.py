from domain.medicament_validator import MedicamentValidator
from repository.medicament_repository import MedicamentInMemoryRepository
from service.medicament_service import MedicamentService

repository = MedicamentInMemoryRepository()
validator = MedicamentValidator()
service = MedicamentService(repository, validator)

service.add_medicament(1, "Nurofen", "Paduden", 13, "no")
service.add_medicament(2, "Aspirin", "Bayer", 10, "no")
service.add_medicament(3, "Vicodin", "Abbott", 65, "yes")

assert len(repository.read()) == 3
assert repository.read(1) is not None
assert repository.read(4) is None

service.delete_medicament(1)
assert repository.read(1) is None

service.populate_meds(12)
assert len(repository.read()) == 14



