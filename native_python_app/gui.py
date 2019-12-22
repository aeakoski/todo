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
        self.brain = brain
        self.frame = tk.Frame(self.master)
        self.master.bind("n", self.new_task)
        self.master.bind("t", self.new_task)
        self.master.bind("q", self.quit)
        self.master.bind("<Escape>", self.quit)
        self.master.bind("<Delete>", self.remove)
        self.frame.pack()
        self.button1 = tk.Button(self.frame, text = 'New Task', width = 50, command = self.new_task)
        self.button1.pack()
        self.listboxes = []
        self.active_listbox = None
        self.initListbox()

    def set_active_listbox(self, n):
        self.active_listbox = n
    def remove(self, event = None):
        if self.active_listbox == None:
            return
        a = self.listboxes[self.active_listbox].curselection()
        #print(self.listboxes[self.active_listbox].curselection())
        try:
            self.brain.remove_from_list(self.listboxes[self.active_listbox].curselection()[0], self.active_listbox)
            self.listboxes[self.active_listbox].delete(self.listboxes[self.active_listbox].curselection())
        except IndexError:
            return

    def new_task(self, _event = None):
        self.newTask = tk.Toplevel(self.master)
        self.app = Demo2(self.newTask, self)

    def initListbox(self):
        inx = 0
        for tl in self.brain.getLists():
            w = tk.Label(self.master, text=tl.short)
            w.pack()
            lbox = DragDropListbox(self.master, width=45, selectmode=tk.BROWSE)
            b = inx
            for t in tl.tasks:
                print(t.short)
                lbox.insert("end", str(t.short))
            lbox.pack()
            self.listboxes.append(lbox)
            lbox.bind('<<ListboxSelect>>',lambda x, _inx = inx : self.set_active_listbox(_inx))
            inx += 1

    def addToListbox(self, short):
        self.brain.add(short)
        self.listboxes[0].insert("end", str(short))
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
        self.other.addToListbox(short)
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
