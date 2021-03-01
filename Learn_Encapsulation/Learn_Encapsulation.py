# Encapsulation
            # Data Hiding
            # Implementation Hiding

class TestLeaf:

    TL_ph_numb = 12345678
    G_Office_Num = 121212
    _GPersonalNum = 54321

    def DataScience(self):
        print('DS')

    def Python(self):
        print('Python')

    def _arrangeInterview(self):
        print('Related to Interivew')

    def get_data(self):
        return TestLeaf._GPersonalNum

    def set_data(self, new_ph_num):
        TestLeaf._GPersonalNum = new_ph_num

    def accessPrivateMethods(self):
        TestLeaf._arrangeInterview(self)


x = TestLeaf()
print(x.get_data())
x.set_data('+443223121')
print(x.get_data())

x.accessPrivateMethods()





