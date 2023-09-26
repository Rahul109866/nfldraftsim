# simulate a nfl draft
print('\033c')
#clears the screen for output

import collections
import data_extract
from random import choice
import random

first_names = data_extract.firstnames() # get all first names
second_names = data_extract.secondnames() # get all second names
universities = data_extract.college()
positions_off, positions_def, positions_special = data_extract.positions()


class Player: 
    player = collections.namedtuple('player', ['name', 'age', 'position', 'squad', 'university'])
    
    def __init__(self):
        
        self.name = choice(first_names) + " " + choice(second_names)
        self.age = random.randint(20,25)
        self.university = random.choice(universities)

    def randomize_position(self):
        
        category = random.choice(['OFF', 'DEF', 'SPT'])
        
        if category == 'OFF':
            self.position = random.choice(positions_off)
        elif category == 'DEF':
            self.position = random.choice(positions_def)
        elif category == 'SPT':
            self.position = random.choice(positions_special)
        else:
            return "Unknown"
    
    


if __name__ == "__main__":
    
    # print(positions_special)
    
    
    
# class Player:
    # player = collections.namedtuple('player', ['name', 'age', 'position', 'university'])
    
    # def __init__(self):
    #     self.name = choice(first_names) + ' ' + choice(second_names)
    #     self.age = random.randint(20, 25)
    #     self.position = self.randomize_position()
        
    # def randomize_position(self):
    #     # Define weighted probabilities for position categories
    #     position_categories = {
    #         'Offense': 0.4,
    #         'Defense': 0.4,
    #         'Special': 0.2
    #     }
        
    #     # Choose a position category
    #     category = random.choices(
    #         list(position_categories.keys()),
    #         weights=list(position_categories.values())
    #     )[0]
        
    #     # Based on the category, randomly select a position
    #     if category == 'Offense':
    #         return random.choice(positions_off)
    #     elif category == 'Defense':
    #         return random.choice(positions_def)
    #     elif category == 'Special':
    #         return random.choice(positions_special)
    #     else:
    #         return "Unknown"
