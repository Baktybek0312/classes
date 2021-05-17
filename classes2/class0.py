# Инкапцуляция
# class Person:
#     def walk(self):
#         print("Иду гулять")
#
# class Driver(Person):
#     def drive_car(self):
#         print("Вожу машину")
#
# class Cook(Person):
#     def do_food(self):
#         print("Готовлю еду")
#
#
# d = Driver()
# c = Cook()
# d.drive_car()
#
# d.do_food()

# class Phone:
#     username = "Baktybek"
#     __serial_number = "125642"
#     __how_many_times_turned_on = 0
#
#     def call(self):
#         print("ZZZZ")
#
#     def __turn_on(self):
#         self.__how_many_times_turned_on += 1
#         print("Вам позвонили, столько раз: ", self.__how_many_times_turned_on)
#
#
#
# my_phone = Phone()
# my_phone._Phone__turn_on()
# my_phone._Phone_serial_number = "6645"
# print("New number: ", my_phone._Phone_serial_number)


# Полимарфизм

class Person:
    def __init__(self, a):
        self.a = a

    def __str__(self):
        return f"Result: {self.a}"


    def move(self):
        return self.a**2


class Dog:
    def __init__(self,a):
        self.a = a

    def __str__(self):
        return f"Result: {self.a}"

    def move(self):
        return self.a + 10

class Car:
    def __init__(self,a):
        self.a = a
    def __str__(self):
        return f"Result: {self.a}"

    def move(self):
        return self.a % 2



p = Person(10)
d = Dog(10)
c = Car(10)
f = [p, d, c]
for i in f:
    print(i)
