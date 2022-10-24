class A:
    __cnt = 0
    def __init__(self, n):
        A.__cnt += 1
        self.__n = n
        self.__lst = []

    def mk_table(self, m):
        for i in range(self.__n+1):
            self.__lst.append(i * m)

    def mk_pot(self, p):
        for i in range(self.__n+1):
            self.__lst.append(i ** p)
        
    def get_lst(self):
        return self.__lst

tab8 = A(8)
print(tab8.get_lst())
tab8.mk_table(8)
print(tab8.get_lst())
print()
print(tab8.__dict__, tab8._A__cnt)




