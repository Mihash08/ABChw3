from extender import *
from sphere import Sphere


def ReadStrArray(container, strArray):
    arrayLen = len(strArray)
    i = 0   # Индекс, задающий текущую строку в массиве
    figNum = 0
    while i < arrayLen - 1:
        str_1 = strArray[i]
        key = int(str_1)   # преобразование в целое
        #print("key = ", key)
        if key == 1: # признак сферы
            i += 1
            shape = Sphere()
            i = shape.ReadStrArray(strArray, i) # чтение сферы с возвратом позиции за ним
        elif key == 2: # признак параллелепипеда
            i += 1
            shape = Parallelepiped()
            i = shape.ReadStrArray(strArray, i) # чтение параллелепипеда с возвратом позиции за ним
        elif key == 3: # признак тетраэдра
            i += 1
            shape = Tetrahedron()
            i = shape.ReadStrArray(strArray, i) # чтение тетраэдра с возвратом позиции за ним
        else:
            # что-то пошло не так. Должен быть известный признак
            # Возврат количества прочитанных фигур
            return figNum
        # Количество пробелами фигур увеличивается на 1
        if i == 0:
            return figNum
        figNum += 1
        if (container.maxlen > len(container.store)):
            container.store.append(shape)
    return figNum
