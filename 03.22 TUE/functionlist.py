def largest(numbers):
    return max(numbers)

def main():
    x = [3, 7, 5 ,10, 15]
    print("가장 큰 수는 {}입니다." .format(largest(x)))

if __name__ == "__main__" :
    main()

print("-"*30)

def largest(numbers) :
    max_num = -1 #-1은 임의의 작은 숫자를 넣어준거임 total=0이랑 비슷한 개념
    for n in numbers:
        if max_num < n:
            max_num = n
    return max_num

def main():
    x = [3, 7, 5 ,10, 15] #리스트를 이용해서 numbers에 x의 리스트를 입력해주는거임
    print("가장 큰 수는 {}입니다." .format(largest(x)))

if __name__ == "__main__" :
    main()

