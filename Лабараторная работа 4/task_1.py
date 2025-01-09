class Weapon:  # Описываем базовый класс Оружие и его поля: цвет и качество
    def __init__(self, color: str, quality: str):
        self.color = color
        self.quality = quality

    def shot(self) -> None:  # Нам неизвестно оружие, из которого будем стрелять, поэтому метод не выполняет действий
        return None

    def recharge(self) -> None:  # Метод, выполняющий перезарядку. Унаследован во всех остальных классах
        print("Оружие перезаряжено")

    def __str__(self):  # Магический метод str
        return f"Оружие цвета {self.color} качества {self.quality}"

    def __repr__(self):  # Магический метод repr
        return f"'{self.__class__.__name__}'(color={self.color!r}, quality={self.quality!r})"


class Gun(Weapon):  # Описываем дочерний класс Пистолет с дополнительным полем "название"
    def __init__(self, color: str, quality: str, name: str):  # Перегружаем конструктор базового класса
        super().__init__(color, quality)
        self.name = name

    def shot(self) -> None:  # Перегружаем метод выстрела
        print("BAM")

    def __str__(self):  # Перегружаем магические методы
        return f"Оружие {self.name} цвета {self.color} качества {self.quality}"

    def __repr__(self):
        return f"{self.__class__.__name__}(color={self.color!r}, quality={self.quality!r}, name={self.name!r})"


class SubmachineGun(Gun):  # Описываем дочерний класс Пистолет-пулемет
    # Конструктор, поля и магические методы наследуются от класса Пистолет и остаются неизменными
    def shot(self) -> None:  # Перегружаем метод выстрела
        print("BABABABAM")


if __name__ == '__main__':
    weapon_1 = Weapon("red", "normal")
    print(weapon_1)
    weapon_2 = Gun("grey", "high", "Makarov")
    print(weapon_2)
    weapon_3 = SubmachineGun("black", "low", "Machine Gun")
    print(weapon_3)
    weapon_2.shot()
    weapon_3.shot()
    weapon_1.shot()
    weapon_1.recharge()
    weapon_3.recharge()