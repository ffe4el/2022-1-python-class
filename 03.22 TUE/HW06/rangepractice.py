def range_list(n):
    return list(range(1,n+1))

def main():
    num = int(input("숫자를 입력하세요. => "))
    print(range_list(num))

if __name__ == "__main__" :
    main()