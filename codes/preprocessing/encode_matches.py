"""    @author:            Guang Yang
       @mktime:            1/26/2015
       @description:       Encode simple or extended matches from json into avro
"""

from utilities import *     # NOQA
import avro.schema
from avro.datafile import DataFileWriter
from avro.io import DatumWriter


def get_writer(schema_file, output_file):
    """ Initialize by reading in schema file and create writer object
    that writes to desired file
    """

    schema = avro.schema.parse(open(schema_file).read())
    writer = DataFileWriter(open(output_file, "w"),
                            DatumWriter(),
                            schema)
    return writer


def encode_match_simple(schema, output, simple_matches):
    """
    """

    writer = get_writer(schema, output)
    writer.append({
        "match_id": simple_matches['id'],
        "replay_id": simple_matches['replays'][0]['id'],
        "replay_url": simple_matches['replays'][0]['url'],
        "release_string": simple_matches['release_string'],
        "expansion": simple_matches['expansion'],
        "map_name": simple_matches['map']['name'],
        "map_id": simple_matches['map']['id'],
        "map_url": simple_matches['map_url'],
        "game_type": simple_matches['game_type'],
        "game_category": simple_matches['category'],
        "duration_seconds": simple_matches['duration_seconds'],
        "winning_team": simple_matches['winning_team'],
        "ended_at": simple_matches['ended_at'],
        "player0_id": simple_matches['entities'][0]['identity']['id'],
        "player1_id": simple_matches['entities'][1]['identity']['id'],
        "player0_bnet_id": simple_matches['entities'][0]['identity']['bnet_id'],
        "player1_bnet_id": simple_matches['entities'][1]['identity']['bnet_id'],
        "player0_name": simple_matches['entities'][0]['identity']['name'],
        "player1_name": simple_matches['entities'][1]['identity']['name'],
        "player0_current_league_1v1":
            simple_matches['entities'][0]['identity']['current_league_1v1'],
        "player1_current_league_1v1":
            simple_matches['entities'][1]['identity']['current_league_1v1'],
        "player0_current_rank_1v1":
            simple_matches['entities'][0]['identity']['current_rank_1v1'],
        "player1_current_rank_1v1":
            simple_matches['entities'][1]['identity']['current_rank_1v1'],
        "player0_matches_count":
            simple_matches['entities'][0]['identity']['matches_count'],
        "player1_matches_count":
            simple_matches['entities'][1]['identity']['matches_count'],
        "player0_season_games":
            simple_matches['entities'][0]['identity']['season_games'],
        "player1_season_games":
            simple_matches['entities'][1]['identity']['season_games'],
        "player0_career_games":
            simple_matches['entities'][0]['identity']['career_games'],
        "player1_career_games":
            simple_matches['entities'][1]['identity']['career_games'],
        "player0_profile_url":
            simple_matches['entities'][0]['identity']['profile_url'],
        "player1_profile_url":
            simple_matches['entities'][1]['identity']['profile_url'],
        "player0_apm_match": simple_matches['entities'][0]['apm'],
        "player1_apm_match": simple_matches['entities'][1]['apm'],
        "player0_apm_career":
            simple_matches['entities'][0]['identity']['stats']['apm']['avg'],
        "player1_apm_career":
            simple_matches['entities'][1]['identity']['stats']['apm']['avg'],
        "player0_wpm_career":
            simple_matches['entities'][0]['identity']['stats']['wpm']['avg'],
        "player1_wpm_career":
            simple_matches['entities'][1]['identity']['stats']['wpm']['avg'],
        "player0_most_played_race":
            simple_matches['entities'][0]['identity']['most_played_race'],
        "player1_most_played_race":
            simple_matches['entities'][1]['identity']['most_played_race'],
        "player0_hours_played":
            simple_matches['entities'][0]['identity']['hours_played'],
        "player1_hours_played":
            simple_matches['entities'][1]['identity']['hours_played'],
        "player0_win": simple_matches['entities'][0]['win'],
        "player1_win": simple_matches['entities'][1]['win'],
        "player0_race": simple_matches['entities'][0]['race'],
        "player1_race": simple_matches['entities'][1]['race'],
        "player0_avg_unspent_resources":
            simple_matches['entities'][0]['summary']
            ['average_unspent_resources'],
        "player1_avg_unspent_resources":
            simple_matches['entities'][1]['summary']
            ['average_unspent_resources'],
    })
    writer.close()


if __name__ == "__main__":
    encoded_simple = "dummy_match_1_simple.avro"
    schema_simple = "schema_match_simple.avsc"

    simple_match = read_json("tests/matches_5720000_simple.json")
    encode_match_simple(schema_simple, encoded_simple, simple_match)
