print("Hello")
from Task import Task
from TaskList import TaskList

# def readTasksFromFile(path, taskList, type):
#     with open(path + "_" + type, "r") as f:
#         taskc=0
#         while True:
#             c = f.readline()
#             if not c:
#               print("File " + type + " succesfully loaded")
#               break
#
#             if c[0] != chr(1):
#                 continue
#             short = c[1:-1]
#
#             c = f.readline()
#             if c[0] != chr(5):
#                 continue
#             state = c[1:-1]
#
#             c = f.readline()
#
#             if c[0] != chr(6):
#                 continue
#             pos = c[1:-1]
#
#             c = f.readline()
#             if c[0] != chr(2):
#                 continue
#             if c[-2] == chr(3): #One liner DESC
#                 desc = c[1:-2]
#             else:
#                 desc = c[1:-1]
#                 c = f.readline()
#                 while c[-2] != chr(3):
#                     desc = desc + c[:-1]
#                     c = f.readline()
#                 desc = desc + c[1:-2]
#
#             t = Task(short=short, desc=desc, pos=pos, state=state)
#             taskList.append(t)

# def writeTodoTasksToFile(path, lista, type):
#     if type == "todo":
#         pass
#     elif type == "prog":
#         pass
#     elif type == "done":
#         pass
#     else:
#         raise ValueError()
#     with open(path + "_" + type , "w") as fd:
#         for i in lista:
#             fd.write(i.storeTaskStr())


def main():

    todo = TaskList("todo")
    prog = []
    done = []

    todo.readTasksFromFile()

    while True:
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
