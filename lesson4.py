from points import get_x, get_y, make_decart_point


# BEGIN (write your solution here)
def make_segment(x, y):
     return x, y


segment = make_segment(make_decart_point(3, 2), make_decart_point(0, 0))


def get_begin_point(segment):
     begin_point = make_decart_point(3, 2)
     return begin_point


get_begin_point(segment)


def get_end_point(segment):
     end_point = make_decart_point(0, 0)
     return (end_point)


get_end_point(segment)


# def get_mid_point_of_segment(segment):
#      x1, y1 = make_decart_point(3, 2)
#      x2, y2 = make_decart_point(0, 0)
#
#      get_x(point) = (x1 + x2) / 2
#
#      # begin_point = (x1 + x2) / 2
#      # end_point = (y1 + y2) / 2
#
#      mid_point = {"x": begin_point, "y": end_point}
#      return mid_point


# point = make_point(3, 4) # мы не знаем как устроена точка
# print(get_y(point)) # мы получаем доступ к частям только через селекторы



get_mid_point_of_segment(segment)



    # # В примерах ниже возвращаются точки с координатами (x, y)
    # get_begin_point(segment)  # {'x': 3, 'y': 2}
    # get_end_point(segment)  # {'x': 0, 'y': 0}
    # get_mid_point_of_segment(segment)  # {'x': 1.5, 'y': 1}
# END

