import sqlite3

from . import util

path = util.PATH

"""
This file contains functions to select rows from a table
"""


# Select everything from the table
# Returns column headers and rows
def select_all(table):
    query = """
            SELECT * FROM {0}
    """
    query = query.format(table)

    connection = sqlite3.connect(path)
    cursor = connection.cursor()
    cursor.execute(query)

    data = cursor.fetchall()
    titles = [description[0] for description in cursor.description]
    connection.close()

    return {
        "titles": titles,
        "data": data
    }


# Select a particular row from the table
def select(table, conditions):
    query = """
            SELECT * FROM {0}
            WHERE
    """
    query = query.format(table)
    query = util.add_conditions(query, conditions)

    connection = sqlite3.connect(path)
    cursor = connection.cursor()
    cursor.execute(query)

    data = cursor.fetchall()
    return data


# Select all characters (player and npc) in Drydock
def drydock_chars():
    query = """
        SELECT pc_id, name, player
        FROM pcs
        INNER JOIN region
            ON pcs.region_id = region.region_id
        UNION
        SELECT npc_id, name
        FROM npcs
        INNER JOIN region
            ON npcs.region_id = region.region_id;
    """


def list_dead():
    query = """
        SELECT pc_id, name, player
        FROM pcs
        WHERE NOT alive
        UNION
        SELECT npc_id, name
        FROM npcs
        WHERE NOT alive;
    """


def list_living():
    query = """
        SELECT pc_id, name, player
        FROM pcs
        WHERE alive
        UNION
        SELECT npc_id, name
        FROM npcs
        WHERE alive;
    """


def items_owned(owner_id):
    query = """
    
    """


def class_chars(dnd_class):
    pass


def org_chars():
    pass