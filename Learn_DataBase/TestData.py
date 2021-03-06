class Test_Data:

    def __init__(self, **kwargs):
        self.fName = kwargs['fName']
        self.lName = kwargs['lName']
        self.email = kwargs['email']
        self.pwd = kwargs['pwd']

# x = Test_Data(fname="Gopinath", lname="Jayakumar", email="gopithri@gmail.com", pwd="123456")
# print(x.fname)