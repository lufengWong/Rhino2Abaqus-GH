# -*- coding: mbcs -*-
import os
import odbAccess
from textRepr import *
from odbAccess import *
import numpy as np



def get_percent(fileName,setName,valueLimited):
    # fieldout

    valueLimited = float(valueLimited)

    newName = 'alreadyUpgradedOdb_' + str(fileName)

    if os.path.exists(newName + '.lck'):
        os.remove(newName + '.lck')

    odbAccess.upgradeOdb(existingOdbPath=fileName,upgradedOdbPath=newName)
    odb = openOdb(newName + '.odb')

    regionPost = odb.rootAssembly.elementSets[setName]
    stepNeed = odb.steps.keys()[-1]
    frames = odb.steps[str(stepNeed)].frames

    listSave = []
    for i in range(len(frames)):

        frameNeed = odb.steps[str(stepNeed)].frames[int(i)]  # .fieldOutputs.keys() #ues .keys()
        miseseFieldOutputNeed = frameNeed.fieldOutputs['S']
        postValue = miseseFieldOutputNeed.getSubset(region=regionPost).values
        listValues = [element.mises for element in postValue]

        #
        listLimited = [x for x in listValues if x >= valueLimited]
        lenListLimited = len(listLimited)
        lenListValues = len(listValues)
        percentLimited = float(lenListLimited) / float(lenListValues)

        listSave.append([i ,percentLimited])

    arrayPercent = np.array(listSave)
    np.savetxt('table_percent_' +str(setName) + '.csv', arrayPercent, delimiter=",", fmt='%.04f')
    odb.close()
    return 'data.csv'


def read_history(dict_rf3, dict_rf1_rf2_rf3, dict_u123):
    # history out
    fileName = 'Job-1'
    newName = 'alreadyUpgradedOdb_'+str(fileName)
    if os.path.exists(newName+'.odb'):
        odb = openOdb(newName + '.odb')
    else:
        odbAccess.upgradeOdb(existingOdbPath=fileName,upgradedOdbPath=newName)
        odb = openOdb(newName + '.odb')

    def get_History(dictName, node, item):
        'history_out'
        step = odb.steps[odb.steps.keys()[-1]]
        historyPoint = step.historyRegions[dictName[node]]
        dataXy = historyPoint.historyOutputs[item].data
        np.savetxt('table_'+ item + '_' + node + ".csv", dataXy, delimiter=",", fmt='%.04f')
        return dataXy

    for keys_edge in dict_rf3:
        get_History(dict_rf3, keys_edge, 'RF3')

    for keys_support in dict_rf1_rf2_rf3:
        get_History(dict_rf1_rf2_rf3, keys_support, 'RF1')
        get_History(dict_rf1_rf2_rf3, keys_support, 'RF2')
        get_History(dict_rf1_rf2_rf3, keys_support, 'RF3')

    for keys_U in dict_u123:
        get_History(dict_u123, keys_U, 'U1')
        get_History(dict_u123, keys_U, 'U2')
        get_History(dict_u123, keys_U, 'U3')

    odb.close()
    os.remove(newName + '.odb')
    return 'data.csv'


if __name__ == "__main__":

    get_percent('Job-1', 'SET-PART-PLATE', '345')
    get_percent('Job-1', 'SET-PART-BEAM1', '345')
    get_percent('Job-1', 'SET-PART-BEAM2', '345')
    get_percent('Job-1', 'SET-PART-BEAM3', '345')


    dict_rf3_1 = {
        'beam1_edge': 'Node ASSEMBLY.3',
        'beam2_edge': 'Node ASSEMBLY.4',
        'beam3_edge': 'Node ASSEMBLY.5',
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

    read_history(dict_rf3_1, dict_rf1_rf2_rf3_1, dict_u123_1)