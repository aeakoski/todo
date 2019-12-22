# -*- coding: utf-8 -*-
import sys
reload(sys)
sys.setdefaultencoding('utf8')

import Tkinter as tk # Tkinter for python 2
#import tkinter as tk # tkinter for python 3
from DragDropListbox import DragDropListbox
class Demo1:
    def __init__(self, master, brain):
        self.master = master
        self.master.configure(bg="#262A2F")
        self.master.title("Native tasks")
        self.brain = brain
        self.frame_top = tk.Frame(self.master, pady=15)
        self.frame_top.configure(bg="#262A2F")
        self.frame_top.pack()
        self.master.bind("n", self.new_task)
        self.master.bind("t", self.new_task)
        self.master.bind("q", self.quit)
        self.master.bind("<Escape>", self.quit)
        self.master.bind("<Delete>", self.remove)
        self.master.bind("<Tab>", self.clear_all)
        self.button1 = tk.Button(self.frame_top, text = 'New Task', width = 50, command = self.new_task)
        self.button1.configure(bg="#3E444F", fg="#DBDBDB", highlightbackground="#000000")
        self.button1.pack()
        self.listboxes = []
        self.active_listbox = None
        self.initListbox()

    def clear_all(self, event = None):
        for l in self.listboxes:
            l.select_clear(0, "end")

    def set_active_listbox(self, n):
        self.active_listbox = n

    def remove(self, event = None):
        if self.active_listbox == None:
            return
        #a = self.listboxes[self.active_listbox].curselection()
        #print(self.listboxes[self.active_listbox].curselection())
        try:
            self.brain.remove_from_list(self.listboxes[self.active_listbox].curselection()[0], self.active_listbox)
            self.listboxes[self.active_listbox].delete(self.listboxes[self.active_listbox].curselection())
        except IndexError:
            return

    def move_task_left(self, inx):
        if not self.listboxes[inx].curselection():
            return
        if 0 > inx-1:
            return
        try:
            a = self.listboxes[inx].curselection()[0]
        except IndexError:
            print(inx, self.active_listbox)
            return
        tsk = self.brain.getLists()[inx][a]
        self.brain.add_existing(tsk, inx-1)

        self.brain.remove_from_list(self.listboxes[inx].curselection()[0], inx)
        self.listboxes[inx].delete(self.listboxes[inx].curselection())

        self.listboxes[inx - 1].insert("end", tsk)


    def move_task_right(self, inx):
        if not self.listboxes[inx].curselection():
            return
        if inx+1 > len(self.brain.getLists())-1:
            return
        try:
            a = self.listboxes[inx].curselection()[0]
        except IndexError:
            print(inx, self.active_listbox)
            return
        tsk = self.brain.getLists()[inx][a]
        self.brain.add_existing(tsk, inx + 1)

        self.brain.remove_from_list(self.listboxes[inx].curselection()[0], inx)

        self.listboxes[inx].delete(self.listboxes[inx].curselection())
        self.listboxes[inx + 1].insert("end", tsk)

    def new_task(self, _event = None):
        self.newTask = tk.Toplevel(self.master)
        self.app = Demo2(self.newTask, self)

    def initListbox(self):
        inx = 0
        for tl in self.brain.getLists():
            lf = tk.Frame(self.master, padx=5, pady = 5)
            lf.configure(bg="#262A2F")
            lf.pack(fill=tk.Y, side=tk.LEFT)
            w = tk.Label(lf, text=str(tl))
            w.configure(bg="#262A2F", fg="#DBDBDB")
            w.pack()
            lbox = DragDropListbox(lf, self.brain, inx, height=25, width=45, selectmode=tk.BROWSE)
            lbox.configure(bg="#2C3037", fg="#DBDBDB", highlightcolor="#2C3037", highlightbackground="#000000")
            for t in tl.tasks:
                lbox.insert("end", t)
            lbox.pack(fill=tk.Y, expand=1)
            self.listboxes.append(lbox)
            lbox.bind('<<ListboxSelect>>',lambda x, _inx = inx : self.set_active_listbox(_inx))
            lbox.bind('<Right>', lambda x, _inx = inx : self.move_task_right(_inx))
            lbox.bind('<Left>', lambda x, _inx = inx : self.move_task_left(_inx))
            inx += 1

    def quit(self, event = None):
        self.master.destroy()


class Demo2:
    def __init__(self, master, other):
        self.master = master
        self.master.bind("<Escape>", self.quit)
        self.master.bind("<Return>", self.submit_task)
        self.other = other
        self.frame = tk.Frame(self.master)
        self.frame.pack()
        self.quitButton = tk.Button(self.frame, text = 'Ok', width = 25, command = self.submit_task)
        self.quitButton.pack()
        self.entry = tk.Entry(self.master)
        self.entry.pack()
        self.entry.focus()

    def submit_task(self, event = None):
        short = str(self.entry.get())
        self.other.brain.add_new(short, 0)
        self.other.listboxes[0].insert("end", self.other.brain.todo[-1])
        self.entry.delete(0, tk.END)
        self.master.destroy()

    def quit(self, event = None):
        self.master.destroy()
# def main():
#     root = tk.Tk()
#     app = Demo1(root)
#     root.mainloop()
#
# if __name__ == '__main__':
#     main()
