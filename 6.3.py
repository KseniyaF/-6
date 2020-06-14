class Worker:
    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._incom = {"wage": wage, "bonus": bonus}


class Position(Worker):
    def __init__(self, name, surname, position, wage, bonus):
        super().__init__(name, surname, position, wage, bonus)

    def get_full_name(self):
        return self.name + ' ' + self.surname

    def get_total_income(self):
        return self._incom.get('wage')+ self._incom.get('bonus')


z = Position('Vanyia', 'Petrov', 'Destroyer', 15000, 30000)
print(z.get_full_name())
print(z.get_total_income())