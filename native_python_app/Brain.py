# -*- coding: utf-8 -*-

from Task import Task
from TaskList import TaskList

class Brain:
    def __init__(self):
        self.todo = TaskList("todo")
        self.prog = TaskList("prog")
        self.done = TaskList("done")

        self.todo.readTasksFromFile()

    def getLists(self):
        return [self.todo, self.prog, self.done]

    def add(self, short):
        self.todo.add(short)
        self.todo.writeTodoTasksToFile()

        #save listboxaswell
