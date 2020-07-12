class MedicamentValidatorError(Exception):
    pass

class MedicamentValidator:

    def validate(self, medicament):

        errors = []
        if medicament.price < 0:
            errors.append("The price of the med must be greater than 0!")
        if medicament.requires_prescription not in ["yes", "no"]:
            errors.append("The prescription field must be filled with either yes or no, not with {}".format(
                medicament.requires_prescription))

        if errors:
            raise MedicamentValidatorError(errors)
