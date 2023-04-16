class Hero():
    '''Создание героя для игры'''
    def __init__(self, name, level, race):
        '''Инициирование героя'''
        self.name = name
        self.level = level
        self.race = race
        self.health = 100
    def show_hero(self):
        '''Принт параметры'''
        description = (self.name  + str(self.level), str(self.race), str(self.health))
        print(description)


    def level_up(self):
        '''Upgrade level hero'''
        self.level += 1

    def move(self):
        '''Start moving hero'''
        print('Hero ' + self.name + ' start moving....')

class SuperHero(Hero):
    '''Class create Seper hero'''
    def __init__(self, name, level, race, magiclevel):
        '''Initiate our Super Hero'''
        super().__init__(name,level, race)
        self.magiclevel = magiclevel
        self.magic = 100

    def makemagic(self):
        '''use magic'''
        self.magic -= 10

    def show_hero(self):
        '''Принт параметры'''
        description = (self.name  + str(self.level), str(self.race), str(self.health) + 'Magic hire' + self.magic)
        print(description)

myhero1 = Hero('Vurdalak', 5, 'ORK')
myhero2 = Hero('Olejean ', 80, ' chelovek')
myhero1.show_hero()
myhero2.move()
myhero1.level_up()
myhero2.show_hero()
myhero3 = Hero("vurdalak", 4, 'ork')
myhero3.show_hero()
