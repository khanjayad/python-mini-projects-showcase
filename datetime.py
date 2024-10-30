import tkinter as tk
from time import strftime
print("codewithjack")
root = tk.Tk()
root.title("Digital Clock")
root.geometry("800x300")
def time():
    string = strftime('%H:%M:%S %p \n %A, %B %d, %Y')  
    label.config(text=string)  
    label.after(1000, time) 
label = tk.Label(root, font=('Times New Roman', 50, 'bold'), background='yellow', foreground='black')
label.pack(anchor='center')
close_button = tk.Button(root, text="Close", command=root.destroy, font=('Times New Roman', 15))
close_button.pack(pady=20)
time()
root.mainloop()
