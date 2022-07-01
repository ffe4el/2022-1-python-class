#1) 총 강수량은? average 쓰기
#2) 강우 일수는? (1mm이상 온 날의 수)
from homeworkprac import download

def count_rain_days(rainfall):
    rain_days = 0
    for x in rainfall :
        if x > 0 :
            rain_days +=1
    return rain_days
    #return len([x for x in rainfall if x > 0]) -> 5줄을 1줄만에 표현가능

#3) 여름철(6월-8월) 총 강수량은?
def sumifs(rainfall, months, selected = [6,7,8]) :
    days = len(rainfall) #365
    total_rain = 0
    for i in range(days) :
        if months[i] in selected:
            total_rain += rainfall[i]
    return total_rain
    #return sum([x[1] for x in zip(months, rainfall) if x[0] in selected])

#4) 최장연속강우일수는?
def longest_rain_days(rainfall):
    rain_days = 0
    rain_days_list = []
    for rain in rainfall:
        if rain > 0 :
            rain_days += 1
        else : #rain = 0
            if rain_days > 0 :
                rain_days_list.append(rain_days)
            rain_days = 0
    # print(rain_days_list)
    return max(rain_days_list)

#5) 강우이벤트 중 최대 강수량은? 비가 연속으로 올 때, 하나의 강우 이벤트로 가정
def maximum_rainfall_event(rainfall):
    rain_days = 0
    rain_total = 0.0
    rain_days_list = []
    rain_total_list = []
    for rain in rainfall:
        if rain > 0 :
            rain_days += 1
            rain_total += rain
        else:
            if rain_days > 0 :
                rain_days_list.append(rain_days)
                rain_total_list.append(rain_total)
            rain_days = 0
            rain_total = 0
    if rain_days > 0 :
        rain_days_list.append(rain_days)
        rain_total_list.append(rain_total)

    return max(rain_total_list)


#6) 일교차가 가장 큰 날짜와 해당일자의 일교차 (최고기온과 최저기온 차이)
def maximum_temp_gap(dates, tmax, tmin):
    # tmax[0] - tmin[0] = temp_gap [0]
    # tmax[1] - tmin[1] = temp_gap [1] 만약 여기서 temp_gap[1]이 더 크다면 temp_gap_list에 넣고 temp_gap[0]은 버린다.
    # tmax[2] - tmin[2] = temp_gap [2] 만약 여기서 temp_gap[1]이 더 크다면 temp_gap_list에 넣고 temp_gap[2]은 버린다.
    # for i in range(365):
    #     temp_gap = tmax[i] - tmin[i]
    #
    # return temp_gap
    # dates_list = []
    # temp_gap_list = []
    # max_gap = 0
    # temp_gap = 0

    # for row in data :
    #     max_temp = float(row[3])
    #     min_temp = float(row[5])
    #     temp_gap = max_temp - (min_temp)

    # tmax[0] - tmin[0] = temp_gap [0]
    # tmax[1] - tmin[1] = temp_gap [1] 만약 여기서 temp_gap[1]이 더 크다면 temp_gap_list에 넣고 temp_gap[0]은 버린다.
    # tmax[2] - tmin[2] = temp_gap [2] 만약 여기서 temp_gap[1]이 더 크다면 temp_gap_list에 넣고 temp_gap[2]은 버린다.
    length = len(dates)
    temp_gap_list = []

    for i in range(length):
        temp_gap = tmax[i] - tmin[i]
        temp_gap_list.append(temp_gap)

        if temp_gap == max(temp_gap_list) :
            p = i

    return dates[p], max(temp_gap_list)

        # if temp_gap[i + 1] > temp_gap[i]:
        #     # p = temp_gap[i+1]
        #     # return p
        #     temp_gap_list.append(temp_gap)
        #     dates_list.append(dates[i + 1])
        # else:
        #     # p= temp_gap[i]
        #     # return p
        #     temp_gap_list.append(temp_gap)
        #     dates_list.append(dates[i])
        #     temp_gap = 0

    # print(dates)
    # return dates[i], max(temp_gap_list)
    # return 0
# 타학생 6번 답
#     day = len(dates)
#     t_gap = [tmax[i] - tmin[i] for i in range(day)]
#     return dates[t_gap.index(max(t_gap))], max(t_gap)

#교수님 답
    # no_of_days = len(dates)
    # max_tgap = -1
    # max_date = None
    # for i in range(no_of_days):
    #     tgap = tmax[i] - tmin[i]
    #     if tgap> max_tgap :
    #         max_tgap = tgap
    #         max_date = dates[i]
    # return max_date, max_tgap


#7) 적산온도
def gdd(dates, tavg):
    length = len(dates)
    tavg_list = []

    # dates[1] = 5,6,7,8,9
    for i in range(length):
        if dates[i][1] in [5,6,7,8,9]:
            if tavg[i] >= 5 :
                tavg_js = (tavg[i] - 5)
                tavg_list.append(tavg_js)


    return sum(tavg_list)







def main():
    filename = "./code.weather(146)_2020-2020.csv"
    download(filename)
    f = open(filename)
    lines = f.readlines()
    print(lines)
    # data = csv.reader(f)
    rainfall = [float(x.split(",")[9]) for x in lines[1:]]
    tmax = [float(x.split(",")[3]) for x in lines[1:]]
    tavg = [float(x.split(",")[4]) for x in lines[1:]]
    tmin = [float(x.split(",")[5]) for x in lines[1:]]
    months = [int(x.split(",")[1]) for x in lines[1:]]
    dates = [[int(x.split(",")[0]), int(x.split(",")[1]), int(x.split(",")[2])] for x in lines[1:]]
    # print(rainfall)
    #총 강수량
    print("총 강수량은 {:.1f}mm 입니다." .format(sum(rainfall)))
    print("연 평균 기온 {} 입니다." .format(sum(tavg)/len(tavg)))
    print("총 강우일수는 {:d} 입니다." .format(count_rain_days(rainfall)))
    print("여름철(6~8월) 총 강수량은 {:.1f}mm 입니다." .format(sumifs(rainfall, months,[6,7,8])))
    print("최장연속강우일수 : {:d} 일 입니다." .format(longest_rain_days(rainfall)))
    print("강우이벤트 중 최대 강수량은 {:.1f} mm 입니다." .format(maximum_rainfall_event(rainfall)))
    print("일교차가 가장 큰 날짜 : {}, 일교차 : {:.1f}" .format(maximum_temp_gap(dates, tmax, tmin)[0], maximum_temp_gap(dates, tmax, tmin)[1]))
    # print("{}" .format(maximum_temp_gap(dates, tmax, tmin)))
    print("적선온도는 {:.1f} degree-days" .format(gdd(dates, tavg)))

    # print(maximum_temp_gap(dates,tmax,tmin))
    # print(tmax)
    # print(tmin)
    # print(dates)
    # print(dates[31])
    # print(tmax[1]-tmin[1])
    # print(tavg)
    # print(dates[1])

if __name__ == "__main__" :
    main()
