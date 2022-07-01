import time
import winsound


def read_input():
    return 5


def beep():
    frequency = 2500  # Set Frequency To 2500 Hertz
    duration = 600  # Set Duration To 1000 ms == 1 second
    winsound.Beep(frequency, duration)


def main():
    # 몇초를 카운트 할지 시간 입력
    countdown_sec = read_input()

    # 주어진 시간에서 매 1초마다 시간이 1초씩 줄어들고,
    # 그때, 남은시간을 출력하고,
    # 시간이 0이 되면, 멈춘다.
    while countdown_sec > 0:
        min = countdown_sec // 60
        sec = countdown_sec % 60
        min, sec = divmod(countdown_sec, 60)
        print("\r남은 시간은 {:02d}:{:02d}".format(min, sec), end="")
        # 1초 쉬고
        time.sleep(1)
        countdown_sec -= 1

    # 0초가 되면 소리는 낸다.
    print("\r카운트다운이 끝났습니다.")
    beep()


if __name__ == "__main__":
    main()
