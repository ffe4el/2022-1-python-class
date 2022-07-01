import random
import tkinter as tk
from tkinter import simpledialog



def gui_input(text:str)->str:
    return simpledialog.askstring(title="CHOSUNGGAME", prompt=text)

# 초성 리스트. 00 ~ 18
CHOSUNG_LIST = ['ㄱ', 'ㄲ', 'ㄴ', 'ㄷ', 'ㄸ', 'ㄹ', 'ㅁ', 'ㅂ', 'ㅃ', 'ㅅ', 'ㅆ', 'ㅇ', 'ㅈ', 'ㅉ', 'ㅊ', 'ㅋ', 'ㅌ', 'ㅍ', 'ㅎ']
# 중성 리스트. 00 ~ 20
JUNGSUNG_LIST = ['ㅏ', 'ㅐ', 'ㅑ', 'ㅒ', 'ㅓ', 'ㅔ', 'ㅕ', 'ㅖ', 'ㅗ', 'ㅘ', 'ㅙ', 'ㅚ', 'ㅛ', 'ㅜ', 'ㅝ', 'ㅞ', 'ㅟ', 'ㅠ', 'ㅡ', 'ㅢ',
                 'ㅣ']
# 종성 리스트. 00 ~ 27 + 1(1개 없음)
JONGSUNG_LIST = [' ', 'ㄱ', 'ㄲ', 'ㄳ', 'ㄴ', 'ㄵ', 'ㄶ', 'ㄷ', 'ㄹ', 'ㄺ', 'ㄻ', 'ㄼ', 'ㄽ', 'ㄾ', 'ㄿ', 'ㅀ', 'ㅁ', 'ㅂ', 'ㅄ', 'ㅅ',
                 'ㅆ', 'ㅇ', 'ㅈ', 'ㅊ', 'ㅋ', 'ㅌ', 'ㅍ', 'ㅎ']

def game(korean_word_list):
    total = 0
    while len(korean_word_list) > 0:
        r_lst = []
        choose_word = random.choice(korean_word_list)

        if choose_word in korean_word_list:
            korean_word_list.remove(choose_word)
        for w in choose_word:
            # 영어인 경우 구분해서 작성함.
            if '가' <= w <= '힣':
                # 588(21 * 28)개 마다 초성이 바뀜.
                ch1 = (ord(w) - ord('가')) // (21 * 28)
                r_lst.append(CHOSUNG_LIST[ch1])
        print(r_lst)

        input_text = gui_input("단어를 입력하십시오. => ")
        if input_text == choose_word:
            total += 1
            print("딩동댕")
        elif input_text != choose_word:
            print("땡")
    print("최종점수는 {}점 입니다." .format(total))



def main():
    window = tk.Tk()
    window.withdraw()

    korean_word_list = ["바나나", "딸기", "멜론", "수박", "자몽", "블루베리"]
    print(game(korean_word_list))
    window.mainloop()


if __name__ == "__main__":
    main()