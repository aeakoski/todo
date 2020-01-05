# -*- coding: utf-8 -*-
import os
try:
    import Tkinter as tk # Tkinter for python 2
except ImportError:
    import tkinter as tk # tkinter for python 3

from Task import Task
from TaskList import TaskList
from gui import *
from Brain import Brain
def main():

    brain = Brain()
    brain.restoreSession()
    root = tk.Tk()
    app = View_todo(root, brain)
    root.mainloop()

main()
