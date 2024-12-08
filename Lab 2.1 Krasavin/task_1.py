import random
class Factory:
    def __init__(self, furniture_object: str, quantity: int, type_: str):
        '''
            Класс фабрика, которая принимает заказы
        :param furniture_object: объект мебели, которую заказывают у фабрики ("chair", "bed", "table")
        :param quantity: количество этих объектов
        :param type_: тип объекта ("premium", "economy class", "normal")
         Примеры:
          order1 = Factory("chair", 1000, "premium") # инициализация экземпляра класса
          order2 = Factory("table", 2, "economy class")
         '''
        self.furniture_object = None
        self.quantity = None
        self.type_ = None
        self.init_get_quantity(quantity)
        self.init_get_type_(type_)
        self.init_get_furniture_object(furniture_object)
    def init_get_quantity(self, quantity: int)-> None: #здесь и далее метод присвоения характеристики
        if not isinstance(quantity, int): #Здесь и далее проверка на принадлежность типу
            raise TypeError
        if not quantity > 0: #количество не может быть отрицательным
            print("quantity cannot be negative")
            raise TypeError
        if not isinstance(quantity, int):
            raise TypeError
        self.quantity = quantity

    def init_get_type_(self,type_: str)-> None:
        list_of_types =["premium", "economy class", "normal"] #Список возможного класса изделия
        if not isinstance(type_, str):
            raise TypeError
        if type_ not in list_of_types:
            print("incorrect type")
            raise TypeError
        self.type_ = type_

    def init_get_furniture_object(self, furniture_object: str) -> None:
        list_of_furniture = ["chair", "bed", "table"]#Список возможных изделий
        if not isinstance(furniture_object, str):
            raise TypeError
        if furniture_object not in list_of_furniture:
            print("incorrect furniture")
            raise TypeError
        self.furniture_object = furniture_object


    def create(self) -> None:
        '''
            Условное создание заказа #можно, например, реализовать формирование и отправку запроса на производство

            Пример
            order1 = Factory("chair", 1000, "premium")
            order1.create()

        '''
        print('order was created')

    def cost_calculation(self) -> int:
        '''
            Функция вычисления стоимости заказа

            Пример:
            order1 = Factory("chair", 1000, "premium")
            order1.cost_calculation()

            :return Стоимость заказа
        '''
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
        '''
        Класс Логистическая компания, которая выполняет перевозки
        :param volume: объем товара в кубометрах
        :param weight: масса товара в килограммах

        Примеры:
        transportation_1 = LogisticCompany(20, 10000)
        transportation_2 = LogisticCompany(10, 1500)
        '''
        self.volume = None
        self.weight = None
        self.car = None
        self.init_get_volume(volume)
        self.init_get_weight(weight)
    def init_get_volume(self, volume: int)-> None:
        if not isinstance(volume, int):
            raise TypeError
        if not volume > 0: #Объем не может быть отрицательным
            raise TypeError
        self.volume = volume

    def init_get_weight(self, weight: int)-> None:
        if not isinstance(weight, int):
            raise TypeError
        if not weight > 0: #Масса не может быть отрицательной
            raise TypeError
        self.weight = weight

    def get_car(self) -> str:
        '''
            Функция, которая подбирает машину для выполнения заказа в соответствии с объемом и массой

            Пример:
            transportation_1 = LogisticCompany(20, 10000)
            transportation_1.get_car()

        :return: Машина, которая повезет заказ
        '''
        global send_the_car #Глобальная переменная нужна для того, чтобы обращаться к ней в других блоках кода,
                            # потому что маштну можно не подобрать,
                            # следовательно не нужно считать стоимоть перевозки и искать водителя
        if self.weight <= 20000 and self.weight >= 10000 and self.volume <= 50 and self.volume >= 20:
            self.car = "Sitrak 082" #Большая машина
            send_the_car = True
            return self.car

        elif self.weight <= 10000 and self.weight >= 3000 and self.volume <= 20 and self.volume >= 12:
            self.car = "GasOn NEXT 115" #Средняя машина
            send_the_car = True
            return self.car

        elif self.weight <= 3000 and self.weight >= 100 and self.volume <= 12 and self.volume >= 1:
            self.car = "Gaselle 005" #Маленькая машина
            send_the_car = True
            return self.car
        else:
            send_the_car = False
            return "other company, because we have not car for your order" #нет подходящей машины

    def cost_of_transportation_calculation(self, km: int) -> int:
        '''
            Функция, которая расчитывает стоимость перевозки
        :param km: Дальность пеервозки в километрах

        Пример:
        transportation_1 = LogisticCompany(20, 10000)
        transportation_1.cost_of_transportation_calculation(500)

        :return: Стоимость перевозки
        '''
        if not isinstance(km, int):
            raise TypeError
        if not km > 100:
            print("The company deals only with long-distance transportation")
            raise TypeError
        list_of_cost_for_car = { #Словарь коэффициентов стоимости перевозки данным автомобилем
            "Sitrak 082" : 20,
            "GasOn NEXT 115" : 5,
            "Gaselle 005" : 2
        }
        if send_the_car:
            return km * 6 * list_of_cost_for_car[self.car] #6 долларов за километр умножаем на кол-во км и коэф. машины

    def get_driver(self) -> str:
        '''
        Функция, которая случайно назначает водителя на перевозку

        Пример:
        transportation_1 = LogisticCompany(20, 10000)
        transportation_1.get_driver()

        :return: Водитель
        '''
        if send_the_car:
            list_of_drivers = ["Sergei", "Alexey", "Ivan"] #Список водителей
            driver = list_of_drivers[random.randint(0,2)]
            return driver
# TODO: и ещё один
class Worker:
    def __init__(self, name: str, surname: str, age: int)-> None:
        '''
        Класс работников
        :param name: Имя
        :param surname: Фамилия
        :param age: Возраст

        Пример:
        person_1 = Worker("Ann", "Ivanova", 50)
        person_2 = Worker("Alexandr", "Vorobiov", 35)
        '''
        self.name = None
        self.surname = None
        self.age = None
        self.profession = None
        self.init_get_name(name)
        self.init_get_surname(surname)
        self.init_get_age(age)

    def init_get_name(self, name: str) -> None:
        if not isinstance(name, str):
            raise TypeError
        self.name = name

    def init_get_surname(self, surname: str)-> None:
        if not isinstance(surname, str):
            raise TypeError
        self.surname = surname

    def init_get_age(self, age: int)-> None:
        if not isinstance(age, int):
            raise TypeError
        if age < 14: #Компания не берет на работу лиц, младше 14 лет
            print("The employee must be at least 14 years old")
            raise TypeError
        self.age = age

    def init_get_profession(self, profession: str) -> str:
        '''
        Функция, которая позволяет дать или сменить профессию человеку
        :param profession: Профессия ("driver", "loader", "logistician", "manager", "carpenter")

        Пример:
        person_1 = Worker("Ann", "Ivanova", 50)
        person_1.init_get_profession("loader")

        :return: Профессия человека
        '''
        list_of_profession = ["driver", "loader", "logistician", "manager", "carpenter"] #Возможные профессии (Водитель, грузчик, логист, менеджер и плотник
        if not isinstance(profession, str):
            raise TypeError
        if profession not in list_of_profession: #Проверка, существует ли такая профессия
            print("incorrect profession")
            raise TypeError
        self.profession = profession
        return self.profession
    def go_to_work(self) -> None:
        '''
        Метод, который вызывает человека на работу

        Пример:
        person_1 = Worker("Ann", "Ivanova", 50)
        person_1.go_to_work()

        :return: Сообщает идти на работу
        '''
        print(f'{self.name} {self.surname} go to work')



if __name__ == "__main__": #Пример реализации всех трёх классов
    order1 = Factory("chair", 1000, "premium")
    print(order1.furniture_object, order1.quantity, order1.type_)
    order1.create()
    print(f'{order1.cost_calculation()} dollars')
    print("--------------------------------------")
    transportation_1 = LogisticCompany(20, 10000)
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



