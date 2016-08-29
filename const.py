import random


def roll(d):
    return random.randrange(1, d)


def calculate_tavern():
    keg_value = 10
    num_rumors = roll(4) - 1
    num_kegs = roll(10) + roll(10)
    income = ((10 * roll(10)) / 30) * 7

    total = income + (num_kegs * keg_value)

    print '[+] The tavern generates:'
    print '\t{} rumors.'.format(num_rumors)
    print '\t{} kegs of alcohol worth {} GP.'.format(num_kegs, num_kegs * keg_value)
    print '\t{} GP'.format(income)

    return total


def calculate_lodgings():
    income = ((30 * roll(10)) / 30) * 7
    print '[+] The lodging generates {} GP.'.format(income)
    return income


def calculate_caravansary():
    income = (20 * (roll(10) + roll(10)) / 30) * 7
    print '[+] The caravansary generates {} GP.'.format(income)
    return income


def calculate_docks_air():
    income = (15 * (roll(10) + roll(10)) / 30) * 7
    print '[+] The air dock generates {} GP.'.format(income)
    return income


def calculate_docks_water():
    income = (25 * (roll(10) + roll(10)) / 30) * 7
    print '[+] The sea dock generates {} GP.'.format(income)
    return income


def calculate_market_stalls():
    income = (30 * (roll(6) + roll(6)) / 30) * 7
    print '[+] The market stalls generate {} GP.'.format(income)
    return income


def calculate_smithy():
    income = (15 * roll(10) / 30) * 7
    print '[+] The smithy generates {} GP.'.format(income)
    return income


HALF_COST_BONUS_ROOM = 'HCBR'

BUILDABLE_STRUCTURES = [
    {
        'name': 'Abbey',
        'room_points': 6,
        'construction_cost': 50000,
        'construction_time': 400,
        'bonus_room': 'Garden',
        'hirelings': (5, 25),
        'description': '',
        'modifiers': []
    },
    {
        'name': 'College / Large School',
        'room_points': 6,
        'construction_cost': 50000,
        'construction_time': 400,
        'bonus_room': 'Theater',
        'hirelings': (5, 25),
        'description': '',
        'modifiers': []
        },
    {
        'name': 'Cottage / Medium House',
        'room_points': 1,
        'construction_cost': 2500,
        'construction_time': 30,
        'bonus_room': 'Any',
        'hirelings': (1, None),
        'description': '',
        'modifiers': [HALF_COST_BONUS_ROOM]
        },
    {
        'name': 'Dungeon / Barrow',
        'room_points': 3,
        'construction_cost': 15000,
        'construction_time': 100,
        'bonus_room': 'Jails',
        'hirelings': (3, 15),
        'description': '',
        'modifiers': []
        },
    {
        'name': 'Guildhall / Lodge',
        'room_points': 2,
        'construction_cost': 5000,
        'construction_time': 60,
        'bonus_room': 'Dining Hall',
        'hirelings': (5, 3),
        'description': '',
        'modifiers': []
        },
    {
        'name': 'Keep / Small Castle',
        'room_points': 6,
        'construction_cost': 50000,
        'construction_time': 400,
        'bonus_room': 'War Room',
        'hirelings': (50, 50),
        'description': '',
        'modifiers': []
        },
    {
        'name': 'Noble Estate with Manor',
        'room_points': 4,
        'construction_cost': 25000,
        'construction_time': 150,
        'bonus_room': 'Library',
        'hirelings': (3, 15),
        'description': '',
        'modifiers': []
        },
    {
        'name': 'Outpost / Fort',
        'room_points': 3,
        'construction_cost': 15000,
        'construction_time': 100,
        'bonus_room': 'Armory',
        'hirelings': (20, 40),
        'description': '',
        'modifiers': []
        },
    {
        'name': 'Palace / Large Castle',
        'room_points': 10,
        'construction_cost': 500000,
        'construction_time': 1200,
        'bonus_room': 'Any',
        'hirelings': (200, 100),
        'description': '',
        'modifiers': []
        },
    {
        'name': 'Temple',
        'room_points': 6,
        'construction_cost': 50000,
        'construction_time': 400,
        'bonus_room': 'Chapel',
        'hirelings': (10, 10),
        'description': '',
        'modifiers': []
        },
    {
        'name': 'Fortified Tower',
        'room_points': 3,
        'construction_cost': 15000,
        'construction_time': 100,
        'bonus_room': 'Stables',
        'hirelings': (10, None),
        'description': '',
        'modifiers': []
        },
    {
        'name': 'Trading Post / Large House',
        'room_points': 2,
        'construction_cost': 5000,
        'construction_time': 60,
        'bonus_room': 'Caravansary or Lodgings',
        'hirelings': (4, 2),
        'description': '',
        'modifiers': []
        }
]

ROOMS = [
    {
        'name': 'Alchemist\'s Lab',
        'size_cost': 1,
        'construction_cost': 2500,
        'construction_time': 15,
        'description': '',
        'benefits': '',
        'other_names': ['Herbalist', 'Witch\'s Hut'],
        'multiple': False,
        'calculate_function': None
        },
    {
        'name': 'Animal Pen',
        'size_cost': [1, 2],
        'construction_cost': [2500, 5000],
        'construction_time': [15, 30],
        'description': '',
        'benefits': '',
        'other_names': ['Monster Cage', 'Griffin Roost', 'Dragon Trap', 'Kennels', 'Aviary', 'Rookery'],
        'multiple': True,
        'calculate_function': None
        },
    {
        'name': 'Arcanist\'s Study',
        'size_cost': 1,
        'construction_cost': 2500,
        'construction_time': 15,
        'description': '',
        'benefits': '',
        'other_names': None,
        'multiple': True,
        'calculate_function': None
        },
    {
        'name': 'Armory',
        'size_cost': 1,
        'construction_cost': 2500,
        'construction_time': 15,
        'description': '',
        'benefits': '',
        'other_names': ['Herbalist', 'Witch\'s Hut'],
        'multiple': False,
        'calculate_function': None
        },
    {
        'name': 'Battle Ring',
        'size_cost': 1,
        'construction_cost': 2500,
        'construction_time': 15,
        'description': '',
        'benefits': '',
        'other_names': ['Training Grounds'],
        'multiple': False,
        'calculate_function': None
        },
    {
        'name': 'Caravansary',
        'size_cost': 1,
        'construction_cost': 2500,
        'construction_time': 15,
        'description': '',
        'benefits': '',
        'other_names': None,
        'multiple': False,
        'calculate_function': calculate_caravansary
        },
    {
        'name': 'Chapel',
        'size_cost': 1,
        'construction_cost': 2500,
        'construction_time': 15,
        'description': '',
        'benefits': '',
        'other_names': ['Shrine', 'Spirit Lodge', 'Observatory'],
        'multiple': False,
        'calculate_function': None
        },
    {
        'name': 'Dining Hall',
        'size_cost': 1,
        'construction_cost': 2500,
        'construction_time': 15,
        'description': '',
        'benefits': '',
        'other_names': ['Ball Room', 'Mess Hall'],
        'multiple': False,
        'calculate_function': None
        },
    {
        'name': 'Docks, Air',
        'size_cost': 2,
        'construction_cost': 10000,
        'construction_time': 30,
        'description': '',
        'benefits': '',
        'other_names': None,
        'multiple': False,
        'calculate_function': calculate_docks_air
        },
    {
        'name': 'Docks, Water',
        'size_cost': 2,
        'construction_cost': 10000,
        'construction_time': 30,
        'description': '',
        'benefits': '',
        'other_names': None,
        'multiple': False,
        'calculate_function': calculate_docks_water
        },
    {
        'name': 'Escape Tunnel',
        'size_cost': 1,
        'construction_cost': 2500,
        'construction_time': 15,
        'description': '',
        'benefits': '',
        'other_names': ['Escape Portal'],
        'multiple': False,
        'calculate_function': None
        },
    {
        'name': 'Garden',
        'size_cost': 1,
        'construction_cost': 2500,
        'construction_time': 15,
        'description': '',
        'benefits': '',
        'other_names': ['Greenhouse', 'Druidic Grove'],
        'multiple': False,
        'calculate_function': None
        },
    {
        'name': 'Graveyard',
        'size_cost': 1,
        'construction_cost': 2500,
        'construction_time': 15,
        'description': '',
        'benefits': '',
        'other_names': ['Crypt', 'Mausoleum', 'Necromancer\'s Labratory'],
        'multiple': False,
        'calculate_function': None
        },
    {
        'name': 'Jails',
        'size_cost': 1,
        'construction_cost': 2500,
        'construction_time': 15,
        'description': '',
        'benefits': '',
        'other_names': ['Prison', 'Torture Chamber', 'Sacrifice Pit'],
        'multiple': False,
        'calculate_function': None
        },
    {
        'name': 'Library',
        'size_cost': 1,
        'construction_cost': 2500,
        'construction_time': 15,
        'description': '',
        'benefits': '',
        'other_names': ['Archives', 'Museum'],
        'multiple': False,
        'calculate_function': None
        },
    {
        'name': 'Lodgings',
        'size_cost': 1,
        'construction_cost': 2500,
        'construction_time': 15,
        'description': '',
        'benefits': '',
        'other_names': ['Barracks', 'Guest Rooms', 'Spare Cots', 'Servant\'s Quarters'],
        'multiple': True,
        'calculate_function': calculate_lodgings
        },
    {
        'name': 'Magical Enchanter',
        'size_cost': 1,
        'construction_cost': 2500,
        'construction_time': 15,
        'description': '',
        'benefits': '',
        'other_names': ['Alter of Blessings'],
        'multiple': False,
        'calculate_function': None
        },
    {
        'name': 'Market Stalls',
        'size_cost': 1,
        'construction_cost': 2500,
        'construction_time': 15,
        'description': '',
        'benefits': '',
        'other_names': ['Shops'],
        'multiple': True,
        'calculate_function': calculate_market_stalls
        },
    {
        'name': 'Prisoner\'s Grotto',
        'size_cost': 1,
        'construction_cost': 2500,
        'construction_time': 15,
        'description': '',
        'benefits': '',
        'other_names': None,
        'multiple': False,
        'calculate_function': None
        },
    {
        'name': 'Ritual Circle',
        'size_cost': 1,
        'construction_cost': 2500,
        'construction_time': 15,
        'description': '',
        'benefits': '',
        'other_names': None,
        'multiple': False,
        'calculate_function': None
        },
    {
        'name': 'Smithy',
        'size_cost': 1,
        'construction_cost': 2500,
        'construction_time': 15,
        'description': '',
        'benefits': '',
        'other_names': ['Forge'],
        'multiple': False,
        'calculate_function': calculate_smithy
        },
    {
        'name': 'Siege Workshop',
        'size_cost': 1,
        'construction_cost': 2500,
        'construction_time': 15,
        'description': '',
        'benefits': '',
        'other_names': None,
        'multiple': False,
        'calculate_function': None
        },
    {
        'name': 'Stables',
        'size_cost': 1,
        'construction_cost': 2500,
        'construction_time': 15,
        'description': '',
        'benefits': '',
        'other_names': None,
        'multiple': False,
        'calculate_function': None
        },
    {
        'name': 'Tavern',
        'size_cost': 1,
        'construction_cost': 2500,
        'construction_time': 15,
        'description': '',
        'benefits': '',
        'other_names': ['Brewery', 'Public House', 'Speakeasy'],
        'multiple': False,
        'calculate_function': calculate_tavern
        },
    {
        'name': 'Theater',
        'size_cost': 1,
        'construction_cost': 2500,
        'construction_time': 15,
        'description': '',
        'benefits': '',
        'other_names': ['Lecture Hall', 'Balcony & Courtyard'],
        'multiple': False,
        'calculate_function': None
        },
    {
        'name': 'War Room',
        'size_cost': 1,
        'construction_cost': 2500,
        'construction_time': 15,
        'description': '',
        'benefits': '',
        'other_names': ['Bureaucrat\'s Office'],
        'multiple': False,
        'calculate_function': None
        }
]

HIRELINGS = [
    {
        'hireling': 'Slave',
        'pay': 0
        },
    {
        'hireling': 'Unskilled',
        'pay': 0.2
        },
    {
        'hireling': 'Skilled',
        'pay': 2
        },
    {
        'hireling': 'Guard',
        'pay': 2
        },
    {
        'hireling': 'Scout',
        'pay': 5
        },
    {
        'hireling': 'Thug',
        'pay': 5
        },
    {
        'hireling': 'Spy',
        'pay': 10
        },
    {
        'hireling': 'Berserker',
        'pay': 20
        },
    {
        'hireling': 'Knight',
        'pay': 40
        },
    {
        'hireling': 'Veteran',
        'pay': 40
        },
    {
        'hireling': 'Assassin',
        'pay': 100
        },
    {
        'hireling': 'Acolyte',
        'pay': 5
        },
    {
        'hireling': 'Druid',
        'pay': 25
        },
    {
        'hireling': 'Mage',
        'pay': 100
        },
    {
        'hireling': 'Priest',
        'pay': 25
        }
]
