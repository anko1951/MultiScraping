import tkinter as tk

def btn_click():
    txt = entry.get()
    btn['text'] = txt

root = tk.Tk()
root.title('MultiScraping')
root.geometry('800x600')
entry = tk.Entry(width=100)
entry.place(x=100,y=50)
root.mainloop()
