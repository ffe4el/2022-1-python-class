def is_leap_year(y):
    if y % 4 ==0 and y%100 != 0:
            # !=는 ~가 아니라 이말이야
            return True
    return False

