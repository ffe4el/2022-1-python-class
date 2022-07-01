import random


def main():
    n = 5
    score = 0

    for i in range(n):
        x = random.randint(2, 9)
        y = random.randint(1, 9)
        ans = int(input("{} * {} = ?".format(x, y)))
        if ans == x * y:
            score += 1
            print("정답입니다.")
        else:
            print("틀렸습니다.")
    print("점수는 {:.0f}점입니다.".format(100 * score / n))


if __name__ == "__main__":
    main()
