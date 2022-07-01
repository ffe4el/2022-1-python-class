
for i in range (10):
    print(i+1)

total = 0
for i in range(100):
    total = total + (i+1)
print(total)

#함수 사용
print(sum(range(1, 11)))

def Hello(name) :
    print("{} 님 안녕하세요.".format(name))

Hello("김솔아")