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
#
# point = make_point(5, 7)  # мы не знаем как устроена точка
# print(get_x(point))       # мы получаем доступ к частям только через селекторы
# print(get_y(point))       # напечатает построчно
# #____________________________#

# begin_point = make_decart_point(4, 2)
# end_point = make_decart_point(0, 0)
# segment = make_segment(begin_point, end_point)

def make_segment(p1, p2):
     x1, y1 = p1.values()
     x2, y2 = p2.values()
     begin_point = make_decart_point(x1, y1)
     end_point = make_decart_point(x2, y2)
     segment = make_segment(make_decart_point(x1, y1), make_decart_point(x2, y2))
     print(begin_point, end_point)
     return begin_point, end_point

    # segment(make_decart_point(x1, y1), make_decart_point(x2, y2))

make_segment(begin_point, end_point)









# def make_segment(x, y):
#      begin_point = make_decart_point(x, y)
#      end_point = make_decart_point(x, y)
#      return begin_point, end_point
#
# # segment = make_segment(begin_point, end_point)
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

