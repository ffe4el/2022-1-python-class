def minmax(nums):
    return min(nums), max(nums)

def main():
    x = [1,2,3,4,5]
    mn, mx = minmax(x)
    print("가장 작은 숫자는 {} 이고, 가장 큰 숫자는 {}입니다." .format(mn, mx))

if __name__=="__main__":
    main()
