#!/usr/bin/env python

from __future__ import print_function
import sys

print('Chess Tournament!')

if len(sys.argv) < 2:
    print('Syntax: {} <num_players>'.format(sys.argv[0]))
    sys.exit(-1)

num_players = int(sys.argv[1])
if num_players % 2 != 0:
    print('Odd number of players. Adding 1 (void player)')
    num_players += 1

num_tables = num_players / 2
num_rounds = num_players - 1
print('There will be {} tables and {} rounds'.format(num_tables, num_rounds))

tournament = [[None for table in range(num_tables)] for num_round in range(num_rounds)]


# First step: set first table && last player
for num_round in range(num_rounds):
    # Note that round 0 is really round 1
    if num_round % 2 == 0:
        tournament[num_round][0] = [None, num_players]
    else:
        tournament[num_round][0] = [num_players, None]


# Second step: from player 1 to player n-1 && from round 1, table 1 to round N, table M
player = 1
for num_round in range(num_rounds):
    for table in range(num_tables):
        if table == 0:
            if num_round % 2 == 0:
                tournament[num_round][table][0] = player
            else:
                tournament[num_round][table][1] = player
        else:
            tournament[num_round][table] = [player, None]
        player = (player % (num_players - 1)) + 1


# Third step: from player 1 to player n-1 && from round N, table M to round 1, table 1
player = 1
for num_round in reversed(range(num_rounds)):
    for table in reversed(range(num_tables)):
        if table != 0:
            tournament[num_round][table][1] = player
            player = (player % (num_players - 1)) + 1


# Show tournament
for num_round in range(num_rounds):
    print('\nRound {}: '.format(num_round + + 1), end='')
    for table in range(num_tables):
        print('{}-{} '.format(tournament[num_round][table][0], tournament[num_round][table][1]), end='')
