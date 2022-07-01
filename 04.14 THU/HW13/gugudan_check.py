import random


def main():
    n = int(input("문제 개수는?"))
    total = 0
    for i in range(n):
        a = random.randint(1,9)
        b = random.randint(1,9)
        print ("구구단을 외자! 구구단을 외자! {}*{}" .format(a,b))
        c = int(input("=> ?"))
        if c == a*b :
            print("딩동댕")
            total += 1
        else :
            print("땡")
    print("점수는 {:.0f}입니다." .format(100*total / n))





if __name__ == "__main__":
    main()