"""
Module with CliPrinter class used for printing battle events in the terminal.
"""
import time
from termcolor import colored

class CliPrinter:
    """
    Defines the CliPrinter

    ...

    Attributes
    ----------
    full_log: str
        Contains all battle events in html format.
    wait: int
        Time in seconds to wait between printing battle events.
    """
    def __init__(self, time_to_wait, color):
        """
        Creates a printer object

        Parameters
        ----------
        time_to_wait: int
            Time in seconds to wait between printing battle events.
        colored: bool
            Set to True for colored terminal output
        """
        self.full_log = ""
        self.wait = time_to_wait
        self.colored_mode = color

    def print_members(self, team_1, team_2):
        """
        Prints the members of the list. Green for alive members and red for out of combat.

        Parameters
        ----------
        team_1: Team object
            First team to print information.
        team_2: Team object
            Second team to print information.

        Returns
        -------
        None
        """
        print('\n' + '#' * 100)

        team_1_colored = colored(team_1.name,'blue')
        team_2_colored = colored(team_2.name,'magenta')
        colored_text = f"\n{ team_1_colored:<70}{team_2_colored:>47}"

        text = f"\n{ team_1.name:<50}{team_2.name:>50}"

        print(colored_text if self.colored_mode else text)
        self.full_log += ('<br><br><br><p style="text-align:left;">'
                                    f'{team_1.name}'
                                '<span style="float:right;">'
                                    f'{team_2.name}'
                                '</span>'
                               '</p>')

        for heroes in zip(team_1.members, team_2.members):

            team_1_hero_name = colored(heroes[0].name, 'green' if  heroes[0].is_alive else 'red')
            team_2_hero_name = colored(heroes[1].name, 'green' if  heroes[1].is_alive else 'red')
            colored_text = f"{team_1_hero_name:<70}{team_2_hero_name:>47}"

            team_1_hero_name = heroes[0].name if  heroes[0].is_alive else 'X ' + heroes[0].name
            team_2_hero_name = heroes[1].name if  heroes[1].is_alive else 'X ' + heroes[0].name
            text = f"{ team_1_hero_name:<50}{team_2_hero_name:>50}"

            print(colored_text if self.colored_mode else text)
            self.full_log += ('<p style="text-align:left;">'
                                    f'{team_1_hero_name}'
                                '<span style="float:right;">'
                                    f'{team_2_hero_name}'
                                '</span>'
                               '</p>')

        print('\n' + '-' * 100)
        time.sleep(self.wait)

    def print_figthers(self, hero_1, hero_2, count):
        """
        Prints the name of the characters figthing

        Parameters
        ----------
        hero_1: Hero object
            First hero to print information.
        hero_2: Hero object
            Second hero to print information.
        count: int
            Number of the combat.

        Returns
        -------
        None
        """
        print(f"\nBattle {count}:")
        self.full_log += f"<br>Battle {count}:<br>"
        

        hero_1_name_hp = f"{colored(hero_1.name,'blue')} ({hero_1.hp}/{hero_1.base_hp})"
        hero_2_name_hp = f"{colored(hero_2.name,'magenta')} ({hero_2.hp}/{hero_2.base_hp})"
        colored_text = f"\n{hero_1_name_hp :<59}vs{hero_2_name_hp:>58}\n"

        hero_1_name_hp = f"{hero_1.name} ({hero_1.hp}/{hero_1.base_hp})"
        hero_2_name_hp = f"{hero_2.name} ({hero_2.hp}/{hero_2.base_hp})"
        text = f"\n{hero_1_name_hp :<49}vs{hero_2_name_hp:>49}\n"

        print(colored_text if self.colored_mode else text)
        self.full_log += ('<p style="text-align:left;">'
                                    f'{hero_1_name_hp}'
                                '<span style="float:right;">'
                                    f'{hero_2_name_hp}'
                                '</span>'
                               '</p>')
        
        time.sleep(self.wait)

    def print_attack(self, attacker, defendant, attack_type, damage):
        """
        Prints the detail of the attack in the following format
        (attacker) attacked (defendant) with a (attack_type) attack, dealing (damage)

        Parameters
        ----------
        attacker: Hero object
            Attacker hero.
        defendant: Hero object
            Attrack receiving hero.
        attack_type: str
            Type of the attack executed by the attacker.
        damage: int
            Damage dealt by the attack.

        Returns
        -------
        None
        """

        attacker_name = f"{colored(attacker.name, 'yellow')}"
        defendant_name = f"{colored(defendant.name, 'yellow')}"
        colored_text = f"> {attacker_name} attacked {defendant_name} with a {attack_type} attack, dealing {damage} of damage"

        attacker_name = attacker.name
        defendant_name = defendant.name
        text = f"> {attacker_name} attacked {defendant_name} with a {attack_type} attack, dealing {damage} of damage"
        
        print(colored_text if self.colored_mode else text)
        self.full_log += (text + '<br>')

        text = f"> {defendant_name} hp: ({defendant.hp}/{defendant.base_hp}) "
        print(text)
        self.full_log += (text + '<br>')

        time.sleep(self.wait)

    def print_hero_combat_results(self, results):
        """
        Prints the results of the fight between 2 heroes

        Parameters
        ----------
        results: dict
            Dictionary with the winner and looser of a combat.

        Returns
        -------
        None
        """

        colored_text = f"\n>> {colored(results['winner'].name, 'green')} defeated {colored(results['looser'].name, 'red')}"

        text = f"\n>> {results['winner'].name} defeated {results['looser'].name}"
    
        print(colored_text if self.colored_mode else text)
        self.full_log += (text + '<br>')
        time.sleep(self.wait)

    def print_team_battle_results(self, team_1, team_2):
        """
        Prints the results of the battle between 2 teams

        Parameters
        ----------
        team_1: Team object
            First team to print information.
        team_2: Team object
            Second team to print information.

        Returns
        -------
        None
        """
        self.print_members( team_1, team_2)

        colored_winner = colored(team_1.name, 'blue') if team_1.is_not_defeated else colored(team_2.name, 'magenta')

        winner = team_1.name if team_1.is_not_defeated else team_2.name

        text = f"\n>>> WINNER: {colored_winner if self.colored_mode else winner}"
        print(text)

        self.full_log += f"<br>>>> WINNER: <strong>{winner}</strong>"
