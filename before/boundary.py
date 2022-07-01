x = int(input("점A의 x좌표를 입력하세요."))
y = int(input("점A의 y좌표를 입력하세요."))

if x > 0 and y > 0 :
    print("점A는 제 1사분면에 위치합니다.")
if x < 0 and y > 0 :
    print("점A는 제 2사분면에 위치합니다.")
if x < 0 and y <0 :
    print("점A는 제 3사분면에 위치합니다.")
if x > 0 and y < 0 :
    print("점A는 제 4사분면에 위치합니다.")
if x==0 or y==0 :
    print("점A는 좌표축에 위치합니다.")