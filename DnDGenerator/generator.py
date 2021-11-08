# DnD Random Name and Stat Generation Microservice
# Microservice accepts a JSON that will have 1 of 2 attributes
# used to determine which generation is being called, then returns appropriate
# response in JSON format

import random
import sqlite3
import json
from args import get_args


def generate_name(length, starting):
    """
    Generates random fantasy name.
    :param length: int, desired length of name
    :param starting: str, starting letters of name
    :return: fantasy name
    """

    if length is None:
        length = 100
    if starting is None:
        starting = ''

    # Establish connection to database
    conn = sqlite3.connect('names.db')
    c = conn.cursor()

    # Fetch data from database
    c.execute("SELECT name FROM names WHERE (length < ?) AND (name LIKE ?)",
              (str(length), starting+'%'))
    results = c.fetchall()  # returns a list of tuples

    # Choose a random result
    choice = random.choice(results)
    name = choice[0]

    return name

def generate_stats(method):
    """
    Runs either the standard method or the Drop Lowest technique for rolling DnD stats.
    Returns all 6 stat rolls.
    :return: JSON object / Python Dictionary
    """

    def drop_lowest():
        """
        Rolls 6 dice and drops the lowest and highest values, then returns sum of remaining values.
        :return: int
        """
        rolls = []
        for roll_number in range(6):
            roll = random.randint(1, 6)
            rolls.append(roll)
        rolls.remove(max(rolls))
        rolls.remove(min(rolls))
        total = 0
        for roll in rolls:
            total += roll
        return total

    stats = {
        'strength': None,
        'dexterity': None,
        'constitution': None,
        'intelligence': None,
        'wisdom': None,
        'charisma': None
    }

    if method == 'drop':
        for attribute in stats:
            stats[attribute] = drop_lowest()
    else:
        standard_array = [15, 14, 13, 12, 10, 8]
        for attribute in stats:
            roll = random.choice(standard_array)
            stats[attribute] = roll
            standard_array.remove(roll)

    return stats

response = None

# Get requested arguments
args = get_args()
if args.n:
    response = generate_name(args.l, args.fl)
elif args.s:
    response = generate_stats(args.t)

with open('response.json', 'w') as outfile:
    json.dump(response, outfile)
