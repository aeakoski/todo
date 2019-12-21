# -*- coding: utf-8 -*-
import os
import Tkinter as tk # Tkinter for python 2
#import tkinter as tk # tkinter for python 3

from Task import Task
from TaskList import TaskList
from gui import *
from Brain import Brain
def main():

    brain = Brain()
    #todo = TaskList("todo")
    #prog = TaskList("prog")
    #done = TaskList("done")

    #todo.readTasksFromFile()

    root = tk.Tk()
    app = Demo1(root, brain)
    root.mainloop()


    while False:
        print("1. View todo list")
        print("2. Add item")
        print("3. Remove item")
        choice = raw_input("Choice: ")

        try:
            choice = int(choice)
        except ValueError:
            print("Need to enter a number")
            continue

        if choice == 1:
            todo.printTasks()
        elif choice == 2:
            i = raw_input("Type todo here: ")
            todo.tasks.append(Task(i, "dd", len(todo.tasks)))
            todo.writeTodoTasksToFile()

        elif choice == 3:
            try:
                ir = int(raw_input("Position to remove: "))
            except ValueError:
                print("Could not find position")
                continue
            try:
                todo.remove(ir)
            except ValueError:
                print("Invalid remove position")
                continue
            todo.writeTodoTasksToFile()



main()
