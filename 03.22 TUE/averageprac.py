def average(nums) :
    return  sum(nums) / len(nums)


def main():
    nums = [1,2,3,4,5,6,7,8,9,10]
    print("숫자 리스트의 평균은 {:.1f} 입니다.".format(average(nums)))


if __name__ == "__main__" :
    main()