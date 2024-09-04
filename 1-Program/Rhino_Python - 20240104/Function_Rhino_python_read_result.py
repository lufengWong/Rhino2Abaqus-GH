# -*- coding: mbcs -*-
import os
import odbAccess
from textRepr import *
from odbAccess import *
import numpy as np

def get_percent(newFileFolder,fileName,setName,valueLimited):
    # fieldout
    # 改变路径
    os.chdir(newFileFolder)

    valueLimited = float(valueLimited)

    newName = 'alreadyUpgradedOdb_' + str(fileName)

    if os.path.exists(newName + '.lck'):
        os.remove(newName + '.lck')

    # main
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
    # #########
        #
        listLimited = [x for x in listValues if x >= valueLimited]
        lenListLimited = len(listLimited)
        lenListValues = len(listValues)
        percentLimited = float(lenListLimited) / float(lenListValues)

        listSave.append([i, lenListLimited, lenListValues, percentLimited])

    arrayPercent = np.array(listSave)
    np.savetxt('table_percent_' +str(setName) + '.csv', arrayPercent, delimiter=",", fmt='%.04f')
    odb.close()
    return 'data.csv'


if __name__ == "__main__":

    # get_percent(path_file, 'Job-1', 'SET-PART-PLATE', '345')

    get_percent(r'PATH_FILE_RE',
                'JOB_NAME_RE',
                'SET_NAME_RE',
                'VALUE_LIMITED')
