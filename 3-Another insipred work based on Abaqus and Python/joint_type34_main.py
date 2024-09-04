# -*- coding:utf8 -*-
import os
import sys
import shutil
import uuid
import warnings
import time
import numpy as np
from constitution_2 import *
from joint_type34_process_step2_result import *


def core(path, inter_outer,
         geometry_column,geometry_plate,geometry_beam_input,geometry_support_board,
         matrerial_name, material_support,):

    """
       主计算程序
       :param path: 文件储存路径
       :param inter_outer: 内环板0;  or 外环板1；
       :param geometry_column: [圆柱高度H， 圆柱半边长d2， 环板半边长d1(d3)， 圆柱钢管厚度t_tube, 柱倾斜角度β]
       :param geometry_plate: [梁腹板高度h，环板厚度t_web]
       :param geometry_beam_input: [[梁长度L1，梁翼缘宽度length_flange_beam(1)，梁腹板厚度thick_web_beam(1)],
                                    [梁长度L2，梁翼缘宽度length_flange_beam(2)，梁腹板厚度thick_web_beam(2)],
                                    [梁长度L3，梁翼缘宽度length_flange_beam(3)，梁腹板厚度thick_web_beam(3)]]

       :param geometry_support_board: 填板几何信息 [支撑的内径R4, 支撑的外径R5, L1_bracket, L2_bracket, L3_bracket, L4_bracket,
                                        L5_bracket, L6_bracket,斜撑倾斜角度aplha，  支托腹板厚度， 斜撑翼缘宽度， 斜撑翼缘厚度 ]
       :param matrerial_name: ['柱钢材标号','柱混凝土标号']
       :param material_support: ['柱钢材标号']
       钢材标号：['Q235', 'Q345', 'Q390', 'Q420']
       混凝土标号：['C30', 'C35', 'C40', 'C45', 'C50', 'C55', 'C60', 'C65', 'C70', 'C75', 'C80']
       :return:
       """

    size_mesh = [75, 75]
    num_beams = 3
    num_supports = 2
    compute_set = [50, 8, 2]

    support_compress = 45000

    geometry_support_board.insert(2, (0.0, 0.0))

    circle_column = geometry_column[1]
    if inter_outer == 1:  # outer
        geometry_column.insert(1, circle_column - 5)
    else:  # inter
        geometry_column.insert(1, circle_column + 5)
        geometry_column[1], geometry_column[3] = geometry_column[3], geometry_column[1]

    geometry_beam_add = [geometry_column[3] + 200, 200, 2]
    geometry_beam_input.insert(3, geometry_beam_add)

    # 创建随机文件夹
    uuid_str = uuid.uuid4().hex
    # newFileFolder = os.getcwd() + '\\%s' % uuid_str
    newFileFolder = path + '\\%s' % uuid_str  # 随机文件夹
    os.mkdir(newFileFolder)
    # print(newFileFolder)

    # 确定当前路径（所需文件所在的路径）
    pathDefault = os.getcwd()

    # copy
    shutil.copy('joint_type34_make_model_user.py', newFileFolder)
    shutil.copy('joint_type34_process_user.py', newFileFolder)
    shutil.copy('joint_type34_make_model.py', newFileFolder)
    shutil.copy('joint_type34_process_step1_field_history.py', newFileFolder)
    shutil.copy('joint_type34_process_step2_result.py', newFileFolder)
    shutil.copy('constitution_2.py', newFileFolder)

    # 完善梁的几何尺寸矩阵
    geometry_beam_input = np.array(geometry_beam_input)
    geometry_beam_add = np.array([geometry_column[3]+200, 200,  2])
    if num_beams == 1:
        geometry_beam = np.vstack((geometry_beam_input, geometry_beam_add, geometry_beam_add, geometry_beam_add ) )
    elif num_beams == 2:
        geometry_beam = np.vstack((geometry_beam_input, geometry_beam_add, geometry_beam_add))
    elif num_beams == 3:
        geometry_beam = np.vstack((geometry_beam_input, geometry_beam_add ) )
    elif num_beams == 4:
        geometry_beam = geometry_beam_input

    # 需要用到的混凝土和钢材列表
    listConcrete = ['C30', 'C35', 'C40', 'C45', 'C50', 'C55', 'C60', 'C65', 'C70', 'C75', 'C80']
    listSteel = ['Q235', 'Q345', 'Q390', 'Q420']

    # 读取材料属性
    steel_plastic_tuple = get_steel_yield(matrerial_name[0])
    concrete_elastic_modu = get_concrete_parameters(matrerial_name[1])[0]
    concrete_compres_tuple = get_concrete_compressive_constitution(get_concrete_parameters(matrerial_name[1])[0],
                                                                   get_concrete_parameters(matrerial_name[1])[3])
    material_property = [steel_plastic_tuple, concrete_elastic_modu, concrete_compres_tuple]

    table_tuple_steel_plastic_support = get_steel_yield(material_support[0])
    strength_steel_support = get_steel_strength(material_support[0])

    material_support_1 = [strength_steel_support, table_tuple_steel_plastic_support]

    # get_inp
    # 改变路径
    os.chdir(newFileFolder)

    fileTemp = ''
    with open('joint_type34_make_model_user.py', "r", encoding="utf-8") as f:
        for line in f:
            if 'num_beams_1' in line:
                line = line.replace('num_beams_1', str(num_beams))
            if 'geometry_column_1' in line:
                line = line.replace('geometry_column_1', str(geometry_column))
            if 'geometry_plate_1' in line:
                line = line.replace('geometry_plate_1',str(geometry_plate))
            if 'geometry_beam1_1' in line:
                line = line.replace('geometry_beam1_1',str(list(geometry_beam[0, :])))
            if 'geometry_beam2_1' in line:
                line = line.replace('geometry_beam2_1', str(list(geometry_beam[1, :])))
            if 'geometry_beam3_1' in line:
                line = line.replace('geometry_beam3_1', str(list(geometry_beam[2, :])))
            if 'geometry_beam4_1' in line:
                line = line.replace('geometry_beam4_1', str(list(geometry_beam[3, :])))
            if 'material_property_1' in line:
                line = line.replace('material_property_1', str(material_property))
            if 'mesh_size_1' in line:
                line = line.replace('mesh_size_1', str(size_mesh))
            if 'compute_set_1' in line:
                line = line.replace('compute_set_1', str(compute_set))
            if 'num_supports' in line:
                line = line.replace('num_supports', str(num_supports))
            if 'geometry_support_board' in line:
                line = line.replace('geometry_support_board', str(geometry_support_board))
            if 'material_support_1' in line:
                line = line.replace('material_support_1', str(material_support_1))
            if 'support_compress_1' in line:
                line = line.replace('support_compress_1', str(support_compress))

            fileTemp += line

    with open('joint_type32_make_model_user_temp.py', "w", encoding="utf-8") as f:
        f.write(fileTemp)

    # get_odb
    order1 = 'abaqus cae nogui=' + 'joint_type32_make_model_user_temp.py'
    d1 = os.popen(order1)
    f1 = d1.read()

    # process_odb
    fileTemp2 = ''
    with open('joint_type34_process_user.py', "r", encoding="utf-8") as f:
        for line in f:
            if 'steel_yield' in line:
                line = line.replace('steel_yield', str(get_steel_yield(matrerial_name[0])[0]))
            fileTemp2 += line
    with open('joint_type32_process_user_temp.py', "w", encoding="utf-8") as f:
        f.write(fileTemp2)

    order3 = 'abaqus python ' + 'joint_type32_process_user_temp.py'
    d3 = os.popen(order3)
    f3 = d3.read()
    # print(f3)

    # get_result
    dict_rf3_1 = {
        'beam1_edge': 'Node ASSEMBLY.3',
        'beam2_edge': 'Node ASSEMBLY.4',
        'beam3_edge': 'Node ASSEMBLY.5',
    }

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

    percent_yield = get_percent_picture(num_beams)

    for num in range(int(num_supports)):
        get_support_rf(int(num) + 1)

    get_rf_beams_picture(num_beams)

    k_beam_all = get_slope_value_picture(num_beams, dict_rf3_1, dict_u123_1, geometry_column[3],
                                       geometry_plate,
                                       geometry_beam[0,:], geometry_beam[1,:], geometry_beam[2,:], geometry_beam[3,:],
                                       matrerial_name[0])

    #  输出文件名列表
    dataOut = ['table_percent.xlsx',
               'table_RF3_beams.xlsx',
               'table_the_Classification_of_connection_stiffness.xlsx',
               'table_RF1_support1_edge.csv',
               'table_RF2_support1_edge.csv',
               'table_RF3_support1_edge.csv',
               'table_RF1_support2_edge.csv',
               'table_RF2_support2_edge.csv',
               'table_RF3_support2_edge.csv',

               'diagram_the_Classification_of_connection_stiffness.png',
               'diagram_percent.png',
               'diagram_RF3_beams.png',
               'diagram_RF_support1.png',
               'diagram_RF_support2.png',
               ]

    # copy出所需文件
    FileFolder = path
    for i in dataOut:
        shutil.copy(i, FileFolder)

    # 返回默认路径，便于下次计算
    os.chdir(pathDefault)

    # 删除缓存文件夹
    # shutil.rmtree(newFileFolder)

    # print('\nCOMPLETED THE WORK.')
    return dataOut, percent_yield, k_beam_all  # 返回输出文件名列表


if __name__ == '__main__':

    path = r'F:\Abaqus_files'

    inter_outer = 1

    geometry_column = [3670, 250, 400, 6, 15]
    geometry_beam_add = np.array([geometry_column[3] + 200, 200, 2])
    geometry_plate = [300, 12]

    geometry_beam_input = [[2200, 300, 8], [2200, 300, 8],  [2200, 300, 8]]
    matrerial_name = ['Q420', 'C40']

    geometry_support_board = [200.0, 400.0,
                              300.0, 800.0, 400.0, 600.0, 600.0, 400.0,
                              45, 4.0, 100.0, 4.0]
    material_support = ['Q420']

    core(path, inter_outer,
         geometry_column, geometry_plate, geometry_beam_input, geometry_support_board,
         matrerial_name, material_support)
    # print('-------cost %s minutes-------' % round((time.time() - start_time) / 60))


