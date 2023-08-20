import tkinter as tk


def clicked():
    b['text'] = 'you clicked me'


page = tk.Tk()
b = tk.Button(page, text='click me', command=clicked)
b.pack()

page.mainloop()
