import random


class Player:
    def __init__(self, name, health, damage, evade_chance): # armour
        self.name = name
        self.health = health
        self.damage = damage
        self.evade_chance = evade_chance

    def take_damage(self, damage_taken, evade_chance=False):
        if random.random() < self.evade_chance and evade_chance is True:
            print(self.name + ' succesfully blocked')
        else:
            self.health = self.health - damage_taken
            print(self.name + ' took ' + str(damage_taken) + ' damage')
            print(self.name + ' now has ' + str(self.health) + ' health')


p1 = Player('You', 20, 5, 2/10)
wolf = Player('Wolf', 20, 1, 2/10)
serpent = Player('Serpent', 50, 2, 1/10)
dragon = Player('Dragon', 100, 5, 0)

print('You awaken in a dark forest')
print('You can hear wolves howling and waves crashing in the distance')
print('Chose an option: ')
print('1. Stare at the stars')
print('2. Stand up and look around')
print('3. Roll over and try to sleep')
choice = input('Pick and option: ')

if choice == '1':
    print('You stare up and gaze at the beautiful night sky above')
    print('Suddenly you hear the crinckling of leaves behind you')
    print('You turn around and notice a pair of eyes staring at you from the darkness')
if choice == '2':
    print('You stand up and see a eyes of a pair of eyes staring at you from the darkness')
if choice == '3':
    print('You roll over to try and fall back asleep but you notice a pair of eyes staring at you from the darkness')
print("The pair of eyes slowly creeps forward until you realise it's a wolf")
print('''Chose an option:
1. Take a step back 
2. Attack the wolf''')
choice = input('Pick an option: ')
print(type(choice))
if choice == '1':
    print('You take a step back but suddenly the wolf lunges at you')
    p1.take_damage(wolf.damage, evade_chance=True)
if choice == '2':
    print('You pull out your knife and attack the wolf')
    wolf.take_damage(p1.damage, evade_chance=True)
