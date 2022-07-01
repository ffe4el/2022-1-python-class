class Cake:
    """케익을 나타내는 클래스"""
    coat = '생크림'

    def __init__(self,topping, price, candles=0):
        """인스턴스를 초기화한다."""
        self.topping = topping
        self.price = price
        self.candles=candles

    def describe(self):
        """이 케익에 관한 정보를 화면에 출력한다."""
        print('이 케익은 {}으로 덮여있다.'.format(self.coat))
        print("{}을 올려 장식했다." .format(self.topping))
        print("가격은 {}원이다." .format(self.price))
        print("초가 {}개 꽂혀있다." .format(self.candles))




def main():
    cake_1 = Cake('눈사람 사탕', 10000)
    cake_2 = Cake('한라봉', 9000, 8)

    print('케익 : 1')
    cake_1.describe()
    print('케익 : 2')
    cake_2.describe()

if __name__ == '__main__':
    main()