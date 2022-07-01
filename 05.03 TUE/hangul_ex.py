# 초성 리스트. 00 ~ 18
CHOSUNG_LIST = ['ㄱ', 'ㄲ', 'ㄴ', 'ㄷ', 'ㄸ', 'ㄹ', 'ㅁ', 'ㅂ', 'ㅃ', 'ㅅ', 'ㅆ', 'ㅇ', 'ㅈ', 'ㅉ', 'ㅊ', 'ㅋ', 'ㅌ', 'ㅍ', 'ㅎ']
# 중성 리스트. 00 ~ 20
JUNGSUNG_LIST = ['ㅏ', 'ㅐ', 'ㅑ', 'ㅒ', 'ㅓ', 'ㅔ', 'ㅕ', 'ㅖ', 'ㅗ', 'ㅘ', 'ㅙ', 'ㅚ', 'ㅛ', 'ㅜ', 'ㅝ', 'ㅞ', 'ㅟ', 'ㅠ', 'ㅡ', 'ㅢ',
                 'ㅣ']
# 종성 리스트. 00 ~ 27 + 1(1개 없음)
JONGSUNG_LIST = [' ', 'ㄱ', 'ㄲ', 'ㄳ', 'ㄴ', 'ㄵ', 'ㄶ', 'ㄷ', 'ㄹ', 'ㄺ', 'ㄻ', 'ㄼ', 'ㄽ', 'ㄾ', 'ㄿ', 'ㅀ', 'ㅁ', 'ㅂ', 'ㅄ', 'ㅅ',
                 'ㅆ', 'ㅇ', 'ㅈ', 'ㅊ', 'ㅋ', 'ㅌ', 'ㅍ', 'ㅎ']


def korean_to_be_englished(korean_word):
    r_lst = []
    for w in list(korean_word.strip()):
        # 영어인 경우 구분해서 작성함.
        if '가' <= w <= '힣':
            # 588(21 * 28)개 마다 초성이 바뀜.
            ch1 = (ord(w) - ord('가')) // (21 * 28)
            # 중성은 총 28가지 종류
            ch2 = ((ord(w) - ord('가')) % (21 * 28)) // 28
            ch3 = (ord(w) - ord('가')) % 28
            r_lst.append([CHOSUNG_LIST[ch1], JUNGSUNG_LIST[ch2], JONGSUNG_LIST[ch3]])
        else:
            r_lst.append([w])
    return r_lst

def korean_word_to_initials(korean_word):
    """
    한글을 입력받아서 한글 초성에 따라서 이니셜로 변환해줍니다.
    한국 성의 경우 조금 다르게 변환되는데 '박' ==> 'Park'인 부분은 반영하지 않음
    """
    w_to_k = {'ㄱ':'K', 'ㄲ':'G', 'ㄴ':'N', 'ㄷ':'D', 'ㄸ':'D', 'ㄹ':'R', 'ㅁ':'M', 'ㅂ':'B',
    'ㅃ':'B', 'ㅅ':'S', 'ㅈ':'J', 'ㅉ':'J', 'ㅊ':'C', 'ㅌ':'T', 'ㅍ':'P', 'ㅎ':'H'}
    r_lst = []
    for i, w in enumerate(korean_to_be_englished(korean_word)):
        if w[0] in w_to_k.keys():
            r_lst.append( w_to_k[w[0]] )
        else:
            if w[1] in ['ㅑ', 'ㅕ', 'ㅛ', 'ㅠ', 'ㅖ']:
                r_lst.append('Y')



def main():
    print(korean_to_be_englished("김철수a"))


if __name__ == "__main__":
    main()
