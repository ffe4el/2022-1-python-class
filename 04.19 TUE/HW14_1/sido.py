import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from copy import deepcopy

# 시각화 설정
from pandas._testing import loc

sns.set_context("talk")
sns.set_style("white")

# Linux 한글 사용 설정
plt.rcParams['font.family']=['NanumGothic', 'sans-serif']
plt.rcParams['axes.unicode_minus'] = False

#다운로드 받은 파일을 파이썬으로 연다.
df_popkr = pd.read_csv("202203_202203_연령별인구현황_월간.csv", encoding="euc-kr")
df_popkr.head()

#행정구역에서 불필요한 번호를 떼어낸다.
df_popkr["행정구역"] = df_popkr["행정구역"].str.split("(").str[0]
df_popkr.head()

df_popkr.replace(",", "", regex=True, inplace=True)
df_popkr.replace(" ", "", regex=True, inplace=True)
df_popkr.head()
#행정구역에서 번호가 떨어진 뒤에 빈칸이 붙어있고,
#숫자들 사이에는 자리수를 표현하는 쉼표가 붙어있다. -> df.replace()로 처리함.

df_popkrM = df_popkr.filter(like="남").filter(like="세")
df_popkrM.head()
#남성과 여성 데이터를 따로 그리기 위해 컬럼명에 "남"이 있는 것들을 골라낸다.
#그중에서도 불피요한 내용을 제거하기 위해 "세"가 있는것만 또 따로 분리한다.

#행-열 전환
#데이터를 편하게 다루려면 열에 지역명, 행에 나이대를 놓는 것이 좋다.
#df.T로 행과 열을 바꾼 뒤 df.astype(int)로 정수형으로 변환합니다
df_popkrMT = df_popkrM.T
df_popkrMT.columns = df_popkr["행정구역"].values
df_popkrMT = df_popkrMT.astype(int)
df_popkrMT.head()

# 나이 정보가 index로 오긴 했지만 불필요한 정보들이 많습니다.
# pd.Series.str.split()을 사용해 나이만 남깁니다.
df_popkrMT["나이"] = df_popkrMT.index.str.split("_").str[2]
df_popkrMT.reset_index(drop=True, inplace=True)
df_popkrMT

# 여성 데이터도 위와 동일하게 정리
df_popkrF = df_popkr.filter(like="여").filter(like="세")
df_popkrFT = df_popkrF.T
df_popkrFT.columns = df_popkr["행정구역"].values
df_popkrFT = df_popkrFT.astype(int)
df_popkrFT["나이"] = df_popkrFT.index.str.split("_").str[2]
df_popkrFT.reset_index(drop=True, inplace=True)
df_popkrFT.head(3)

# 성별, 연령별 인구 분포는 많이 사용하는 형식이 있습니다.
# 등을 맞대고 있는 구도로 남 vs 여를 표현합니다.
# bar plot으로 해당 구간의 데이터에 집중합니다.

# plt.subplots()명령으로 fig(Figure)와 axs(Axes)를 동시에 생성합니다.
# ncols=2로 bar plot이 들어갈 Axes를 두 개 만듭니다.
# gridspec_kw={"wspace":0}으로 Axes 사이 간격을 없앱니다.
# sharey=True로 두 Axes의 y 범위를 통일합니다.
# fig, axs = plt.subplots(ncols=2, sharey=True,
#                         figsize=(10, 5), gridspec_kw={"wspace":0})

# ax.barh()명령으로 가로 bar plot을 그립니다.
# x에 나이, y에 전국 인구 수를 넣습니다.
# 남성은 green, 여성은 darkorange로 표현합니다.
# fig, axs = plt.subplots(ncols=2, sharey=True, figsize=(10, 5), gridspec_kw={"wspace":0})
# axs[0].barh(df_popkrMT["나이"], df_popkrMT["전국"], color="green")
# axs[1].barh(df_popkrFT["나이"], df_popkrFT["전국"], color="darkorange")

# 남성좌우반전
# 데이터 범위의 최대값xmax을 충분히 큰 수로 지정하고,
# 남성은 xmax에서 0으로, 여성은 0에서 xmax로 가도록 지정합니다.
# ax.set_xlim()을 사용합니다.
# fig, axs = plt.subplots(ncols=2, sharey=True, figsize=(10, 5), gridspec_kw={"wspace":0})
# axs[0].barh(df_popkrMT["나이"], df_popkrMT["전국"], color="green")
# axs[1].barh(df_popkrFT["나이"], df_popkrFT["전국"], color="darkorange")
# xmax = 4.5e6
# axs[0].set_xlim(xmax, 0)
# axs[1].set_xlim(0, xmax)

# x축 눈금 레이블 수정
# xticks = np.arange(0, xmax, 1e6)
# for ax, title in zip(axs, ["남성", "여성"]):
#     ax.set_xticks(xticks)
#     ax.set_xticklabels([f"{int(x*1e-6)}백만" if x != 0 else "0" for x in xticks])
#     # 정량적인 비교를 돕기 위해 grid추가, 남녀 title 추가
#     # 제목은 ax.set_title(), 눈금은 ax.grid()명령입니다
#     ax.grid(c="lightgray")
#     ax.set_title(title, color="gray", fontweight="bold", pad=16)

# bar plot은 Matplotlib이 patch라는 객체로 관리합니다.
# ax.patches[0]이라면 맨 처음에 붙인 객체를 의미합니다.
# ax.patches와 for loop을 결합하면 하나씩 순회하면서 숫자를 달아봅시다.
# for ax in axs:
#     for i, p in enumerate(ax.patches):
#         w = p.get_width()
#         ax.text(w, i, f" {format(w, ',')} ", #ax.text()명령으로 글자를 넣을 수 있습니다.
#                 fontsize="x-small", va="center", ha="right")
# 2중 for loop으로 Axes마다, patch마다 숫자를 달았습니다.
# ax.patch에 .get_width()를 적용해서 위치를 구했습니다.
# format()으로 천 단위마다 쉼표를 추가했고, ha=”right”로 우측 정렬을 했습니다.
# 그런데 여성 데이터마저 우측 정렬이 되어버렸습니다. if를 사용해 여성은 좌측 정렬을 합니다.


# fig, axs = plt.subplots(ncols=2, sharey=True, figsize=(10, 5), gridspec_kw={"wspace": 0})
# axs[0].barh(df_popkrMT["나이"], df_popkrMT["전국"], color="green")
# axs[1].barh(df_popkrFT["나이"], df_popkrFT["전국"], color="darkorange")
#
# xmax = 6e6 ??????????
# axs[0].set_xlim(xmax, 0)
# axs[1].set_xlim(0, xmax)
#
# xticks = np.arange(0, xmax, 1e6)
# for ax, title in zip(axs, ["남성", "여성"]):
#     ax.set_xticks(xticks)
#     ax.set_xticklabels([f"{int(x * 1e-6)}백만" if x != 0 else "0" for x in xticks])
#     ax.grid(c="lightgray")
#     ax.set_title(title, color="gray", fontweight="bold", pad=16)

# for ax in axs:
#     for i, p in enumerate(ax.patches):
#         w = p.get_width()
#         if ax == axs[0]:
#             ha = "right"
#         else:
#             ha = "left"
#
#         ax.text(w, i, f" {format(w, ',')} ",
#                 fontsize="x-small", va="center", ha=ha)
def plot_pop(loc, popmax, poptick):
    fig, axs = plt.subplots(ncols=2, sharey=True, figsize=(10, 5), gridspec_kw={"wspace": 0})

    c_M = "indigo"
    c_F = "salmon"
    axs[0].barh(df_popkrMT["나이"], df_popkrMT[loc], color=c_M)
    axs[1].barh(df_popkrFT["나이"], df_popkrFT[loc], color=c_F)

    axs[0].set_xlim(popmax, 0)
    axs[1].set_xlim(0, popmax)

    xticks = np.arange(0, popmax, poptick)
    if poptick >= 1e6:
        factor, unit = 1e-6, "백만"
    elif 1e5 <= poptick < 1e6:
        factor, unit = 1e-5, "십만"
    elif 1e4 <= poptick < 2e5:
        factor, unit = 1e-4, "만"
    elif 1e3 <= poptick < 2e4:
        factor, unit = 1e-3, "천"

    for ax, title in zip(axs, ["남성", "여성"]):
        ax.set_xticks(xticks)
        ax.set_xticklabels([f"{int(x * factor)}{unit}" if x != 0 else "0" for x in xticks])
        ax.grid(axis="x", c="lightgray")
        ax.set_title(title, color="gray", fontweight="bold", pad=16)

    for ax in axs:
        for i, p in enumerate(ax.patches):
            w = p.get_width()
            if ax == axs[0]:
                ha = "right"
                c = c_M
            else:
                ha = "left"
                c = c_F

            ax.text(w, i, f" {format(w, ',')} ",
                    c=c, fontsize="x-small", va="center", ha=ha,
                    fontweight="bold", alpha=0.5)

    fig.suptitle(f"                 {loc}", fontweight="bold")
    fig.tight_layout()

    return fig
#
def main():
#   print("1.전라북도 2.전주시 3.군산시 4.익산시 5.정읍시 6.남원시 7.김제시 8.완주군 9.진안군\n10.무주군 11.장수군 12.임실군 13.순창군 14.고창군 15.부안군")
    loc = str(input("찾을 지역을 설정해주세요."))
    if loc == "전라북도" :
        popmax=2e5
        poptick=5e4
    elif loc == "전라북도전주시":
        popmax=1e5
        poptick=2e4
    elif loc == "전라북도전주시덕진구" or loc =="전라북도전주시완산구" or loc =="전라북도군산시" or loc =="전라북도익산시":
        popmax = 3.5e4
        poptick = 5e3
    elif loc =="전라북도남원시" or loc =="전라북도김제시" or loc =="전라북도완주군":
        popmax=1e4
        poptick=2e3
    elif loc == "전라북도정읍시":
        popmax=1.2e4
        poptick=2e3
    elif loc == "전라북도진안군" or loc =="전라북도무주군" or loc =="전라북도장수군" or loc =="전라북도임실군" or loc =="전라북도순창군" :
        popmax=4e3
        poptick=1e3
    elif loc == "전라북도고창군" or loc == "전라북도부안군" :
        popmax=6e3
        poptick=1e3

    fig = plot_pop(loc, popmax, poptick)
    plt.show()




if __name__ == "__main__":
    main()





