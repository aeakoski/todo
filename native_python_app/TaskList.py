# -*- coding: utf-8 -*-
import io

from Task import Task
import os
class TaskList:
    """docstring for Task."""

    def __init__(self, name):
        self.short = str(name)
        self.path = "./" + self.short + ".data"
        self.tasks = []
    def __str__(self):
        return self.short + "\n"
    def __len(self):
        return len(self.tasks)
    def printTasks(self):
        for t in self.tasks:
            print(t)
    def add(self, short, desc="dd", pos = False, state="t"):
        if not pos:
            pos = len(self.tasks)
        t = Task(short=short, desc=desc, pos=pos, state=state)
        self.tasks.append(t)
    def remove(self, pos):
        if pos > len(self.tasks):
            raise ValueError("Invalid remove position")
        ind = self.tasks.index(pos)
        self.tasks.remove(ind)
        for t in self.tasks:
            if t.pos > ind:
                t.pos = t.pos -1

    def writeTodoTasksToFile(self):
        with io.open(self.path, "w", encoding="utf-8") as fd:
            for t in self.tasks:
                fd.write(t.storeTaskStr().decode("utf-8"))
    def readTasksFromFile(self):
        with io.open(self.path, "r", encoding="utf-8") as f:
            while True:
                c = f.readline()
                if not c:
                  print("File " + self.short + " succesfully loaded")
                  break

                if c[0] != chr(1):
                    continue
                short = c[1:-1]

                c = f.readline()
                # print("Short: " + c)
                if c[0] != chr(5):
                    continue
                state = c[1:-1]

                c = f.readline()
                # print("Position: " + c)
                if c[0] != chr(6):
                    continue
                pos = c[1:-1]

                c = f.readline()
                # print("Desc: " + c)
                if c[0] != chr(2):
                    continue
                # print(ord(c[-1]))
                if os.name == "posix":
                    if c[-2] == chr(3): #One liner DESC
                        desc = c[1:-3]
                    else:
                        desc = c[1:-1]
                        c = f.readline()
                        while c[-2] != chr(3):
                            desc = desc + c[:-1]
                            c = f.readline()
                        desc = desc + c[1:-2]

                else:
                    if c[-2] == chr(3): #One liner DESC
                        desc = c[1:-2]
                    else:
                        desc = c[1:-1]
                        c = f.readline()
                        while c[-2] != chr(3):
                            desc = desc + c[:-1]
                            c = f.readline()
                        desc = desc + c[1:-2]

                self.add(short, desc, pos, state)
                #t = Task(short=short, desc=desc, pos=pos, state=state)
                #self.tasks.append(t)
