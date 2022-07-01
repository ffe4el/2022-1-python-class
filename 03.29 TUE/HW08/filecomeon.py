def main():
    f = open('numberrr.txt')
    text = f.readlines()
    text = [int(x.strip()) for x in text]
    print(text)
    print(len(text))
    print(sum(text) / len(text))
    print(max(text))
    print(min(text))


if __name__ == "__main__" :
    main()