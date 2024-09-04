# -*- coding:utf8 -*-
import numpy as np
import matplotlib.pyplot as plt
from constitution_2 import *
import pandas as pd
from scipy import interpolate


def show_BSEN_classification_of_connection_stifness():
    '''
    绘制刚接, 铰接分类曲线
    :return:
    '''
    array_rigid_without_support = np.array([[0, 0], [2 / 75, 2 / 3], [0.12, 1], [0.2, 1], [0.3, 1]])
    array_rigid_with_support = np.array([[0, 0], [1 / 12, 2 / 3], [0.2, 1], [0.3, 1]])
    array_hinge_with_support = np.array([[0, 0], [0.3, 0.15]])

    plt.figure(figsize=[12, 8])
    plt.plot(array_rigid_without_support[:, 0], array_rigid_without_support[:, 1], '-',
             linewidth=2, color='#FF6666',
             label='boundary between the rigid joint and Semi-rigid joint without support')
    plt.plot(array_rigid_with_support[:, 0], array_rigid_with_support[:, 1],
             linewidth=2, color='#CCCC00', label='boundary between the rigid joint and Semi-rigid joint with support')
    plt.plot(array_hinge_with_support[:, 0], array_hinge_with_support[:, 1],
             linewidth=2, color='#0066CC', label='boundary between the rigid joint and hinge joint')
    plt.xlim((0, 0.3))
    plt.ylim((0, 2))
    plt.yticks(fontproperties='Times New Roman', size=12)
    plt.xticks(fontproperties='Times New Roman', size=12)
    plt.xlabel('${{\\theta }_{j1} } / {{ \\theta }_{jp}}$', fontdict={'family': 'Times New Roman', 'size': 16})
    plt.ylabel('${M}/{M_p}$', fontdict={'family': 'Times New Roman', 'size': 16})
    plt.title('the Classification of connection stiffness ', font='Times New Roman', size=16, )
    plt.legend(loc=4, bbox_to_anchor=(1, 0.14), prop={'family': 'Times New Roman', 'size': 16})
    plt.grid()
    plt.savefig('the_Classification_of_connection_stiffness.png', dpi=600)
    plt.show()
    return 'the_Classification_of_connection_stiffness.png'


def get_rf_beams_picture(num_beams):
    plt.figure(figsize=[10, 6])
    percent_beam1 = np.abs(np.loadtxt('table_RF3_beam1_edge.csv', delimiter=','))
    percent_beam2 = np.abs(np.loadtxt('table_RF3_beam2_edge.csv', delimiter=','))
    percent_beam3 = np.abs(np.loadtxt('table_RF3_beam3_edge.csv', delimiter=','))

    if num_beams == 4:
        assert 'error!'

    elif num_beams == 3:
        plt.plot(percent_beam1[:, 0], percent_beam1[:, 1] / 1000, linewidth=1, color='orange', marker='o',label='Beam1')
        plt.plot(percent_beam2[:, 0], percent_beam2[:, 1] / 1000, linewidth=1, color='blue', marker='s', label='Beam2')
        plt.plot(percent_beam3[:, 0], percent_beam3[:, 1] / 1000, linewidth=1, color='green', marker='p', label='Beam3')
        data_percent_3 = np.hstack(
            (percent_beam1[:, 0].reshape(-1, 1),  percent_beam1[:, 1].reshape(-1, 1),
             percent_beam2[:, 1].reshape(-1, 1), percent_beam3[:, 1].reshape(-1, 1)))
        df_precent = pd.DataFrame(data_percent_3, columns=['frame', 'beam1', 'beam2', 'beam3'])

    elif num_beams == 2:
        plt.plot(percent_beam1[:, 0], percent_beam1[:, 1] / 1000, linewidth=1, color='orange', marker='o',label='Beam1')
        plt.plot(percent_beam2[:, 0], percent_beam2[:, 1] / 1000, linewidth=1, color='blue', marker='s', label='Beam2')
        data_percent_2 = np.hstack(
            (percent_beam1[:, 0].reshape(-1, 1),  percent_beam1[:, 1].reshape(-1, 1),
             percent_beam2[:, 1].reshape(-1, 1)))
        df_precent = pd.DataFrame(data_percent_2, columns=['frame',  'beam1', 'beam2'])

    else:
        plt.plot(percent_beam1[:, 0], percent_beam1[:, 1] / 1000, linewidth=1, color='orange', marker='o',label='Beam1')
        data_percent_1 = np.hstack((percent_beam1[:, 0].reshape(-1, 1),
                                    percent_beam1[:, 1].reshape(-1, 1)))
        df_precent = pd.DataFrame(data_percent_1, columns=['frame',  'beam1'])

    plt.xlabel('Frames', fontdict={'family': 'Times New Roman', 'size': 16})
    plt.ylabel('RF3(kN)', fontdict={'family': 'Times New Roman', 'size': 16})
    plt.yticks(fontproperties='Times New Roman', size=12)
    plt.xticks(fontproperties='Times New Roman', size=12)
    plt.title('the RF3 of Beams ', font='Times New Roman', size=15, )
    plt.legend(prop={'family': 'Times New Roman', 'size': 14})
    plt.grid()
    plt.savefig('diagram_RF3_beams.png', dpi=600)
    plt.show()
    df_precent.to_excel("table_RF3_beams.xlsx")

    data_rf_last = [percent_beam1[:, 1][-1] * 1000,
                    percent_beam2[:, 1][-1] * 1000,
                    percent_beam3[:, 1][-1] * 1000]

    return data_rf_last[0:num_beams + 1]



def get_percent_picture(num_beams):
    plt.figure(figsize=[10, 6])
    percent_beam1 = np.loadtxt('table_percent_SET-PART-BEAM1.csv', delimiter=',')
    percent_beam2 = np.loadtxt('table_percent_SET-PART-BEAM2.csv', delimiter=',')
    percent_beam3 = np.loadtxt('table_percent_SET-PART-BEAM3.csv', delimiter=',')
    percent_plate = np.loadtxt('table_percent_SET-PART-PLATE.csv', delimiter=',')

    plt.plot(percent_plate[:, 0], percent_plate[:, 1] * 100, linewidth=2, color='coral', marker='*', label='PlateRing')
    plt.plot(percent_plate[:, 0], percent_plate[:, 1] * 100 / 4, linewidth=2, color='teal', marker='s',
             label='PlateRing/4')

    if num_beams == 4:
        print('error!')

    elif num_beams == 3:
        plt.plot(percent_beam1[:, 0], percent_beam1[:, 1] * 100, linewidth=1, color='orange', label='Beam1')
        plt.plot(percent_beam2[:, 0], percent_beam2[:, 1] * 100, linewidth=1, color='blue', label='Beam2')
        plt.plot(percent_beam3[:, 0], percent_beam3[:, 1] * 100, linewidth=1, color='green', label='Beam3')
        data_percent_3 = np.hstack(
            (percent_beam1[:, 0].reshape(-1, 1), percent_plate[:, 1].reshape(-1, 1), percent_beam1[:, 1].reshape(-1, 1),
             percent_beam2[:, 1].reshape(-1, 1), percent_beam3[:, 1].reshape(-1, 1)))
        df_precent = pd.DataFrame(data_percent_3, columns=['frame', 'plate', 'beam1', 'beam2', 'beam3'])

    elif num_beams == 2:
        plt.plot(percent_beam1[:, 0], percent_beam1[:, 1] * 100, linewidth=1, color='orange', label='Beam1')
        plt.plot(percent_beam2[:, 0], percent_beam2[:, 1] * 100, linewidth=1, color='blue', label='Beam2')
        data_percent_2 = np.hstack(
            (percent_beam1[:, 0].reshape(-1, 1), percent_plate[:, 1].reshape(-1, 1), percent_beam1[:, 1].reshape(-1, 1),
             percent_beam2[:, 1].reshape(-1, 1)))
        df_precent = pd.DataFrame(data_percent_2, columns=['frame', 'plate', 'beam1', 'beam2'])

    else:
        plt.plot(percent_beam1[:, 0], percent_beam1[:, 1] * 100, linewidth=1, color='orange', label='Beam1')
        data_percent_1 = np.hstack((percent_beam1[:, 0].reshape(-1, 1), percent_plate[:, 1].reshape(-1, 1),
                                    percent_beam1[:, 1].reshape(-1, 1)))
        df_precent = pd.DataFrame(data_percent_1, columns=['frame', 'plate', 'beam1'])

    plt.xlabel('Frames', fontdict={'family': 'Times New Roman', 'size': 16})
    plt.ylabel('Percent(%)', fontdict={'family': 'Times New Roman', 'size': 16})
    plt.yticks(fontproperties='Times New Roman', size=12)
    plt.xticks(fontproperties='Times New Roman', size=12)
    plt.title('the Percent of Yield Elements ', font='Times New Roman', size=15, )
    plt.legend(prop={'family': 'Times New Roman', 'size': 14})
    plt.grid()
    plt.savefig('diagram_percent.png', dpi=600)
    plt.show()
    df_precent.to_excel("table_percent.xlsx")

    data_percent_last = [percent_plate[:, 1][-1] * 100, percent_beam1[:, 1][-1] * 100,
                         percent_beam2[:, 1][-1] * 100, percent_beam3[:, 1][-1] * 100,
                        ]
    return data_percent_last[0:num_beams + 1]


def get_rf_picture(dict_process_data):
    plt.figure(figsize=[10, 6])
    plt.plot(dict_process_data['beam1_rf'][:, 0], dict_process_data['beam1_rf'][:, 1] / 1000, linewidth=2,
             color='#336699',
             marker='p', label='Beam1')
    plt.plot(dict_process_data['beam2_rf'][:, 0], dict_process_data['beam2_rf'][:, 1] / 1000, linewidth=2,
             color='#339933',
             marker='s', label='Beam2')

    plt.xlabel('Frames', fontdict={'family': 'Times New Roman', 'size': 16})
    plt.ylabel('RF(${K}_{n}$)', fontdict={'family': 'Times New Roman', 'size': 16})
    plt.yticks(fontproperties='Times New Roman', size=12)
    plt.xticks(fontproperties='Times New Roman', size=12)
    plt.title('the Reaction Force in the end of beam ', font='Times New Roman', size=15, )
    plt.legend(loc=4, prop={'family': 'Times New Roman', 'size': 18})
    plt.grid()
    plt.savefig('diagram_RF.png', dpi=600)
    plt.show()
    return 'diagram_RF.png'


def get_support_rf(support_order):
    rf_1 = np.loadtxt('table_RF1_support' + str(support_order) + '_edge.csv', delimiter=',')
    rf_2 = np.loadtxt('table_RF2_support' + str(support_order) + '_edge.csv', delimiter=',')
    rf_3 = np.loadtxt('table_RF3_support' + str(support_order) + '_edge.csv', delimiter=',')

    plt.figure(figsize=[10, 6])
    plt.plot(rf_1[:, 0], -rf_1[:, 1] / 1000, linewidth=2,
             color='#336699',
             marker='p', label='X')
    plt.plot(rf_2[:, 0], -rf_2[:, 1] / 1000, linewidth=2,
             color='#339933',
             marker='s', label='Y')
    plt.plot(rf_1[:, 0], -rf_3[:, 1] / 1000, linewidth=2,
             color='#FFCC99',
             marker='p', label='Z')
    plt.plot(rf_2[:, 0], ((rf_1[:, 1])**2 + (rf_2[:, 1])**2 + (rf_3[:, 1])**2)**0.5 / 1000, linewidth=2,
             color='#FF0000',
             marker='s', label='euclidean metric')

    plt.xlabel('Frames', fontdict={'family': 'Times New Roman', 'size': 16})
    plt.ylabel('RF(${K}_{n}$)', fontdict={'family': 'Times New Roman', 'size': 16})
    plt.yticks(fontproperties='Times New Roman', size=12)
    plt.xticks(fontproperties='Times New Roman', size=12)
    plt.title('the Reaction Force in the end of support'+str(support_order), font='Times New Roman', size=15, )
    plt.legend(loc=4, prop={'family': 'Times New Roman', 'size': 18})
    plt.grid()
    plt.savefig('diagram_RF_support' + str(support_order) + '.png', dpi=600)
    plt.show()
    return 'diagram_RF_support' + str(support_order) + '.png'


def I_beam_geomotry_property(tWeb, hWeb, wFlange, tFlange):
    '''
    计算工字钢截惯性矩
    :param tWeb: 腹板厚度
    :param hWeb: 腹板高度
    :param wFlange: 翼缘宽度
    :param tFlange: 翼缘厚度
    :return: 截面惯性矩
    '''
    parameter1 = np.float64(wFlange * np.float64((hWeb + tFlange * 2) ** 3))  # 精度问题，每一步的warning都很重要
    parameter2 = np.float64(np.float64(wFlange - tWeb) * np.float64((hWeb) ** 3))
    moment_of_inertia = np.float64((parameter1 - parameter2) / 12)

    elastic_section_modulus = np.float64(wFlange * np.float64(np.float64(hWeb + tFlange * 2) ** 2) -
                                         np.float64((wFlange - tWeb) * np.float64((hWeb) ** 2))) / 6

    plastic_section_modulus = np.float64(np.float64(wFlange * np.float64((hWeb + tFlange * 2) ** 2) -
                                                    np.float64((wFlange - tWeb) * np.float64((hWeb) ** 2))) / 6) * 1.5

    return moment_of_inertia, elastic_section_modulus, plastic_section_modulus


def get_steel_yield_from(ID):
    list_steel = ['Q235', 'Q345', 'Q390', 'Q420']
    return get_steel_yield(list_steel[ID])[0]


def get_slope_value_picture(num_beams, dict_rf3, dict_u123, circleR3,
                            geometry_plate,
                            geometry_beam1, geometry_beam2, geometry_beam3, geometry_beam4,
                            steel_name):
    webH, tPlate = geometry_plate
    cCL1, flangeH1, tWeb1 = geometry_beam1
    cCL2, flangeH2, tWeb2 = geometry_beam2
    cCL3, flangeH3, tWeb3 = geometry_beam3
    cCL4, flangeH4, tWeb4 = geometry_beam4

    dict_process_data = {}
    for key_edge in dict_rf3:
        dict_process_data['RF3_' + key_edge] = np.loadtxt('table_RF3_' + key_edge + '.csv', delimiter=',')

    for key_u in dict_u123:
        dict_process_data['U1_' + key_u] = np.loadtxt('table_U1_' + key_u + '.csv', delimiter=',')
        dict_process_data['U2_' + key_u] = np.loadtxt('table_U2_' + key_u + '.csv', delimiter=',')
        dict_process_data['U3_' + key_u] = np.loadtxt('table_U3_' + key_u + '.csv', delimiter=',')

    # 计算规范常量
    yieldModulu = get_steel_yield(steel_name)[0]
    M_p_1 = yieldModulu * I_beam_geomotry_property(tWeb1, webH, flangeH1, tPlate)[2]
    M_p_2 = yieldModulu * I_beam_geomotry_property(tWeb2, webH, flangeH2, tPlate)[2]
    M_p_3 = yieldModulu * I_beam_geomotry_property(tWeb3, webH, flangeH3, tPlate)[2]
    M_p_4 = yieldModulu * I_beam_geomotry_property(tWeb4, webH, flangeH4, tPlate)[2]

    E_steel = 206000
    theta_jp_1 = (M_p_1 * cCL1 * 2) / (E_steel * I_beam_geomotry_property(tWeb1, webH, flangeH1, tPlate)[0])
    theta_jp_2 = (M_p_2 * cCL2 * 2) / (E_steel * I_beam_geomotry_property(tWeb2, webH, flangeH2, tPlate)[0])
    theta_jp_3 = (M_p_3 * cCL3 * 2) / (E_steel * I_beam_geomotry_property(tWeb3, webH, flangeH3, tPlate)[0])
    theta_jp_4 = (M_p_4 * cCL4 * 2) / (E_steel * I_beam_geomotry_property(tWeb4, webH, flangeH4, tPlate)[0])

    theta_ab_1 = (dict_process_data['U1_beam1_up'][:, 1] - dict_process_data['U1_beam1_down'][:, 1]).reshape(-1, 1) \
                 / (dict_process_data['U3_beam1_up'][:, 1] + (webH + 2 * tPlate) - dict_process_data['U3_beam1_down'][:,
                                                                                   1]).reshape(-1, 1)

    theta_ab_2 = (dict_process_data['U2_beam2_up'][:, 1] - dict_process_data['U2_beam2_down'][:, 1]).reshape(-1, 1) \
                 / (dict_process_data['U3_beam2_up'][:, 1] + (webH + 2 * tPlate) - dict_process_data['U3_beam2_down'][:,
                                                                                   1]).reshape(-1, 1)

    theta_ab_3 = (dict_process_data['U1_beam3_up'][:, 1] - dict_process_data['U1_beam3_down'][:, 1]).reshape(-1, 1) \
                 / (dict_process_data['U3_beam3_up'][:, 1] + (webH + 2 * tPlate) - dict_process_data['U3_beam3_down'][:,
                                                                                   1]).reshape(-1, 1)

    theta_ab_4 = (dict_process_data['U2_beam4_up'][:, 1] - dict_process_data['U2_beam4_down'][:, 1]).reshape(-1, 1) \
                 / (dict_process_data['U3_beam4_up'][:, 1] + (webH + 2 * tPlate) - dict_process_data['U3_beam4_down'][:,
                                                                                   1]).reshape(-1, 1)

    if num_beams <= 3:
        theta_cd_1 = (dict_process_data['U1_beam4_up'][:, 1] - dict_process_data['U1_beam4_down'][:, 1]).reshape(-1, 1) \
                     / (dict_process_data['U3_beam4_up'][:, 1] + (webH + 2 * tPlate) - dict_process_data[
                                                                                           'U3_beam4_down'][:,
                                                                                       1]).reshape(-1, 1)

        theta_cd_2 = (dict_process_data['U2_beam4_up'][:, 1] - dict_process_data['U2_beam4_down'][:, 1]).reshape(-1, 1) \
                     / (dict_process_data['U3_beam4_up'][:, 1] + (webH + 2 * tPlate) - dict_process_data[
                                                                                           'U3_beam4_down'][:,
                                                                                       1]).reshape(-1, 1)

        theta_cd_3 = (dict_process_data['U1_beam4_up'][:, 1] - dict_process_data['U1_beam4_down'][:, 1]).reshape(-1, 1) \
                     / (dict_process_data['U3_beam4_up'][:, 1] + (webH + 2 * tPlate) - dict_process_data[
                                                                                           'U3_beam4_down'][:,
                                                                                       1]).reshape(-1, 1)

        theta_cd_4 = (dict_process_data['U2_beam4_up'][:, 1] - dict_process_data['U2_beam4_down'][:, 1]).reshape(-1, 1) \
                     / (dict_process_data['U3_beam4_up'][:, 1] + (webH + 2 * tPlate) - dict_process_data[
                                                                                           'U3_beam4_down'][:,
                                                                                       1]).reshape(-1, 1)
    else:
        theta_cd_1 = np.zeros_like(theta_ab_1)
        theta_cd_2 = np.zeros_like(theta_ab_1)
        theta_cd_3 = np.zeros_like(theta_ab_1)
        theta_cd_4 = np.zeros_like(theta_ab_1)

    theta_j1_1 = np.abs(theta_ab_1 - theta_cd_1)
    theta_j1_2 = np.abs(theta_ab_2 - theta_cd_2)
    theta_j1_3 = np.abs(theta_ab_3 - theta_cd_3)


    M_1 = np.abs(dict_process_data['RF3_beam1_edge'][:, 1]) * cCL1
    M_2 = np.abs(dict_process_data['RF3_beam2_edge'][:, 1]) * cCL2
    M_3 = np.abs(dict_process_data['RF3_beam3_edge'][:, 1]) * cCL3


    id_max_M_1 = int((np.where(M_1 == np.max(M_1)))[0][0])
    id_max_M_2 = int((np.where(M_2 == np.max(M_2))[0][0]))
    id_max_M_3 = int((np.where(M_3 == np.max(M_3))[0][0]))


    x_value_1 = theta_j1_1 / theta_jp_1
    x_value_2 = theta_j1_2 / theta_jp_2
    x_value_3 = theta_j1_3 / theta_jp_3


    y_value_1 = M_1 / M_p_1
    y_value_2 = M_2 / M_p_2
    y_value_3 = M_3 / M_p_3

    frame = dict_process_data['RF3_beam1_edge'][:, 0].reshape(-1, 1)
    array_stiff_beam1 = np.hstack(
        (frame, theta_ab_1.reshape(-1, 1), theta_cd_1.reshape(-1, 1), theta_j1_1.reshape(-1, 1), M_1.reshape(-1, 1),
         np.ones_like(theta_ab_1) * M_p_1, np.ones_like(theta_ab_1) * theta_jp_1, x_value_1.reshape(-1, 1),
         y_value_1.reshape(-1, 1)))
    array_stiff_beam2 = np.hstack(
        (frame, theta_ab_2.reshape(-1, 1), theta_cd_2.reshape(-1, 1), theta_j1_2.reshape(-1, 1), M_2.reshape(-1, 1),
         np.ones_like(theta_ab_2) * M_p_2, np.ones_like(theta_ab_2) * theta_jp_2, x_value_2.reshape(-1, 1),
         y_value_2.reshape(-1, 1)))
    array_stiff_beam3 = np.hstack(
        (frame, theta_ab_3.reshape(-1, 1), theta_cd_3.reshape(-1, 1), theta_j1_3.reshape(-1, 1), M_3.reshape(-1, 1),
         np.ones_like(theta_ab_3) * M_p_3, np.ones_like(theta_ab_3) * theta_jp_3, x_value_3.reshape(-1, 1),
         y_value_3.reshape(-1, 1)))


    df_stiff_beam1 = pd.DataFrame(array_stiff_beam1,
                                  columns=['frame', 'theta_ab', 'theta_cd', ' theta_j1', 'M', 'M_p', 'theta_jp',
                                           ' x_value',
                                           'y_value'])
    df_stiff_beam2 = pd.DataFrame(array_stiff_beam2,
                                  columns=['frame', 'theta_ab', 'theta_cd', ' theta_j1', 'M', 'M_p', 'theta_jp',
                                           ' x_value',
                                           'y_value'])
    df_stiff_beam3 = pd.DataFrame(array_stiff_beam3,
                                  columns=['frame', 'theta_ab', 'theta_cd', ' theta_j1', 'M', 'M_p', 'theta_jp',
                                           ' x_value',
                                           'y_value'])


    array_rigid_without_support = np.array([[0, 0], [2 / 75, 2 / 3], [0.12, 1], [0.2, 1], [0.3, 1], [0.4, 1]])
    array_rigid_with_support = np.array([[0, 0], [1 / 12, 2 / 3], [0.2, 1], [0.3, 1], [0.4, 1]])
    array_hinge_with_support = np.array([[0, 0], [0.3, 0.15], [0.4, 0.2]])

    plt.figure(figsize=[14, 8])
    plt.plot([0, 10], [2 / 3, 2 / 3], linewidth=2, color='red', label='2/3${M_p}/{M_p}$')
    plt.plot(array_rigid_without_support[:, 0], array_rigid_without_support[:, 1], '-.',
             linewidth=2, color='#FF6666',
             label='boundary between the Rigid joint and Semi-rigid joint without support')
    plt.plot(array_rigid_with_support[:, 0], array_rigid_with_support[:, 1], '-.',
             linewidth=2, color='#CCCC00', label='boundary between the Rigid joint and Semi-rigid joint with support')
    plt.plot(array_hinge_with_support[:, 0], array_hinge_with_support[:, 1], '-.',
             linewidth=2, color='#0066CC', label='boundary between the Rigid joint and Hinge joint')

    writer = pd.ExcelWriter('table_the_Classification_of_connection_stiffness.xlsx')
    if num_beams == 4:
       print('error!')

    elif num_beams == 3:
        plt.plot(x_value_1[:id_max_M_1], y_value_1[:id_max_M_1], linewidth=2, color=(224 / 255, 122 / 255, 95 / 255),
                 marker='o', label='joint1')
        plt.plot(x_value_2[:id_max_M_2], y_value_2[:id_max_M_2], linewidth=2, color=(61 / 255, 64 / 255, 91 / 255),
                 marker='p', label='joint2')
        plt.plot(x_value_3[:id_max_M_3], y_value_3[:id_max_M_3], linewidth=2, color=(129 / 255, 178 / 255, 154 / 255),
                 marker='*', label='joint3')

        df_stiff_beam1.to_excel(writer, sheet_name='beam1')
        df_stiff_beam2.to_excel(writer, sheet_name='beam2')
        df_stiff_beam3.to_excel(writer, sheet_name='beam3')

        function_inter_beam1 = interpolate.interp1d(np.array(y_value_1[:id_max_M_1]).flatten(),
                                                    np.array(x_value_1[:id_max_M_1]).flatten(), kind='linear')
        function_inter_beam2 = interpolate.interp1d(np.array(y_value_2[:id_max_M_2]).flatten(),
                                                    np.array(x_value_2[:id_max_M_2]).flatten(), kind='linear')
        function_inter_beam3 = interpolate.interp1d(np.array(y_value_3[:id_max_M_3]).flatten(),
                                                    np.array(x_value_3[:id_max_M_3]).flatten(), kind='linear')
        k_beam1 = (2 / 3) / function_inter_beam1(2 / 3)
        k_beam2 = (2 / 3) / function_inter_beam2(2 / 3)
        k_beam3 = (2 / 3) / function_inter_beam3(2 / 3)
        x_k_beam_all = [function_inter_beam1(2 / 3), function_inter_beam2(2 / 3), function_inter_beam3(2 / 3)]
        k_beam_all = [k_beam1, k_beam2, k_beam3]

    elif num_beams == 2:
        plt.plot(x_value_1[:id_max_M_1], y_value_1[:id_max_M_1], linewidth=2, color=(224 / 255, 122 / 255, 95 / 255),
                 marker='o', label='joint1')
        plt.plot(x_value_2[:id_max_M_2], y_value_2[:id_max_M_2], linewidth=2, color=(61 / 255, 64 / 255, 91 / 255),
                 marker='p', label='joint2')
        df_stiff_beam1.to_excel(writer, sheet_name='beam1')
        df_stiff_beam2.to_excel(writer, sheet_name='beam2')

        function_inter_beam1 = interpolate.interp1d(np.array(y_value_1[:id_max_M_1]).flatten(),
                                                    np.array(x_value_1[:id_max_M_1]).flatten(), kind='linear')
        function_inter_beam2 = interpolate.interp1d(np.array(y_value_2[:id_max_M_2]).flatten(),
                                                    np.array(x_value_2[:id_max_M_2]).flatten(), kind='linear')
        k_beam1 = (2 / 3) / function_inter_beam1(2 / 3)
        k_beam2 = (2 / 3) / function_inter_beam2(2 / 3)
        x_k_beam_all = [function_inter_beam1(2 / 3), function_inter_beam2(2 / 3)]
        k_beam_all = [k_beam1, k_beam2]

    else:
        plt.plot(x_value_1[:id_max_M_1], y_value_1[:id_max_M_1], linewidth=2, color=(224 / 255, 122 / 255, 95 / 255),
                 marker='o', label='joint1')

        df_stiff_beam1.to_excel(writer, sheet_name='beam1')

        function_inter_beam1 = interpolate.interp1d(np.array(y_value_1[:id_max_M_1]).flatten(),
                                                    np.array(x_value_1[:id_max_M_1]).flatten(), kind='linear')

        k_beam1 = (2 / 3) / function_inter_beam1(2 / 3)
        x_k_beam_all = [function_inter_beam1(2 / 3)]
        k_beam_all = [k_beam1]

    writer._save()
    writer.close()

    plt.scatter(x_k_beam_all, ([2 / 3] * 4)[0:num_beams], s=40, marker='o', c='red')

    plt.xlim((0, 0.4))
    plt.ylim((0, 1.5))
    plt.yticks(fontproperties='Times New Roman', size=12)
    plt.xticks(fontproperties='Times New Roman', size=12)
    plt.xlabel('${{\\theta }_{j1} } / {{ \\theta }_{jp}}$', fontdict={'family': 'Times New Roman', 'size': 16})
    plt.ylabel('${M}/{M_p}$', fontdict={'family': 'Times New Roman', 'size': 16})
    plt.title('the Classification of connection stiffness ', font='Times New Roman', size=16, )
    plt.legend(loc=4, bbox_to_anchor=(0.9, 0.07), prop={'family': 'Times New Roman', 'size': 16})
    plt.grid()
    plt.savefig('diagram_the_Classification_of_connection_stiffness.png', dpi=600)
    plt.show()

    return k_beam_all


if __name__ == '__main__':
    dict_rf3_1 = {
        'beam1_edge': 'Node ASSEMBLY.3',
        'beam2_edge': 'Node ASSEMBLY.4',
        'beam3_edge': 'Node ASSEMBLY.5',
        'beam4_edge': 'Node ASSEMBLY.6',
    }

    dict_rf1_rf2_rf3_1 = {'support1_edge': 'Node ASSEMBLY.14'}

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

    geometry_column_1 = [3500, 225, 250, 450, 6]
    geometry_plate_1 = [300, 12]  # h, t

    num_beams_1 = 3
    geometry_beam_add = np.array([geometry_column_1[3] + 200, 200, 2])
    geometry_beam1_1 = [2200, 300, 8]
    geometry_beam2_1 = [2200, 300, 8]
    geometry_beam3_1 = [2200, 300, 8]
    geometry_beam4_1 = [2200, 300, 8]

    steel_name_1 = 'Q345'

    circleR3 = geometry_column_1[3]

    get_percent_picture(num_beams_1)

    example1 = get_slope_value_picture(num_beams_1, dict_rf3_1, dict_u123_1, circleR3,
                                       geometry_plate_1,
                                       geometry_beam1_1, geometry_beam2_1, geometry_beam3_1, geometry_beam4_1,
                                       steel_name_1)
    get_support_rf(1)