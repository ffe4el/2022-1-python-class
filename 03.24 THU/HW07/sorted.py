

def text2list(input_text):
    tokens = input_text.split()
    nums = []
    for token in tokens:
        nums.append(int(token))
    return nums

def average(nums):
    return sum(nums)/len(nums)

def median(nums):
    if len(nums) % 2 == 0:
        ian = len(nums) // 2
        med=nums[ian]
        return med
    else:
        ian = len(nums) // 2
        med=nums[ian]
        return med

def main():
    input_text = "1 2 3 4 5" # 3 4 5 7 10
    nums = text2list(input_text)
    nums = sorted(nums)
    print("주어진 리스트는" , nums)
    print("평균값은 {:.1f}" .format(average(nums)))
    print("중앙값은 {}" .format(median(nums)))

if __name__ == "__main__" :
    main()