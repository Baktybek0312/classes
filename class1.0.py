# Нужно создать класс который принимет модель ноутбука(Acer, Asus, ...) и возвращает полную комплектацию ноутбука со всеми характеристиками.
#
# В характеристики должны входить:
#
# Процессор
#
# Оперативная Память
#
# Видео карта
#
# Жёсткий Диск
#
# Материнская плата
#
# Размер экрана
#
# Для каждой характеристики создайте внутри класса функцию которая добавляет по одной характеристики к Dictionary.
#
# В итоге Ваш класс должен вернуть Dictionary в котором перечислены:
#
# Модель Ноутбука и его Характеристики.

class Models:

    def __init__(self, name, cpu, ram, video_card, HDD, motherboard, screen_diagonal):
        self.name = name
        self.cpu = cpu
        self.ram = ram
        self.video_card = video_card
        self.hdd = HDD
        self.motherboard = motherboard
        self.screen_digonal = screen_diagonal

    def get_dict(self):
        my_dict = {'Модель ноутбука': [ ], 'Процессор': [], 'Оперативная Память': [ ], 'Видео карта': [ ],
                   'Жёсткий Диск': [ ],
                   'Материнская плата': [ ], 'Размер экрана': []}

        my_dict['Модель ноутбука'].append (self.name)
        my_dict['Процессор'].append(self.cpu)
        my_dict['Оперативная Память'].append (self.ram)
        my_dict['Видео карта'].append(self.video_card)
        my_dict['Жёсткий Диск'].append(self.hdd)
        my_dict['Материнская плата'].append(self.motherboard)
        my_dict['Размер экрана'].append(self.screen_digonal)
        print(my_dict)


models = Models('Acer', 'intel core i5', 'DDR4X 32GB', 'Nvidia gtx 2060', 'HDD 512GB', 'Материнская плата hbr',
                 'Размер экрана 16 дюймов')
models1 = Models('Asus', 'AMD Raizer 7', 'DDR3 16GB', 'Nvidia GTX 1060TI', 'SSD 1TR', 'Материнская плата Tdr', 'Размер экрана 15,6 дюймов')
models.get_dict()
models1.get_dict()
