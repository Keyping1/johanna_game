import random


class Character:
    def __init__(self, name, health, damage, evade_chance): # armour
        self.name = name
        self.health = health
        self.damage = damage
        self.evade_chance = evade_chance

    def took_damage(self):
        pass

    def successful_attack(self):
        print('sriugdlzurhglziudhrg;dg')

    def missed_attack(self):
        pass

    def dodged_attack(self):
        return 'The ' + self.name + ' evaded the attack'

    def died(self):
        pass

    def take_damage(self, attacking_character, evade=False):
        if random.random() < self.evade_chance and evade is True:
            self.dodged_attack()
        else:
            self.health = self.health - attacking_character.damage
            self.took_damage()
            print(self.name + ' took ' + str(attacking_character.damage) + ' damage')
            print(self.name + ' now has ' + str(self.health) + ' health')


p1 = Player('You', 20, 5, 2 / 10)
wolf = Wolf('Wolf', 20, 1, 2 / 10)
serpent = Character('Serpent', 50, 2, 1 / 10)
dragon = Character('Dragon', 100, 5, 0)

print('You awaken in a dark forest')
print('You can hear wolves howling and waves crashing in the distance')
print('Chose an option: ')
print('1. Stare at the stars')
print('2. Stand up and look around')
print('3. Roll over and try to sleep')
choice = input('Pick an option: ')

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

if choice == '1':
    print('You take a step back')
    p1.take_damage(wolf)
if choice == '2':
    # print('You pull out your knife and attack the wolf') FIX THIS LATER
    wolf.take_damage(p1, evade=True)



while wolf.health > 0:
    print('''Chose an option:
    1. Attempt to evade the wolf's attack
    2. Attack the wolf''')
    choice = input('Pick an option: ')
    if choice == '1':
        print("You attempt to evade the wolf's attack")
        p1.take_damage(wolf, evade=True)
    if choice == '2':
        wolf.take_damage(p1) # if dead shouldnt do next thing
        p1.take_damage(wolf)
print()
print('You killed the wolf')
del wolf
