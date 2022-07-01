def sum_n(n):
    total = 0
    for i in range(n) :
        total = total + (i+1)
#    print(total)
    return total

def main():
    n = int(input("숫자를 입력하세요. => "))
    sum_n(n)

if __name__ == "__main__" :
    main()