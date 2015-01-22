"""     @author:        Guang Yang
        @mktime:        1/21/2015
        @description:   Extract Information from GGtracker Parsed JSONs for
                        simple and extended matches
"""
from extract_ggtracker_json import *            # NOQA


def test_frame_to_second():
    frame1 = 213
    second1 = int(213/16)
    assert frame1 == second1
