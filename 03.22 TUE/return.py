def minmax(numbers):


def main():
    x = [3, 7, 25, 10, 2, 13]
    mn = minmax(x)[0]
    mx = minmax(x)[1]
    # mn, mx = minmax(x) 로 쓸 수 있다. 언패킹이라고 한다.
    print("가장 작은 수는 {}이고, 가장 큰 수는 {}입니다." .format(mn, mx))

if __name__ == "__main__”:
    main()

