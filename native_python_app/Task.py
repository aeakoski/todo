# -*- coding: utf-8 -*-

class Task:
    """docstring for Task."""

    def __init__(self, short, desc, pos, state="t"):
        self.short = short.encode("utf-8")
        self.desc = str(desc)
        self.state = str(state)
        self.pos = int(pos)
    def __str__(self):
        #return str(self.pos) + ". " + self.short + "\n" + "-" + "\n" + self.desc + "\n"
        return self.short.capitalize()
    def __eq__(self, other):
        return self.pos == other
    def eq(self, other):
        return self.short == other
    def intersection(self, lst1, lst2):
        lst3 = [value for value in lst1 if value in lst2]
        return lst3
    def storeTaskStr(self):
        """
        \1SHORT\n
        \5STATE\n
        \6POS\n
        \2DESC\3\n
        \1SHORT\n
        \5STATE\n
        \6POS\n
        \2DESC\n
        \n\n
        \3\n
        ...
        """
        # inters = self.intersection("åäöÅÄÖ", self.short)
        # if not inters:
        #     return chr(1) + self.short + "\n" + chr(5) + str(self.state) + "\n" + chr(6) + str(self.pos) + "\n" + chr(2) + self.desc + chr(3) + "\n"
        # else:
        #     sh = self.short
        #     for c in inters:
        #         sh = sh.replace(c, chr())

        a = chr(1) + self.short + "\n" + chr(5) + str(self.state) + "\n" + chr(6) + str(self.pos) + "\n" + chr(2) + self.desc + chr(3) + "\n"
        return a
