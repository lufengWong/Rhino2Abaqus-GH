
# -*- coding: mbcs -*-
import os
import odbAccess
from textRepr import *
from odbAccess import *
import numpy as np

def get_percent(path_files, fileName, setName,valueLimited):
    # fieldout

    valueLimited = float(valueLimited)

    newName = 'alreadyUpgradedOdb_' + str(fileName)

    if os.path.exists(newName + '.lck'):
        os.remove(newName + '.lck')

    # main
    odbAccess.upgradeOdb(existingOdbPath=os.path.join(path_files, fileName),
                         upgradedOdbPath=os.path.join(path_files,newName))

    odb = openOdb(os.path.join(path_files, newName + '.odb'))

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
        # percentLimited = float(lenListLimited) / float(lenListValues)

        listSave.append([i, lenListLimited, lenListValues])

    arrayPercent = np.array(listSave)
    np.savetxt(os.path.join(path_files, 'A_table_' + str(fileName) + '.csv'),
               arrayPercent,
               delimiter=",", fmt='%.04f')
    odb.close()


if __name__ == '__main__':

    get_percent('Path_files','Odb_Name_No_ext', 'SET-PART', steel_yield_defined)