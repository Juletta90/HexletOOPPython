# Реализуйте функцию, которая находит точку посередине между двумя указанными точками:
#
# Пример работы:
#
# point1 = {'x': 0, 'y': 0}
# point2 = {'x': 4, 'y': 4}
# get_mid_point(point1, point2)  # {'x': 2, 'y': 2}

# Средняя точка вычисляется по формуле x = (x1 + x2) / 2 и y = (y1 + y2) / 2.


def get_mid_point(p1, p2):
    """ Функция вычисляет среднюю точку между
        двумя точками на плоскости"""

    x1, y1 = p1.values()
    x2, y2 = p2.values()
    begin_point = (x1 + x2) / 2
    end_point = (y1 + y2) / 2

    mid_point = {"x": begin_point, "y": end_point}
    return mid_point


