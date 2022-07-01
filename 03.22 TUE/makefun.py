def largest(a, b):
    if a > b :
        p = a
    if b > a :
        p = b
    return p

def main():
    x1 = 5
    x2 = 7
    print("가장 큰 수는 {}입니다." .format(largest(x1, x2)))

if __name__ == "__main__":
    main()

print("-"*30)



def largest(a,b,c) :
    if a<b:
        if b>c:
            return b
        else : return c

    else:
        if a>c:
            return a
        else:
            return c

def main ():
    x1 = 5
    x2 = 7
    x3 = 2
    print("가장 큰 수는 {}입니다." .format(largest(x1, x2, x3)))


if __name__ == "__main__":
    main()
