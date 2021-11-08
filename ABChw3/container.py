import sys

import sphere
import parallelepiped

#----------------------------------------------
class Container:
    def __init__(self):
        self.store = []
        self.maxlen = 10000

    def Print(self):
        print("The container contains ", len(self.store), "shapes:")
        for shape in self.store:
            shape.Print()
        pass

    def Write(self, ostream):
        ostream.write("The container contains {} shapes:\n".format(len(self.store)))
        for shape in self.store:
            shape.Write(ostream)
            ostream.write("\n")
        pass

    def Volume(self):
        vol = 0.0
        for shape in self.store:
            vol += shape.Volume()
        return vol

    def ShellSort(self):
        n = int(len(self.store))
        gap = int(n / 2)
        while gap > 0:

            for i in range(gap, n):

                temp = self.store[i]

                j = i
                while j >= gap and self.store[j - gap].Volume() > temp.Volume():
                    self.store[j] = self.store[j - gap]
                    j -= gap

                self.store[j] = temp
            gap = int(gap / 2)
