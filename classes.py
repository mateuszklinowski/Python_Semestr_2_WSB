import math

class Prostokat:
    def __init__(self, a, b):
        self.a = a
        self.b = b
        self.c = (a[0], b[1])
        self.d = (b[0], a[1])

    def wsp(self):
        print(c,d)

    def pole(self):
        side1_len = self.length(self.a, self.c)
        side2_len = self.length(self.b, self.c)
        return (side1_len*side2_len)

    def length(self, point1, point2):
        return math.sqrt((point2[0]-point1[0])**2 + (point2[1]-point1[1])**2)

    def obw(self):
        side1_len = self.length(self.a, self.c)
        side2_len = self.length(self.b, self.c)
        return side1_len*2 + side2_len*2

p = Prostokat((1,0), (1,1))

print(p.pole())
