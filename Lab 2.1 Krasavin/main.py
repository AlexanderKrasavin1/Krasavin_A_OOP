from task_1 import Factory, LogisticCompany, Worker

if __name__ == "__main__":

    order1 = Factory("chair", 1000, "premium")
    transportation_1 = LogisticCompany(20, 10000)
    person_1 = Worker("Ann", "Ivanova", 50)
    try:
        order1.init_get_furniture_object("lamp")
    except TypeError:
        print('Ошибка: неправильные данные')

    try:
        transportation_1.cost_of_transportation_calculation(-12)
    except TypeError:
        print('Ошибка: неправильные данные')

    try:
        person_1.init_get_profession("director")
    except TypeError:
        print('Ошибка: неправильные данные')
