# -*- coding:utf8 -*-
import numpy as np
import matplotlib.pyplot as plt
from constitution_2 import *
from joint_type34_process_step1_field_history import *

if __name__ == '__main__':

    dict_rf3_1 = {
        'beam1_edge': 'Node ASSEMBLY.3',
        'beam2_edge': 'Node ASSEMBLY.4',
        'beam3_edge': 'Node ASSEMBLY.5',
    }

    dict_rf1_rf2_rf3_1 = {'support1_edge': 'Node ASSEMBLY.14',
                          'support2_edge': 'Node ASSEMBLY.15'}

    dict_u123_1 = {
        'beam1_up': 'Node ASSEMBLY.6',
        'beam1_down': 'Node ASSEMBLY.7',
        'beam2_up': 'Node ASSEMBLY.8',
        'beam2_down': 'Node ASSEMBLY.9',
        'beam3_up': 'Node ASSEMBLY.10',
        'beam3_down': 'Node ASSEMBLY.11',
        'beam4_up': 'Node ASSEMBLY.12',
        'beam4_down': 'Node ASSEMBLY.13',

    }

    get_percent('Job-1', 'SET-PART-PLATE', steel_yield)
    get_percent('Job-1', 'SET-PART-BEAM1', steel_yield)
    get_percent('Job-1', 'SET-PART-BEAM2', steel_yield)
    get_percent('Job-1', 'SET-PART-BEAM3', steel_yield)


    read_history(dict_rf3_1,dict_rf1_rf2_rf3_1, dict_u123_1)











