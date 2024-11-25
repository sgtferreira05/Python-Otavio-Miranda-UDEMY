# Enum -> enumerations
# Enumerations in programming are used in situations where there is a fixed set of possible values to choose from.
# Enums have members, and theirs values are constante.
# Enums in Pythom:
#   - They're a set of symbolic names (members) associated with unique values
#   - They can be itereted to return their canonical members in the order of definition
# enum.Enum is the superclass to its enumerates. But, it can also be used directly (Nevertheless, enums aren't ordinary classes in Python)
# You will be able to use your Enum with: type annotations, isinstance checks and others type related operations.
# To get the data:
    # member = Class(value), Class['key']
    # key = Class.key.name
    # value = Class.key.value


import enum

#       This way, the vs doesn't know wich type directions are
# Directions = enum.Enum('Directions', ['LEFT', 'RIGHT'])
# print(Directions(1), Directions['LEFT'], Directions.LEFT)
# print(Directions(1).name, Directions.LEFT.value)

#       This way, the vs know wich type directions are
class Directions(enum.Enum):
    LEFT = enum.auto()
    RIGHT = enum.auto()
    UP = enum.auto()
    DOWN = enum.auto()
    STRAIGHT = enum.auto()


    


def move(direction: Directions): # to inform the type
    if not isinstance(direction, Directions):
        raise ValueError('Direction not founded')
    
    print(f'Moving to {direction.name}, ({direction.value})')

move(Directions.LEFT)
move(Directions.RIGHT)
move(Directions.UP)
move(Directions.DOWN)
move(Directions.STRAIGHT)


# move('left')
# move('right')
# move('up')
# move('down')
# move('straight')
