class A:

    def getData(self):
        print("Hello everyone")

    def setData(self):
        print("need data to append")


class B(A):

    def getData(self):
        print("Hi all")



a = A()
a.getData1()


b = B()
b.getData()


