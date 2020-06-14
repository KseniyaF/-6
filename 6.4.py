from random import choice

class Car:
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        return f'{self.name} Поехал'

    def stop(self):
        return f'{self.name} Остановилася'

    def turn(self):
        a = ("повернула направо", "повернула налево")
        b = choice(a)
        return f'{self.name} {b}'

    def show_speed(self):
        return f'Скорость {self.name} составляет {self.speed}'

class TownCar(Car):
    def __init__(elf, speed, color, name, is_police):
       super().__init__(speed, color, name, is_police)

    def show_speed(self):
        if self.speed > 60:
            return f'Скорость {self.name} превышена'
        else:
            return f'Скорость {self.name} не превышена'

class SportCar(Car):

    def __init__(elf, speed, color, name, is_police):
       super().__init__(speed, color, name, is_police)

class WorkCar(Car):

    def __init__(elf, speed, color, name, is_police):
       super().__init__(speed, color, name, is_police)

    def show_speed(self):
        if self.speed > 40:
            return f'Скорость {self.name} превышена'
        else:
            return f'Скорость {self.name} не превышена'

class PoliceCar(Car):

    def __init__(self, speed, color, name, is_police):
       super().__init__(speed, color, name, is_police)

auto_1 = TownCar(50, 'Белый', 'TownCar', False)
auto_2 = SportCar(200, 'Cине-желтый', 'SportCar', False)
auto_3 = WorkCar(60, 'Грязно-зеленый', 'WorkCar', False)
auto_4 = PoliceCar(100, 'Черно-белый', 'PoliceCar', True)
print(f'{auto_1.color} {auto_1.go()}')
print(f'{auto_2.color} {auto_2.stop()}')
print(auto_2.go())
print(auto_3.show_speed())
print(auto_1.show_speed())
print(auto_4.show_speed())
print(f'{auto_1.name} это полицейская машина? {auto_1.is_police}')
print(f'{auto_4.name} это полицейская машина? {auto_4.is_police}')
print(auto_4.turn())
print(auto_1.turn())
























