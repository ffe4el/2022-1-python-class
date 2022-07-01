def range_list(n):
    results = []
    for i in range(n):
        results.append(i+1)
    return results

# def range_list(n):
#   return [x for x in range(1,n+1)]
# ctrl+/하면 #처리된다.

def main():
    num = int(input("숫자를 입력하세요. => "))
    print(range_list(num))
if __name__ == "__main__" :
    main()