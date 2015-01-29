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


def serialize_match_simple(schema, output, simple_match_json):
    """ Serialize simple match details from json into an avro file using
    specified schema.

    Args:
        schema:             The avro schema file (avsc) to be used for
                            serialization.
        output:             The file path where the resulting serialized avro
                            file is to be written.
        simple_match_json:     The raw json file to be serialized.
    """

    writer = get_writer(schema, output)
    writer.append({
        "match_id": simple_match_json['id'],
        "game_time": 0,
        "replay_id": simple_match_json['replays'][0]['id'],
        "replay_url": simple_match_json['replays'][0]['url'],
        "release_string": simple_match_json['release_string'],
        "expansion": simple_match_json['expansion'],
        "map_name": simple_match_json['map']['name'],
        "map_id": simple_match_json['map']['id'],
        "map_url": simple_match_json['map_url'],
        "game_type": simple_match_json['game_type'],
        "game_category": simple_match_json['category'],
        "duration_seconds": simple_match_json['duration_seconds'],
        "winning_team": simple_match_json['winning_team'],
        "ended_at": simple_match_json['ended_at'],
        "player0_id": simple_match_json['entities'][0]['identity']['id'],
        "player1_id": simple_match_json['entities'][1]['identity']['id'],
        "player0_bnet_id": simple_match_json['entities'][0]['identity']['bnet_id'],
        "player1_bnet_id": simple_match_json['entities'][1]['identity']['bnet_id'],
        "player0_name": simple_match_json['entities'][0]['identity']['name'],
        "player1_name": simple_match_json['entities'][1]['identity']['name'],
        "player0_current_league_1v1":
            simple_match_json['entities'][0]['identity']['current_league_1v1'],
        "player1_current_league_1v1":
            simple_match_json['entities'][1]['identity']['current_league_1v1'],
        "player0_current_rank_1v1":
            simple_match_json['entities'][0]['identity']['current_rank_1v1'],
        "player1_current_rank_1v1":
            simple_match_json['entities'][1]['identity']['current_rank_1v1'],
        "player0_matches_count":
            simple_match_json['entities'][0]['identity']['matches_count'],
        "player1_matches_count":
            simple_match_json['entities'][1]['identity']['matches_count'],
        "player0_season_games":
            simple_match_json['entities'][0]['identity']['season_games'],
        "player1_season_games":
            simple_match_json['entities'][1]['identity']['season_games'],
        "player0_career_games":
            simple_match_json['entities'][0]['identity']['career_games'],
        "player1_career_games":
            simple_match_json['entities'][1]['identity']['career_games'],
        "player0_profile_url":
            simple_match_json['entities'][0]['identity']['profile_url'],
        "player1_profile_url":
            simple_match_json['entities'][1]['identity']['profile_url'],
        "player0_apm_match": simple_match_json['entities'][0]['apm'],
        "player1_apm_match": simple_match_json['entities'][1]['apm'],
        "player0_apm_career":
            simple_match_json['entities'][0]['identity']['stats']['apm']['avg'],
        "player1_apm_career":
            simple_match_json['entities'][1]['identity']['stats']['apm']['avg'],
        "player0_wpm_career":
            simple_match_json['entities'][0]['identity']['stats']['wpm']['avg'],
        "player1_wpm_career":
            simple_match_json['entities'][1]['identity']['stats']['wpm']['avg'],
        "player0_most_played_race":
            simple_match_json['entities'][0]['identity']['most_played_race'],
        "player1_most_played_race":
            simple_match_json['entities'][1]['identity']['most_played_race'],
        "player0_hours_played":
            simple_match_json['entities'][0]['identity']['hours_played'],
        "player1_hours_played":
            simple_match_json['entities'][1]['identity']['hours_played'],
        "player0_win": simple_match_json['entities'][0]['win'],
        "player1_win": simple_match_json['entities'][1]['win'],
        "player0_race": simple_match_json['entities'][0]['race'],
        "player1_race": simple_match_json['entities'][1]['race'],
        "player0_avg_unspent_resources":
            simple_match_json['entities'][0]['summary']
            ['average_unspent_resources'],
        "player1_avg_unspent_resources":
            simple_match_json['entities'][1]['summary']
            ['average_unspent_resources'],
    })
    writer.close()


def serialize_match_extended_snapshot(schema, output, extended_match_json):
    """ Serialize the 10s snapshots from extended match details from json into
    timestamped avro files

    Args:
        schema:                 The avro schema file (avsc) to be used for
                                serialization.
        output:                 The file path where the resulting serialized
                                avro file is to be written.
        extended_match_json:    The raw json file to be serialized.
    """

    player0_id = get_player_id(extended_match_json, 0)
    player1_id = get_player_id(extended_match_json, 1)
    num_snapshot = get_num_snapshot(extended_match_json, player0_id)

    for snapshot in range(num_snapshot):
        snapshot_output = "{}_snapshot{}.{}".format(
            output.splitext(match_name)[0]),
            snapshot,
            output.splitext(match_name)[0]))

        writer = get_writer(schema, output)

    writer.append({
        "match_id": extended_match_json['id'],
        "game_time":
            extended_match_json['VespeneCollectionRate'][player0_id][snapshot]
    })




def serialize_match_extended_event(schema, output, extended_match_json):
    """ Ser
    """



def serialize_match(match_name, match_path, target_name, target_path,
                    match_type, schema):
    """ Serialize a single match in json into an avro file at specificed target
    path

    Args:
        match_name:     name of the match file (.json)
        match_path:     full path of the match file
        target_name:    name of the resulting avro file (.avro)
        target_path:    full path of the resulting avro file
        match_type:     simple, extended_snapshot, or extended_event
        schema:         schema file (.avsc) used in the process
    """
    try:
        match_json = read_json(match_path)
        try:
            if match_type == "simple":
                serialize_match_simple(schema, target_path, match_json)
                if match_json['game_type'] != "1v1":
                    print("Skipping {}: not 1v1".format(match_name))
                    os.remove(target_path)
                else:
                    print("Successfully wrote to {}".format(target_name))
            elif match_type == "extended_snapshot":
                serialize_match_extended_snapshot(schema, target_path,
                                                  match_json))
                if len(match_json['SupplyUsage'].keys()) != 2:
                    print("Skipping {}: not 1v1".format(match_name))
                    os.remove(target_path)
        except KeyError:
            print("Skipping {}: no file found".format(match_name))
            os.remove(target_path)
        except TypeError:
            print("Skipping {}: one player is AI".format(match_name))
            os.remove(target_path)
        except IndexError:
            print("Skipping {}: one player missing".format(match_name))
            os.remove(target_path)
    except ValueError:
        print("Skipping {}: file corrupted".format(match_name))


def batch_serialize_matches(source_dir, target_dir, match_type, schema):
    """ Serialize matches from source directory (raw jsons) to destination
    directory (serialized avros) by repeating calling serialize_match()

    Args:
        source_dir:     source directory where raw jsons are stored
        target_dir:     destination directory where the resulting serialized
                        avro files will live
        match_type:     simple, extended_snapshot, or extended_event
        schema:         schema to be enforced depending on match_type

    """

    match_names = os.listdir(source_dir)
    for match_name in match_names:
        match_path = "{}/{}".format(source_dir, match_name)
        # gotta change extension from .json to .avro for target name
        target_name = "{}.avro".format(os.path.splitext(match_name)[0])
        target_path = "{}/{}".format(target_dir, target_name)

        serialize_match(match_name, match_path, target_name, target_path,
                        match_type, schema)


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

    batch_serialize_matches(yolo_raw_simple_dir, yolo_parsed_simple_dir,
                            'simple', schema_simple)
