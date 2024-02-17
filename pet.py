class Животное:
    def __init__(self, name, command, birth_date):
        self.__name = name
        self.__command = command
        self.__birth_date = birth_date

    def get_name(self):
        return self.__name

    def get_command(self):
        return self.__command

    def get_birth_date(self):
        return self.__birth_date

class Домашнее_животное(Животное):
    def __init__(self, name, command, birth_date):
        super().__init__(name, command, birth_date)

class Вьючное_животное(Животное):
    def __init__(self, name, command, birth_date):
        super().__init__(name, command, birth_date)
