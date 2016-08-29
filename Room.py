class Room:
    def __init__(self, name, description, size_cost, construction_cost, construction_time, benefits, other_names, multiple, calculate_function, half_cost=False):
        """
        Initializes the Room object.

        :param name: [str] the name of the room (should be the name of an entry in the ROOMS list)
        :param description: [str, None] the description of the room
        :param size_cost: [int] the number of room points this room requires
        :param construction_cost: [int] the construction cost of the structure in GP
        :param construction_time: [int] the construction time of the structure in DAYS
        :param benefits: [str, None] the benefits provided by this room
        :param other_names: [list, None] the other names that this room can be called
        :param multiple: [bool] True if a structure can contain more than one of this room type
        :param calculate_function: [func] callback function for calculating cost and income
        :param half_cost: [bool] True if the room is purchased at half cost (for some structures)
        """
        assert isinstance(name, str), \
            '[Room::__init__] name must be a string - {}'.format(name)
        assert isinstance(description, str) or description is None, \
            '[Room::__init__] description must be a string or None - {}'.format(description)
        assert isinstance(size_cost, int), \
            '[Room::__init__] size_cost must be an int - {}'.format(size_cost)
        assert isinstance(construction_cost, int), \
            '[Room::__init__] cost must be an int - {}'.format(construction_cost)
        assert isinstance(construction_time, int), \
            '[Room::__init__] time must be an int - {}'.format(construction_time)
        assert isinstance(benefits, str) or benefits is None, \
            '[Room::__init__] benefits must be a string or None - {}'.format(benefits)
        assert (isinstance(other_names, list) and len(filter(lambda x: isinstance(x, str), other_names)) == len(
            other_names)) or other_names is None, \
            '[Room::__init__] other_names must be a list of strings or None - {}'.format(other_names)
        assert isinstance(multiple, bool), \
            '[Room::__init__] multiple must be a boolean - {}'.format(multiple)
        assert isinstance(half_cost, bool), \
            '[Room::__init__] half_cost must be a boolean - {}'.format(half_cost)

        self._name = name
        self._description = description
        self._size_cost = size_cost if half_cost is False else int(size_cost / 2)
        self._construction_cost = construction_cost
        self._construction_time = construction_time
        self._benefits = benefits
        self._other_names = other_names
        self._multiple = multiple
        self.calculate_function = calculate_function

    def __str__(self):
        """
        :return: [str] a string representation of this object.
        """
        s = '{}\nDescription: {}\nSize Cost: {}\nConstruction Cost: {:,} GP\nConstruction Time: {} Days\n' \
            'Benefits: {}\n'.format(self._name, self._description, self._size_cost,
                                    self._construction_cost, self._construction_time, self._benefits)

        if self._other_names is not None:
            s += 'Other Names: {}\n'.format(', '.join(self._other_names))
        return s

    @property
    def name(self):
        return self._name

    @property
    def description(self):
        return self._description

    @property
    def size_cost(self):
        return self._size_cost

    @property
    def construction_cost(self):
        return self._construction_cost

    @property
    def construction_time(self):
        return self._construction_time

    @property
    def benefits(self):
        return self._benefits

    @property
    def other_names(self):
        return self._other_names

    @property
    def multiple(self):
        return self._multiple
