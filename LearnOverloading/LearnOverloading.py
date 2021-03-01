class OverLoadingClass:

    def __init__(self, *args):
        print(len(args))

    def __init__(self):
        print("init function")

    def getData(self, a, b):
        pass



x = OverLoadingClass(1, 2, 3)
