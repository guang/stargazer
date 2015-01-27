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




def yolo_encode_match_simple(writer, simple_matches):
    # match_id
    writer.append({
        "match_id": simple_matches['id'],
        "replay_id": simple_matches['replays'][0]['id'],
        "replay_url": simple_matches['replays'][0]['url'],
        "release_string": simple_matches['release_string'],
        "expansion": simple_matches['expansion'],
    })

    # # map_name
    # writer.append(simple_matches['map']['name'])
    # # map_id
    # writer.append(simple_matches['map']['id'])
    # # map_url
    # writer.append(simple_matches['map_url'])
    # # game_type
    # writer.append(simple_matches['game_type'])
    # # game_category
    # writer.append(simple_matches['category'])
    # # duration_seconds
    # writer.append(simple_matches['duration_seconds'])
    # # winning_team
    # writer.append(simple_matches['winning_team'])
    # # ended_at
    # writer.append(simple_matches['ended_at'])

    # return writer


# def yolo_decode_match_simple(writer, encoded_simple_matches):


if __name__ == "__main__":
    encoded_simple = "dummy_match_1_simple.avro"
    schema_simple = "schema_match_simple.avsc"

    simple_match = read_json("tests/matches_5720000_simple.json")
    avro_writer = get_writer(schema_simple, encoded_simple)
    yolo_encode_match_simple(avro_writer, simple_match)
    avro_writer.close()

