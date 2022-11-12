"""
This module contains the function for fetching the superhero api
and the function for returning a random sample of heroes
"""

import random
import requests

def fetch_all_heroes():
    """
    fetches the data of all heroes from the api.

    Parameters
    ----------
    None

    Returns
    -------
    heroes: array
        Array of heroes dictionaries.
    """
    try:
        response = requests.get(
                            'https://cdn.jsdelivr.net/gh/akabab/superhero-api@0.3.0/api/all.json',
                            timeout=30)
        response.raise_for_status()
    except requests.exceptions.HTTPError as err:
        raise SystemExit(err) from err
    heroes = response.json()
    return heroes

def get_heroes_data(number_of_heroes):
    """
    Select n random heroes fetched from the superhero api.

    Parameters
    ----------
    n: int
        Number of heroes to select.

    Returns
    -------
    selected_heroes: array
        Array of selected heroes dictionaries.
    """
    all_heroes = fetch_all_heroes()

    random_indexes = random.sample(range(len(all_heroes)), number_of_heroes)
    selected_heroes = []

    for index in random_indexes:

        # Modify in case of changes on structure of the hero api data
        hero_data_dict = {
            'name': all_heroes[index]['name'],
            'alignment': all_heroes[index]['biography']['alignment'],
            'intelligence': all_heroes[index]['powerstats']['intelligence'],
            'strength': all_heroes[index]['powerstats']['strength'],
            'speed': all_heroes[index]['powerstats']['speed'],
            'durability': all_heroes[index]['powerstats']['durability'],
            'power': all_heroes[index]['powerstats']['power'],
            'combat': all_heroes[index]['powerstats']['combat']
        }
        selected_heroes.append(hero_data_dict)

    return selected_heroes
