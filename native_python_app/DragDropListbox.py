
try:
    import Tkinter as tk # Tkinter for python 2
except ImportError:
    import tkinter as tk # tkinter for python 3

class DragDropListbox(tk.Listbox):
    """ A Tkinter listbox with drag'n'drop reordering of entries. """
    def __init__(self, master, brain, li, **kw):
        self.brain = brain
        self.made_change = False
        kw['selectmode'] = tk.SINGLE
        tk.Listbox.__init__(self, master, kw)
        self.list_inx = li
        self.bind('<Button-1>', self.setCurrent)
        self.bind('<B1-Motion>', self.shiftSelection)
        self.bind('<ButtonRelease-1>', self.investigate_change)
        self.curIndex = None
        self._bg = self['bg']
        # bind to focus events
        self.bind('<FocusIn>', self._on_focus)
        self.bind('<FocusOut>', self._on_lose_focus)


    def _on_focus(self, event):
        self.configure(bg="#30363F")

    def _on_lose_focus(self, event):
        self.configure(bg="#2C3037")

    def setCurrent(self, event):
        self.curIndex = self.nearest(event.y)

    def investigate_change(self, event):
        if not self.made_change:
            return
        self.brain.updateOrder(self.get(0,self.size()), self.list_inx)
        self.made_change = False

    def shiftSelection(self, event):
        i = self.nearest(event.y)
        if i < self.curIndex:
            self.made_change = True
            x = self.get(i)
            self.delete(i)
            self.insert(i+1, x)
            self.curIndex = i
        elif i > self.curIndex:
            self.made_change = True
            x = self.get(i)
            self.delete(i)
            self.insert(i-1, x)
            self.curIndex = i
