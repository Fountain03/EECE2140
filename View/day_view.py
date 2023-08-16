from Model.day import Day
from Model.reminder import Reminder
import tkinter as tk


class DayView():

    def __init__(self, day) -> None:
        self.day = day
        self.page = tk.Toplevel()
        self.page.title('Daily View')
        self.page.geometry('500x300')

    def schedule(self):
        for t in self.day.tasks.values():
            self.task_list(t)

        self.page.mainloop()

    def task_list(self, task):
        def complete():
            if var.get() == 1:
                task.make_done()
            else:
                task.done == False
            self.day.update(task)

        var = tk.IntVar()
        f = tk.Frame(self.page)
        c = tk.Checkbutton(master=f, text='Completed', variable=var, onvalue=1, offvalue=0,
                           command=complete)
        c.pack(side=tk.LEFT)
        t = tk.Button(master=f, text=str(task))
        t.pack(side=tk.RIGHT)
        f.pack()
