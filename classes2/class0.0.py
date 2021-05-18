# Класс Human

class Human:
    #Статические поля(атрибут)
    default_name = "No name"
    default_age = 0

    def __init__(self, name = default_name, age =default_age):
        # Динамичекие поля
        # публичные поля
        self.name = name
        self.age = age
        # Приватные
        self.__money = 0
        self.__house = None

    def info(self):
        print(f"name : {self.name}")
        print(f"age : {self.age}")
        print(f"Money : {self.__money}")
        print(f"House : {self.__house}")

#     статический метод
    @staticmethod
    def default_info():
        print(f"Default name: {Human.default_name}")
        print(f"Default age: {Human.default_age}")

    def earn_money(self, amount):
        self.__money += amount
        print(f"Erned {amount} money! Current value: {self.__money}")

    def buy_house(self, house, discount):
        price = house.final_price(discount)
        if self.__money >= price:
            self.__make_deal(house,price)
        else:
            print("Sorry, No money!!")

    #приватны метод
    def __make_deal(self, house, price):
        self.__money -= price
        self.__house = house

class House:
    def __init__(self,_area,_price):
        self._area = _area
        self._price = _price

    def final_price(self, discount):
        final_price = self._price * (100 - discount) / 100
        print(f"Final price: {final_price}")
        return final_price


class SmallHouse(House):
#     статичное поле
    default_area = 40

    def __init__(self, price):
        super().__init__(SmallHouse.default_area, price)


if __name__ == "__main__":
    # b = Human("Baktybek", 25)
    # b.info()
    # b.default_info()
    # b.earn_money(1000)
    # b.earn_money(1000)
    # b.

    Human.default_info()
    baha = Human('Baktybek', 26)
    baha.info()

    small_house = SmallHouse(35000)
    baha.buy_house(small_house, 10)

    baha.earn_money(40000)
    baha.buy_house(small_house, 10)
    baha.info()
