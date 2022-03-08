import tkinter as tk
import random
def on_closing():
    pass
def Well():
    welc.pack_forget()
    ending.pack()
    win.update()
    win.after(3000, win.quit())
def gg():
    btn2.place(x=random.randint(20, 200), y=random.randint(20, 200))
x, y = 160, 120
win = tk.Tk()
win.protocol("WM_DELETE_WINDOW", on_closing)
win.title('Тест на дурачка')
win.geometry("200x300+860+340")
win.minsize(300, 300); win.maxsize(300, 300)
win.config(bg='#808080') #fg; font; padx; width; height; anchor; font; text; relief; justify
btn1 = tk.Button(win, text='да', cursor='gumby', height=1, width=10, bg='#000', font=('bold arial', 12), command=Well, fg='#fff')
btn1.place(x=40, y=120)
btn2 = tk.Button(win, text='нет', cursor='gumby', height=1, width=10, bg='#000', font=('bold arial', 12), command=gg, fg='#fff')
btn2.place(x=160, y=120)
ending = tk.Label(win, text='''Я знал :)''', width = 150, height=300, font='20')
welc = tk.Label(win, text='''Ты дурачек?''', width = 50, font='20')
welc.pack(pady=(10, 0))#; out.pack()
win.mainloop()