# -*- coding:utf8 -*-
import numpy as np
import math
import matplotlib.pyplot as plt


def get_steel_yield(steel):
    # Mpa
    dictSteelYieldStressPlasticStrain = {
        'Q235': (215.0, 0.0),
        'Q345': (310.0, 0.0),
        'Q390': (350.0, 0.0),
        'Q420': (380.0, 0.0)
    }

    return dictSteelYieldStressPlasticStrain[steel]


def get_steel_strength(steel):
    # thickness < 16
    dictSteelStrength = {
        'Q235': 215,
        'Q345': 310,
        'Q390': 350,
        'Q420': 380,
    }

    return dictSteelStrength[steel]


def get_concrete_parameters(concrete):
    """
    混凝土材料属性
    :param concrete:
    :return: 混凝土的弹性模量、混凝土的轴心抗压强度设计值、混凝土的轴心抗拉强度设计值、 #Mpa
    """
    concreteElasticModulus = {
        'C30': 30000, 'C35': 31500, 'C40': 32500, 'C45': 33500, 'C50': 34500,
        'C55': 35500, 'C60': 36000, 'C65': 36500, 'C70': 37000, 'C75': 37500, 'C80': 38000
    }
    concreteAxialCompressiveStrengthDesignValue = {
        'C30': 14.3, 'C35': 16.7, 'C40': 19.1, 'C45': 21.1, 'C50': 23.1,
        'C55': 25.3, 'C60': 27.5, 'C65': 29.7, 'C70': 31.8, 'C75': 33.8, 'C80': 35.9
    }

    concreteAxialTensileStrengthDesignValue = {
        'C30': 1.43, 'C35': 1.57, 'C40': 1.71, 'C45': 1.80, 'C50': 1.89,
        'C55': 1.96, 'C60': 2.04, 'C65': 2.09, 'C70': 2.14, 'C75': 2.18, 'C80': 2.22
    }

    concreteAxialCompressiveStrengthStandardValue = {
        'C30': 20.1, 'C35': 23.4, 'C40': 26.8, 'C45': 29.6, 'C50': 32.4,
        'C55': 35.5, 'C60': 38.5, 'C65': 41.5, 'C70': 44.5, 'C75': 47.4, 'C80': 50.2
    }

    return concreteElasticModulus[concrete], \
           concreteAxialCompressiveStrengthDesignValue[concrete], \
           concreteAxialTensileStrengthDesignValue[concrete], \
           concreteAxialCompressiveStrengthStandardValue[concrete]


def get_concrete_compressive_constitution(Ec, Fcr):
    """
    混凝土受压规范本构

    :param Ec:  混凝土弹性模量
    :param Fcr: 混凝土单轴抗压强度代表值，可取Fc，Fck，Fcm
    :param Ftr: 混凝土单轴抗拉强度代表值，可取Ft，Ftk，Fcm
    :return:    混凝土受压规范本构曲线
    """

    # Ftr: 混凝土单轴抗拉强度代表值，可取Ft，Ftk，Fcm
    Ftr = 0.375 * (Fcr ** 0.55)

    epselonCR = (700 + 172 * (Fcr ** 0.5)) * 0.000001
    alphaC = 0.157 * (Fcr ** 0.785) - 0.9005
    strainNominal = [epselonCR * x / 10 for x in range(0, 72, 2)]  # 取得范围0-1
    nPrameters = Ec * epselonCR / (Ec * epselonCR - Fcr)
    rouC = Fcr / (Ec * epselonCR)

    dc1 = [1 - (rouC * nPrameters / (nPrameters - 1 + ((x / 10) ** nPrameters))) for x in range(0, 12, 2)]
    dc7 = [1 - rouC / (alphaC * (x / 10 - 1) ** 2 + x / 10) for x in range(12, 72, 2)]
    dc = dc1 + dc7

    stressNominal = [(1 - dc[i]) * Ec * strainNominal[i] for i in range(len(dc))]
    Dc = [1 - (1 - dc[i]) ** 0.5 for i in range(len(dc))]
    stressTrue = [stressNominal[i] * (1 + strainNominal[i]) for i in range(len(strainNominal))]
    strainTrue = [math.log(1 + strainNominal[i]) for i in range(len(strainNominal))]
    strainInelastic = [strainTrue[i] - stressTrue[i] / Ec for i in range(len(strainTrue))]

    # plt.plot(strainInelastic[0:], stressTrue[0:],  linewidth=2, color='r', marker='o')
    # plt.xlabel('strainInelastic')
    # plt.ylabel('stressTrue')
    # plt.title('Concrete Compressive Constitutive according to GB50010-2010 ')
    # plt.show()

    strainInelastic[1] = 0
    abaqusNeedCompressive = tuple(zip(stressTrue[1:], strainInelastic[1:]))

    return abaqusNeedCompressive


def get_concrete_tensile_constitution(Ec, Ftr):
    """

    :param Ec: 混凝土弹性模量
    :param Ftr: 单轴抗拉强度代表值，可取Ft，Ftk，Fcm
    :return: 混凝土受拉规范本构
    """

    epselonTR = (Ftr ** 0.54) * 65 * 0.000001
    alphaT = 0.312 * (Ftr ** 2)
    strainNOM = [x / 10 * epselonTR for x in range(0, 72, 2)]
    rouT = Ftr / (Ec * epselonTR)

    dt1 = [1 - rouT * (1.2 - 0.2 * ((x / 10) ** 0.5)) for x in range(0, 12, 2)]
    dt2 = [1 - rouT / (alphaT * ((x / 10 - 1) ** 1.7) + x / 10) for x in range(12, 72, 2)]
    dt = dt1 + dt2

    stressNom = [(1 - dt[i]) * Ec * strainNOM[i] for i in range(len(dt))]
    stressTru = [stressNom[i] * (1 + strainNOM[i]) for i in range(len(stressNom))]
    strainTru = [math.log(1 + strainNOM[i]) for i in range(len(stressNom))]
    strainPlastic = [strainTru[i] - stressTru[i] / Ec for i in range(len(strainTru))]

    # plt.plot(strainPlastic[0:], stressTru[0:], linewidth=2, color='g', marker='o')
    # plt.xlabel('strainInelastic')
    # plt.ylabel('stressTrue')
    # plt.title('Concrete Tensile Constitutive according to GB50010-2010 ')
    # plt.show()

    strainPlastic[1] = 0
    abaqusNeedTensile = tuple(zip(stressTru[1:], strainPlastic[1:]))

    return abaqusNeedTensile


if __name__ == '__main__':
    print(str(get_concrete_compressive_constitution(34500, 23.1)))
    # print( get_concrete_tensile_constitution(36000, 1.62) )
