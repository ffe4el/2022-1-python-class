def main():
    eng_text = "Hello, World!"

    ascii_list = []
    for letter in eng_text: #한글자씩 띠어서 보여준다.
        print(letter)
        ascii_list.append(ord(letter))

    print(ascii_list)

    print(ord("A"))
    print(ord("a"))


if __name__ == "__main__":
    main()
