def toggle_text(text:str):
    ascii_list = []
    for letter in text:
        ascii_list.append(ord(letter))
    ch_ascii_list = []
    for i in range(len(ascii_list)):
        if 65 <= ascii_list[i] <= 90:
            ch_ascii_list.append(chr(ascii_list[i]+32))
        elif 97 <= ascii_list[i] <= 122:
            ch_ascii_list.append(chr(ascii_list[i]-32))

    return ch_ascii_list


def main():
    text = str(input("문자를 입력해주세요.=> "))
    string = toggle_text(text)
    print("".join(string))




if __name__ == "__main__":
    main()