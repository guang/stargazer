"""    @author:            Guang Yang
       @mktime:            1/26/2015
       @description:       Decode simple or extended matches from json into avro
"""

from utilities import *     # NOQA
from avro.datafile import DataFileReader
from avro.io import DatumReader


def get_reader(input_file):
    """ Reading in avro
    """

    reader = DataFileReader(open(input_file, "r"), DatumReader())
    return reader


if __name__ == "__main__":
    encoded_simple = "dummy_match_1_simple.avro"

    avro_reader = get_reader(encoded_simple)
    for line in avro_reader:
        print(line)
    avro_reader.close()
