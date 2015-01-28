"""    @author:            Guang Yang
       @mktime:            1/27/2015
       @description:       Connect and write json data to s3
"""

import os
import boto
from boto.s3.key import Key


def store_simple(file_name_path, file_name, bucket):
    """ stores simple match details in match_simple bucket on S3
    """

    k = Key(bucket)
    k.key = file_name
    k.set_contents_from_filename(file_name_path)


def store_extended(file_name_path, file_name, bucket):
    """ stores extended match details in match_extended bucket on S3 """

    k = Key("match_extended")
    k.key = file_name
    k.set_contents_from_filename(file_name_path)


def store_all(file_dir, match_type, bucket):
    """ puts whole directory of simple or extended files into S3
    """

    matches = os.listdir(file_dir)
    for match in matches:
        match_path = "{}/{}".format(file_dir, match)
        if match_type == "simple":
            store_simple(match_path, match, bucket)
        elif match_type == "extended":
            store_extended(match_path, match, bucket)
        else:
            print("-ruh roh- Unknown match_type, please specify simple or "
                  "extended.")


if __name__ == "__main__":
    conn = boto.connect_s3()
    current_dir = os.getcwd()

    my_bucket = conn.get_bucket('guang-stargazer-raw-json')

    match_simple_dir = "{}/../../data/raw/match_simple".format(current_dir)
    match_extended_dir = "{}/../../data/raw/match_extended".format(current_dir)

    store_all(match_simple_dir, 'simple', my_bucket)
    # store_all(match_extended_dir, 'extended')
