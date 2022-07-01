def main():
    numbers = []

    while True :
        num = int(input("숫자 입력 = ?"))
        if num< 0 :
            break
        numbers.append(num)

    print(numbers)

if __name__ == "__main__" :
    main()