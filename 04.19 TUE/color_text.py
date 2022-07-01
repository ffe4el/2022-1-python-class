import termcolor


def main():
    print(termcolor.colored('Hello, World!', 'red', attrs=['reverse', 'blink']))
    print(termcolor.colored('Hello, World!', "grey", "on_cyan"))
    print(termcolor.colored('Hello, Universe!', "blue", "on_grey"))
    print(termcolor.colored('안녕하세요.', "red"))


if __name__ == "__main__":
    main()
