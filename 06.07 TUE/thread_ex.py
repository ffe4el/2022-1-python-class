import threading

def sum_range(low, high):
    total = 0
    for i in range(low, high):
        total += i
    print("Subthread", total)


#나중에 위에처럼 함수를 만들어 놓은다음에 밑에 3줄의 코드를 써서 쓰레드를 실행시키면 됨!
t = threading.Thread(target=sum_range, args=(1, 1_000_000))
t.start()
print("Main thread")
