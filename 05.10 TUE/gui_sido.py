import tkinter as tk

window = tk.Tk()
window.title("Caesar_Code")
window.resizable(width=False, height=False)  # false면 크기 조정 불가!
frm_entry = tk.Frame(master=window)
ent_code = tk.Entry(master=frm_entry, width=10)

lbl_code = tk.Label(master=frm_entry, text="caesar_code")
ent_code.grid(row=0, column=0, sticky="e")
lbl_code.grid(row=0, column=1, sticky="w")
btn_convert = tk.Button(
master=window,
text="\N{RIGHTWARDS BLACK ARROW}",
)

lbl_result = tk.Label(master=window, text="encoding") #출력나오는 라벨
frm_entry.grid(row=0, column=0, padx=10) #입력하는 칸 넓이
lbl_result.grid(row=0, column=2, padx=10) #출력나오는 칸 넓이


# text = str(input("암호를 입력하시오.=> "))
# string = caesar_encode(text, 3)
# print("result_encoding =>","".join(string))
# ent_code, shift=3

def caesar_encode(shift=3) -> str:
    ascii_list = []
    text = ent_code.get()
    for letter in text:
        ascii_list.append(ord(letter))
    ch_ascii_list = []
    for i in range(len(ascii_list)):
        if 65 <= ascii_list[i] <= 87:
            ch_ascii_list.append(chr(ascii_list[i] + shift))
        elif 88 <= ascii_list[i] <= 90:
            ch_ascii_list.append(chr(ascii_list[i] - 20 - shift))
        elif 97 <= ascii_list[i] <= 119:
            ch_ascii_list.append(chr(ascii_list[i] + shift))
        elif 120 <= ascii_list[i] <= 122:
            ch_ascii_list.append(chr(ascii_list[i] - 20 - shift))
    lbl_result["text"]= "".join(ch_ascii_list)

# def caesar_decode(text: str, shift=3) -> str:
#     ascii_list = []
#     for letter in text:
#         ascii_list.append(ord(letter))
#     ch_ascii_list1 = []
#     for i in range(len(ascii_list)):
#         if 68 <= ascii_list[i] <= 90:
#             ch_ascii_list1.append(chr(ascii_list[i]-shift))
#         elif 65 <= ascii_list[i] <= 67:
#             ch_ascii_list1.append(chr(ascii_list[i]+20+shift))
#         elif 100 <= ascii_list[i] <= 122:
#             ch_ascii_list1.append(chr(ascii_list[i]-shift))
#         elif 97 <= ascii_list[i] <= 99:
#             ch_ascii_list1.append(chr(ascii_list[i]+20+shift))
#     return ch_ascii_list1

btn_convert = tk.Button(
    master=window,
    text="\N{RIGHTWARDS BLACK ARROW}",
    command=caesar_encode
)
btn_convert.grid(row=0, column=1, pady=10)

def main():
    window.mainloop()



if __name__ == "__main__":
    main()