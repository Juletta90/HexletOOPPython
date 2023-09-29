# BEGIN (write your solution here)

#import solution


# def rgb2tuple(rgb):
#     if isinstance(rgb, solution.RGB):
#          return rgb.red, rgb.green, rgb.blue
#
#
# rgb2tuple(42)
# rgb2tuple(solution.red)  # (255, 0, 0)
# rgb2tuple(solution.green)  # (0, 255, 0)
# rgb2tuple(solution.blue)  # (0, 0, 255)



# https://docs-python.ru/tutorial/klassy-jazyke-python/atributy-peremennye-klassa-peremennye-ekzempljara-klassa/

# https://pythonist.ru/peremennye-klassa-i-ekzemplyara-v-python/



# Переменные класса позволяют нам определять переменные при построении класса.
# Затем эти переменные и связанные с ними значения становятся доступными для каждого экземпляра класса.
class RGB:

    # переменные класса RGB
    red = (0, 0, 0)
    green = (0, 0, 0)
    blue = (0, 0, 0)

    # Метод-конструктор с переменной экземпляра solution
    def __init__(self, solution):
        self.solution = solution


# экземпляр (он же - объект) класса RGB это red = RGB().
# определение объектов (или экземпляров) класса RGB:
new_red = RGB((255, 0, 0))
new_green = RGB((0, 255, 0))
new_blue = RGB((0, 0, 255))
print(new_red.red, new_green.green, new_blue.blue)



# END