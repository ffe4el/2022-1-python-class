import matplotlib.pyplot as plt
import numpy as np
def main():
    plt.rcParams['font.family'] = ['NanumGothic', 'sans-serif']
    plt.rcParams['axes.unicode_minus'] = False
    tmax = np.random.rand(30) * 15 + 15
    tmin = tmax - (np.random.rand(30) * 5 + 5)
    plt.plot(tmax, "r^", label="최고기온") #colored="r"하면 선으로 빨강색이 나옴!
    plt.plot(tmin, "b", label="최저기온")
    plt.ylabel("기온(℃)")
    plt.legend() #자동으로 빈칸에 범례를 넣어줌
    plt.show()
    # plt.savefig("./line_temp.png")
if __name__ == "__main__":
    main()
