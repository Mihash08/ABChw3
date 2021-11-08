#----------------------------------------------
import math


class Tetrahedron:
    def __init__(self):
        self.a = 0
        self.density = 0

    def ReadStrArray(self, strArray, i):
        # должно быть как минимум одно непрочитанное значения в массиве
        if i >= len(strArray) - 1:
            return 0
        self.a = int(strArray[i])
        self.density = int(strArray[i+1])
        i += 2
        return i

    def Print(self):
        print("Tetrahedron: a = ", self.a, ", Volume = ", self.Volume(), ", Density = ", self.density)
        pass

    def Write(self, ostream):
        ostream.write("Tetrahedron: a = {}, Volume = {}, Density = {}".format \
                     (self.a, self.Volume(), self.density))
        pass

    def Volume(self):
        return float(self.a * self.a * self.a * math.sqrt(2) / 12.0)
        pass
