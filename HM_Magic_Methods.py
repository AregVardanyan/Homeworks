class Triangle:
    NUMBER_OF_DELETED = 0

    def __init__(self, a, b, c):
        try:
            self.a = a + 0
            self.b = b + 0
            self.c = c + 0

            assert not (a >= b + c or b >= a + c or c >= b + a)
        except TypeError:
            raise ValueError

        except AssertionError:
            print("The one side can't be greater than the sum of others")
            raise ValueError

    def __del__(self):
         Triangle.NUMBER_OF_DELETED += 1

    def pariemetr(self):
        return self.a + self.b + self.c

    def area(self):
        return (self.pariemetr() / 2 * (self.pariemetr() / 2 - self.a) *
                (self.pariemetr() / 2 - self.b) *
                (self.pariemetr() / 2 - self.c)) ** 0.5

    def is_alike(self, other):
        all_1 = sorted([self.a, self.b, self.c])
        all_2 = sorted([other.a, other.b, other.c])
        return all_1[0] / all_2[0] == all_1[1] / all_2[1] == all_1[2] / all_2[2]

    def __str__(self):
        return f"Triangle with sides {self.a} {self.b} {self.c}"

    def __int__(self):
        return self.pariemetr()

    def __bool__(self):
        return self.area()

    def __gt__(self, other):
        if not isinstance(other, Triangle):
            raise ValueError("You can't do comparison between Triangle and not Triangle")
        all_1 = sorted([self.a, self.b, self.c])
        all_2 = sorted([other.a, other.b, other.c])
        return all_1[0] > all_2[0] and all_1[1] > all_2[1] and all_1[2] > all_2[2]


class Rectangle:
    NUMBER_OF_DELETED = 0

    def __init__(self, a, b):
        try:
            self.a = a + 0
            self.b = b + 0

            assert self.a != 0 or self.b != 0
        except TypeError:
            raise ValueError

        except AssertionError:
            print("The sides can't be 0")
            raise ValueError

    def __del__(self):
         Rectangle.NUMBER_OF_DELETED += 1

    def pariemetr(self):
        return 2 * (self.a + self.b)

    def area(self):
        return self.a * self.b

    def __str__(self):
        return f"Rectangle with sides {self.a} {self.b}"

    def __int__(self):
        return self.pariemetr()

    def __bool__(self):
        return self.area()

    def __gt__(self, other):
        if not isinstance(other, Rectangle):
            raise ValueError("You can't do comparison between Rectangle and not Rectangle")
        all_1 = sorted([self.a, self.b])
        all_2 = sorted([other.a, other.b])
        return all_1[0] > all_2[0] and all_1[1] > all_2[1]


class Cube:
    NUMBER_OF_DELETED = 0

    def __init__(self, a):
        try:
            self.a = a + 0

            assert self.a != 0
        except TypeError:
            raise ValueError

        except AssertionError:
            print("The side can't be 0")
            raise ValueError

    def __del__(self):
         Cube.NUMBER_OF_DELETED += 1

    def pariemetr(self):
        return 6 * self.a

    def area(self):
        return (self.a ** 2) * 6

    def volume(self):
        return self.a ** 3

    def __str__(self):
        return f"Cube side {self.a}"

    def __int__(self):
        return self.pariemetr()

    def __bool__(self):
        return self.volume()

    def __gt__(self, other):
        if not isinstance(other, Cube):
            raise ValueError("You can't do comparison between Rectangle and not Rectangle")
        return self.a > other.a


obj_1 = Triangle(2, 4, 3)
obj_2 = Triangle(4, 6, 8)
print(obj_1.is_alike(obj_2))
obj_3 = Rectangle(1, 2)
obj_4 = Rectangle(2, 4)
print(obj_3 < obj_4)
obj_5 = Cube(1)
obj_6 = Cube(2)
print(obj_6 > obj_5)
