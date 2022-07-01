def main():
    numbers = []
    while True:
        try:

            num = input("x = ?")
            num = int(num)
            if int(num) > 0:
                numbers.append(num)
            if num == -1:
                break

        except ValueError:
            pass

    print(numbers)

if __name__ == "__main__":
    main()