# создаем класс Vehicle - любой транспорт
class Vehicle:
    __COLOR_VARIANTS = ['blue','green', 'white', 'black', 'silver']  #атрибут класса, который содержит список допустимых цветов для окрашивания

    def __init__(self, owner, model, engine_power, color):
        self.owner = owner
        self.__model = model
        self.__engine_power = engine_power
        self.__color = color.lower()  # чтобы сравнивать цвет без учета регистра

    def get_model(self):
        return f"Модель: {self.__model}"

    def get_horsepower(self):
        return f"Мощность двигателя: {self.__engine_power}"

    def get_color(self):
        return f"Цвет: {self.__color}"

    def print_info(self):
        return f"{self.get_model()}\n{self.get_horsepower()}\n{self.get_color()}\nВладелец: {self.owner}"


    def set_color(self, new_color):
        if new_color.lower() in self.__COLOR_VARIANTS:
            self.__color = new_color.lower()
        else:
            print(f"Нельзя сменить цвет на {new_color}")

# создаем класс Sedan - наследник класса Vehicle
class Sedan(Vehicle):
    __PASSENGERS_LIMIT = 5  # атрибут класса Sedan, ограничение посадочных мест

    def __init__(self, owner, model, engine_power, color):
        super().__init__(owner, model, engine_power, color)

# Тестирование
vehicle1 = Sedan('Fedos', 'Toyota Mark II', 500, 'blue')
print(vehicle1.print_info())
vehicle1.set_color('Pink')
print(vehicle1.print_info())
vehicle1.set_color('BLACK')
vehicle1.owner = 'Vasyok'
print(vehicle1.print_info())

#```
#Этот код создает классы `Vehicle` и `Sedan`, наследника класса `Vehicle`. В классе `Vehicle` есть атрибут `__COLOR_VARIANTS`, который содержит список допустимых цветов для окрашивания. Класс `Vehicle` имеет методы `get_model`, `get_horsepower`, `get_color`, `print_info` и `set_color`. Класс `Sedan` имеет атрибут `__PASSENGERS_LIMIT` и наследует свою версию метода `__init__`.
