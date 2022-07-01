import tkinter as tk

def main():
    window = tk.Tk()
    label = tk.Label(text="Name")
    entry = tk.Entry() #입력을 받는다.
    btn = tk.Button(text="입력", command=lambda : print(entry.get())) #입력을 받으면 입력받은 값을 출력한다.
    label.pack()
    entry.pack()
    btn.pack()

    window.mainloop()

if __name__ == "__main__":
    main()