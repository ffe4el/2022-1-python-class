temp_f = int(input("온도를 입력해주세요."))
def f2c(temp_f):
    temp_c = (temp_f -32) / 1.8
    return temp_c
print("{}F => {}C 입니다." .format(temp_f, f2c(temp_f)))

def main():
    print("{:.1f}F => {:.1f}C" .format(temp_f, f2c(temp_f)))

if __name__=="__main__":
        main()


def add (x, y):
    return x+y
#print(add(3,4))
if __name__=="__main__":
    print(add(3,4))

