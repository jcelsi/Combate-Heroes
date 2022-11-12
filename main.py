"""
Main Module for simulating the battle between 2 hero teams
"""
import random
import argparse

from modules.team import Team
from utils.cli_printer import CliPrinter
from utils.fetcher import get_heroes_data
from utils.mail_sender import send_simple_message

def combat(hero_1, hero_2, printer):
    """
    Contains the logic for executing a combat between 2 heroes
    """
    contestants = []

    if hero_1.spd < hero_2.spd: 
        contestants = [hero_2, hero_1]
    else:
        contestants = [hero_1, hero_2]

    while True:
        turn(contestants[0], contestants[1], printer)
        if not contestants[1].is_alive:
            return {'winner': contestants[0], 'looser': contestants[1]}

        turn(contestants[1], contestants[0], printer)
        if not contestants[0].is_alive:
            return {'winner': contestants[0], 'looser': contestants[1]}

def turn(attacker_hero, defendant_hero, printer):
    """
    Randomly selects a hero attack type and executes the attack
    """
    attack_type = random.choice(['mental', 'fast', 'strong'])
    damage = attacker_hero.attack(defendant_hero, attack_type)

    printer.print_attack(attacker_hero, defendant_hero, attack_type, damage)

def update_team(team):
    """
    Executes team methods to prepare them for the next round
    """
    team.set_team_status()
    team.reorder()
    team.heal_members()

def main(args):
    """
    Contains the logic for executing the team battle
    """
    team_length = args.team_size
    printer = CliPrinter(0, args.colored)
    selected_heroes = get_heroes_data( 2 * team_length)

    team_1 = Team(selected_heroes[ 0 : team_length ], 'Team 1')
    team_2 = Team(selected_heroes[ team_length : 2 * team_length ], 'Team 2')

    while (team_1.is_not_defeated and team_2.is_not_defeated):

        printer.print_members(team_1, team_2)

        for count, heroes in enumerate(zip(team_1.members, team_2.members)):
            if (heroes[0].is_alive and heroes[1].is_alive):

                printer.print_figthers(heroes[0], heroes[1], count + 1)

                results = combat(heroes[0], heroes[1], printer)

                printer.print_hero_combat_results(results)

        update_team(team_1)
        update_team(team_2)

    printer.print_team_battle_results(team_1, team_2)

    if len(args.mail) > 0:
        send_simple_message(args.mail, printer.full_log)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--colored', action = argparse.BooleanOptionalAction, 
                                     help = 'Activates colored output for better readability')
    parser.add_argument('--team_size', default = 5, type = int,
                                     help = 'Number of members per team')
    parser.add_argument('--mail', default = '', type = str,
                                     help = 'Enter a mail address for receiving a mail with all the battle events')
    main(parser.parse_args())
