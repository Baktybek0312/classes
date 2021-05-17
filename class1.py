class Car:
    #Статические поля
    door = 4
    wheelse = 4
    role = 1
    window = 6
    #Динамические поля
    def __init__(self, year, mark):
        self.year = year
        self.mark = mark
    #Вывод полей
    def info(self):
        print(f'year: {self.year}')
        print(f'mark: {self.mark}')

    def __priceCar(self, price):
        self.__price = price

car = Car(2006, "BMW")
car.info()
