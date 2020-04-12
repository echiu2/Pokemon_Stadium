import time
import random
import requests
import json
import sys

sys.path.insert(0, '/Users/echiu2/Desktop/Pokemon_Stadium/Model')

import get_pokemon

# Create pokemon class with attributes
class Pokemon:
    def __init__ (self, name, level, types, health, moves, stats):
        #Values are being saved as attributes
        self.name = name 
        self.level = level
        self.types = types
        self.health = health 
        self.moves = moves
        self.attack = stats['Attack']
        self.defense = stats['Defense']
        self.speed = stats['Speed']

    def start(self, pkmon2):
        #Begin Pokemon introduction

        print("-----Pokemon Stadium-----\n")
        time.sleep(1)
        print(self.name + " vs. " + pkmon2.name + '\n')
        print(self.name, "Stats:")
        print('Level:', self.level, 'Health', self.health, 'Type:', self.types)
        print('Attack:', self.attack, 'Defense:', self.defense, 'Speed:', self.speed, '\n')
        time.sleep(1)
        print(pkmon2.name, "Stats:")
        print('Level:', pkmon2.level, 'Health', pkmon2.health, 'Type:', pkmon2.types)
        print('Attack:', pkmon2.attack, 'Defense:', pkmon2.defense, 'Speed:', pkmon2.speed, '\n')

        time.sleep(1)

    def battle(self, pkmon2):

        self.start(pkmon2)
        attacker = ""
        attacker_turn = False
        if self.speed > pkmon2.speed:
            attacker_turn = True
            attacker = self
        else:
            attacker_turn = True
            attacker = pkmon2

    #     #Begin pokemon battle
        print("---------Battle!----------\n")
        while (self.health > 0) and (pkmon2.health > 0):
            if attacker_turn:
                attacker = self
                print('-----Choose your attack!-----')
                print(attacker.name)

                for i, move in enumerate(attacker.moves):
                    print(str(i) + ": " + move)
                
                x = input('Type the number of the move: ')
                print(attacker.name + ', attack with ' + attacker.moves[int(x)] + '!\n')

                if attacker.types == pkmon2.types:
                    None
                elif attacker.types == 'lightening' and pkmon2.types == "water":
                    attacker.attack = attacker.attack * 1.5
                elif attacker.types == 'water' and pkmon2.types =='lightening':
                    attacker.attack = attacker.attack * 0.5

                pkmon2.health -= attacker.attack
                print(pkmon2.name + ' has ' + str(pkmon2.health) + ' health left!\n')

                attacker_turn = False

                time.sleep(1)

            else:
                attacker = pkmon2
                print('-----Choose your attack!-----')
                print(attacker.name)

                for i, move in enumerate(attacker.moves):
                    print(str(i) + ": " + move)

                x = input('Type the number of the move: ')
                print(attacker.name + ', attack with ' + attacker.moves[int(x)] + '!\n')

                if attacker.types == pkmon2.types:
                    None
                elif attacker.types == 'lightening' and pkmon2.types == "water":
                    attacker.attack = attacker.attack * 1.5
                elif attacker.types == 'water' and pkmon2.types =='lightening':
                    attacker.attack = attacker.attack * 0.5

                self.health -= attacker.attack
                print(self.name + ' has ' + str(self.health) + ' health left!\n')

                attacker_turn = True

                time.sleep(1)
        
        time.sleep(1)
        
        if self.health != 0:
            print(self.name + ' has defeated ' + pkmon2.name + '!')
        else:
            print(pkmon2.name + ' has defeated ' + self.name + '!')


if __name__ == "__main__":
    #Testing pokemon battle
    Pikachu = Pokemon('Pikachu', '5', 'lightening', 35, ['spark', 'tackle'], {'Attack' : 10, 'Defense': 4, 'Speed': 10})
    Charmander = Pokemon('Charmander', '5', 'fire', 35, ['ember', 'tackle'], {'Attack': 12, 'Defense': 6, 'Speed': 6})
    Squirtle = Pokemon('Squirtle', '5', 'water', 35, ['bubble', 'tackle'], {'Attack': 8, 'Defense': 12, 'Speed': 4})
    Bulbasaur = Pokemon('Bulbasaur', '5', 'grass', 35, ['vine whip', 'tackle'], {'Attack': 8, 'Defense': 10, 'Speed': 6})

    Pikachu.battle(Squirtle)