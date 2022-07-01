import random

def main():
    list = ["apple", "lemon", "strawberry", "watermelon", "melon", "banana", "grape", "cucumber", "tomato"]
    p = random.choice(list)
    print ("답은 {} 입니다." .format(p))
    trial = int(len(p) + 1)
    print("*소문자만 입력해주세요")
    # answer = ["_"]*(len(p))
    answer = ["_" for x in range(len(p))]

    while trial > 0 :
        print("".join(answer)) #현재 상태 출력 (예시 : _ _ _ _ _)
        letter = (input("알파벳을 입력하세요 (남은 목숨 : {})   => " .format(trial)))
        if letter in p:
            for i in range(len(p)):
                if letter == p[i]:
                    answer[i] = letter
        else:
            trial -= 1

        if "_" not in answer:
            break
        #입력한 글자가 포함되어 있으면, 빈출을 입력한 값으로 바꾼다.
        #입력한 글자가 포함되어 있지 않으면 trials를 하나 줄인다.

    if trial > 0:
        print("축하합니다")
    else :
        print("정답을 맞추지 못했습니다. 정답은 {}입니다." .format(p))

if __name__ == "__main__" :
    main()