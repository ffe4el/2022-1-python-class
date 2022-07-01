import hw11_submission
def find_tmin(dates, tmin):
    length = len(dates)
    for i in range(length) :
        if tmin[i] == min(tmin) :
            p = i
    return dates[p], min(tmin)

def find_tmax(dates, tmax):
    length = len(dates)
    for i in range(length) :
        if tmax[i] == max(tmax) :
            p = i
    return dates[p] , max(tmax)


def main():
    f = open("ta_20220407110548.csv.csv")
    lines = f.readlines()
    # print(lines)
    tmax = [float(x.split(",")[4]) for x in lines[1:]]
    tmin = [float(x.split(",")[3]) for x in lines[1:]]
    tavg = [float(x.split(",")[2]) for x in lines[1:]]
    location = [(x.split(",")[1]) for x in lines[1:]]
    dates = [(x.split(",")[0]) for x in lines[1:]]
    print("관측이래 최저기온은 {}에 나타났고 {} 입니다." .format(*find_tmin(dates, tmin)))
    print("관측이래 최저기온은 {}에 나타났고 {} 입니다.".format(*find_tmax(dates, tmax)))
    # print(min(tmin))
    # print(max(tmax))
    # print(dates)
    hw11_submission.submit(
        "김솔아", "2018-08-13", 38.9, "1933-01-27", -17.1
    )

if __name__ == "__main__" :
    main()