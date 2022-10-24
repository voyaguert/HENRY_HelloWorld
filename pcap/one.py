class A:
    __objcnt = 0
    def __init__(self, n=0):
        A.__objcnt += 1
        self.__lst = []
        for i in range(n):
            self.__lst.append(i * i)

o = A(7)
print(o.__dict__, o._A__objcnt)
