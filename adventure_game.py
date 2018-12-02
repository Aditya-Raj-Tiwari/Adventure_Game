# This is a adventure game for all those adventerous guys and girls
import random

print('Hellow adventurer let us begin the great next adventure in the history of our universe ')
print('But first you need to name your character ,what might we call it : ')
nameOftheCharacter = input()
print('Let us take ' + nameOftheCharacter + ' to a great adventure back to 0B.C (many years back from now)')
print('Lets goooooooooo!!!!!!! ')


def YnAnswer():
    print('Type y for yes and n for no: ', end=' ')
    answer = input().lower()
    if answer == 'y':
        return 1
    else:
        return -1


def Weapon(numberWeapon):
    WeaponsArray = ['Stone', 'Stick', 'Hand']
    if numberWeapon == 1:
        print('You got ' + WeaponsArray[0])
        return WeaponsArray[0]
    elif numberWeapon == 2:
        print('You got ' + WeaponsArray[1])
        return WeaponsArray[1]
    else:
        print('Sorry but you did not get anything ')
        return WeaponsArray[2]


print('Type a number between 1 and 3 it will decide what weapon you will have .. ')
input()
numberGot = random.randint(1, 4)
WeapnYouGot = Weapon(numberGot)

print('So lets talk like ancient humans now shall we? ooobaoioa oooiuio  oiioooo')
input()
print('Just kidding !!')

# Cave part answer
print('Oh wait I see a cave shall we get inside it?  : Type y for yes and n for no')
AnswerToCave = input().lower()


def inThCave():
    print(
        'Finally we are in the cave and wait there is a box !!! Wait what .. Shall we open it? : : Type y for yes and n for no')
    answer = input().lower()
    if answer == 'y':
        print('Oh wait there are some stuffs but we dont have anything to carry it and every thing is important ')
        print('Lets pick a random number and shall faith decide it: ')
        input()
        stuffsIntheBox = ['sharp stone', 'harp', 'stone knife']
        stuffYougot = random.randint(1, 4)

        if stuffYougot == 1:
            print('You got ' + stuffsIntheBox[0])
            return stuffsIntheBox[0]

        elif stuffYougot == 2:
            print('You got ' + stuffsIntheBox[1])
            return stuffsIntheBox[1]
        else:
            print('You got ' + stuffsIntheBox[2])
            return stuffsIntheBox[2]


if AnswerToCave == 'y':
    inThCave()

print('Oh wait i hear something and it doesnt sound good it came from inside the cave shall we check it out?')
answer = YnAnswer()
if answer == 1:
    print('It sounds as if something big is in there .. going..')
    print('going..............')
    print('Oh no its a giant bear what shall we do .. ')
    print('press 1 to attack it and press 2 to exit from cave..')
    number = input()

