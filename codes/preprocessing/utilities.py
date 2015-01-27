"""    @author:            Guang Yang
       @mktime:            1/26/2015
       @description:       Utility functions for encoding/decoding avro files
"""
import json


def read_json(fname):
    """ Open json file puts it into dictionary """

    with open(fname, 'r') as my_json:
        my_dict = json.load(my_json)
    return my_dict
