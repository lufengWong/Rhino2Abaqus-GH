
# from driverUtils import executeOnCaeGraphicsStartup
# executeOnCaeGraphicsStartup()
#: Executing "onCaeGraphicsStartup()" in the site directory ...


from abaqus import *
from abaqusConstants import *
from caeModules import *
from driverUtils import executeOnCaeStartup

executeOnCaeStartup()

mdb.saveAs(pathName=r'Path_define')
#: The model database has been saved to "C:\Users\18328\Desktop\04-LinTongYan\001.cae".

a = mdb.models['Model-1'].rootAssembly