# У нас есть какой-то юнит, которому мы в параметры передаем
# - наше игровое поле
# - х координату
# - у координату
# - направление смещения
# - летит ли он
# - крадется ли он
# - скорость
# В этом примере есть сразу несколько запахов плохого кода. Исправьте их
#   (длинный метод, длинный список параметров)


# -------------------------------------------------------------------------------------------------------------------- #
# 1 - создаём класс Unit
class Unit:
    # 2 - делаем инициализатор пустым.
    def __init__(self):
        pass

    # 3 - делаем метод move. передаём один параметр - direction, пишем условия if параметр UP устанавливаем
    # self.field.set_unit ( y=self.y + speed, x=self.x, unit=self ), elif, elif, else.
    # speed = self._get_speed
    def movie(self, direction):
        speed = self._get_speed()

        if direction == 'UP':
            self.field.set_unit(y=self.y + speed, x=self.x, unit=self)
        elif direction == 'DOWN':
            self.field.set_unit(y=self.y - speed, x=self.x, unit=self)
        elif direction == 'LEFT':
            self.field.set_unit(y=self.y, x=self.x - speed, unit=self)
        elif direction == 'RIGTH':
            self.field.set_unit(y=self.y, x=self.x + speed, unit=self)

    # 4 - делаем метод _get_speed
    # внутри данного метода определяем состояние юнита, if ... fly: скорость 1.2
    # elif crawl установить скорость 0.5, else вернуть raise.
    # параметр self.state - не определен. " но он есть "
    def _get_speed(self):
        if self.state == 'fly':
            return self.speed * 1.2
        elif self.state == 'crawl':
            return self.speed * 0.5
        raise ValueError('Эк тебя раскорячило')


# -------------------------------------------------------------------------------------------------------------------- #
# class Unit:
#     def move(self, field, x_coord, y_coord, direction, is_fly, crawl, speed = 1):
#
#         if is_fly and crawl:
#             raise ValueError('Рожденный ползать летать не должен!')
#
#         if is_fly:
#             speed *= 1.2
#             if direction == 'UP':
#                 new_y = y_coord + speed
#                 new_x = x_coord
#             elif direction == 'DOWN':
#                 new_y = y_coord - speed
#                 new_x = x_coord
#             elif direction == 'LEFT':
#                 new_y = y_coord
#                 new_x = x_coord - speed
#             elif direction == 'RIGTH':
#                 new_y = y_coord
#                 new_x = x_coord + speed
#         if crawl:
#             speed *= 0.5
#             if direction == 'UP':
#                 new_y = y_coord + speed
#                 new_x = x_coord
#             elif direction == 'DOWN':
#                 new_y = y_coord - speed
#                 new_x = x_coord
#             elif direction == 'LEFT':
#                 new_y = y_coord
#                 new_x = x_coord - speed
#             elif direction == 'RIGTH':
#                 new_y = y_coord
#                 new_x = x_coord + speed
#
#             field.set_unit(x=new_x, y=new_y, unit=self)

#     ...
