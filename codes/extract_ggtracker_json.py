"""     @author:        Guang Yang
        @mktime:        1/21/2015
        @description:   Extract Information from GGtracker Parsed JSONs for
                        simple and extended matches
"""
import json


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
# extended_matches['VespeneCollectionRate'][player0_id])
# extended_matches['VespeneCurrent'][player0_id])
# extended_matches['MineralsCollectionRate'][player0_id])
# extended_matches['MineralsCurrent'][player0_id])
# extended_matches['SupplyUsage'][player0_id][first column])
# extended_matches['SupplyUsage'][player0_id][second column])
# extended_matches['WorkersActiveCount'][player0_id])
# extended_matches['Lost'][player0_id])
# extended_matches['upgrades'][player0_id])
# extended_matches['scouting'][player0_id])
# extended_matches['num_bases'][0])
#   *Need to look up how this is coded up*
# extended_matches['armies_by_frame'][player0_id])
# extended_matches['aggressions'][player0_id])
#   *Need to look up how this is coded up*
# extended_matches['VespeneCollectionRate'][player1_id])
# extended_matches['VespeneCurrent'][player1_id])
# extended_matches['MineralsCollectionRate'][player1_id])
# extended_matches['MineralsCurrent'][player1_id])
# extended_matches['SupplyUsage'][player1_id][first column])
# extended_matches['SupplyUsage'][player1_id][second column])
# extended_matches['WorkersActiveCount'][player1_id])
# extended_matches['Lost'][player1_id])
# extended_matches['upgrades'][player1_id])
# extended_matches['scouting'][player1_id])
# extended_matches['num_bases'][1])
# extended_matches['armies_by_frame'][player1_id])
# extended_matches['aggressions'][player1_id])


def extract_match_invariant(simple_matches):
    temp_about_match = match_invariant_about_match(simple_matches)
    return temp_about_match


def extract_match_specific(extended_matches):
    pass

if __name__ == "__main__":
    simple_match_fname = ("/Users/guangyang/Work/project_insight/data/raw/"
                          "matches_5746684_simple.json")
    extended_match_fname = ("/Users/guangyang/Work/project_insight/data/raw/"
                            "matches_5746684_extended.json")
    simple_match = read_json(simple_match_fname)
    extended_match = read_json(extended_match_fname)
    match_invariant_part = extract_match_invariant(simple_match)
    match_specific_part = extract_match_specific(extended_match)
    # TODO Add Validations here maybe?
    # output = [match_invariant_part match_specific_part]
