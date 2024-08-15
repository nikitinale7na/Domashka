class Horse:                                  # Лошадь
    def __init__(self, x_distance=0, sound='Frrr'):    # пройденный путь, звук издает
        self.x_distance = x_distance
        self.sound = sound
        super().__init__()
    def run(self, dx):
        self.x_distance += dx
        return self.x_distance

class Eagle:                                 # Орел
    def __init__(self, y_distance=0, sound='I train, eat, sleep, and repeat'):   # путь, звук
        self.y_distance = y_distance
        self.sound = sound
    def fly(self, dy):
        self.y_distance += dy
        return self.y_distance

class Pegasus(Horse, Eagle):                 # Пегас
    def __init__(self):
        super().__init__()
    def move(self, dx, dy):
        super().run(dx)
        super().fly(dy)

    def get_pos(self):
        return self.x_distance, self.y_distance

    def voice(self):
        print(self.sound)

p1 = Pegasus()

print(p1.get_pos())
p1.move(10, 15)
print(p1.get_pos())
p1.move(-5, 20)
print(p1.get_pos())

p1.voice()