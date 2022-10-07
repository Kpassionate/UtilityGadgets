#!/usr/bin/python
# -*- coding:utf-8 -*-

import os


class FileStatist(object):
    def __init__(self):
        self.index = 0

    def get_all_file(self, lj):
        lj_list = os.listdir(lj)
        for item_lj in lj_list:
            new_lj = os.path.join(lj, item_lj)
            if os.path.isfile(new_lj):
                # print(new_lj)
                self.index += 1
            else:
                self.get_all_file(new_lj)
        return self.index


if __name__ == '__main__':
    d = FileStatist()
    path = '/Users/akai/ME/xz_work/report_system'
    res = d.get_all_file(path)
    print(res)
