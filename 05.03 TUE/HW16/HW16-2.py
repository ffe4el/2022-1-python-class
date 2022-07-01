def caesar_encode(text: str, shift: int) -> str:
    ascii_list = []
    for letter in text:
        ascii_list.append(ord(letter))
    ch_ascii_list = []
    for i in range(len(ascii_list)):
        if 65 <= ascii_list[i] <= 87:
            ch_ascii_list.append(chr(ascii_list[i]+shift))
        elif 88 <= ascii_list[i] <= 90:
            ch_ascii_list.append(chr(ascii_list[i]-20-shift))
        elif 97 <= ascii_list[i] <= 119:
            ch_ascii_list.append(chr(ascii_list[i]+shift))
        elif 120 <= ascii_list[i] <= 122:
            ch_ascii_list.append(chr(ascii_list[i]-20-shift))

    return ch_ascii_list

def caesar_decode(text: str, shift: int) -> str:
    ascii_list = []
    for letter in text:
        ascii_list.append(ord(letter))
    ch_ascii_list1 = []
    for i in range(len(ascii_list)):
        if 68 <= ascii_list[i] <= 90:
            ch_ascii_list1.append(chr(ascii_list[i]-shift))
        elif 65 <= ascii_list[i] <= 67:
            ch_ascii_list1.append(chr(ascii_list[i]+20+shift))
        elif 100 <= ascii_list[i] <= 122:
            ch_ascii_list1.append(chr(ascii_list[i]-shift))
        elif 97 <= ascii_list[i] <= 99:
            ch_ascii_list1.append(chr(ascii_list[i]+20+shift))
    return ch_ascii_list1

def main():
    text = str(input("암호를 입력하시오.=> "))
    string = caesar_encode(text, 3)
    print("result_encoding =>","".join(string))
    string = caesar_decode(text, 3)
    print("result_decoding =>","".join(string))

if __name__ == "__main__":
    main()