# -*- coding: utf-8 -*-

from region_mapping import mohu_dict, title_dict, fulltitle_dict


def get_region_code(content):
    if not content:
        return None
    for key in fulltitle_dict:
        end = key[-2:]
        if end == '城关' or end == '和平':
            continue
        if key in content:
            the_region = key
            return the_region
    for key in mohu_dict:
        if key in content:
            the_region = mohu_dict[key]
            return the_region
    for key in title_dict:
        if key in content:
            the_region = title_dict[key]
            return the_region
    return None


print(get_region_code('松原'))
