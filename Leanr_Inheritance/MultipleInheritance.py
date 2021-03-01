class GA:
    def ga(self):
        print("I'm from class GA")



class GB:
    def gb(self):
        print("I'm from class GB")

    def e(self):
        print("I'm d method. come's from class GB")


class A(GA, GB):

    def a(self):
        print("I'm from class A")

class B:

    def b(self):
        print("I'm from class B")

    def d(self):
        print("I'm d method. come's from class B")

class C(A, B):

    def c(self):
        print("I'm from class C")


cc = C()
cc.d()

print(C.__mro__) # MRO: Method Resolution Order


