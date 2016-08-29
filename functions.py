
import pickle
import random

from const import *
from Structure import Structure
from Room import Room


def build_stronghold():
    """
    Prompts the user with various questions to build up a structure.
    :return: [Structure] the structure object.
    """
    print_structure_list()

    ts = None
    while ts is None:
        try:
            idx = int(raw_input('\nSelect the main structure for the stronghold: '))
            if idx < 0 or idx > len(BUILDABLE_STRUCTURES):
                raise IndexError
            ts = BUILDABLE_STRUCTURES[idx]
        except (IndexError, TypeError):
            print '[!] Invalid selection.'

    br = next((item for item in ROOMS if ts['bonus_room'] in item['name']), None)

    if br is not None:
        print '[+] The {} comes with {} as a bonus room.\n'.format(ts['name'], br['name'])
    else:
        print '[+] Select a bonus room for the {}.'.format(ts['name'])
        br = select_room(ts['bonus_room'])
        print '[+] {} selected as the bonus room for the stronghold.\n'.format(br['name'])

    ts['bonus_room'] = br['name']
    s = Structure(**ts)

    while s.room_points_remaining > 0:
        r = select_room()
        if r['multiple'] is False and s.contains_room(r['name']):
            print '[-] Structure already contains a {}.'.format(r['name'])
        else:
            s.add_room(r['name'])

    while 'Y' == raw_input('[+] Do you want to add another room to the structure (Y/n)? '):
        r = select_room()
        if r['multiple'] is False and s.contains_room(r['name']):
            print '[-] Structure already contains a {}.'.format(r['name'])
        else:
            s.add_room(r['name'])

    return s


def load_stronghold(fn):
    """
    Loads a previously built structure.
    :param fn: [str] filename of file containing structure.
    :return: [Structure] the structure object.
    """
    fin = open(fn, 'r')
    s = pickle.loads(fin.read())
    return s


def save_stronghold(s, fn):
    """
    Writes the specified structure to a file.
    :param s: [Structure] the structure to write.
    :param fn: [str] the filename to write the structure to.
    :return: None
    """
    assert isinstance(s, Structure)
    assert isinstance(fn, str)

    fout = open(fn, 'w')
    fout.write(pickle.dumps(s))
    fout.close()


def calculate_taxes():
    """
    Calculates the taxes imposed on the stronghold.
    :return: [int] the amount of taxes.
    """
    return 0


def calculate_earnings(s, weeks):
    """
    Calculates the earnings for the structure for the number of weeks specified.

    :param s: [Structure] the structure to calculate earnings for.
    :param weeks: [int] the number of weeks to calculate the earnings for.
    :return: None
    """
    assert isinstance(s, Structure)
    assert isinstance(weeks, int)

    total = 0

    for i in range(weeks):
        income = 0
        cost = 0

        print '\n[+] WEEK {}:'.format(i)

        for r in s.rooms:
            assert isinstance(r, Room)
            income += r.calculate_function()

        cost += s.skilled_hirelings * next((item['pay'] for item in HIRELINGS if item['hireling'] == 'Skilled'), 0) * 7
        cost += s.unskilled_hirelings * next((item['pay'] for item in HIRELINGS if item['hireling'] == 'Unskilled'), 0) * 7
        cost += calculate_taxes()

        print '[+] The total cost to run the structure for week {} is {} GP.'.format(i, cost)
        print '[+] The total earnings (income - cost) for week {} is {} GP.'.format(i, income - cost)

        total += income - cost

    print '\n[+] The overall total income for {} weeks is {} GP.'.format(weeks, total)


def select_room(limited=None):
    """
    Prompts the user to select a room.

    :param limited: [str, None] what rooms the user should be limited to.
    :return: [Dict] dictionary containing the selected room parameters.
    """
    print_room_list(limited)
    r = None
    while r is None:
        try:
            idx = int(raw_input('\nSelect a room for the stronghold: '))
            if idx < 0 or idx > len(ROOMS):
                raise IndexError
            r = ROOMS[idx]

            if limited is not None:
                if 'Any' not in limited and r['name'] not in limited:
                    r = None
                    raise
        except (TypeError, IndexError):
            print '[!] Invalid selection.'
    return r


def print_structure_list():
    """
    Prints the structure list.
    :return: None
    """
    s = '\nBuildable Structures:\n'
    for i in range(len(BUILDABLE_STRUCTURES)):
        s += '\t[{}]: {}\n'.format(i, BUILDABLE_STRUCTURES[i]['name'])
    print s


def print_room_list(limited=None):
    """
    Prints the room list.
    :param limited: [str, None] what rooms the user should be limited to.
    :return: None
    """
    s = '\nAvailable Rooms:\n'
    for i in range(len(ROOMS)):
        if limited is not None:
            if not ('Any' in limited or ROOMS[i]['name'] in limited):
                continue
        s += '\t[{}]: {}\n'.format(i, ROOMS[i]['name'])
    print s
