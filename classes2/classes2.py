# Создайте Класс Zoo.
#
# Инициализируйте класс в объект.
#
# К объекту Zoo добавьте атрибут animal_1 и присвойте ему значение "Тигр"
#
# К объекту Zoo добавьте атрибут animal_2 и присвойте ему значение "Бегемот"
#
# К объекту Zoo добавьте атрибут animal_3 и присвойте ему значение "Жираф"
#
# В объекте Zoo измените значение атрибута animal_1 и присвойте ему значение "Лев".
#
# К объекту Zoo добавьте атрибут animal_4 и присвойте ему list состоящий из animal_2 и animal_3
#
# В объекте Zoo измените значение атрибута animal_3 и присвойте ему значение "Змея".

class Zoo:
    def __init__(self, animal_1, animal_2, animal_3):
        self.animal_1 = animal_1
        self.animal_2 = animal_2
        self.animal_3 = animal_3


a = Zoo("Тигр","Бегемот","Жираф")
print(a.animal_1, a.animal_2, a.animal_3)
a.animal_4 = [a.animal_2, a.animal_3]
print(a.animal_4)
a.animal_3 = "Змея"
print(a.animal_3)


