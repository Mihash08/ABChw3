#----------------------------------------------
class Sphere:
    def __init__(self):
        self.r = 0
        self.density = 0

    def ReadStrArray(self, strArray, i):
        # должно быт как минимум одно непрочитанных значения в массиве
        if i >= len(strArray) - 1:
            return 0
        self.r = int(strArray[i])
        self.density = int(strArray[i+1])
        i += 2
        return i

    def Print(self):
        print("Sphere: x = ", self.r, ", Volume = ", self.Volume(), ", Density = ", self.density)
        pass

    def Write(self, ostream):
        ostream.write("Sphere: x = {}, Volume = {}, Density = {}".format(self.r, self.Volume(), self.density))
        pass

    def Volume(self):
        return 3.0 / 4.0 * self.r * self.r * self.r
        pass
