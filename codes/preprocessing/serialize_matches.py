"""    @author:             Guang Yang
       @mktime:             1/26/2015
       @description:        Serialize simple or extended matches from json into
                            avro
"""

import os
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


def serialize_match_simple(schema, output, simple_matches):
    """ Serialize simple match details from json into an avro file using
    specified schema.

    Args:
        schema:             The avro schema file (avsc) to be used for
                            serialization.
        output:             The file path where the resulting serialized avro
                            file is to be written.
        simple_matches:     The raw json file to be serialized.
    """

    writer = get_writer(schema, output)
    writer.append({
        "match_id": simple_matches['id'],
        "game_time": 0,
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


def serialize_match_extended_snapshot(schema, output, extended_matches):
    """ Serialize the 10s snapshots from extended match details from json into
    timestamped avro files

    Args:
        schema:             The avro schema file (avsc) to be used for
                            serialization.
        output:             The file path where the resulting serialized avro
                            file is to be written.
        simple_matches:     The raw json file to be serialized.


    """

    writer = get_writer(schema, output)

    writer.append({
        "match_id": extended_matches['id'],
        "game_time":
            extended_matches['VespeneCollectionRate'][player0_id][snapshot]
    })


def get_num_snapshot(extended_matches):
    pass


def serialize_match_extended_event(schema, output, extended_matches):
    pass


def serialize_matches(source_dir, target_dir, match_type, schema):
    """ Serialize matches from source directory (raw jsons) to destination
    directory (serialized avros)
    """

    matches = os.listdir(source_dir)
    for match in matches:
        match_path = "{}/{}".format(source_dir, match)

        # gotta change extension from .json to .avro for target name
        target_name = "{}.avro".format(os.path.splitext(match)[0])
        target_path = "{}/{}".format(target_dir, target_name)

        if match_type == "simple":
            try:
                match_simple_json = read_json(match_path)
            except ValueError:
                print("Skipping {}: file corrupted".format(match))

            try:
                serialize_match_simple(schema, target_path, match_simple_json)
                if match_simple_json['game_type'] != "1v1":
                    print("Skipping {}: not 1v1".format(match))
                    os.remove(target_path)
                else:
                    print("Successfully wrote to {}".format(target_name))
            except KeyError:
                print("Skipping {}: no file found".format(match))
                os.remove(target_path)
            except TypeError:
                print("Skipping {}: one player is AI".format(match))
                os.remove(target_path)
            except IndexError:
                print("Skipping {}: one player missing".format(match))
                os.remove(target_path)

        elif match_type == "extended":
            match_extended_json = read_json(match_path)
            serialize_match_extended(schema, target_path, match_extended_json)
        else:
            print("-ruh roh- Unknown match_type, please specify simple or "
                  "extended.")


if __name__ == "__main__":
    current_dir = os.getcwd()
    # raw_simple_dir = "{}/../../data/raw/match_simple".format(current_dir)
    # raw_extended_dir = "{}/../../data/raw/match_extended".format(current_dir)

    # parsed_simple_dir = \
    #     "{}/../../data/parsed/match_simple".format(current_dir)
    # parsed_extended_dir = \
    #     "{}/../../data/parsed/match_extended".format(current_dir)

    schema_simple = "schema_match_simple.avsc"

    yolo_raw_simple_dir = \
        "{}/../../data/yolo_raw/match_simple".format(current_dir)
    yolo_parsed_simple_dir = \
        "{}/../../data/yolo_parsed/match_simple".format(current_dir)

    serialize_matches(yolo_raw_simple_dir, yolo_parsed_simple_dir, 'simple',
                      schema_simple)
