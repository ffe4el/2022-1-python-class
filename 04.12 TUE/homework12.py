def read_data(filename) -> (List[str], List[float], List[float]):
    """기상자료를 읽어서 날짜, 최저기온, 최고기온 리스트를 리턴한다."""
    date_list = []
    tmin_list = []
    tmax_list = []
    with open (filename) as f:
        lines = f.readlines()
        for line in lines[8:] :
            line = line.strip()
            if line == "" :
                continue

            tokens = line.split(",")
            date_list.append(tokens[0])
            if tokens[3] == "":
            # tokens[3] = tmin
                tmin = 999
            else:
                tmin = float(tokens[3])
            if tokens[4] == "" :
                tmax = -999
            else:
                tmax = float(tokens[4])
            tmin_list.append(tmin)
            tmax_list.append(tmax)
    return date_list, tmin_list, tmax_list


def main():
    #1) 데이터 구해오기(기상청)
    filename =