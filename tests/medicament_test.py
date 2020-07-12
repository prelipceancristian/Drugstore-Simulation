from domain.medicament import Medicament

med1 = Medicament(1, "Nurofen", "Paduden", 13, "no")
med2 = Medicament(2, "Aspirin", "Bayer", 10, "no")
med3 = Medicament(3, "Vicodin", "Abbott", 65, "yes")
med4 = Medicament(3, "aacodin", "Abbott", 65, "yes")

assert med1.id_entity == 1
assert med2.price == 10
assert med3.manufacturer == "Abbott"
assert med1 != med2
assert med3 == med4
