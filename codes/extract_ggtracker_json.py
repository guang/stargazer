"""     @author:        Guang Yang
        @mktime:        1/21/2015
        @description:   Extract Information from GGtracker Parsed JSONs for
                        simple and extended matches
"""
import json
import numpy as np


def read_json(fname):
    """ open json file puts it into dictionary """
    with open(fname, 'r') as my_json:
        my_dict = json.load(my_json)
    return my_dict


def match_invariant_about_match(simple_matches):
    temp = []
    # match_id
    temp.append(simple_matches['id'])
    # replay_id
    temp.append(simple_matches['replays'][0]['id'])
    # replay_url
    temp.append(simple_matches['replays'][0]['url'])
    # release_string
    temp.append(simple_matches['release_string'])
    # expansion
    temp.append(simple_matches['expansion'])
    # map_name
    temp.append(simple_matches['map']['name'])
    # map_id
    temp.append(simple_matches['map']['id'])
    # map_url
    temp.append(simple_matches['map_url'])
    # game_type
    temp.append(simple_matches['game_type'])
    # game_category
    temp.append(simple_matches['category'])
    # duration_seconds
    temp.append(simple_matches['duration_seconds'])
    # winning_team
    temp.append(simple_matches['winning_team'])
    # ended_at
    temp.append(simple_matches['ended_at'])

    return temp
#     temp.append(simple_matches['entities'][0]['identity']['id'])
#     temp.append(simple_matches['entities'][0]['identity']['bnet_id'])
#     temp.append(simple_matches['entities'][0]['identity']['name'])
#     temp.append(simple_matches['entities'][0]['identity']['current_league_1v1'])
#     temp.append(simple_matches['entities'][0]['identity']['current_rank_1v1'])
#     temp.append(simple_matches['entities'][0]['identity']['matches_count'])
#     temp.append(simple_matches['entities'][0]['identity']['season_games'])
#     temp.append(simple_matches['entities'][0]['identity']['career_games'])
#     temp.append(simple_matches['entities'][0]['identity']['profile_url'])
#     temp.append(simple_matches['entities'][0]['minutes'][minute])
#     temp.append(simple_matches['entities'][0]['apm'])
#     temp.append(simple_matches['entities'][0]['identity']['stats']['apm']['avg'])
#     temp.append(simple_matches['entities'][0]['identity']['stats']['wpm']['avg'])
#     temp.append(simple_matches['entities'][0]['identity']['most_played_race'])
#     temp.append(simple_matches['entities'][0]['identity']['hours_played'])
#     temp.append(simple_matches['entities'][0]['win'])
#     temp.append(simple_matches['entities'][0]['race'])
#     temp.append(simple_matches['entities'][0]['average_unspent_resources'])
#     temp.append(  need to change naming here
#     temp.append(*NOTE* cleared ['entities'][0]['identity'], still have alot that need parsed, need to change
#     temp.append(naming style to get all 3 layers for basic stats being tracked.
#     temp.append(simple_matches['entities'][1]['identity']['id'])
#     temp.append(simple_matches['entities'][1]['identity']['bnet_id'])
#     temp.append(simple_matches['entities'][1]['identity']['name'])
#     temp.append(simple_matches['entities'][1]['identity']['current_league_1v1'])
#     temp.append(simple_matches['entities'][1]['identity']['current_rank_1v1'])
#     temp.append(simple_matches['entities'][1]['identity']['matches_count'])
#     temp.append(simple_matches['entities'][1]['identity']['season_games'])
#     temp.append(simple_matches['entities'][1]['identity']['career_games'])
#     temp.append(simple_matches['entities'][1]['identity']['profile_url'])
#     temp.append(simple_matches['entities'][1]['minutes'][minute])
#     temp.append(simple_matches['entities'][1]['apm'])
#     temp.append(simple_matches['entities'][1]['identity']['stats']['apm']['avg'])
#     temp.append(simple_matches['entities'][1]['identity']['stats']['wpm']['avg'])
#     temp.append(simple_matches['entities'][1]['identity']['most_played_race'])
#     temp.append(simple_matches['entities'][1]['identity']['hours_played'])
#     temp.append(simple_matches['entities'][1]['win'])
#     temp.append(simple_matches['entities'][1]['race'])


def match_specific_snapshot(extended_matches, player0_id, player1_id):
    temp = []
    # player 0
    temp.append(extended_matches['VespeneCollectionRate'][player0_id])
    temp.append(extended_matches['VespeneCurrent'][player0_id])
    temp.append(extended_matches['MineralsCollectionRate'][player0_id])
    temp.append(extended_matches['MineralsCurrent'][player0_id])
    temp.append(extended_matches['SupplyUsage'][player0_id][firstcolumn])
    temp.append(extended_matches['SupplyUsage'][player0_id][secondcolumn])
    temp.append(extended_matches['WorkersActiveCount'][player0_id])
    temp.append(extended_matches['Lost'][player0_id])
    # player 1
    temp.append(extended_matches['VespeneCollectionRate'][player1_id])
    temp.append(extended_matches['VespeneCurrent'][player1_id])
    temp.append(extended_matches['MineralsCollectionRate'][player1_id])
    temp.append(extended_matches['MineralsCurrent'][player1_id])
    temp.append(extended_matches['SupplyUsage'][player1_id][firstcolumn])
    temp.append(extended_matches['SupplyUsage'][player1_id][secondcolumn])
    temp.append(extended_matches['WorkersActiveCount'][player1_id])
    temp.append(extended_matches['Lost'][player1_id])


def match_specific_byframe(extended_matches, player0_id, player1_id):
    temp.append(extended_matches['upgrades'][player1_id])
    temp.append(extended_matches['scouting'][player1_id])
    temp.append(extended_matches['num_bases'][1])
    temp.append(extended_matches['armies_by_frame'][player1_id])
    temp.append(extended_matches['aggressions'][player1_id])

    temp.append(extended_matches['upgrades'][player0_id])
    temp.append(extended_matches['scouting'][player0_id])
    temp.append(extended_matches['num_bases'][0])
    temp.append(extended_matches['armies_by_frame'][player0_id])
    temp.append(extended_matches['aggressions'][player0_id])


def frame_to_second(frame_val):
    """ note: rounds the output second """
    assert type(frame_val) == int
    return int(frame_val/16)


def find_player_id(simple_matches, player):
    assert player in ('player0', 'player1')
    if player == 'player0':
        return str(simple_matches['entities'][0]['identity']['id'])
    else:
        return str(simple_matches['entities'][1]['identity']['id'])


def extract_match_invariant(simple_matches):
    """ Main Part 1 """
    temp_about_match = match_invariant_about_match(simple_matches)
    return temp_about_match


def extract_match_specific(extended_matches, player0_id, player1_id):
    """ Main Part 2 """
    temp = np.array()
    match_specific_snapshot(extended_matches, player0_id, player1_id):
    match_specific_byframe(extended_matches, player0_id, player1_id):
    pass


def construct_match_events(match_invariant, match_specific):
    pass


if __name__ == "__main__":
    # loading
    simple_match_fname = ("/Users/guangyang/Work/project_insight/data/raw/"
                          "matches_5746684_simple.json")
    extended_match_fname = ("/Users/guangyang/Work/project_insight/data/raw/"
                            "matches_5746684_extended.json")
    simple_match = read_json(simple_match_fname)
    extended_match = read_json(extended_match_fname)

    # match-invariant
    match_invariant_part = extract_match_invariant(simple_match)

    # match-specific
    player0 = find_player_id(simple_match, 'player0')
    player1 = find_player_id(simple_match, 'player1')
    total_timestamp_num = find_total_timestamp_num(extended_match)

    match_specific_part = extract_match_specific(extended_match,
                                                 player0, player1)

    # all together now
    result = construct_match_events(match_invariant_part, match_specific_part)

    # TODO Add Validations here maybe?
