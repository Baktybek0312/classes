# Нужно создать класс который принимает данные в формате dict.
# Эти данные, вы сможете взять из Data #1.
#
# Вам нужно создать 6 методов класса:
#
# Получить все ключи в TUPLE.
#
# Получить все значения в TUPLE.
#
# Получить все ключи в LIST.
#
# Получить все значения в LIST.
#
# Получить все ключи в SET.
#
# Получить все значения в SET.
#
#
#
# Ниже когда вы будете передавать Словарь классу он и вызывать из него любой метод.
# Вы должны получать соответственно нужные типы данных.
#
# Example: my_class = Parser("DICT") | my_class.get_keys_tuple()

def second():
    colors = {
        "black": {
            "category": "hue",
            "type": "primary",
            "code": {
                "rgba": [ 255, 255, 255, 1 ],
                "hex": "#000"
            }
        },
        "red": {
            "category": "hue",
            "type": "primary",
            "code": {
                "rgba": [ 255, 0, 0, 1 ],
                "hex": "#FF0"
            }
        },
        "white": {
            "category": "value",
            "type": "primary",
            "code": {
                "rgba": [ 0, 0, 0, 1 ],
                "hex": "#FFF"
            }
        },
        "blue": {
            "category": "hue",
            "type": "primary",
            "code": {
                "rgba": [ 0, 0, 255, 1 ],
                "hex": "#00F"
            }
        },
        "yellow": {
            "category": "hue",
            "type": "primary",
            "code": {
                "rgba": [ 255, 255, 0, 1 ],
                "hex": "#FF0"
            }
        },
        "green": {
            "category": "hue",
            "type": "secondary",
            "code": {
                "rgba": [ 0, 255, 0, 1 ],
                "hex": "#0F0"
            }
        }
    }

    class Parser:
        def __init__(self, dict1) -> None:
            self.dict1 = dict1

        def get_keys_tuple(self):
            inner_keys = list (colors.keys ( ))
            for i in colors:
                inner_keys += list (colors[ i ].keys ( ))
                for j in colors[ i ]:
                    try:
                        inner_keys += list (colors[ i ][ j ].keys ( ))
                    except AttributeError:
                        continue
            return set (set (inner_keys))

        def get_values_tuple(self):
            tuple1 = tuple (self.dict1.values ( ))
            return tuple1

        def get_keys_list(self):
            list1 = list (self.dict1.keys ( ))
            return list1

        def get_values_list(self):
            list1 = list (self.dict1.values ( ))
            return list1

        def get_keys_set(self):
            set1 = set (self.dict1.keys ( ))
            return set1

        def get_values_set(self):
            set1 = str (self.dict1.values ( ))
            return set1

    my_class = Parser (colors)

    print (my_class.get_keys_tuple ( ))
    # # print(my_class.get_values_tuple())
    # # print(my_class.get_keys_list())
    # # print(my_class.get_values_list())
    # # print(my_class.get_keys_set())
    # print(my_class.get_values_set())
    # print(colors['green']['code'].keys())


def third():
    data = {
        "markers": [
            {
                "name": "Rixos The Palm Dubai",
                "position": [ 25.1212, 55.1535 ],
            },
            {
                "name": "Shangri-La Hotel",
                "location": [ 25.2084, 55.2719 ]
            },
            {
                "name": "Grand Hyatt",
                "location": [ 25.2285, 55.3273 ]
            }
        ]
    }

    class Hotels:
        def __init__(self, ):
            pass


second()
