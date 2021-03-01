class Mobile:

    def __init__(self, name, ph):
       self.name = name                             # instance variable
       self.ph = ph


    def dial_number(self):                              # Instance method
        print('dialing...... ', self.ph)


    def send_sms(self):
        print('sending.... ', self.ph)


gn = Mobile('Gopinath', 959770458)
gn.dial_number()
#print(gn)

#
dv = Mobile('Divya', 9597704569)
dv.send_sms()
# print(dv)
