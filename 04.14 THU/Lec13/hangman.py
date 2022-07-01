

def main():
    secret = "apple"
    answer = ["_"] * len(secret)    # 사용자가 입력한 답
    answer = ["_" for x in range(len(secret))]
    # print(answer)

    trials = 7

    while trials > 0:
        print(" ".join(answer))     # 현재 상태 출력 (예시: _ _ _ _ _ )
        letter = input("알파벳을 입력하세요 (남은 목숨: {})> ".format(trials))
        if letter in secret:
            for i in range(len(secret)):
                if letter == secret[i]:
                    answer[i] = letter
        else:
            trials -= 1
        # 입력한 글자가 포함되어 있으면, 빈줄을 입력한 값으로 바꾼다.
        # 입력한 글자가 포함되어 있지않으면, trials를 하나 줄인다.
        if "_" not in answer:
            break

    if trials > 0:
        print("축하합니다.")
    else:
        print("정답을 맞추지 못했습니다. 정답은 {}입니다.".format(secret))


if __name__ == "__main__":
    main()
