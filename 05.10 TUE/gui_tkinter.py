import tkinter as tk



window = tk.Tk()
window.title("Temperature Converter")
window.resizable(width=False, height=False) #false면 크기 조정 불가!
frm_entry = tk.Frame(master=window)
ent_temperature = tk.Entry(master=frm_entry, width=10)
lbl_temp = tk.Label(master=frm_entry, text="\N{DEGREE FAHRENHEIT}")
ent_temperature.grid(row=0, column=0, sticky="e")
lbl_temp.grid(row=0, column=1, sticky="w")
btn_convert = tk.Button(
master=window,
text="\N{RIGHTWARDS BLACK ARROW}",
)


lbl_result = tk.Label(master=window, text="\N{DEGREE CELSIUS}")
frm_entry.grid(row=0, column=0, padx=10)

lbl_result.grid(row=0, column=2, padx=10)

def fahrenheit_to_celsius():
    """Convert the value for Fahrenheit to Celsius and insert the
    result into lbl_result.
    """
    fahrenheit = ent_temperature.get()
    celsius = (5 / 9) * (float(fahrenheit) - 32)
    lbl_result["text"] = f"{round(celsius, 2)} \N{DEGREE CELSIUS}"

btn_convert = tk.Button(
    master=window,
    text="\N{RIGHTWARDS BLACK ARROW}",
    command=fahrenheit_to_celsius
    )

btn_convert.grid(row=0, column=1, pady=10)

window.mainloop()
