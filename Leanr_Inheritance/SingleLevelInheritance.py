class A:

    def a(self):
        print("I'm from class A")



class B(A):

    def b(self):
        print("I'm from class B")



aa = A()
aa.a()

bb = B()
bb.b()
bb.a()