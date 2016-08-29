from Room import Room
from const import *


class Structure:
    def __init__(self, name, description, room_points, construction_cost, construction_time, bonus_room, hirelings, modifiers=None):
        """
        Initialization function for the Structure class.

        :param name: [str] the name of the structure (should be the name of an entry in the BUILDABLE_STRUCTURES list)
        :param description: [str, None] the description of the structure
        :param room_points: [int] the number of room points available for the structure
        :param construction_cost: [int] the construction cost of the structure in GP
        :param construction_time: [int] the construction time of the structure in DAYS
        :param bonus_room: [str] the name of the bonus room for the structure
        :param hirelings: [tuple] the number of skilled and unskilled hirelings for the structure
        :param modifiers: [list, None]
        """
        assert isinstance(name, str), \
            '[Structure::__init__] name must be a string - {}'.format(name)
        assert isinstance(description, str) or description is None, \
            '[Structure::__init__] description must be a string or None - {}'.format(description)
        assert isinstance(room_points, int), \
            '[Structure::__init__] room_points must be an int - {}'.format(room_points)
        assert isinstance(construction_cost, int), \
            '[Structure::__init__] construction_cost must be an int - {}'.format(construction_cost)
        assert isinstance(construction_time, int), \
            '[Structure::__init__] construction_time must be an int - {}'.format(construction_time)
        assert isinstance(bonus_room, str), \
            '[Structure::__init__] bonus_room must be a string - {}'.format(bonus_room)
        assert isinstance(hirelings, tuple) and len(hirelings) == 2, \
            '[Structure::__init__] hirelings must be a tuple with a length of 2 - {}'.format(hirelings)

        self._name = name
        self._description = description
        self._total_room_points = room_points
        self._construction_cost = construction_cost
        self._construction_time = construction_time
        self._bonus_room = bonus_room
        self._hirelings = hirelings
        self._calculate_functions = []

        self._rooms = []
        self.add_room(bonus_room, HALF_COST_BONUS_ROOM in modifiers)

    def __str__(self):
        """
        :return: [str] a string representation of this object.
        """
        s = '{}\nDescription: {}\nRoom Points: {} ({} used)\nConstruction Cost: {:,} GP\n' \
            'Construction Time: {} Days\nBonus Room: {}\nSkilled Hirelings: {}\nUnskilled Hirelings: {}\n' \
            'Rooms:'.format(self._name, self._description, self._total_room_points,
                              sum([x.size_cost for x in self._rooms]), self._construction_cost, self._construction_time,
                              self._bonus_room, self._hirelings[0], self._hirelings[1])

        for r in self.rooms:
            s += '\n{}'.format(r).replace('\n', '\n\t')

        s += '\n'
        return s

    def add_room(self, room_name, half_cost=False):
        """
        Adds a room to the structures room list.

        :param room_name: the name of the room to add to the structure.
        :param half_cost: [bool] if the room should be purchased at half cost or not.
        :return: None
        """
        assert isinstance(room_name, str), \
            '[Structure::add_room] room must be a string - {}'.format(room_name)

        tr = next((item for item in ROOMS if item['name'] == room_name), None)
        assert tr is not None, \
            '[Structure::add_room] invalid room name - {}'.format(room_name)

        print '[+] Adding {} to the stronghold.'.format(tr['name'])
        self._rooms.append(Room(half_cost=half_cost, **tr))

    def contains_room(self, room_name):
        """
        Determines if the structure has a room of the specified type already.

        :param room_name: [str] the name of the room to look for.
        :return: True of the structure has a room of the specified type, False if not.
        """
        for r in self._rooms:
            if r.name == room_name:
                return True
        return False

    @property
    def name(self):
        return self._name

    @property
    def description(self):
        return self._description

    @property
    def room_points(self):
        return self._total_room_points

    @property
    def room_points_remaining(self):
        return self._total_room_points - len(self._rooms)

    @property
    def construction_cost(self):
        return self._construction_cost

    @property
    def construction_time(self):
        return self._construction_time

    @property
    def bonus_room(self):
        return self._bonus_room

    @property
    def hirelings(self):
        return self._hirelings

    @property
    def skilled_hirelings(self):
        return self._hirelings[0]

    @property
    def unskilled_hirelings(self):
        return self._hirelings[1]

    @property
    def rooms(self):
        return self._rooms
