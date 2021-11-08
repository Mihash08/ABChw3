#----------------------------------------------
import sys


class Parallelepiped:
    def __init__(self):
        self.a = 0
        self.b = 0
        self.c = 0
        self.density = 0

    def ReadStrArray(self, strArray, i):
        # должно быт как минимум три непрочитанных значения в массиве
        if i >= len(strArray) - 3:
            return 0
        self.a = int(strArray[i])
        self.b = int(strArray[i+1])
        self.c = int(strArray[i+2])
        self.density = int(strArray[i+3])
        i += 4
        return i

    def Print(self):
        print("Parallelepiped: a = ", self.a, " b = ", self.b, " c = ", self.c, ", Volume = ", self.Volume(),
              ", Density = ", self.density)
        pass

    def Write(self, ostream):
        ostream.write("Parallelepiped: a = {}  b = {}  c = {}, Volume = {}, Density = {}".format \
                     (self.a, self.b, self.c, self.Volume(), self.density))
        pass

    def Volume(self):
        return float(self.a * self.b * self.c)
        pass
