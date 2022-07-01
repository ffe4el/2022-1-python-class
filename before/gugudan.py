
def gugudan(dan) :

    for i in range(9) :
        p = i+1
        f = p * dan
        print("구구단을 외자! {} * {} = {:2d}" .format(dan, p, f))



if __name__ == "__main__":
    dan = int(input("구구단을 외자. 구구단을 외자. =>"))
    gugudan(dan)