# -*- coding: utf-8 -*-

from Task import Task
from TaskList import TaskList

class Brain:
    def __init__(self):
        self.todo = TaskList("todo")
        self.prog = TaskList("prog")
        self.done = TaskList("done")
        self.tl = [self.todo, self.prog, self.done]


    def restoreSession(self):
        for i in self.tl:
            i.readTasksFromFile()
            print(i)
            print(i.printTasks())
            print("----")


    def remove_from_list(self, task_pos, list_inx):
        self.tl[list_inx].remove(task_pos)
        self.tl[list_inx].writeTodoTasksToFile()

    def updateOrder(self, tupleOrder, list_inx):
        if not tupleOrder:
            return
        new_order = []

        for i in tupleOrder:
            for j in self.tl[list_inx].tasks:
                if j.eq(i):
                    new_order.append(j)
                    break
        for p in range(len(new_order)):
            new_order[p].pos = p
        self.tl[list_inx].tasks = new_order
        self.tl[list_inx].writeTodoTasksToFile()


    def getLists(self):
        return self.tl

    def add_existing(self, _task, inx):
        self.tl[inx].add(_task.short, _task.desc)
        self.tl[inx].writeTodoTasksToFile()

    def add_new(self, short, inx):
        self.tl[inx].add(short)
        self.tl[inx].writeTodoTasksToFile()

        #save listboxaswell
