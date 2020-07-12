class ClientCardValidator:

    def validate(self, client_card):

        errors = []
        """
        if type(client_card.birth_date) is not datetime.date:
            x = client_card.birth_date
            print(type(x))
            print(x)
            args_birth = x.split(".")
            d1 = datetime.date(int(args_birth[2]), int(args_birth[1]), int(args_birth[0]))
            print(d1)
            args_reg = client_card.register_date.split(".")
            d2 = datetime.date(int(args_reg[2]), int(args_reg[1]), int(args_reg[0]))
            print(d2)
        """
        if isinstance(client_card.CNP, int) is not True:
            errors.append("The CNP is not a number!")

        if errors:
            raise ValueError(errors)
