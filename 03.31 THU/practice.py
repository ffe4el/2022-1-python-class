dates_list = []
temp_gap_list = []
max_gap = 0
temp_gap = 0

# for row in data :
#     max_temp = float(row[3])
#     min_temp = float(row[5])
#     temp_gap = max_temp - (min_temp)

# tmax[0] - tmin[0] = temp_gap [0]
# tmax[1] - tmin[1] = temp_gap [1] 만약 여기서 temp_gap[1]이 더 크다면 temp_gap_list에 넣고 temp_gap[0]은 버린다.
# tmax[2] - tmin[2] = temp_gap [2] 만약 여기서 temp_gap[1]이 더 크다면 temp_gap_list에 넣고 temp_gap[2]은 버린다.
for i in range(364):
    temp_gap[i] = tmax[i] - tmin[i]

    if temp_gap[i + 1] > temp_gap[i]:
    # p = temp_gap[i+1]
    # return p
        temp_gap_list.append(temp_gap)
        dates_list.append(dates[i + 1])
    else:
    # p= temp_gap[i]
    # return p
        temp_gap_list.append(temp_gap)
        dates_list.append(dates[i])
        temp_gap = 0

# print(dates)
return dates_list, temp_gap_list
# return 0