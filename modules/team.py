"""
This module contains the Team class.
"""
from modules.hero import Hero

class Team:
    """
    Defines a team of heroes.

    ...

    Attributes
    ----------
    members : array
        Array of hero members.
    alignment : str
        Team alignment given by the most common member's alignment. Can be 'good', 'bad' or 'neutral'
    is_not_defeated : bool
        True if at least on member of the team is alive.
    """

    def __init__(self, data_list, name):
        """
        Creates a team, defining its members and team name.

        Parameters
        ----------
        data_list : array
            Array of dictionaries with the info of every hero.
        name : str
            Team name.
        """
        self.members = []
        self.alignment = self.__get_alignment(data_list)
        self.is_not_defeated = True
        self.name = name

        for hero_data in data_list:
            hero = Hero(hero_data, self.alignment)
            self.members.append(hero)

    def __get_alignment(self, data_list):
        # Definess the alignment of the team taking the most repeated alignment from its members
        alignment_array = []
        for hero_data in data_list:
            alignment_array.append(hero_data['alignment'])
        return max(set(alignment_array), key = alignment_array.count)

    def reorder(self):
        """
        Reorders the team, leaving the dead members at the end of the array.

        Returns
        -------
        None
        """
        self.members.sort(key=lambda x: x.is_alive, reverse=True)

    def set_team_status(self):
        """
        Sets the team's status to defeated if all members are dead

        Returns
        -------
        None
        """
        dead_counter = len([hero for hero in self.members if not hero.is_alive])
        if dead_counter == len(self.members):
            self.is_not_defeated = False

    def heal_members(self):
        """
        Fully heals alive members.

        Returns
        -------
        None
        """
        for hero in self.members:
            if hero.is_alive:
                hero.hp = hero.base_hp
