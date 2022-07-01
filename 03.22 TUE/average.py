def average(nums) :
# total = 0
   # for n in range :
        #total_num = total + x[n]
    #return total_num
    total = (nums) / 4
    return total


def main():
    x1 = int(input("x1을 입력하세요 =>"))
    x2 = int(input("x2을 입력하세요 =>"))
    x3 = int(input("x3을 입력하세요 =>"))
    x4 = int(input("x4을 입력하세요 =>"))
    print("입력하신 숫자들의 평균은 {} 입니다." .format(average(x1+x2+x3+x4)))

if __name__ == "__main__" :
    main()