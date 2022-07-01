def range_list(n):
    p = 0
    for i in range(1, n+1):
        p = print(i)
    return p


def main():
    num = int(input("숫자를 입력하세요. => "))
    print("숫자의 리스트를 보여드리겠습니다. \n{}" .format(range_list(num)))

if __name__ == "__main__" :
    main()