# BEGIN (write your solution here)

# import solution
#
#
# def rgb2tuple(rgb):
#     if isinstance(rgb, solution.RGB):
#         return rgb.red, rgb.green, rgb.blue

# rgb2tuple(42)
# rgb2tuple(solution.red)  # (255, 0, 0)
# rgb2tuple(solution.green)  # (0, 255, 0)
# rgb2tuple(solution.blue)  # (0, 0, 255)


# https://docs-python.ru/tutorial/klassy-jazyke-python/atributy-peremennye-klassa-peremennye-ekzempljara-klassa/
# https://pythonist.ru/peremennye-klassa-i-ekzemplyara-v-python/
# https://dev-gang.ru/article/ponimanie-peremennyh-klassa-i-ekzempljara-v-python-3-6d1imzdg9w/

# Переменные класса позволяют нам определять переменные при построении класса.
# Затем эти переменные и связанные с ними значения становятся доступными для каждого экземпляра класса.
def some_func(data: str | None):
    match data:
        case "first":
            print("Yeas")
        case "second":
            print("Nnoo")
        case _:
            print('highly likely :(')

print(some_func("first"))


class RGB:
    """реализация цветовой модели RGB в виде класса с именем RGB"""
    # переменные класса RGB, использую для инициализации переменных
    red = 0
    green = 0
    blue = 0

    #  # Метод-конструктор с переменной экземпляра color
    # def __init__(self, color):
    #     self.color = color


red, green, blue = RGB(), RGB(), RGB()

red.red = 255
green.green = 255
blue.blue = 255

# red = RGB('255, 0, 0')
# green = RGB('0, 255, 0')
# blue = RGB('0, 0, 255')
# print(red.color)
# экземпляр (он же - объект) класса RGB это red = RGB().
# определение объектов (или экземпляров) класса RGB:

print(red.red, green.green, blue.blue)

# END
