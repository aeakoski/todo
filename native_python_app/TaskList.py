from Task import Task
class TaskList:
    """docstring for Task."""

    def __init__(self, name):
        self.short = str(name)
        self.path = "./data_" + self.short
        self.tasks = []
    def __str__(self):
        return self.short + "\n"
    def __len(self):
        return len(self.tasks)
    def printTasks(self):
        for t in self.tasks:
            print(t)
    def remove(self, pos):
        if pos > len(self.tasks):
            raise ValueError("Invalid remove position")
        ind = self.tasks.index(pos)
        self.tasks.remove(ind)
        for t in self.tasks:
            if t.pos > ind:
                t.pos = t.pos -1

    def writeTodoTasksToFile(self):
        with open(self.path, "w") as fd:
            for t in self.tasks:
                fd.write(t.storeTaskStr())
    def readTasksFromFile(self):
        with open(self.path, "r") as f:
            while True:
                c = f.readline()
                if not c:
                  print("File " + self.short + " succesfully loaded")
                  break

                if c[0] != chr(1):
                    continue
                short = c[1:-1]

                c = f.readline()
                if c[0] != chr(5):
                    continue
                state = c[1:-1]

                c = f.readline()

                if c[0] != chr(6):
                    continue
                pos = c[1:-1]

                c = f.readline()
                if c[0] != chr(2):
                    continue
                if c[-2] == chr(3): #One liner DESC
                    desc = c[1:-2]
                else:
                    desc = c[1:-1]
                    c = f.readline()
                    while c[-2] != chr(3):
                        desc = desc + c[:-1]
                        c = f.readline()
                    desc = desc + c[1:-2]

                t = Task(short=short, desc=desc, pos=pos, state=state)
                self.tasks.append(t)
