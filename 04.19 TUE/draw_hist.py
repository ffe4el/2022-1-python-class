import matplotlib.pyplot as plt
import numpy as np


def main():
    plt.rcParams['font.family'] = ['NanumGothic', 'sans-serif']
    plt.rcParams['axes.unicode_minus'] = False

    dices = np.random.randint(1, 7, size=100) #7은 안들어감(주사위는 눈이 6개까지) numpy랑 random의 함수는 살짝 다름.

    print(dices)

    plt.hist(dices, bins=6, color="b")
    plt.show()


if __name__ == "__main__":
    main()
