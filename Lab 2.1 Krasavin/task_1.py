import random
class Factory:
    def __init__(self, furniture_object: str, quantity: int, type_: str):
        """
        Создание и подготовка к работе объекта "Фабрика мебели".

        :param furniture_object: Тип мебели (например, "chair", "bed", "table").
        :param quantity: Количество мебели.
        :param type_: Класс мебели ("premium", "economy class", "normal").

        Примеры:
         factory = Factory("chair", 10, "premium")  # инициализация экземпляра класса
        """
        self.furniture_object = None
        self.quantity = None
        self.type_ = None
        self.init_get_quantity(quantity)
        self.init_get_type_(type_)
        self.init_get_furniture_object(furniture_object)
    def init_get_quantity(self, quantity: int)-> None: #здесь и далее метод присвоения характеристики
        """
                Установка количества мебели.

                :param quantity: Количество мебели.
                :raise TypeError: Если количество не является положительным целым числом.

                Примеры:
                factory = Factory("chair", 10, "premium")
                 factory.init_get_quantity(20)
                """
        if not isinstance(quantity, int): #Здесь и далее проверка на принадлежность типу
            raise TypeError
        if not quantity > 0: #количество не может быть отрицательным
            print("quantity cannot be negative")
            raise TypeError
        if not isinstance(quantity, int):
            raise TypeError
        self.quantity = quantity

    def init_get_type_(self,type_: str)-> None:
        """
                Установка типа мебели.

                :param type_: Тип мебели ("premium", "economy class", "normal").
                :raise TypeError: Если тип не является строкой или не входит в список возможных типов.

                Примеры:
                 factory = Factory("chair", 10, "premium")
                 factory.init_get_type_("economy class")
        """
        list_of_types =["premium", "economy class", "normal"] #Список возможного класса изделия
        if not isinstance(type_, str):
            raise TypeError
        if type_ not in list_of_types:
            print("incorrect type")
            raise TypeError
        self.type_ = type_

    def init_get_furniture_object(self, furniture_object: str) -> None:
        """
                Установка объекта мебели.

                :param furniture_object: Объект мебели (например, "chair", "bed", "table").
                :raise TypeError: Если объект не является строкой или не входит в список возможных объектов.

                Примеры:
                 factory = Factory("chair", 10, "premium")
                 factory.init_get_furniture_object("table")
                """
        list_of_furniture = ["chair", "bed", "table"]#Список возможных изделий
        if not isinstance(furniture_object, str):
            raise TypeError
        if furniture_object not in list_of_furniture:
            print("incorrect furniture")
            raise TypeError
        self.furniture_object = furniture_object


    def create(self) -> None:
        """
        Метод для создания заказа.

        Примеры:
         factory = Factory("chair", 10, "premium")
         factory.create()  # создание заказа
        """
        print('order was created')

    def cost_calculation(self) -> int:
        """
        Расчет стоимости мебели.

        :return: Общая стоимость мебели.

        Примеры:
         factory = Factory("chair", 10, "premium")
         total_cost = factory.cost_calculation()
        """
        list_of_furniture = { #Cловарь, который хранит коэффициенты для расчета стоимости единицы определённой мебели
            "chair" : 5,
            "bed" : 50,
            "table" : 15
        }
        list_of_types = { #Cловарь, который хранит коэффициенты для расчета стоимости единицы определенного класса
            "premium": 5,
            "economy class": 1,
            "normal": 2
        }
        return list_of_furniture[self.furniture_object] * list_of_types[self.type_] * self.quantity






# TODO: описать ещё класс

class LogisticCompany:
    def __init__(self, volume: int, weight: int):
        """
        Создание и подготовка к работе заказа логистической компании.

        :param volume: Объем грузоперевозки (в кубических метрах).
        :param weight: Вес груза (в килограммах).

        Примеры:
         order1 = LogisticCompany(30, 15000)  # инициализация экземпляра класса
        """
        self.volume = None
        self.weight = None
        self.car = None
        self.send_the_car = False  # атрибут для отслеживания состояния
        self.discount = 0  # Изначально скидка равна 0
        self.init_get_volume(volume)
        self.init_get_weight(weight)


    def init_get_volume(self, volume: int) -> None:
        """
        Установка объема груза.

        :param volume: Объем груза (в кубических метрах).
        :raise TypeError: Если объем не является положительным целым числом.
        """
        if not isinstance(volume, int):
            raise TypeError("Объем должен быть целым числом.")
        if volume <= 0:  # Объем не может быть отрицательным
            raise ValueError("Объем должен быть положительным.")
        self.volume = volume

    def init_get_weight(self, weight: int) -> None:
        """
        Установка веса груза.

        :param weight: Вес груза (в килограммах).
        :raise TypeError: Если вес не является положительным целым числом.
        """
        if not isinstance(weight, int):
            raise TypeError("Вес должен быть целым числом.")
        if weight <= 0:  # Масса не может быть отрицательной
            raise ValueError("Вес должен быть положительным.")
        self.weight = weight

    def set_discount(self, discount: float = 0.0) -> None:
        """
        Установка скидки на стоимость доставки.

        :param discount: Процент скидки (по умолчанию 0.0).
        :raise ValueError: Если скидка не в пределах 0-100.
        """
        if not (0 <= discount <= 100):
            raise ValueError("Скидка должна быть от 0 до 100.")
        self.discount = discount

    def get_car(self) -> str:
        """
        Выбор автомобиля для перевозки в зависимости от веса и объема груза.

        :return: Название автомобиля, подходящего для перевозки, или сообщение об отсутствии подходящего автомобиля.
        """
        if self.weight <= 20000 and self.weight >= 10000 and self.volume <= 50 and self.volume >= 20:
            self.car = "Sitrak 082"  # Большая машина
            self.send_the_car = True
            return self.car

        elif self.weight <= 10000 and self.weight >= 3000 and self.volume <= 20 and self.volume >= 12:
            self.car = "GasOn NEXT 115"  # Средняя машина
            self.send_the_car = True
            return self.car

        elif self.weight <= 3000 and self.weight >= 100 and self.volume <= 12 and self.volume >= 1:
            self.car = "Gaselle 005"  # Маленькая машина
            self.send_the_car = True
            return self.car
        else:
            self.send_the_car = False
            return "Other company, because we have not car for your order"  # нет подходящей машины

    def cost_of_transportation_calculation(self, km: int) -> int:
        """
        Расчет стоимости перевозки.

        :param km: Расстояние перевозки (в километрах).
        :raise TypeError: Если расстояние не является целым числом или меньше 100 км.
        :return: Стоимость перевозки.
        """
        if not isinstance(km, int):
            raise TypeError("Расстояние должно быть целым числом.")
        if km <= 100:
            print("The company deals only with long-distance transportation.")
            raise ValueError("Минимальное расстояние равно 100 км.")

        list_of_cost_for_car = {  # Словарь коэффициентов стоимости перевозки данным автомобилем
            "Sitrak 082": 20,
            "GasOn NEXT 115": 5,
            "Gaselle 005": 2
        }

        if self.send_the_car:
            cost = km * 6 * list_of_cost_for_car[self.car]  # 6 долларов за километр умножаем на кол-во км и кoэф. машины
            discount_amount = cost * (self.discount / 100)
            return int(cost - discount_amount)  # возвращаем стоимость с учетом скидки

    def get_driver(self) -> str:
        """
        Выбор водителя для выбранного автомобиля.

        :return: Имя выбранного водителя.
        """
        if self.send_the_car:
            list_of_drivers = ["Sergei", "Alexey", "Ivan"]  # Список водителей
            driver = random.choice(list_of_drivers)  # выбираем случайного водителя
            return driver
# TODO: и ещё один
class Worker:
    def __init__(self, name: str, surname: str, age: int)-> None:
        """
        Создание и подготовка к работе объекта "Работник".

        :param name: Имя работника.
        :param surname: Фамилия работника.
        :param age: Возраст работника.

        Примеры:
         worker1 = Worker("Ivan", "Ivanov", 30)  # инициализация экземпляра класса
        """
        self.name = None
        self.surname = None
        self.age = None
        self.profession = None
        self.init_get_name(name)
        self.init_get_surname(surname)
        self.init_get_age(age)

    def init_get_name(self, name: str) -> None:
        """
                Установка имени работника.

                :param name: Имя работника.
                :raise TypeError: Если имя не является строкой.

                Примеры:
                 worker1 = Worker("Ivan", "Ivanov", 30)
                 worker1.init_get_name("Ivan")
        """
        if not isinstance(name, str):
            raise TypeError
        self.name = name

    def init_get_surname(self, surname: str)-> None:
        """
                Установка фамилии работника.

                :param surname: Фамилия работника.
                :raise TypeError: Если фамилия не является строкой.

                Примеры:
                worker1 = Worker("Ivan", "Ivanov", 30)
                 worker1.init_get_surname("Ivanov")
        """
        if not isinstance(surname, str):
            raise TypeError
        self.surname = surname

    def init_get_age(self, age: int)-> None:
        """
                Установка возраста работника.

                :param age: Возраст работника.
                :raise TypeError: Если возраст не является целым числом или меньше 14.

                Примеры:
                worker1 = Worker("Ivan", "Ivanov", 30)
                 worker1.init_get_age(30)
        """
        if not isinstance(age, int):
            raise TypeError
        if age < 14: #Компания не берет на работу лиц, младше 14 лет
            print("The employee must be at least 14 years old")
            raise TypeError
        self.age = age

    def init_get_profession(self, profession: str) -> str:
        """
                Установка профессии работника.

                :param profession: Профессия работника.
                :raise TypeError: Если профессия не является строкой или не входит в список возможных профессий.

                :return: Установленная профессия.

                Примеры:
                worker1 = Worker("Ivan", "Ivanov", 30)
                worker1.init_get_profession("driver")
        """
        list_of_profession = ["driver", "loader", "logistician", "manager", "carpenter"] #Возможные профессии (Водитель, грузчик, логист, менеджер и плотник
        if not isinstance(profession, str):
            raise TypeError
        if profession not in list_of_profession: #Проверка, существует ли такая профессия
            print("incorrect profession")
            raise TypeError
        self.profession = profession
        return self.profession
    def go_to_work(self) -> None:
        """
        Метод для отправки работника на работу.

        Примеры:
        worker1 = Worker("Ivan", "Ivanov", 30)
        worker1.go_to_work()
        Ivan Ivanov go to work
        """
        print(f'{self.name} {self.surname} go to work')



if __name__ == "__main__": #Пример реализации всех трёх классов
    order1 = Factory("chair", 1000, "premium")
    print(order1.furniture_object, order1.quantity, order1.type_)
    order1.create()
    print(f'{order1.cost_calculation()} dollars')
    print("--------------------------------------")
    transportation_1 = LogisticCompany(20, 10000)
    transportation_1.set_discount(15)
    print(f'Required volume:{transportation_1.volume} cubic meters, Required weight: {transportation_1.weight} kg')
    print(f'The order will be fulfilled by {transportation_1.get_car()}')
    print(f'Your driver is {transportation_1.get_driver()}')
    print(f'The cost of transportation will be {transportation_1.cost_of_transportation_calculation(5000)} dollars')
    print("--------------------------------------")
    person_1 = Worker("Ann", "Ivanova", 50)
    person_1.init_get_profession("loader")
    print(person_1.name, person_1.surname, person_1.age, person_1.init_get_profession("driver") )
    person_1.go_to_work()
    print(person_1.name, person_1.surname, person_1.age, person_1.init_get_profession("logistician") )


# TODO


# TODO



