# -*- coding: utf-8 -*-

from Task import Task
from TaskList import TaskList

class Brain:
    def __init__(self):
        self.todo = TaskList("todo")
        self.prog = TaskList("prog")
        self.done = TaskList("done")
        self.tl = [self.todo, self.prog, self.done]
        self.todo.readTasksFromFile()

    def remove_from_list(self, task_pos, list_inx):
        self.tl[list_inx].remove(task_pos)
        self.tl[list_inx].writeTodoTasksToFile()

    def getLists(self):
        return self.tl

    def add(self, short):
        self.todo.add(short)
        self.todo.writeTodoTasksToFile()

        #save listboxaswell
