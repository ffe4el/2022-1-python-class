import random

def get_lotto():
    lotto = []
    while len(lotto) < 6 :
        num = random.randint(1,45)
        if num not in lotto:
            lotto.append(num)
    return lotto



def main():
    p = int(input("몇번 시도하시겠습니까?  =>  "))
    # lotto = get_lotto()
    for i in range(p):
        print (get_lotto())


if __name__ == "__main__":
    main()