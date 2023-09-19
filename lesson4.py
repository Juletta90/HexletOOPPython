from points import get_x, get_y, make_decart_point


# BEGIN (write your solution here)

# #____ ПРИМЕРЫ ИЗ ТЕОРИИ______#
# def make_point(x, y):
#     return {"x": x, "y": y}
#
#
# def get_x(point):
#     return point["x"]
#
#
# def get_y(point):
#     return point["y"]
#
#
# point = make_point(3, 4)
# symmetrical_point = make_point(-get_x(point), get_y(point))
# print(symmetrical_point)  # напечатает в виде словаря

# point = make_decart_point(3, 4)
# begin_point = make_decart_point(get_x(point), get_y(point))
# end_point = make_decart_point(get_x(point), get_y(point))
#
# point = make_point(5, 7)  # мы не знаем как устроена точка
# print(get_x(point))       # мы получаем доступ к частям только через селекторы
# print(get_y(point))       # напечатает построчно
#
#
# # def get_middle_point(p1, p2):
# #     x1, y1 = p1
# #     x2, y2 = p2
# #     x = (x1 + x2) / 2
# #     y = (y1 + y2) / 2
# #     return x, y
# #
# # point1 = 2, 3
# # point2 = -4, 1
# # get_middle_point(point1, point2)
#
#
# # def make_segment(p1, p2):
# #      [x1, y1], [x2, y2] = p1, p2
# #      return segment(p1, p2)
# #
# # make_segment([15, 7], [22, 11])
# #__________________________________________________________________________#


# begin_point = make_decart_point(4, 2)
# end_point = make_decart_point(0, 0)
# segment = make_segment(begin_point, end_point)



def get_mid_point_of_segment(begin_point, end_point):
     x1, y1 = begin_point
     x2, y2 = end_point
     x = (x1 + x2) / 2
     y = (y1 + y2) / 2
     return x, y


point1 = 2, 3
point2 = -4, 1
get_mid_point_of_segment(point1, point2)


def make_segment(x, y):
     begin_point = make_decart_point(x, y)
     end_point = make_decart_point(x, y)
     return begin_point, end_point

point1 = 2, 3
point2 = -4, 1
segment = make_segment(point1, point2)


def get_begin_point(segment):
     begin_point = make_decart_point(get_x(point), get_y(point))    #make_decart_point(get_x(point), get_y(point))
     return begin_point


point = 2, 3
get_begin_point(point)


def get_end_point(segment):
     end_point = make_decart_point(x, 0)
     return end_point


get_end_point(segment)


#
#
# point = make_decart_point(3, 4)
# print(get_y(point))  # выводит значение 4
# print(get_x(point))  # выводит значение 3
#
# segment = make_segment(make_decart_point(3, 2), make_decart_point(0, 0))
#
#
# def get_begin_point(segment):
#      begin_point = make_decart_point(3, 2)    #make_decart_point(get_x(point), get_y(point))
#      return begin_point
#
#
# #get_begin_point(segment)
#
#
# def get_end_point(segment):
#      end_point = make_decart_point(0, 0)
#      return (end_point)
#
#
# #get_end_point(segment)
#
#
# def get_mid_point_of_segment(segment):
#
#
#
#      x1, y1 = make_decart_point(3, 2)
#      x2, y2 = make_decart_point(0, 0)
#
#      begin_point = (x1 + x2) / 2
#      end_point = (y1 + y2) / 2
#
#      mid_point = {"x": begin_point, "y": end_point}
#      return mid_point


# point = make_point(3, 4) # мы не знаем как устроена точка
# print(get_y(point)) # мы получаем доступ к частям только через селекторы



#get_mid_point_of_segment(segment)



    # # В примерах ниже возвращаются точки с координатами (x, y)
    # get_begin_point(segment)  # {'x': 3, 'y': 2}
    # get_end_point(segment)  # {'x': 0, 'y': 0}
    # get_mid_point_of_segment(segment)  # {'x': 1.5, 'y': 1}
# END

