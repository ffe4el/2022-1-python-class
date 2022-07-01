import math

R = int(input("원의 반지름은 무엇입니까?"))
L = 2 * math.pi * R
S = math.pi * R ** 2

print("원의 둘레는 {:.1f} cm 이고 원의 면적은 {:.2f} cm^2 입니다." .format(L, S))
