def is_leap_year(y) :
    if y % 4 == 0 :
        if y % 100 == 0 :
            year1 = "False"
        else :
            year1 = "True"
    else :
        year1 = "False"
    return year1

def main():
    year = int(input("윤년입니까? => "))
    print("{}" .format(is_leap_year(year)))

if __name__ == "__main__" :
    main()