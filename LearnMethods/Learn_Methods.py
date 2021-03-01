class Hospital:

    def __init__(self, name):
        self.name = name

    def adm(self):                          # Instance Methods
        print('Admin')

    def doctor(self):
        print('doc name: '+ self.name)

    @classmethod
    def police_info(cls):                   # class Method
        print('Police: enq ')

    @staticmethod
    def yoga_details():                     # static Method
        print('some info about yoga')








d1 = Hospital('Person1')
d1.doctor()
d1.police_info()

d2 = Hospital('Person2')
d2.doctor()


