"""
This module contains the Hero class.
"""
import random

class Hero:
    """
    Defines a Hero.

    ...

    Attributes
    ----------
    name : str
        Name of the hero.
    alignment : str
        Can be 'good', 'bad' or 'neutral'.
    sta : int
        Stamina stat.
    fb : float
        Alignment factor for multiplying stats and damage.
    int : int
        Intelligence stat.
    str : int
        Strength stat.
    spd : int
        Speed stat.
    dur : int
        Durability stat.
    pow : int
        Power stat.
    cbt : int
        Combat stat.
    hp : int
        Current health points.
    base_hp: int
        Max health points.
    is_alive : bool
        True if the hero is alive.
    """
    def __init__(self, hero_data, team_aligment):
        """
        Initilizes a hero.

        Parameters
        ----------
        hero_data : dict
            Dict with hero data.
        team_aligment: str
            Team alignment. Can be 'good', 'bad' or 'neutral'.
        """
        self.name = hero_data['name']
        self.alignment = hero_data['alignment']

        self.sta = random.randint(0,10)
        self.fb = self.__calculate_aligment_factor(team_aligment)

        self.int = self.__calculate_stat(hero_data['intelligence'])
        self.str = self.__calculate_stat(hero_data['strength'])
        self.spd = self.__calculate_stat(hero_data['speed'])
        self.dur = self.__calculate_stat(hero_data['durability'])
        self.pow = self.__calculate_stat(hero_data['power'])
        self.cbt = self.__calculate_stat(hero_data['combat'])

        self.base_hp = self.__calculate_hp()
        self.hp = self.base_hp
        self.is_alive = True

    def __calculate_hp(self):
        return int((self.str * 0.8 + self.dur * 0.7 + self.pow) / 2 * (1 + self.sta / 10)) + 100

    def __calculate_stat(self, base_stat):
        return int((2 * self.fb * (base_stat + self.sta)) / 1.1)

    def __calculate_aligment_factor(self, team_aligment):
        aligment_factor = 1 if self.alignment == team_aligment else -1
        return (1.0 + random.randint(0, 9)) ** aligment_factor

    def __calculate_mental_attack_dmg(self):
        return int((self.int * 0.7 + self.spd * 0.2 + self.cbt * 0.1 ) * self.fb)

    def __calculate_strong_attack_dmg(self):
        return int((self.str * 0.6 + self.pow * 0.2 + self.cbt * 0.2 ) * self.fb)

    def __calculate_fast_attack_dmg(self):
        return int((self.spd * 0.55 + self.dur * 0.25 + self.str * 0.2 ) * self.fb)

    def attack(self, defendant, attack_type):
        """
        Method for attacking an oponent
        defendant: hero to be attacked

        Parameters
        ----------
        defendant : Hero object
            Hero receiving the attack
        attack_type: str
            Type of the attack. Can be 'mental', 'strong' or 'fast'

        Returns
        -------
        damage: int
            damage dealt by the attack.
        """
        match attack_type:
            case 'mental':
                damage = self.__calculate_mental_attack_dmg()
            case 'strong':
                damage = self.__calculate_strong_attack_dmg()
            case 'fast':
                damage = self.__calculate_fast_attack_dmg()

        defendant.hp = defendant.hp - damage
        if defendant.hp <=0:
            defendant.hp = 0
            defendant.is_alive = False

        return damage
    