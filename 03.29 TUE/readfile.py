def text2list(input_text):
    tokens = input_text.split()
    nums = []
    for token in tokens:
        nums.append(int(token))
    return nums

def average(nums):
    return sum(nums)/len(nums)


def main():
    input_text = "1 3 5 7 9"
    #f = open('numbers1.txt')
    #input_text = f.readline().strip()
    f = open("numbers2.txt")
    lines = f.readlines()
    print(lines)
    nums = [int(x.strip()) for x in lines]
    print(nums)
    #print("AAA {} EEE" .format(input_text))
    #nums = text2list(input_text)
    #print("평균은?", average(nums))

    #nums = [int(x.strip()) for x in lines]
    nums = []
    for line in f :
        token = line.strip()
        nums.append(int(token))


if __name__ == "__main__" :
    main()