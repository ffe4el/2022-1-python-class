import math
import turtle as t
from abc import ABC, abstractmethod
import matplotlib.pyplot as plt
import time

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass
    @abstractmethod
    def perimeter(self):
        pass



class Rectangle(Shape):
    def __init__(self,h,v):
        self.h = h
        self.v = v
    def area(self):
        return self.h * self.v
    def perimeter(self):
        return 2*self.h + 2*self.v
    def draw(self):
        plt.plot([0, 0, self.h, self.h, 0], [0, self.v, self.v, 0, 0])
        plt.title("Rectangle")
        plt.xlabel("h")
        plt.ylabel("v")
        plt.grid(True)
        plt.show()
    def __repr__(self):
        return "사각형(밑변={}, 높이{})".format(self.h, self.v)




class Triangle(Shape):
    def __init__(self,h,v):
        self.h = h
        self.v = v
    def area(self):
        return self.h * self.v * 0.5
    def perimeter(self):
        return self.h + self.v + math.sqrt(self.h^2 + self.v^2)
    def draw(self):
        plt.plot([0, self.h, self.h/2, 0], [0, 0, self.v, 0])
        plt.title("Triangle")
        plt.xlabel("h")
        plt.ylabel("v")
        plt.grid(True)
        plt.show()

    def __repr__(self):
        return "삼각형(밑변={}, 높이{})".format(self.h, self.v)

class Circle(Shape):
    def __init__(self,r):
        self.r = r
    def area(self):
        return self.r * self.r * math.pi
    def perimeter(self):
        return 2 * math.pi * self.r
    def draw(self):
        t.shapesize(1, 1, 1)
        t.speed(20)
        t.width(1)
        # x축 y축을 그린다.
        t.goto(-500, 0)  # x축 가장 왼쪽 부터
        t.goto(500, 0)  # x축 가장 오른쪽 까지
        t.pu()  # 팬을 들어 올린다. 만약 팬을 올리지 않는다면 이동하면서 캔버스에 그려질것이다.
        t.goto(0, 500)  # y축 가장 위부터
        t.pd()  # 팬을 내린다.
        t.goto(0, -500)  # y축 가장 아래까지

        t.color("red")  # 팬의 색을 red로 변경

        # x축 범위만큼 반복하며 식에 대입해 y의 값을 찾은뒤 점을 찍는다.
        # 이때의 범위는 원의 중심의 x값에서 반지름을 뺀 값부터, 원의 중심의 x값에서 반지름을 더한 값까지이다.
        # 이때 원이 그려지는 속도를 위해 x값을 2씩 증가시키겠다.
        for x in range(-self.r, self.r + 1, 2):
            y = math.sqrt(self.r ** 2 - x ** 2)
            t.goto(x, y)
            # t.dot(3, "red")

            t.pd()
            print(f"({x}, {y})")

        # 다시 x축 범위만큼 반복하여 y의 값을 찾아 점을 찍는다. 이때 y값은 음의 제곱근이다.
        for x in reversed(range(-self.r,  self.r + 1, 2)):
            y = -math.sqrt(self.r ** 2 - x ** 2)
            t.goto(x, y)
            # t.dot(3, "red")
            print(f"({x}, {y})")

        # 반지름을 그린다.
        t.width(3)
        t.goto(0, 0)  # 현재 위치에서 중심까지 이동한다. 원의 한점에서 원의 중심을 이은 선분 == 원의 반지름

        t.up()
        t.left(135)
        t.forward(30)
        t.left(45)
        t.forward(20)
        t.write(self.r)

        t.ht()
        t.mainloop()


class RegularHexagon(Shape):
    def __init__(self, r):
        self.r = r
    def area(self):
        return self.r * self.r * math.sqrt(3)* 1.5
    def perimeter(self):
        return 6*self.r
    def draw(self):
        plt.plot(self.r,[0,0,math.sqrt(3), 2*math.sqrt(3), 2*math.sqrt(3), math.sqrt(3),0])
        plt.title("RegularHexagon")
        plt.show()


def main():
    shapes = [
        Rectangle(3,4),
        # Rectangle(7,2),
        Triangle(4,4),
        # Triangle(4,8),
        Circle(100),
        # Circle(200),
        RegularHexagon(2),
        # RegularHexagon(5)
    ]
    for shape in shapes:
        print(shape)
        print(shape.area())
        print(shape.perimeter())

    R = Rectangle(3,4)
    R.draw()
    # r = Rectangle(7,2)
    # r.draw()
    T = Triangle(4,4)
    T.draw()
    H = RegularHexagon([1,3,4,3,1,0,1])
    H.draw()
    C = Circle(100)
    C.draw()


if __name__ == '__main__':
    main()

