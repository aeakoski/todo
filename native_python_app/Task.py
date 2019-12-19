class Task:
    """docstring for Task."""

    def __init__(self, short, desc, pos, state="t"):
        self.short = str(short)
        self.desc = str(desc)
        self.state = str(state)
        self.pos = int(pos)
    def __str__(self):
        return self.short + "\n" + "-" + "\n" + self.desc + "\n"

    def storeTaskStr(self):
        """
        \1SHORT\n
        \5STATE\n
        \6POS\n
        \2DESC\3
        \1SHORT\n
        \5STATE\n
        \6POS\n
        \2DESC\3
        ...
        """
        return chr(1) + self.short + "\n" + chr(5) + str(self.state) + "\n" + chr(6) + str(self.pos) + "\n" + chr(2) + self.desc + chr(3) + "\n"
