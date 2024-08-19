from math import pi, sqrt
class Figure:
    sides_count = 0

    def __init__(self, color:list[int], sides, filled=bool):

        self.__color = color  # список цветов в формате RGB
        self.__sides = sides  # Список сторон целые числа
        self.filled = False        #закрашенный, bool

    def get_color(self):
        return self.__color

    def __is_valid_color(self, r, g, b):

        if 0 < r <= 255 and 0 < g <= 255 and 0 < b <= 255:  # Цвет корректный
            self.filled = True
            return r, g, b
        else:
            self.filled = False
            return self.__color  # Цвет некорректный

    def set_color(self, r, g, b):
        new_color = self.__is_valid_color(r, g, b)  # изменение цвета после проверки на корректность
        self.__color = list(new_color)
        return self.__color


class Circle(Figure):
    sides_count = 1
    def __init__(self):
        super().__init__()
        self.__radius = self.sides / 2 * pi

    def get_square(self):


circle1 = Circle((200, 200, 100), 10)

figure1 = Figure((200, 200, 100), 10)
print(figure1.get_color())
#figure1.set_color(55, 66, 77) # Изменится
#print(figure1.get_color())
figure1.set_color(555, 666, 777) # не изменится
print(figure1.get_color())