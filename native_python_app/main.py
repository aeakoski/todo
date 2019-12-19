print("Hello")
from Task import Task

def readTasksFromFile(path, type):
    with open(path + "_" + type, "r") as f:
        taskc=0
        while True:
            c = f.read(1)
            if not c:
              print("File succesfully read")
              break
            if c == chr(1):
                short = ""
                while True: #short
                    c = f.read(1)
                    if c == "\n":
                        break
                    short = short + c

            c = f.read(1)
            if c == chr(5):
                state = ""
                c = f.read(1)
                if c == "t":
                    state = "t"
                elif c == "p":
                    state = "p"
                elif c == "d":
                    state = "d"
                else:
                    raise ValueError("Cant read state!")

            c = f.read(1) # Read "\n"

            c = f.read(1)
            if c == chr(6):
                pos = ""
                while True: #pos
                    c = f.read(1)
                    if c == "\n":
                        break
                    pos = pos + c

            c = f.read(1)
            if c == chr(2):
                desc = ""
                while True: #pos
                    c = f.read(1)
                    if c == chr(3):
                        break
                    desc = desc + c

            t = Task(short=short, desc=desc, pos=pos, state=state)
            prog.append(t)
            taskc +=1



def writeTodoTasksToFile(path):
    with open(path + "_todo", "w") as fd:
        for i in todo:
            fd.write(i.storeTaskStr())

def writeDoingTasksToFile(path):
    with open(path + "_doing", "w") as fd:
        for i in todo:
            fd.write(i.storeTaskStr())

def writeDoneTasksToFile(path):
    with open(path + "_done", "w") as fd:
        for i in todo:
            fd.write(i.storeTaskStr())


todo = []
prog = []
done = []

readTasksFromFile(".\\data", "todo")

c = 0
while c < 2:
    i = raw_input("Type todo here: ")
    todo.append(Task(i, "dd", len(todo)))
    c+=1

for i in todo:
    print(i)

for i in prog:
    print(i)

writeTodoTasksToFile(".\\data")
