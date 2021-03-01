class Mobile:

    def dial_num(self, ph):
        print(self)
        print('dailing ' ,ph )


    def send_sms(self):
        print('sending')


per1 = Mobile()
print(per1)
per1.dial_num(9597704568)



per2 = Mobile()
print(per2)
per2.dial_num(123456789)