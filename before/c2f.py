def c2f(t_c) :
    t_f = (t_c) * (1.8) + 32
    return t_f
# return을 해줘야지 c2f 함수의 결과값으로 t_F가 출력되는 것임.
def main():
    t_c = int(input("섭씨를 입력하세요. => "))
    print("{} C => {} F" .format(t_c, c2f(t_c)))

if __name__ == '__main__':
    main()