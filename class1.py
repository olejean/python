class Car():
    def exclaim(self):
        print('I M A CAR!')


class Yugo(Car):
    pass

give_me_a_car = Car()
give_me_a_yugo = Yugo()
give_me_a_car.exclaim()

give_me_a_yugo.exclaim()