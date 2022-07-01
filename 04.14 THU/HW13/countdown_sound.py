import time
import winsound

from playsound import playsound



def beep():
    frequency = 2500  # Set Frequency To 2500 Hertz
    duration = 500  # Set Duration To 1000 ms == 1 second
    winsound.Beep(frequency, duration)
    time.sleep(0.3)
    winsound.Beep(frequency, duration)

def read_input():
    num = int(input("시간을 입력하세요. => "))
    return num
    # for i in range(10) :
    #     time.sleep(1)
    #     print (i\n)

def main():
    # 몇초를 카운트 할지 시간입력 받아야함
    countdown_sec = read_input()
    # 주어진 시간에서 매 1초마다 시간이 1초씩 줄어들고
    # 그때 남은 시간을 출력하고
    # 시간이 0이 되면, 멈춘다
    while countdown_sec > 0:
        # min = countdown_sec // 60
        # sec = countdown_sec % 60
        min, sec = divmod(countdown_sec, 60)
        print("\r남은 시간은 {:02d}:{:02d} 입니다." .format(min, sec), end="")
        # 02를 쓰는 이유는 입력된 숫자가 한자리 수일때 십의자리수 자리에 0을 넣어주기 위함이다.
        # end를 써야지 \r과 함께 작동하여 출력값이 나오는 줄 수가 한개가 된다.
        # 1초 쉬고
        time.sleep(1)
        countdown_sec -= 1


    # 0초가 되면 소리를 낸다
    # beep()
    playsound("[IVE] 그 파트 (128 kbps).mp3") #이거 시도해봤는데, playsound 모듈을 만들어야되더라구요....
    print("\r카운트다운이 끝났습니다.")

if __name__ == "__main__":
    main()