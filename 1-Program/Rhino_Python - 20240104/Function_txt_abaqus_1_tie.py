# -*- coding: mbcs -*-
#
# Abaqus/CAE Release 2022 replay file
# Internal Version: 2021_09_16-01.57.30 176069
# Run by Administrator on Wed Dec 20 10:17:01 2023
#

# from driverUtils import executeOnCaeGraphicsStartup
# executeOnCaeGraphicsStartup()
#: Executing "onCaeGraphicsStartup()" in the site directory ...
from abaqus import *
from abaqusConstants import *
session.Viewport(name='Viewport: 1', origin=(0.0, 0.0), width=220.681243896484,
    height=180.614822387695)
session.viewports['Viewport: 1'].makeCurrent()
session.viewports['Viewport: 1'].maximize()
from caeModules import *
from driverUtils import executeOnCaeStartup
executeOnCaeStartup()
session.viewports['Viewport: 1'].partDisplay.geometryOptions.setValues(
    referenceRepresentation=ON)

# ########################################3
openMdb(pathName=r'PATH_CAE') # F:/temp/A-abaqus-08-wlf-1220-2.cae
# #: The model database "F:\temp\A-abaqus-08-wlf-1220-2.cae" has been opened.
session.viewports['Viewport: 1'].setValues(displayedObject=None)
p = mdb.models['Model-1'].parts['P-1']
session.viewports['Viewport: 1'].setValues(displayedObject=p)
a = mdb.models['Model-1'].rootAssembly
session.viewports['Viewport: 1'].setValues(displayedObject=a)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(
    optimizationTasks=OFF, geometricRestrictions=OFF, stopConditions=OFF)
session.viewports['Viewport: 1'].view.setValues(nearPlane=329688,
    farPlane=476009, width=35247.4, height=13980.8, viewOffsetX=-45010.2,
    viewOffsetY=18808.4)
session.viewports['Viewport: 1'].view.setValues(width=36702.5, height=14558,
    viewOffsetX=-44987.5, viewOffsetY=19032.7)
i1 = mdb.models['Model-1'].rootAssembly.allInstances['P-2-1']
leaf = dgm.LeafFromInstance(instances=(i1, ))
session.viewports['Viewport: 1'].assemblyDisplay.displayGroup.replace(
    leaf=leaf)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(interactions=ON,
    constraints=ON, connectors=ON, engineeringFeatures=ON)
i1 = mdb.models['Model-1'].rootAssembly.allInstances['P-1-1']
leaf = dgm.LeafFromInstance(instances=(i1, ))
session.viewports['Viewport: 1'].assemblyDisplay.displayGroup.replace(
    leaf=leaf)
i1 = mdb.models['Model-1'].rootAssembly.allInstances['P-2-1']
leaf = dgm.LeafFromInstance(instances=(i1, ))
session.viewports['Viewport: 1'].assemblyDisplay.displayGroup.replace(
    leaf=leaf)
session.viewports['Viewport: 1'].view.setValues(nearPlane=418542,
    farPlane=451193, width=46611.4, height=18488.3, cameraPosition=(40259.4,
    119628, 409832), cameraUpVector=(-0.283085, 0.764175, -0.579569),
    cameraTarget=(-82552.1, -20907.5, 52824.8), viewOffsetX=-57133.1,
    viewOffsetY=24171.1)
session.viewports['Viewport: 1'].view.setValues(nearPlane=421436,
    farPlane=448300, width=14366.5, height=5698.44, viewOffsetX=-58858,
    viewOffsetY=23979.7)
i1 = mdb.models['Model-1'].rootAssembly.allInstances['P-1-1']
leaf = dgm.LeafFromInstance(instances=(i1, ))
session.viewports['Viewport: 1'].assemblyDisplay.displayGroup.replace(
    leaf=leaf)
session.viewports['Viewport: 1'].view.setValues(nearPlane=420438,
    farPlane=449295, width=22456.3, height=8907.25, viewOffsetX=-58445.2,
    viewOffsetY=23635.9)
session.viewports['Viewport: 1'].view.setValues(nearPlane=424208,
    farPlane=460760, width=22657.6, height=8987.11, cameraPosition=(274844,
    -11192.4, 138135), cameraUpVector=(-0.260327, 0.765829, -0.587993),
    cameraTarget=(-104641, -61267, 12553.9), viewOffsetX=-58969.2,
    viewOffsetY=23847.8)
i1 = mdb.models['Model-1'].rootAssembly.allInstances['P-2-1']
leaf = dgm.LeafFromInstance(instances=(i1, ))
session.viewports['Viewport: 1'].assemblyDisplay.displayGroup.replace(
    leaf=leaf)
session.viewports['Viewport: 1'].view.setValues(nearPlane=424782,
    farPlane=460187, width=17883.4, height=7093.4, viewOffsetX=-62414.4,
    viewOffsetY=21139.6)
session.viewports['Viewport: 1'].view.setValues(nearPlane=424334,
    farPlane=460396, width=17864.5, height=7085.92, cameraPosition=(249568,
    -12134.5, 216718), cameraUpVector=(-0.155649, 0.781704, -0.603914),
    cameraTarget=(-99976, -60155.3, 22295.8), viewOffsetX=-62348.5,
    viewOffsetY=21117.3)
session.viewports['Viewport: 1'].view.setValues(width=17150, height=6802.52,
    viewOffsetX=-62391.2, viewOffsetY=21047)
session.viewports['Viewport: 1'].view.setValues(nearPlane=424355,
    farPlane=460237, width=17150.8, height=6802.83, cameraPosition=(236109,
    2048.55, 244719), cameraUpVector=(-0.126223, 0.75701, -0.641096),
    cameraTarget=(-98049.7, -59551.2, 28315.2), viewOffsetX=-62394.1,
    viewOffsetY=21047.9)
session.viewports['Viewport: 1'].view.setValues(nearPlane=424158,
    farPlane=460435, width=20218.7, height=8019.7, viewOffsetX=-61833.8,
    viewOffsetY=21272.2)
session.viewports['Viewport: 1'].view.setValues(nearPlane=424315,
    farPlane=460497, width=20226.2, height=8022.68, cameraPosition=(260717,
    43396.3, 176184), cameraUpVector=(-0.256907, 0.646473, -0.718381),
    cameraTarget=(-98459.1, -59226.4, 25357.9), viewOffsetX=-61856.7,
    viewOffsetY=21280.1)
session.viewports['Viewport: 1'].view.setValues(nearPlane=424082,
    farPlane=460731, width=23842.2, height=9456.95, viewOffsetX=-61493.9,
    viewOffsetY=21057.2)
session.viewports['Viewport: 1'].view.setValues(nearPlane=423948,
    farPlane=460393, width=23834.6, height=9453.96, cameraPosition=(241858,
    91996.8, 201503), cameraUpVector=(-0.277971, 0.602232, -0.748364),
    cameraTarget=(-93171.6, -52196.6, 30474.1), viewOffsetX=-61474.4,
    viewOffsetY=21050.6)
session.viewports['Viewport: 1'].view.setValues(nearPlane=423581,
    farPlane=460760, width=29206.3, height=11584.6, viewOffsetX=-60862.2,
    viewOffsetY=20842.6)
session.viewports['Viewport: 1'].view.setValues(nearPlane=423408,
    farPlane=461453, width=29194.3, height=11579.9, cameraPosition=(249580,
    22042.7, 213115), cameraUpVector=(-0.195427, 0.721621, -0.664132),
    cameraTarget=(-97822.3, -58434.3, 25705.8), viewOffsetX=-60837.2,
    viewOffsetY=20834.1)
a = mdb.models['Model-1'].rootAssembly
s1 = a.instances['P-1-1'].faces
side1Faces1 = s1.getSequenceFromMask(mask=('[#3 ]', ), )
region1=regionToolset.Region(side1Faces=side1Faces1)
a = mdb.models['Model-1'].rootAssembly
s1 = a.instances['P-2-1'].edges
side1Edges1 = s1.getSequenceFromMask(mask=('[#44444444:2 ]', ), )
region2=regionToolset.Region(side1Edges=side1Edges1)
mdb.models['Model-1'].Tie(name='Constraint-1', main=region1, secondary=region2,
    positionToleranceMethod=COMPUTED, adjust=ON, tieRotations=ON, thickness=ON)
session.viewports['Viewport: 1'].view.setValues(nearPlane=423701,
    farPlane=461159, width=24813.3, height=9842.15, viewOffsetX=-61309.5,
    viewOffsetY=20823.6)
session.viewports['Viewport: 1'].view.setValues(nearPlane=424302,
    farPlane=461074, width=24848.5, height=9856.12, cameraPosition=(272118,
    4058.35, 149047), cameraUpVector=(-0.232177, 0.638111, -0.734104),
    cameraTarget=(-104330, -66283.5, 24043), viewOffsetX=-61396.5,
    viewOffsetY=20853.2)
leaf = dgm.Leaf(leafType=DEFAULT_MODEL)
session.viewports['Viewport: 1'].assemblyDisplay.displayGroup.replace(
    leaf=leaf)
session.viewports['Viewport: 1'].view.setValues(nearPlane=284008,
    farPlane=471237, width=22133.9, height=8779.36, viewOffsetX=-41800.8,
    viewOffsetY=14240.5)
session.viewports['Viewport: 1'].view.setValues(nearPlane=300676,
    farPlane=464565, width=23432.9, height=9294.62, cameraPosition=(217194,
    144289, 205468), cameraUpVector=(-0.310371, 0.485656, -0.817195),
    cameraTarget=(-77911.2, -65323.7, 28655.5), viewOffsetX=-44254.1,
    viewOffsetY=15076.3)
session.viewports['Viewport: 1'].view.setValues(nearPlane=299136,
    farPlane=466105, width=41429.4, height=16432.9, viewOffsetX=-54714.4,
    viewOffsetY=21952.6)
session.viewports['Viewport: 1'].view.setValues(nearPlane=278535,
    farPlane=461730, width=38576.3, height=15301.2, cameraPosition=(265255,
    85479.7, 100353), cameraUpVector=(-0.459476, 0.574644, -0.677249),
    cameraTarget=(-98170.9, -67862.3, 18530.3), viewOffsetX=-50946.4,
    viewOffsetY=20440.8)
session.viewports['Viewport: 1'].view.setValues(nearPlane=276223,
    farPlane=464042, width=70694.9, height=28041, viewOffsetX=-47211.9,
    viewOffsetY=23306.2)
session.viewports['Viewport: 1'].view.setValues(nearPlane=297347,
    farPlane=464539, width=76101.1, height=30185.4, cameraPosition=(208783,
    165465, 195313), cameraUpVector=(-0.452273, 0.541877, -0.708391),
    cameraTarget=(-71553.8, -59120, 12940), viewOffsetX=-50822.4,
    viewOffsetY=25088.6)
session.viewports['Viewport: 1'].view.setValues(nearPlane=272382,
    farPlane=467444, width=69711.8, height=27651.1, cameraPosition=(273453,
    50241.4, 93204.4), cameraUpVector=(-0.478552, 0.799612, -0.362779),
    cameraTarget=(-102365, -52990.7, -8730.26), viewOffsetX=-46555.4,
    viewOffsetY=22982.2)
session.viewports['Viewport: 1'].view.setValues(nearPlane=276295,
    farPlane=463529, width=30005.3, height=11901.6, viewOffsetX=-44657.5,
    viewOffsetY=21878.7)
session.viewports['Viewport: 1'].view.setValues(nearPlane=281874,
    farPlane=460078, width=30611.1, height=12141.9, cameraPosition=(257061,
    119859, 87949.5), cameraUpVector=(-0.627266, 0.692221, -0.356885),
    cameraTarget=(-93494.2, -53578.8, -8574.83), viewOffsetX=-45559.2,
    viewOffsetY=22320.5)
session.viewports['Viewport: 1'].view.setValues(nearPlane=284142,
    farPlane=457809, width=4174.96, height=1655.99, viewOffsetX=-50581.4,
    viewOffsetY=27184)
i1 = mdb.models['Model-1'].rootAssembly.allInstances['P-1-1']
leaf = dgm.LeafFromInstance(instances=(i1, ))
session.viewports['Viewport: 1'].assemblyDisplay.displayGroup.remove(leaf=leaf)
session.viewports['Viewport: 1'].view.setValues(nearPlane=282416,
    farPlane=459561, width=25534.8, height=10128.3, viewOffsetX=-46468.5,
    viewOffsetY=29769.8)
a = mdb.models['Model-1'].rootAssembly
s1 = a.instances['P-1-1'].faces
side2Faces1 = s1.getSequenceFromMask(mask=('[#3 ]', ), )
region1=regionToolset.Region(side2Faces=side2Faces1)
a = mdb.models['Model-1'].rootAssembly
s1 = a.instances['P-33-1'].edges
side1Edges1 = s1.getSequenceFromMask(mask=('[#28 ]', ), )
s2 = a.instances['P-32-1'].edges
side1Edges2 = s2.getSequenceFromMask(mask=('[#1 ]', ), )
s3 = a.instances['P-20-1'].edges
side1Edges3 = s3.getSequenceFromMask(mask=('[#a101 ]', ), )
s4 = a.instances['P-19-1'].edges
side1Edges4 = s4.getSequenceFromMask(mask=('[#101 ]', ), )
region2=regionToolset.Region(side1Edges=side1Edges1+side1Edges2+side1Edges3+\
    side1Edges4)
mdb.models['Model-1'].Tie(name='Constraint-2', main=region1, secondary=region2,
    positionToleranceMethod=COMPUTED, adjust=ON, tieRotations=ON, thickness=ON)
session.viewports['Viewport: 1'].view.setValues(nearPlane=282236,
    farPlane=459742, width=27689.3, height=10982.9, viewOffsetX=-45925.2,
    viewOffsetY=29759.7)
session.viewports['Viewport: 1'].view.setValues(nearPlane=286412,
    farPlane=460406, width=28099, height=11145.4, cameraPosition=(246059,
    137416, 116801), cameraUpVector=(-0.63376, 0.664606, -0.395785),
    cameraTarget=(-86454, -52302.4, -8611.81), viewOffsetX=-46604.8,
    viewOffsetY=30200)
leaf = dgm.Leaf(leafType=DEFAULT_MODEL)
session.viewports['Viewport: 1'].assemblyDisplay.displayGroup.replace(
    leaf=leaf)
session.viewports['Viewport: 1'].view.setValues(nearPlane=285620,
    farPlane=461155, width=37289.8, height=14790.9, viewOffsetX=-47289.3,
    viewOffsetY=31690.8)
session.viewports['Viewport: 1'].view.setValues(nearPlane=274964,
    farPlane=453202, width=35898.5, height=14239.1, cameraPosition=(257285,
    103941, -28115.9), cameraUpVector=(-0.661852, 0.749033, -0.0300263),
    cameraTarget=(-116269, -46365.9, -15798.8), viewOffsetX=-45525,
    viewOffsetY=30508.4)
session.viewports['Viewport: 1'].view.setValues(nearPlane=274531,
    farPlane=453635, width=40582, height=16096.8, viewOffsetX=-37038.4,
    viewOffsetY=30293.8)
session.viewports['Viewport: 1'].view.setValues(nearPlane=266756,
    farPlane=455396, width=39432.8, height=15640.9, cameraPosition=(248107,
    59035.5, -97758.1), cameraUpVector=(-0.570607, 0.820057, 0.0437447),
    cameraTarget=(-130358, -45373.3, -7483.25), viewOffsetX=-35989.5,
    viewOffsetY=29435.9)
session.viewports['Viewport: 1'].view.setValues(nearPlane=268415,
    farPlane=453739, width=20720.4, height=8218.73, viewOffsetX=-24456.8,
    viewOffsetY=24901.4)
session.viewports['Viewport: 1'].view.setValues(nearPlane=266624,
    farPlane=454385, width=20582.2, height=8163.91, cameraPosition=(248990,
    10217.1, -109276), cameraUpVector=(-0.511261, 0.850749, -0.121816),
    cameraTarget=(-133899, -46020.2, 2613.63), viewOffsetX=-24293.6,
    viewOffsetY=24735.3)
session.viewports['Viewport: 1'].view.setValues(nearPlane=265618,
    farPlane=455390, width=33582, height=13320.2, viewOffsetX=-16991,
    viewOffsetY=18512.4)
session.viewports['Viewport: 1'].view.setValues(nearPlane=264159,
    farPlane=452729, width=33397.6, height=13247.1, cameraPosition=(258109,
    26847.2, -71871.1), cameraUpVector=(-0.531438, 0.832224, -0.158041),
    cameraTarget=(-131672, -47507.5, -2384), viewOffsetX=-16897.7,
    viewOffsetY=18410.7)
session.viewports['Viewport: 1'].view.setValues(nearPlane=262892,
    farPlane=453996, width=50080.7, height=19864.4, viewOffsetX=-18333.1,
    viewOffsetY=18976.7)
session.viewports['Viewport: 1'].view.setValues(nearPlane=258539,
    farPlane=448310, width=49251.5, height=19535.5, cameraPosition=(264527,
    38448.8, 37996.6), cameraUpVector=(-0.4818, 0.808146, -0.338775),
    cameraTarget=(-125347, -49205.4, -13007.2), viewOffsetX=-18029.5,
    viewOffsetY=18662.5)
session.viewports['Viewport: 1'].view.setValues(nearPlane=258430,
    farPlane=448420, width=49316.4, height=19561.3, viewOffsetX=-28818.1,
    viewOffsetY=16803.2)
session.viewports['Viewport: 1'].view.setValues(nearPlane=258606,
    farPlane=448244, width=49350, height=19574.6, cameraPosition=(264238,
    41608.8, 34776.5), cameraUpVector=(-0.498441, 0.830235, -0.249534),
    cameraTarget=(-125636, -46045.4, -16227.3), viewOffsetX=-28837.8,
    viewOffsetY=16814.6)
session.viewports['Viewport: 1'].view.setValues(nearPlane=255947,
    farPlane=450904, width=83037.3, height=32936.6, viewOffsetX=-25175.4,
    viewOffsetY=17026.3)
session.viewports['Viewport: 1'].view.setValues(nearPlane=257656,
    farPlane=444858, width=83591.9, height=33156.6, cameraPosition=(220167,
    75818.2, 176392), cameraUpVector=(-0.385473, 0.757206, -0.527304),
    cameraTarget=(-104986, -52023.7, -24152.2), viewOffsetX=-25343.5,
    viewOffsetY=17140)
session.viewports['Viewport: 1'].view.setValues(nearPlane=262000,
    farPlane=440514, width=34625.2, height=13734, viewOffsetX=-52535.7,
    viewOffsetY=12825.5)
i1 = mdb.models['Model-1'].rootAssembly.allInstances['P-1-1']
leaf = dgm.LeafFromInstance(instances=(i1, ))
session.viewports['Viewport: 1'].assemblyDisplay.displayGroup.remove(leaf=leaf)
session.viewports['Viewport: 1'].view.setValues(nearPlane=261184,
    farPlane=441435, width=45934.6, height=18219.9, viewOffsetX=-52283,
    viewOffsetY=13097.7)
session.viewports['Viewport: 1'].view.setValues(nearPlane=244249,
    farPlane=436189, width=42956.3, height=17038.5, cameraPosition=(252132,
    8170.39, 63395.4), cameraUpVector=(-0.385742, 0.866537, -0.316728),
    cameraTarget=(-138048, -42222, -23243.6), viewOffsetX=-48893.1,
    viewOffsetY=12248.5)
session.viewports['Viewport: 1'].view.setValues(nearPlane=242186,
    farPlane=438252, width=72413.1, height=28722.5, viewOffsetX=-44286.2,
    viewOffsetY=11431.4)
session.viewports['Viewport: 1'].view.setValues(nearPlane=234952,
    farPlane=429752, width=70250.2, height=27864.6, cameraPosition=(234762,
    -33140.7, -61990.6), cameraUpVector=(-0.363348, 0.917449, -0.162065),
    cameraTarget=(-163662, -34050.6, -2455.72), viewOffsetX=-42963.3,
    viewOffsetY=11089.9)
session.viewports['Viewport: 1'].view.setValues(nearPlane=240386,
    farPlane=424319, width=9724.52, height=3857.21, viewOffsetX=-23590.3,
    viewOffsetY=6538.2)
a = mdb.models['Model-1'].rootAssembly
s1 = a.instances['P-1-1'].faces
side1Faces1 = s1.getSequenceFromMask(mask=('[#3 ]', ), )
region1=regionToolset.Region(side1Faces=side1Faces1)
a = mdb.models['Model-1'].rootAssembly
s1 = a.instances['P-3-1'].edges
side1Edges1 = s1.getSequenceFromMask(mask=('[#9 ]', ), )
region2=regionToolset.Region(side1Edges=side1Edges1)
mdb.models['Model-1'].Tie(name='Constraint-3', main=region1, secondary=region2,
    positionToleranceMethod=COMPUTED, adjust=ON, tieRotations=ON, thickness=ON)
session.viewports['Viewport: 1'].view.setValues(nearPlane=239434,
    farPlane=425271, width=21913.9, height=8692.12, viewOffsetX=-24610.3,
    viewOffsetY=6359.26)
session.viewports['Viewport: 1'].view.setValues(nearPlane=240752,
    farPlane=428085, width=22034.5, height=8739.96, cameraPosition=(208742,
    -58172, -127512), cameraUpVector=(-0.340814, 0.929765, -0.139223),
    cameraTarget=(-167097, -30203.8, 14789.8), viewOffsetX=-24745.7,
    viewOffsetY=6394.26)
session.viewports['Viewport: 1'].view.setValues(nearPlane=241810,
    farPlane=427026, width=9390.84, height=3724.86, viewOffsetX=-19171,
    viewOffsetY=4787.71)
i1 = mdb.models['Model-1'].rootAssembly.allInstances['P-2-1']
leaf = dgm.LeafFromInstance(instances=(i1, ))
session.viewports['Viewport: 1'].assemblyDisplay.displayGroup.remove(leaf=leaf)
session.viewports['Viewport: 1'].view.setValues(nearPlane=240958,
    farPlane=426746, width=20359.8, height=8075.67, viewOffsetX=-17894.2,
    viewOffsetY=4591.52)
i1 = mdb.models['Model-1'].rootAssembly.allInstances['P-6-1']
leaf = dgm.LeafFromInstance(instances=(i1, ))
session.viewports['Viewport: 1'].assemblyDisplay.displayGroup.replace(
    leaf=leaf)
session.viewports['Viewport: 1'].view.setValues(nearPlane=396912,
    farPlane=420734, width=25201.5, height=9996.13, viewOffsetX=-28351.5,
    viewOffsetY=8116.05)
leaf = dgm.Leaf(leafType=DEFAULT_MODEL)
session.viewports['Viewport: 1'].assemblyDisplay.displayGroup.replace(
    leaf=leaf)
i1 = mdb.models['Model-1'].rootAssembly.allInstances['P-4-1']
i2 = mdb.models['Model-1'].rootAssembly.allInstances['P-5-1']
i3 = mdb.models['Model-1'].rootAssembly.allInstances['P-6-1']
leaf = dgm.LeafFromInstance(instances=(i1, i2, i3, ))
session.viewports['Viewport: 1'].assemblyDisplay.displayGroup.replace(
    leaf=leaf)
i1 = mdb.models['Model-1'].rootAssembly.allInstances['P-7-1']
leaf = dgm.LeafFromInstance(instances=(i1, ))
session.viewports['Viewport: 1'].assemblyDisplay.displayGroup.remove(leaf=leaf)
i1 = mdb.models['Model-1'].rootAssembly.allInstances['P-8-1']
leaf = dgm.LeafFromInstance(instances=(i1, ))
session.viewports['Viewport: 1'].assemblyDisplay.displayGroup.remove(leaf=leaf)
i1 = mdb.models['Model-1'].rootAssembly.allInstances['P-9-1']
leaf = dgm.LeafFromInstance(instances=(i1, ))
session.viewports['Viewport: 1'].assemblyDisplay.displayGroup.remove(leaf=leaf)
i1 = mdb.models['Model-1'].rootAssembly.allInstances['P-50-1']
leaf = dgm.LeafFromInstance(instances=(i1, ))
session.viewports['Viewport: 1'].assemblyDisplay.displayGroup.remove(leaf=leaf)
i1 = mdb.models['Model-1'].rootAssembly.allInstances['P-4-1']
leaf = dgm.LeafFromInstance(instances=(i1, ))
session.viewports['Viewport: 1'].assemblyDisplay.displayGroup.remove(leaf=leaf)
i1 = mdb.models['Model-1'].rootAssembly.allInstances['P-4-1']
leaf = dgm.LeafFromInstance(instances=(i1, ))
session.viewports['Viewport: 1'].assemblyDisplay.displayGroup.add(leaf=leaf)
i1 = mdb.models['Model-1'].rootAssembly.allInstances['P-12-1']
leaf = dgm.LeafFromInstance(instances=(i1, ))
session.viewports['Viewport: 1'].assemblyDisplay.displayGroup.remove(leaf=leaf)
i1 = mdb.models['Model-1'].rootAssembly.allInstances['P-11-1']
leaf = dgm.LeafFromInstance(instances=(i1, ))
session.viewports['Viewport: 1'].assemblyDisplay.displayGroup.remove(leaf=leaf)
i1 = mdb.models['Model-1'].rootAssembly.allInstances['P-4-1']
i2 = mdb.models['Model-1'].rootAssembly.allInstances['P-5-1']
i3 = mdb.models['Model-1'].rootAssembly.allInstances['P-6-1']
leaf = dgm.LeafFromInstance(instances=(i1, i2, i3, ))
session.viewports['Viewport: 1'].assemblyDisplay.displayGroup.replace(
    leaf=leaf)
i1 = mdb.models['Model-1'].rootAssembly.allInstances['P-4-1']
i2 = mdb.models['Model-1'].rootAssembly.allInstances['P-5-1']
i3 = mdb.models['Model-1'].rootAssembly.allInstances['P-6-1']
leaf = dgm.LeafFromInstance(instances=(i1, i2, i3, ))
session.viewports['Viewport: 1'].assemblyDisplay.displayGroup.replace(
    leaf=leaf)
session.viewports['Viewport: 1'].view.setValues(nearPlane=396937,
    farPlane=420662, width=17454, height=6923.1, viewOffsetX=-30818.1,
    viewOffsetY=7247.44)
i1 = mdb.models['Model-1'].rootAssembly.allInstances['P-4-1']
i2 = mdb.models['Model-1'].rootAssembly.allInstances['P-5-1']
i3 = mdb.models['Model-1'].rootAssembly.allInstances['P-6-1']
leaf = dgm.LeafFromInstance(instances=(i1, i2, i3, ))
session.viewports['Viewport: 1'].assemblyDisplay.displayGroup.replace(
    leaf=leaf)
session.viewports['Viewport: 1'].view.setValues(nearPlane=396748,
    farPlane=420851, width=18172.6, height=7208.12, viewOffsetX=-30573.8,
    viewOffsetY=7667.16)
i1 = mdb.models['Model-1'].rootAssembly.allInstances['P-4-1']
leaf = dgm.LeafFromInstance(instances=(i1, ))
session.viewports['Viewport: 1'].assemblyDisplay.displayGroup.replace(
    leaf=leaf)
i1 = mdb.models['Model-1'].rootAssembly.allInstances['P-5-1']
leaf = dgm.LeafFromInstance(instances=(i1, ))
session.viewports['Viewport: 1'].assemblyDisplay.displayGroup.add(leaf=leaf)
i1 = mdb.models['Model-1'].rootAssembly.allInstances['P-6-1']
leaf = dgm.LeafFromInstance(instances=(i1, ))
session.viewports['Viewport: 1'].assemblyDisplay.displayGroup.add(leaf=leaf)
session.viewports['Viewport: 1'].view.setValues(nearPlane=396678,
    farPlane=420920, width=20536.6, height=8145.79, viewOffsetX=-30325.2,
    viewOffsetY=7983.75)
i1 = mdb.models['Model-1'].rootAssembly.allInstances['P-6-1']
leaf = dgm.LeafFromInstance(instances=(i1, ))
session.viewports['Viewport: 1'].assemblyDisplay.displayGroup.replace(
    leaf=leaf)
i1 = mdb.models['Model-1'].rootAssembly.allInstances['P-4-1']
i2 = mdb.models['Model-1'].rootAssembly.allInstances['P-5-1']
leaf = dgm.LeafFromInstance(instances=(i1, i2, ))
session.viewports['Viewport: 1'].assemblyDisplay.displayGroup.replace(
    leaf=leaf)
i1 = mdb.models['Model-1'].rootAssembly.allInstances['P-6-1']
leaf = dgm.LeafFromInstance(instances=(i1, ))
session.viewports['Viewport: 1'].assemblyDisplay.displayGroup.replace(
    leaf=leaf)
session.viewports['Viewport: 1'].view.setValues(nearPlane=397297,
    farPlane=420349, width=20604.4, height=8172.69, viewOffsetX=-28452.8,
    viewOffsetY=7821.65)
i1 = mdb.models['Model-1'].rootAssembly.allInstances['P-4-1']
i2 = mdb.models['Model-1'].rootAssembly.allInstances['P-5-1']
leaf = dgm.LeafFromInstance(instances=(i1, i2, ))
session.viewports['Viewport: 1'].assemblyDisplay.displayGroup.replace(
    leaf=leaf)
session.viewports['Viewport: 1'].view.setValues(nearPlane=396934,
    farPlane=420664, width=17484.3, height=6935.11, viewOffsetX=-30184.3,
    viewOffsetY=7971.16)
session.viewports['Viewport: 1'].view.setValues(nearPlane=396498,
    farPlane=420785, width=17465.1, height=6927.48, cameraPosition=(167683,
    -61904.5, -196874), cameraUpVector=(-0.323406, 0.945644, -0.0341528),
    cameraTarget=(-172912, -28707.8, 15681.3), viewOffsetX=-30151.1,
    viewOffsetY=7962.39)
session.viewports['Viewport: 1'].view.setValues(nearPlane=396436,
    farPlane=420846, width=18947.9, height=7515.64, viewOffsetX=-30161.3,
    viewOffsetY=7997.95)
session.viewports['Viewport: 1'].view.setValues(nearPlane=396373,
    farPlane=420742, width=18944.9, height=7514.46, cameraPosition=(138926,
    -57235.6, -232909), cameraUpVector=(-0.323651, 0.945969, 0.0198192),
    cameraTarget=(-175839, -28207.3, 16825), viewOffsetX=-30156.6,
    viewOffsetY=7996.7)
session.viewports['Viewport: 1'].view.setValues(nearPlane=396227,
    farPlane=420889, width=21479.7, height=8519.9, viewOffsetX=-25267.6,
    viewOffsetY=8729.6)
session.viewports['Viewport: 1'].view.setValues(nearPlane=397149,
    farPlane=421405, width=21529.7, height=8539.72, cameraPosition=(86825.1,
    -75221.3, -278864), cameraUpVector=(-0.264292, 0.962554, 0.0603359),
    cameraTarget=(-180022, -27664, 19158.9), viewOffsetX=-25326.3,
    viewOffsetY=8749.9)
session.viewports['Viewport: 1'].view.setValues(nearPlane=396621,
    farPlane=421932, width=28662.7, height=11369, viewOffsetX=-28320.5,
    viewOffsetY=8890.96)
a = mdb.models['Model-1'].rootAssembly
s1 = a.instances['P-6-1'].faces
side1Faces1 = s1.getSequenceFromMask(mask=('[#ffffffff:6 ]', ), )
region1=regionToolset.Region(side1Faces=side1Faces1)
a = mdb.models['Model-1'].rootAssembly
s1 = a.instances['P-5-1'].edges
side1Edges1 = s1.getSequenceFromMask(mask=('[#88444444 #738e38 ]', ), )
s2 = a.instances['P-4-1'].edges
side1Edges2 = s2.getSequenceFromMask(mask=('[#c71c71c7 #71c1c71 #707 ]', ), )
region2=regionToolset.Region(side1Edges=side1Edges1+side1Edges2)
mdb.models['Model-1'].Tie(name='Constraint-4', main=region1, secondary=region2,
    positionToleranceMethod=COMPUTED, adjust=ON, tieRotations=ON, thickness=ON)
leaf = dgm.Leaf(leafType=DEFAULT_MODEL)
session.viewports['Viewport: 1'].assemblyDisplay.displayGroup.replace(
    leaf=leaf)
session.viewports['Viewport: 1'].view.setValues(nearPlane=268055,
    farPlane=429114, width=31616.3, height=12540.5, viewOffsetX=-15997,
    viewOffsetY=5616.56)
session.viewports['Viewport: 1'].view.setValues(nearPlane=267585,
    farPlane=429584, width=37223.6, height=14764.7, viewOffsetX=-14690.9,
    viewOffsetY=5224.18)
session.viewports['Viewport: 1'].view.setValues(nearPlane=241093,
    farPlane=423254, width=33538.3, height=13302.9, cameraPosition=(153745,
    -30021.9, -213325), cameraUpVector=(-0.411246, 0.911519, 0.00308137),
    cameraTarget=(-184760, -36163.5, 4994.31), viewOffsetX=-13236.4,
    viewOffsetY=4706.96)
session.viewports['Viewport: 1'].view.setValues(nearPlane=238738,
    farPlane=425609, width=66823.9, height=26505.6, viewOffsetX=-11476,
    viewOffsetY=6276.66)
session.viewports['Viewport: 1'].view.setValues(nearPlane=238510,
    farPlane=425837, width=66760.1, height=26480.3, cameraPosition=(154628,
    -31575.9, -212000), cameraUpVector=(-0.470554, 0.877787, -0.0898254),
    cameraTarget=(-183877, -37717.5, 6319.62), viewOffsetX=-11465.1,
    viewOffsetY=6270.66)
session.viewports['Viewport: 1'].view.setValues(nearPlane=236317,
    farPlane=428031, width=95679.5, height=37951.1, viewOffsetX=-8749.41,
    viewOffsetY=8150.33)
session.viewports['Viewport: 1'].view.setValues(nearPlane=193732,
    farPlane=392686, width=78438, height=31112.3, cameraPosition=(209590,
    -16792.1, 13965), cameraUpVector=(-0.297712, 0.679781, -0.670273),
    cameraTarget=(-189340, -42880.4, -35643.2), viewOffsetX=-7172.77,
    viewOffsetY=6681.64)
session.viewports['Viewport: 1'].view.setValues(nearPlane=195663,
    farPlane=390756, width=70700.3, height=28043.2, viewOffsetX=-29263.9,
    viewOffsetY=-13946.2)
session.viewports['Viewport: 1'].view.setValues(nearPlane=195911,
    farPlane=390507, width=70790.1, height=28078.8, cameraPosition=(209686,
    -21234.2, 15530.1), cameraUpVector=(-0.285552, 0.615745, -0.734383),
    cameraTarget=(-189244, -47322.5, -34078.1), viewOffsetX=-29301.1,
    viewOffsetY=-13963.9)
session.viewports['Viewport: 1'].view.setValues(nearPlane=193605,
    farPlane=392814, width=101016, height=40067.8, viewOffsetX=-23734.2,
    viewOffsetY=-10992.6)
session.viewports['Viewport: 1'].view.setValues(nearPlane=200888,
    farPlane=364943, width=104816, height=41575.1, cameraPosition=(118211,
    43366.6, 218316), cameraUpVector=(0.222858, 0.539805, -0.811754),
    cameraTarget=(-119089, -69230.5, -87131.1), viewOffsetX=-24627,
    viewOffsetY=-11406.1)
session.viewports['Viewport: 1'].view.setValues(nearPlane=205852,
    farPlane=359980, width=45892.8, height=18203.3, viewOffsetX=-56968.8,
    viewOffsetY=-36184.3)
session.viewports['Viewport: 1'].view.setValues(nearPlane=165639,
    farPlane=357305, width=36927.7, height=14647.3, cameraPosition=(171032,
    -58456.8, 64774), cameraUpVector=(-0.0239711, 0.791047, -0.611285),
    cameraTarget=(-203741, -7130.22, -73783), viewOffsetX=-45840,
    viewOffsetY=-29115.7)
session.viewports['Viewport: 1'].view.setValues(nearPlane=160824,
    farPlane=349103, width=35854.3, height=14221.5, cameraPosition=(164794,
    -68149.4, 4515.8), cameraUpVector=(-0.113719, 0.831684, -0.543479),
    cameraTarget=(-227801, 5194.54, -48179.2), viewOffsetX=-44507.5,
    viewOffsetY=-28269.4)
session.viewports['Viewport: 1'].view.setValues(nearPlane=162701,
    farPlane=347226, width=14801.4, height=5870.95, viewOffsetX=-28422.6,
    viewOffsetY=-23831.4)
i1 = mdb.models['Model-1'].rootAssembly.allInstances['P-1-1']
leaf = dgm.LeafFromInstance(instances=(i1, ))
session.viewports['Viewport: 1'].assemblyDisplay.displayGroup.remove(leaf=leaf)
session.viewports['Viewport: 1'].view.setValues(nearPlane=161910,
    farPlane=348067, width=26085, height=10346.6, viewOffsetX=-28044,
    viewOffsetY=-23458.1)
session.viewports['Viewport: 1'].view.setValues(nearPlane=165063,
    farPlane=346442, width=26592.9, height=10548, cameraPosition=(154781,
    -83175.1, -36698), cameraUpVector=(-0.14257, 0.853359, -0.50145),
    cameraTarget=(-235555, 15773.1, -25120.8), viewOffsetX=-28590.1,
    viewOffsetY=-23914.9)
session.viewports['Viewport: 1'].view.setValues(nearPlane=166304,
    farPlane=345202, width=12357.4, height=4901.54, viewOffsetX=-22446,
    viewOffsetY=-23110.9)
i1 = mdb.models['Model-1'].rootAssembly.allInstances['P-2-1']
leaf = dgm.LeafFromInstance(instances=(i1, ))
session.viewports['Viewport: 1'].assemblyDisplay.displayGroup.remove(leaf=leaf)
session.viewports['Viewport: 1'].view.setValues(nearPlane=164811,
    farPlane=345651, width=30168.5, height=11966.3, viewOffsetX=-22942.1,
    viewOffsetY=-22715.9)
session.viewports['Viewport: 1'].view.setValues(nearPlane=173493,
    farPlane=349686, width=31757.8, height=12596.7, cameraPosition=(112882,
    -128580, -104600), cameraUpVector=(-0.0772671, 0.903353, -0.42188),
    cameraTarget=(-228297, 47712.2, 17075.8), viewOffsetX=-24150.7,
    viewOffsetY=-23912.7)
session.viewports['Viewport: 1'].view.setValues(nearPlane=174731,
    farPlane=348448, width=16644.8, height=6602.14, viewOffsetX=-14063.5,
    viewOffsetY=-25149.6)
a = mdb.models['Model-1'].rootAssembly
s1 = a.instances['P-1-1'].faces
side1Faces1 = s1.getSequenceFromMask(mask=('[#3 ]', ), )
region1=regionToolset.Region(side1Faces=side1Faces1)
a = mdb.models['Model-1'].rootAssembly
s1 = a.instances['P-4-1'].edges
side1Edges1 = s1.getSequenceFromMask(mask=('[#10410410 #50414104 #1050 ]', ), )
s2 = a.instances['P-5-1'].edges
side1Edges2 = s2.getSequenceFromMask(mask=('[#22111111 #42082 ]', ), )
s3 = a.instances['P-16-1'].edges
side1Edges3 = s3.getSequenceFromMask(mask=('[#800820 ]', ), )
region2=regionToolset.Region(side1Edges=side1Edges1+side1Edges2+side1Edges3)
mdb.models['Model-1'].Tie(name='Constraint-5', main=region1, secondary=region2,
    positionToleranceMethod=COMPUTED, adjust=ON, tieRotations=ON, thickness=ON)
session.viewports['Viewport: 1'].view.setValues(nearPlane=175158,
    farPlane=348022, width=11555.3, height=4583.38, viewOffsetX=-15846.9,
    viewOffsetY=-25984.6)
session.viewports['Viewport: 1'].view.setValues(nearPlane=179748,
    farPlane=348379, width=11858.1, height=4703.48, cameraPosition=(98961.1,
    -136011, -122054), cameraUpVector=(-0.0572639, 0.918795, -0.39056),
    cameraTarget=(-223163, 53811.9, 27913), viewOffsetX=-16262.2,
    viewOffsetY=-26665.5)
session.viewports['Viewport: 1'].view.setValues(nearPlane=178928,
    farPlane=349198, width=21813, height=8652.09, viewOffsetX=-10395.9,
    viewOffsetY=-26625.6)
session.viewports['Viewport: 1'].view.setValues(nearPlane=185061,
    farPlane=349591, width=22560.7, height=8948.68, cameraPosition=(83842.7,
    -145307, -137352), cameraUpVector=(-0.039065, 0.923613, -0.38133),
    cameraTarget=(-216812, 59038.9, 36245.4), viewOffsetX=-10752.3,
    viewOffsetY=-27538.3)
session.viewports['Viewport: 1'].view.setValues(nearPlane=186221,
    farPlane=348432, width=8181.78, height=3245.29, viewOffsetX=-11025,
    viewOffsetY=-28376.9)
session.viewports['Viewport: 1'].view.setValues(nearPlane=191779,
    farPlane=348161, width=8426, height=3342.16, cameraPosition=(71443.4,
    -152936, -147299), cameraUpVector=(-0.00526782, 0.931135, -0.364636),
    cameraTarget=(-210412, 63835.6, 42053.6), viewOffsetX=-11354.1,
    viewOffsetY=-29224)
session.viewports['Viewport: 1'].view.setValues(nearPlane=192336,
    farPlane=347604, width=1728.73, height=685.696, viewOffsetX=-11153.5,
    viewOffsetY=-29894)
i1 = mdb.models['Model-1'].rootAssembly.allInstances['P-8-1']
i2 = mdb.models['Model-1'].rootAssembly.allInstances['P-9-1']
leaf = dgm.LeafFromInstance(instances=(i1, i2, ))
session.viewports['Viewport: 1'].assemblyDisplay.displayGroup.replace(
    leaf=leaf)
session.viewports['Viewport: 1'].view.setValues(nearPlane=318003,
    farPlane=336096, width=3962.11, height=1571.56, viewOffsetX=-18291.8,
    viewOffsetY=-49424.1)
i1 = mdb.models['Model-1'].rootAssembly.allInstances['P-6-1']
leaf = dgm.LeafFromInstance(instances=(i1, ))
session.viewports['Viewport: 1'].assemblyDisplay.displayGroup.add(leaf=leaf)
session.viewports['Viewport: 1'].view.setValues(nearPlane=317329,
    farPlane=336815, width=6073.21, height=2408.93, viewOffsetX=-17311.4,
    viewOffsetY=-49457.9)
i1 = mdb.models['Model-1'].rootAssembly.allInstances['P-6-1']
leaf = dgm.LeafFromInstance(instances=(i1, ))
session.viewports['Viewport: 1'].assemblyDisplay.displayGroup.remove(leaf=leaf)
session.viewports['Viewport: 1'].view.setValues(nearPlane=317690,
    farPlane=336409, width=7701.86, height=3054.93, viewOffsetX=-17852.4,
    viewOffsetY=-49336)
session.viewports['Viewport: 1'].view.setValues(nearPlane=316960,
    farPlane=334628, width=7684.15, height=3047.91, cameraPosition=(26531.5,
    -168358, -180377), cameraUpVector=(0.0350005, 0.937705, -0.345666),
    cameraTarget=(-202806, 68676, 50937), viewOffsetX=-17811.4,
    viewOffsetY=-49222.5)
session.viewports['Viewport: 1'].view.setValues(nearPlane=316874,
    farPlane=334714, width=9044.71, height=3587.57, viewOffsetX=-17861,
    viewOffsetY=-49234.8)
session.viewports['Viewport: 1'].view.setValues(nearPlane=315991,
    farPlane=329306, width=9019.5, height=3577.57, cameraPosition=(-107170,
    -162151, -244133), cameraUpVector=(0.118279, 0.957788, -0.262016),
    cameraTarget=(-178411, 73982.6, 74383), viewOffsetX=-17811.2,
    viewOffsetY=-49097.7)
session.viewports['Viewport: 1'].view.setValues(nearPlane=316234,
    farPlane=329064, width=6522.91, height=2587.3, viewOffsetX=-18075.8,
    viewOffsetY=-49304.1)
session.viewports['Viewport: 1'].view.setValues(nearPlane=316382,
    farPlane=334222, width=6525.97, height=2588.51, cameraPosition=(23473.4,
    -143530, -197551), cameraUpVector=(0.0290638, 0.968644, -0.246747),
    cameraTarget=(-204198, 67362.9, 59308.6), viewOffsetX=-18084.3,
    viewOffsetY=-49327.2)
session.viewports['Viewport: 1'].view.setValues(nearPlane=316194,
    farPlane=334410, width=9041.02, height=3586.1, viewOffsetX=-18212.8,
    viewOffsetY=-49336.1)
session.viewports['Viewport: 1'].view.setValues(nearPlane=316500,
    farPlane=335749, width=9049.77, height=3589.57, cameraPosition=(60533.9,
    -130565, -172493), cameraUpVector=(0.015291, 0.973339, -0.228859),
    cameraTarget=(-209428, 64851.8, 53824.4), viewOffsetX=-18230.4,
    viewOffsetY=-49383.9)
session.viewports['Viewport: 1'].view.setValues(nearPlane=316692,
    farPlane=335557, width=7126.22, height=2826.6, viewOffsetX=-18726.8,
    viewOffsetY=-49287.1)
session.viewports['Viewport: 1'].view.setValues(nearPlane=315533,
    farPlane=329036, width=7100.15, height=2816.26, cameraPosition=(-118517,
    -106773, -268054), cameraUpVector=(-0.045949, 0.993098, -0.107915),
    cameraTarget=(-189173, 64068.9, 89866.7), viewOffsetX=-18658.3,
    viewOffsetY=-49106.7)
session.viewports['Viewport: 1'].view.setValues(nearPlane=315725,
    farPlane=328844, width=5134, height=2036.39, viewOffsetX=-18933.8,
    viewOffsetY=-49297.9)
session.viewports['Viewport: 1'].view.setValues(nearPlane=315455,
    farPlane=334212, width=5129.63, height=2034.66, cameraPosition=(26901.1,
    -78740.4, -219501), cameraUpVector=(-0.206956, 0.966266, -0.153292),
    cameraTarget=(-221673, 52753.7, 68954.2), viewOffsetX=-18917.6,
    viewOffsetY=-49255.8)
session.viewports['Viewport: 1'].view.setValues(nearPlane=315437,
    farPlane=334230, width=5565.69, height=2207.62, viewOffsetX=-18852.5,
    viewOffsetY=-49290.5)
session.viewports['Viewport: 1'].view.setValues(nearPlane=315762,
    farPlane=329681, width=5571.42, height=2209.89, cameraPosition=(-106720,
    -101205, -268278), cameraUpVector=(-0.0881407, 0.991284, -0.0979114),
    cameraTarget=(-195043, 61735.2, 89403), viewOffsetX=-18871.9,
    viewOffsetY=-49341.3)
session.viewports['Viewport: 1'].view.setValues(nearPlane=313289,
    farPlane=332154, width=35309.6, height=14005.5, viewOffsetX=-17972.9,
    viewOffsetY=-46313.1)
session.viewports['Viewport: 1'].view.setValues(nearPlane=315383,
    farPlane=327695, width=35545.7, height=14099.1, cameraPosition=(-114210,
    -326467, -35289.8), cameraUpVector=(0.0040137, 0.421837, -0.906663),
    cameraTarget=(-188226, 67965.4, -210.348), viewOffsetX=-18093,
    viewOffsetY=-46622.7)
session.viewports['Viewport: 1'].view.setValues(nearPlane=311520,
    farPlane=329388, width=35110.3, height=13926.4, cameraPosition=(-219602,
    -206053, 296549), cameraUpVector=(0.113224, -0.675812, -0.728326),
    cameraTarget=(-161725, -16867.4, -54371), viewOffsetX=-17871.4,
    viewOffsetY=-46051.6)
session.viewports['Viewport: 1'].view.setValues(nearPlane=311527,
    farPlane=329552, width=35111.1, height=13926.7, cameraPosition=(-223860,
    -111855, 344699), cameraUpVector=(0.00658757, -0.873273, -0.487186),
    cameraTarget=(-167341, -45755.9, -48648.3), viewOffsetX=-17871.8,
    viewOffsetY=-46052.6)
session.viewports['Viewport: 1'].view.setValues(nearPlane=311472,
    farPlane=329606, width=37206.8, height=14758, viewOffsetX=-11293.7,
    viewOffsetY=-47152.2)
session.viewports['Viewport: 1'].view.setValues(nearPlane=306660,
    farPlane=331397, width=36632, height=14530, cameraPosition=(44629.3,
    43448.8, -199373), cameraUpVector=(-0.415258, -0.856573, -0.306339),
    cameraTarget=(-221315, -82746.6, 75643), viewOffsetX=-11119.2,
    viewOffsetY=-46423.8)
session.viewports['Viewport: 1'].view.setValues(nearPlane=308241,
    farPlane=330795, width=36820.8, height=14604.9, cameraPosition=(-28990.4,
    -1928.17, -252532), cameraUpVector=(-0.47636, -0.878213, -0.0426975),
    cameraTarget=(-209027, -74341, 100496), viewOffsetX=-11176.5,
    viewOffsetY=-46663.1)
session.viewports['Viewport: 1'].view.setValues(nearPlane=309635,
    farPlane=329402, width=21512.1, height=8532.75, viewOffsetX=-6748.78,
    viewOffsetY=-45753.8)
session.viewports['Viewport: 1'].view.setValues(nearPlane=308758,
    farPlane=330544, width=21451.2, height=8508.57, cameraPosition=(28633.4,
    14355.1, -217811), cameraUpVector=(-0.488616, -0.845752, -0.214379),
    cameraTarget=(-222023, -76180.5, 84282.6), viewOffsetX=-6729.65,
    viewOffsetY=-45624.1)
session.viewports['Viewport: 1'].view.setValues(nearPlane=310352,
    farPlane=328950, width=3372.7, height=1337.78, viewOffsetX=-14123.9,
    viewOffsetY=-41977.7)
a = mdb.models['Model-1'].rootAssembly
s1 = a.instances['P-6-1'].faces
side2Faces1 = s1.getSequenceFromMask(mask=('[#ffffffff:6 ]', ), )
region1=regionToolset.Region(side2Faces=side2Faces1)
a = mdb.models['Model-1'].rootAssembly
s1 = a.instances['P-9-1'].edges
side1Edges1 = s1.getSequenceFromMask(mask=(
    '[#c1820830 #83041820 #820c1060 #41041060 #410410 ]', ), )
s2 = a.instances['P-8-1'].edges
side1Edges2 = s2.getSequenceFromMask(mask=(
    '[#ab56ad5a #5ab56ad5 #d5ab56ad #ad5ab56a #6ad5ab56 #ab ]', ), )
region2=regionToolset.Region(side1Edges=side1Edges1+side1Edges2)
mdb.models['Model-1'].Tie(name='Constraint-6', main=region1, secondary=region2,
    positionToleranceMethod=COMPUTED, adjust=ON, tieRotations=ON, thickness=ON)
session.viewports['Viewport: 1'].view.setValues(nearPlane=310273,
    farPlane=329029, width=4315.14, height=1711.59, viewOffsetX=-13877.5,
    viewOffsetY=-41997)
leaf = dgm.Leaf(leafType=DEFAULT_MODEL)
session.viewports['Viewport: 1'].assemblyDisplay.displayGroup.replace(
    leaf=leaf)
session.viewports['Viewport: 1'].view.setValues(nearPlane=183870,
    farPlane=335840, width=6058.03, height=2402.91, viewOffsetX=-7819.65,
    viewOffsetY=-25127)
session.viewports['Viewport: 1'].view.setValues(session.views['Right'])
session.viewports['Viewport: 1'].view.setValues(session.views['Iso'])
session.viewports['Viewport: 1'].view.setValues(nearPlane=320196,
    farPlane=485501, width=137157, height=54403.1, viewOffsetX=-28070.8,
    viewOffsetY=13529.6)
# mdb.save()
#: The model database has been saved to "F:\temp\A-abaqus-08-wlf-1220-2.cae".
session.viewports['Viewport: 1'].view.setValues(nearPlane=328223,
    farPlane=477474, width=48643.4, height=19294.3, viewOffsetX=-44632.7,
    viewOffsetY=16863.4)
a = mdb.models['Model-1'].rootAssembly
f1 = a.instances['P-1-1'].faces
faces1 = f1.getSequenceFromMask(mask=('[#1 ]', ), )
leaf = dgm.LeafFromGeometry(faceSeq=faces1)
session.viewports['Viewport: 1'].assemblyDisplay.displayGroup.remove(leaf=leaf)
a = mdb.models['Model-1'].rootAssembly
f1 = a.instances['P-1-1'].faces
faces1 = f1.getSequenceFromMask(mask=('[#2 ]', ), )
leaf = dgm.LeafFromGeometry(faceSeq=faces1)
session.viewports['Viewport: 1'].assemblyDisplay.displayGroup.remove(leaf=leaf)
session.viewports['Viewport: 1'].view.setValues(nearPlane=327998,
    farPlane=477802, width=57232.4, height=22701.1, viewOffsetX=-42123.4,
    viewOffsetY=17109.4)
session.viewports['Viewport: 1'].view.setValues(nearPlane=383863,
    farPlane=499827, width=66980.2, height=26567.6, cameraPosition=(-203213,
    105194, 436968), cameraUpVector=(-0.0626855, 0.782531, -0.619448),
    cameraTarget=(-74016.7, -2600.55, 70941.6), viewOffsetX=-49297.9,
    viewOffsetY=20023.5)
session.viewports['Viewport: 1'].view.setValues(nearPlane=385532,
    farPlane=498158, width=36594, height=14514.9, viewOffsetX=-87239.3,
    viewOffsetY=17731.2)
session.viewports['Viewport: 1'].view.setValues(nearPlane=385395,
    farPlane=516635, width=36581, height=14509.8, cameraPosition=(-263426,
    140141, 414303), cameraUpVector=(0.102844, 0.736278, -0.668819),
    cameraTarget=(-84946.2, -3433.67, 82915.2), viewOffsetX=-87208.3,
    viewOffsetY=17724.9)
session.viewports['Viewport: 1'].view.setValues(nearPlane=383986,
    farPlane=518044, width=54917.2, height=21782.8, viewOffsetX=-80349.3,
    viewOffsetY=13359.6)
session.viewports['Viewport: 1'].view.setValues(nearPlane=383632,
    farPlane=512296, width=54866.6, height=21762.8, cameraPosition=(-245769,
    165015, 407940), cameraUpVector=(0.100066, 0.696518, -0.710528),
    cameraTarget=(-81736.4, -816.452, 79489.3), viewOffsetX=-80275.3,
    viewOffsetY=13347.3)
session.viewports['Viewport: 1'].view.setValues(nearPlane=382325,
    farPlane=513604, width=72766.1, height=28862.5, viewOffsetX=-80243,
    viewOffsetY=13535.9)
leaf = dgm.Leaf(leafType=DEFAULT_MODEL)
session.viewports['Viewport: 1'].assemblyDisplay.displayGroup.replace(
    leaf=leaf)
session.viewports['Viewport: 1'].view.setValues(nearPlane=383228,
    farPlane=512519, width=54809, height=21739.9, viewOffsetX=-79874.1,
    viewOffsetY=11334.5)
a = mdb.models['Model-1'].rootAssembly
i1 = a.instances['P-1-1']
leaf = dgm.LeafFromInstance((i1, ))
session.viewports['Viewport: 1'].assemblyDisplay.displayGroup.remove(leaf=leaf)
session.viewports['Viewport: 1'].view.setValues(nearPlane=384814,
    farPlane=511115, width=43079.8, height=17087.5, viewOffsetX=-77976.4,
    viewOffsetY=9400)
session.viewports['Viewport: 1'].view.setValues(nearPlane=388329,
    farPlane=523794, width=43473.4, height=17243.6, cameraPosition=(-280621,
    75515.5, 430607), cameraUpVector=(-0.245374, 0.732186, -0.63537),
    cameraTarget=(-92623.7, 16944.8, 79162.5), viewOffsetX=-78688.7,
    viewOffsetY=9485.87)
session.viewports['Viewport: 1'].view.setValues(nearPlane=396698,
    farPlane=529121, width=44410.3, height=17615.2, cameraPosition=(-273009,
    -90525.6, 442060), cameraUpVector=(-0.340425, 0.872916, -0.34947),
    cameraTarget=(-94404, -7752.48, 90583.6), viewOffsetX=-80384.5,
    viewOffsetY=9690.3)
session.viewports['Viewport: 1'].view.setValues(nearPlane=389894,
    farPlane=535924, width=126379, height=50127.9, viewOffsetX=-67226.3,
    viewOffsetY=13832.6)
session.viewports['Viewport: 1'].view.setValues(nearPlane=328840,
    farPlane=501091, width=106589, height=42278.3, cameraPosition=(237407,
    254713, 83321.8), cameraUpVector=(-0.71923, 0.504321, -0.47788),
    cameraTarget=(-44721.3, -2744.77, -44763.7), viewOffsetX=-56699.2,
    viewOffsetY=11666.5)
session.viewports['Viewport: 1'].view.setValues(nearPlane=346243,
    farPlane=506463, width=112230, height=44515.8, cameraPosition=(194658,
    263544, -160227), cameraUpVector=(-0.924094, 0.321193, -0.207087),
    cameraTarget=(-72333.9, -19823.7, -56762.9), viewOffsetX=-59699.9,
    viewOffsetY=12283.9)
session.viewports['Viewport: 1'].view.setValues(nearPlane=348404,
    farPlane=504302, width=85157, height=33777.4, viewOffsetX=-56436.2,
    viewOffsetY=27528.4)
session.viewports['Viewport: 1'].view.setValues(nearPlane=359157,
    farPlane=497745, width=87785.1, height=34819.8, cameraPosition=(152456,
    321539, -133039), cameraUpVector=(-0.959288, 0.281909, 0.0171575),
    cameraTarget=(-80979.2, -388.986, -68565.4), viewOffsetX=-58177.9,
    viewOffsetY=28378)
session.viewports['Viewport: 1'].view.setValues(nearPlane=365200,
    farPlane=491702, width=16553.6, height=6565.95, viewOffsetX=-75020.4,
    viewOffsetY=42219.7)
session.viewports['Viewport: 1'].view.setValues(nearPlane=351723,
    farPlane=494345, width=15942.7, height=6323.65, cameraPosition=(179783,
    275279, -161142), cameraUpVector=(-0.924351, 0.381533, -0.00266145),
    cameraTarget=(-84882.3, -13316.7, -66533.6), viewOffsetX=-72251.9,
    viewOffsetY=40661.7)
session.viewports['Viewport: 1'].view.setValues(nearPlane=352154,
    farPlane=493912, width=12603.7, height=4999.22, viewOffsetX=-69123.3,
    viewOffsetY=36647)
session.viewports['Viewport: 1'].view.setValues(nearPlane=343536,
    farPlane=495924, width=12295.2, height=4876.87, cameraPosition=(195341,
    238474, -181878), cameraUpVector=(-0.889911, 0.456055, -0.00848402),
    cameraTarget=(-89700.6, -21115.7, -65044.1), viewOffsetX=-67431.6,
    viewOffsetY=35750.1)
session.viewports['Viewport: 1'].view.setValues(nearPlane=343369,
    farPlane=496091, width=13938.6, height=5528.73, viewOffsetX=-63873.9,
    viewOffsetY=33189.5)
session.viewports['Viewport: 1'].view.setValues(nearPlane=327389,
    farPlane=498431, width=13290, height=5271.44, cameraPosition=(225589,
    149762, -209110), cameraUpVector=(-0.791726, 0.60681, -0.0703664),
    cameraTarget=(-99219.7, -35328.2, -59020.2), viewOffsetX=-60901.4,
    viewOffsetY=31645)
session.viewports['Viewport: 1'].view.setValues(nearPlane=328111,
    farPlane=497710, width=5444.52, height=2159.56, viewOffsetX=-56687.6,
    viewOffsetY=22510.8)
session.viewports['Viewport: 1'].view.setValues(nearPlane=323279,
    farPlane=498788, width=5364.35, height=2127.76, cameraPosition=(237116,
    105940, -215006), cameraUpVector=(-0.743014, 0.655872, -0.133274),
    cameraTarget=(-102068, -41031.7, -54882), viewOffsetX=-55852.9,
    viewOffsetY=22179.3)
session.viewports['Viewport: 1'].view.setValues(nearPlane=320994,
    farPlane=501074, width=32947.6, height=13068.6, viewOffsetX=-53328.9,
    viewOffsetY=19465.6)
session.viewports['Viewport: 1'].view.setValues(nearPlane=312982,
    farPlane=499920, width=32125.3, height=12742.4, cameraPosition=(244549,
    -26259.5, -223585), cameraUpVector=(-0.529381, 0.816964, -0.228747),
    cameraTarget=(-117343, -47186.3, -47850.9), viewOffsetX=-51997.9,
    viewOffsetY=18979.8)
session.viewports['Viewport: 1'].view.setValues(nearPlane=314612,
    farPlane=501219, width=32292.6, height=12808.8, cameraPosition=(247325,
    29312.1, -220255), cameraUpVector=(-0.613161, 0.771433, -0.170073),
    cameraTarget=(-111254, -44574.8, -52183.3), viewOffsetX=-52268.6,
    viewOffsetY=19078.6)
session.viewports['Viewport: 1'].view.setValues(nearPlane=316207,
    farPlane=499624, width=14420.8, height=5719.97, viewOffsetX=-48660.2,
    viewOffsetY=10383.8)
session.viewports['Viewport: 1'].view.setValues(nearPlane=317188,
    farPlane=497533, width=14465.5, height=5737.71, cameraPosition=(244645,
    86143.2, -207442), cameraUpVector=(-0.692119, 0.711882, -0.119144),
    cameraTarget=(-106164, -40863, -55490.6), viewOffsetX=-48811.1,
    viewOffsetY=10416)
session.viewports['Viewport: 1'].view.setValues(nearPlane=316449,
    farPlane=498272, width=23842.4, height=9457.04, viewOffsetX=-50772.8,
    viewOffsetY=16067.9)
session.viewports['Viewport: 1'].view.setValues(nearPlane=315996,
    farPlane=494176, width=23808.3, height=9443.52, cameraPosition=(255662,
    129696, -160732), cameraUpVector=(-0.737234, 0.658293, -0.152103),
    cameraTarget=(-96445.5, -36917.6, -58032.8), viewOffsetX=-50700.2,
    viewOffsetY=16045)
session.viewports['Viewport: 1'].view.setValues(nearPlane=316311,
    farPlane=493862, width=19432, height=7707.66, viewOffsetX=-54926,
    viewOffsetY=17728.3)
session.viewports['Viewport: 1'].view.setValues(nearPlane=316381,
    farPlane=493791, width=19436.3, height=7709.38, cameraPosition=(256509,
    128484, -159794), cameraUpVector=(-0.739595, 0.650467, -0.172894),
    cameraTarget=(-95598.2, -38129.8, -57094.6), viewOffsetX=-54938.2,
    viewOffsetY=17732.2)
session.viewports['Viewport: 1'].view.setValues(nearPlane=319695,
    farPlane=490188, width=19639.9, height=7790.12, cameraPosition=(252605,
    167371, -131752), cameraUpVector=(-0.782399, 0.597384, -0.176023),
    cameraTarget=(-88859.6, -33660.4, -59120.3), viewOffsetX=-55513.6,
    viewOffsetY=17917.9)
session.viewports['Viewport: 1'].view.setValues(nearPlane=319240,
    farPlane=490643, width=25672.4, height=10182.9, viewOffsetX=-64605.9,
    viewOffsetY=17865.1)
leaf = dgm.Leaf(leafType=DEFAULT_MODEL)
session.viewports['Viewport: 1'].assemblyDisplay.displayGroup.replace(
    leaf=leaf)
session.viewports['Viewport: 1'].view.setValues(nearPlane=319127,
    farPlane=490847, width=27012.8, height=10714.6, viewOffsetX=-65334.1,
    viewOffsetY=17347.6)
session.viewports['Viewport: 1'].view.setValues(nearPlane=320880,
    farPlane=486201, width=27161.2, height=10773.4, cameraPosition=(261604,
    190094, -70565.7), cameraUpVector=(-0.771152, 0.625689, -0.117638),
    cameraTarget=(-82848.1, -18727.9, -64755.6), viewOffsetX=-65693,
    viewOffsetY=17442.8)
session.viewports['Viewport: 1'].view.setValues(nearPlane=322183,
    farPlane=484898, width=12578.2, height=4989.12, viewOffsetX=-75160.8,
    viewOffsetY=19143)
a = mdb.models['Model-1'].rootAssembly
i1 = a.instances['P-2-1']
leaf = dgm.LeafFromInstance((i1, ))
session.viewports['Viewport: 1'].assemblyDisplay.displayGroup.remove(leaf=leaf)
leaf = dgm.Leaf(leafType=DEFAULT_MODEL)
session.viewports['Viewport: 1'].assemblyDisplay.displayGroup.replace(
    leaf=leaf)
a = mdb.models['Model-1'].rootAssembly
i1 = a.instances['P-1-1']
leaf = dgm.LeafFromInstance((i1, ))
session.viewports['Viewport: 1'].assemblyDisplay.displayGroup.remove(leaf=leaf)
session.viewports['Viewport: 1'].view.setValues(nearPlane=321836,
    farPlane=485197, width=16720.6, height=6632.2, viewOffsetX=-74389.2,
    viewOffsetY=19356.1)
session.viewports['Viewport: 1'].view.setValues(nearPlane=322329,
    farPlane=486991, width=16746.2, height=6642.34, cameraPosition=(238423,
    198014, -125272), cameraUpVector=(-0.809989, 0.58304, -0.0631051),
    cameraTarget=(-92028.8, -24129.1, -64101.1), viewOffsetX=-74503,
    viewOffsetY=19385.7)
session.viewports['Viewport: 1'].view.setValues(nearPlane=321822,
    farPlane=487498, width=23461, height=9305.78, viewOffsetX=-69077.5,
    viewOffsetY=22482)
session.viewports['Viewport: 1'].view.setValues(nearPlane=316738,
    farPlane=489420, width=23090.4, height=9158.76, cameraPosition=(180139,
    91661.1, -273490), cameraUpVector=(-0.681262, 0.72738, 0.0824687),
    cameraTarget=(-129842, -39171.8, -51945.1), viewOffsetX=-67986.2,
    viewOffsetY=22126.8)
session.viewports['Viewport: 1'].view.setValues(nearPlane=314118,
    farPlane=492040, width=55690.4, height=22089.5, viewOffsetX=-45345.7,
    viewOffsetY=18213.3)
session.viewports['Viewport: 1'].view.setValues(nearPlane=348429,
    farPlane=488757, width=61773.6, height=24502.4, cameraPosition=(47957.4,
    24879.4, -379646), cameraUpVector=(-0.596065, 0.774951, 0.210137),
    cameraTarget=(-146613, -45239.5, -33938.8), viewOffsetX=-50299,
    viewOffsetY=20202.8)
session.viewports['Viewport: 1'].view.setValues(nearPlane=347615,
    farPlane=489572, width=67690.7, height=26849.4, viewOffsetX=-31273.9,
    viewOffsetY=21513.6)
session.viewports['Viewport: 1'].view.setValues(nearPlane=404195,
    farPlane=480648, width=78708.4, height=31219.5, cameraPosition=(-122643,
    -17781.3, -424118), cameraUpVector=(-0.51874, 0.778275, 0.353832),
    cameraTarget=(-155346, -49030.4, -23815.7), viewOffsetX=-36364.2,
    viewOffsetY=25015.3)
session.viewports['Viewport: 1'].view.setValues(nearPlane=407483,
    farPlane=477360, width=32604.7, height=12932.6, viewOffsetX=-17061.1,
    viewOffsetY=28448.6)
session.viewports['Viewport: 1'].view.setValues(nearPlane=367986,
    farPlane=479634, width=29444.4, height=11679.1, cameraPosition=(-17506.9,
    50645.7, -397132), cameraUpVector=(-0.549139, 0.754437, 0.359544),
    cameraTarget=(-146975, -41963.2, -27064.6), viewOffsetX=-15407.4,
    viewOffsetY=25691.1)
session.viewports['Viewport: 1'].view.setValues(nearPlane=367676,
    farPlane=479944, width=37650.1, height=14933.8, viewOffsetX=-16806.6,
    viewOffsetY=26178.7)
session.viewports['Viewport: 1'].view.setValues(nearPlane=346779,
    farPlane=479067, width=35510.1, height=14085, cameraPosition=(39507.2,
    106097, -359449), cameraUpVector=(-0.631196, 0.686734, 0.360537),
    cameraTarget=(-141303, -37794.1, -29462.4), viewOffsetX=-15851.3,
    viewOffsetY=24690.8)
session.viewports['Viewport: 1'].view.setValues(nearPlane=347888,
    farPlane=477957, width=25967.9, height=10300.1, viewOffsetX=-24746.7,
    viewOffsetY=26642.4)
session.viewports['Viewport: 1'].view.setValues(nearPlane=327931,
    farPlane=476613, width=24478.2, height=9709.24, cameraPosition=(101047,
    152505, -301280), cameraUpVector=(-0.707374, 0.631657, 0.317224),
    cameraTarget=(-135026, -33866.4, -33281.1), viewOffsetX=-23327,
    viewOffsetY=25114)
session.viewports['Viewport: 1'].view.setValues(nearPlane=330003,
    farPlane=474542, width=2134.51, height=846.65, viewOffsetX=-37647,
    viewOffsetY=25153.7)
a = mdb.models['Model-1'].rootAssembly
s1 = a.instances['P-21-1'].faces
side1Faces1 = s1.getSequenceFromMask(mask=('[#1 ]', ), )
region1=regionToolset.Region(side1Faces=side1Faces1)
a = mdb.models['Model-1'].rootAssembly
s1 = a.instances['P-20-1'].edges
side1Edges1 = s1.getSequenceFromMask(mask=('[#80 ]', ), )
region2=regionToolset.Region(side1Edges=side1Edges1)
mdb.models['Model-1'].Tie(name='Constraint-7', main=region1, secondary=region2,
    positionToleranceMethod=COMPUTED, adjust=ON, tieRotations=ON, thickness=ON)
session.viewports['Viewport: 1'].view.setValues(nearPlane=327424,
    farPlane=477121, width=33094.7, height=13126.9, viewOffsetX=-28651.7,
    viewOffsetY=27267.9)
leaf = dgm.Leaf(leafType=DEFAULT_MODEL)
session.viewports['Viewport: 1'].assemblyDisplay.displayGroup.replace(
    leaf=leaf)
session.viewports['Viewport: 1'].view.setValues(nearPlane=327932,
    farPlane=476829, width=27026.4, height=10720, viewOffsetX=-30763.8,
    viewOffsetY=26487.4)
i1 = mdb.models['Model-1'].rootAssembly.allInstances['P-1-1']
leaf = dgm.LeafFromInstance(instances=(i1, ))
session.viewports['Viewport: 1'].assemblyDisplay.displayGroup.remove(leaf=leaf)
session.viewports['Viewport: 1'].view.setValues(nearPlane=329623,
    farPlane=474922, width=6314.17, height=2504.51, viewOffsetX=-30599.4,
    viewOffsetY=28322)
a = mdb.models['Model-1'].rootAssembly
s1 = a.instances['P-1-1'].faces
side1Faces1 = s1.getSequenceFromMask(mask=('[#3 ]', ), )
region1=regionToolset.Region(side1Faces=side1Faces1)
a = mdb.models['Model-1'].rootAssembly
s1 = a.instances['P-10-1'].edges
side1Edges1 = s1.getSequenceFromMask(mask=('[#24491421 #90a2288a ]', ), )
s2 = a.instances['P-51-1'].edges
side1Edges2 = s2.getSequenceFromMask(mask=('[#41 ]', ), )
region2=regionToolset.Region(side1Edges=side1Edges1+side1Edges2)
mdb.models['Model-1'].Tie(name='Constraint-8', main=region1, secondary=region2,
    positionToleranceMethod=COMPUTED, adjust=ON, tieRotations=ON, thickness=ON)
session.viewports['Viewport: 1'].view.setValues(nearPlane=329416,
    farPlane=475129, width=9321.5, height=3697.36, viewOffsetX=-29639.1,
    viewOffsetY=28312.1)
a = mdb.models['Model-1'].rootAssembly
s1 = a.instances['P-2-1'].faces
side1Faces1 = s1.getSequenceFromMask(mask=('[#4000 ]', ), )
region1=regionToolset.Region(side1Faces=side1Faces1)
a = mdb.models['Model-1'].rootAssembly
s1 = a.instances['P-10-1'].edges
side1Edges1 = s1.getSequenceFromMask(mask=('[#40100040 #1000000 ]', ), )
region2=regionToolset.Region(side1Edges=side1Edges1)
mdb.models['Model-1'].Tie(name='Constraint-9', main=region1, secondary=region2,
    positionToleranceMethod=COMPUTED, adjust=ON, tieRotations=ON, thickness=ON)
session.viewports['Viewport: 1'].view.setValues(nearPlane=328958,
    farPlane=475587, width=14789, height=5866.02, viewOffsetX=-35224.6,
    viewOffsetY=26623.7)
a = mdb.models['Model-1'].rootAssembly
s1 = a.instances['P-2-1'].faces
side1Faces1 = s1.getSequenceFromMask(mask=('[#8000 ]', ), )
region1=regionToolset.Region(side1Faces=side1Faces1)
a = mdb.models['Model-1'].rootAssembly
s1 = a.instances['P-10-1'].edges
side1Edges1 = s1.getSequenceFromMask(mask=('[#0 #40100 ]', ), )
region2=regionToolset.Region(side1Edges=side1Edges1)
mdb.models['Model-1'].Tie(name='Constraint-10', main=region1,
    secondary=region2, positionToleranceMethod=COMPUTED, adjust=ON,
    tieRotations=ON, thickness=ON)
session.viewports['Viewport: 1'].view.setValues(nearPlane=328250,
    farPlane=476295, width=23242.7, height=9219.17, viewOffsetX=-32907.6,
    viewOffsetY=26370.8)
session.viewports['Viewport: 1'].view.setValues(nearPlane=324083,
    farPlane=477299, width=22947.6, height=9102.14, cameraPosition=(108957,
    110276, -312614), cameraUpVector=(-0.654275, 0.70719, 0.267967),
    cameraTarget=(-138299, -35669.6, -30031.9), viewOffsetX=-32489.9,
    viewOffsetY=26036)
session.viewports['Viewport: 1'].view.setValues(nearPlane=324533,
    farPlane=476849, width=18834.8, height=7470.79, viewOffsetX=-33171.9,
    viewOffsetY=21971.1)
session.viewports['Viewport: 1'].view.setValues(nearPlane=322324,
    farPlane=477414, width=18706.6, height=7419.95, cameraPosition=(113701,
    66652.3, -321068), cameraUpVector=(-0.619841, 0.761072, 0.191225),
    cameraTarget=(-140072, -37696.2, -26112), viewOffsetX=-32946.2,
    viewOffsetY=21821.6)
session.viewports['Viewport: 1'].view.setValues(nearPlane=322681,
    farPlane=477057, width=15349.7, height=6088.41, viewOffsetX=-30329.8,
    viewOffsetY=17316.5)
session.viewports['Viewport: 1'].view.setValues(nearPlane=326189,
    farPlane=477104, width=15516.5, height=6154.6, cameraPosition=(103521,
    36752.6, -333554), cameraUpVector=(-0.626876, 0.768176, 0.130123),
    cameraTarget=(-140125, -40030.9, -22058.6), viewOffsetX=-30659.5,
    viewOffsetY=17504.8)
session.viewports['Viewport: 1'].view.setValues(nearPlane=326076,
    farPlane=477217, width=17335.7, height=6876.17, viewOffsetX=-25900.7,
    viewOffsetY=14596.9)
session.viewports['Viewport: 1'].view.setValues(nearPlane=317238,
    farPlane=475995, width=16865.8, height=6689.78, cameraPosition=(129223,
    85362.8, -302475), cameraUpVector=(-0.676144, 0.719796, 0.157237),
    cameraTarget=(-136984, -38402.9, -26604.3), viewOffsetX=-25198.7,
    viewOffsetY=14201.3)
session.viewports['Viewport: 1'].view.setValues(nearPlane=316747,
    farPlane=476487, width=23922, height=9488.63, viewOffsetX=-29405.3,
    viewOffsetY=18284.5)
a = mdb.models['Model-1'].rootAssembly
s1 = a.instances['P-2-1'].faces
side2Faces1 = s1.getSequenceFromMask(mask=('[#4 ]', ), )
region1=regionToolset.Region(side2Faces=side2Faces1)
a = mdb.models['Model-1'].rootAssembly
s1 = a.instances['P-10-1'].edges
side1Edges1 = s1.getSequenceFromMask(mask=('[#2000000 #10040 ]', ), )
region2=regionToolset.Region(side1Edges=side1Edges1)
mdb.models['Model-1'].Tie(name='Constraint-11', main=region1,
    secondary=region2, positionToleranceMethod=COMPUTED, adjust=ON,
    tieRotations=ON, thickness=ON)
session.viewports['Viewport: 1'].view.setValues(nearPlane=317927,
    farPlane=475307, width=9832.08, height=3899.88, viewOffsetX=-34950.7,
    viewOffsetY=16185.8)
leaf = dgm.Leaf(leafType=DEFAULT_MODEL)
session.viewports['Viewport: 1'].assemblyDisplay.displayGroup.replace(
    leaf=leaf)
session.viewports['Viewport: 1'].view.setValues(nearPlane=315720,
    farPlane=477723, width=36178.5, height=14350.1, viewOffsetX=-30958.4,
    viewOffsetY=18369.9)
session.viewports['Viewport: 1'].view.setValues(nearPlane=315815,
    farPlane=474795, width=36189.4, height=14354.5, cameraPosition=(128482,
    158827, -270959), cameraUpVector=(-0.715162, 0.636324, 0.289199),
    cameraTarget=(-134714, -33515.5, -34270.6), viewOffsetX=-30967.7,
    viewOffsetY=18375.5)
session.viewports['Viewport: 1'].view.setValues(nearPlane=317019,
    farPlane=473591, width=23306.8, height=9244.62, viewOffsetX=-37987.9,
    viewOffsetY=24661.5)
session.viewports['Viewport: 1'].view.setValues(nearPlane=318960,
    farPlane=471862, width=23449.5, height=9301.21, cameraPosition=(127149,
    198543, -246196), cameraUpVector=(-0.748118, 0.569985, 0.339759),
    cameraTarget=(-132144, -29725.5, -38953.6), viewOffsetX=-38220.5,
    viewOffsetY=24812.5)
session.viewports['Viewport: 1'].view.setValues(nearPlane=319320,
    farPlane=471501, width=19973.9, height=7922.63, viewOffsetX=-39303.2,
    viewOffsetY=28154.8)
session.viewports['Viewport: 1'].view.setValues(nearPlane=323055,
    farPlane=468751, width=20207.6, height=8015.32, cameraPosition=(123243,
    241172, -212221), cameraUpVector=(-0.791622, 0.481777, 0.375799),
    cameraTarget=(-128275, -24695.7, -43870.3), viewOffsetX=-39763,
    viewOffsetY=28484.2)
session.viewports['Viewport: 1'].view.setValues(nearPlane=324175,
    farPlane=467632, width=6854.21, height=2718.71, viewOffsetX=-36441.1,
    viewOffsetY=38230.6)
session.viewports['Viewport: 1'].view.setValues(nearPlane=323896,
    farPlane=467911, width=10767.4, height=4270.86, viewOffsetX=-36700.4,
    viewOffsetY=37685)
a = mdb.models['Model-1'].rootAssembly
i1 = a.instances['P-1-1']
leaf = dgm.LeafFromInstance((i1, ))
session.viewports['Viewport: 1'].assemblyDisplay.displayGroup.remove(leaf=leaf)
session.viewports['Viewport: 1'].view.setValues(nearPlane=323449,
    farPlane=468189, width=16103.8, height=6387.53, viewOffsetX=-44290.1,
    viewOffsetY=33580.5)
leaf = dgm.Leaf(leafType=DEFAULT_MODEL)
session.viewports['Viewport: 1'].assemblyDisplay.displayGroup.replace(
    leaf=leaf)
a = mdb.models['Model-1'].rootAssembly
s1 = a.instances['P-16-1'].edges
side1Edges1 = s1.getSequenceFromMask(mask=('[#820820 ]', ), )
s2 = a.instances['P-51-1'].edges
side1Edges2 = s2.getSequenceFromMask(mask=('[#41 ]', ), )
s3 = a.instances['P-34-1'].edges
side1Edges3 = s3.getSequenceFromMask(mask=('[#81 ]', ), )
s4 = a.instances['P-22-1'].edges
side1Edges4 = s4.getSequenceFromMask(mask=('[#1020 ]', ), )
region1=regionToolset.Region(side1Edges=side1Edges1+side1Edges2+side1Edges3+\
    side1Edges4)
a = mdb.models['Model-1'].rootAssembly
s1 = a.instances['P-1-1'].faces
side2Faces1 = s1.getSequenceFromMask(mask=('[#2 ]', ), )
region2=regionToolset.Region(side2Faces=side2Faces1)
mdb.models['Model-1'].Tie(name='Constraint-12', main=region1,
    secondary=region2, positionToleranceMethod=COMPUTED, adjust=ON,
    tieRotations=ON, thickness=ON)
session.viewports['Viewport: 1'].view.setValues(nearPlane=323742,
    farPlane=468065, width=11627.6, height=4612.06, viewOffsetX=-45439.8,
    viewOffsetY=33244.9)
a = mdb.models['Model-1'].rootAssembly
i1 = a.instances['P-1-1']
leaf = dgm.LeafFromInstance((i1, ))
session.viewports['Viewport: 1'].assemblyDisplay.displayGroup.remove(leaf=leaf)
session.viewports['Viewport: 1'].view.setValues(nearPlane=323930,
    farPlane=467709, width=10365.2, height=4111.33, viewOffsetX=-46275.2,
    viewOffsetY=33014.7)
session.viewports['Viewport: 1'].view.setValues(nearPlane=326085,
    farPlane=468075, width=10434.1, height=4138.68, cameraPosition=(110544,
    226037, -238796), cameraUpVector=(-0.789417, 0.496304, 0.361252),
    cameraTarget=(-129228, -29467.5, -40009.9), viewOffsetX=-46583.1,
    viewOffsetY=33234.4)
session.viewports['Viewport: 1'].view.setValues(nearPlane=326359,
    farPlane=467802, width=7533.41, height=2988.11, viewOffsetX=-44028.8,
    viewOffsetY=32458.8)
leaf = dgm.Leaf(leafType=DEFAULT_MODEL)
session.viewports['Viewport: 1'].assemblyDisplay.displayGroup.replace(
    leaf=leaf)
a = mdb.models['Model-1'].rootAssembly
f1 = a.instances['P-1-1'].faces
faces1 = f1.getSequenceFromMask(mask=('[#2 ]', ), )
leaf = dgm.LeafFromGeometry(faceSeq=faces1)
session.viewports['Viewport: 1'].assemblyDisplay.displayGroup.remove(leaf=leaf)
session.viewports['Viewport: 1'].view.setValues(nearPlane=325661,
    farPlane=468572, width=15865.9, height=6293.19, viewOffsetX=-36115.1,
    viewOffsetY=36832.2)
a = mdb.models['Model-1'].rootAssembly
s1 = a.instances['P-1-1'].faces
side2Faces1 = s1.getSequenceFromMask(mask=('[#2 ]', ), )
region1=regionToolset.Region(side2Faces=side2Faces1)
a = mdb.models['Model-1'].rootAssembly
s1 = a.instances['P-21-1'].edges
side1Edges1 = s1.getSequenceFromMask(mask=('[#111 ]', ), )
s2 = a.instances['P-15-1'].edges
side1Edges2 = s2.getSequenceFromMask(mask=('[#111 ]', ), )
region2=regionToolset.Region(side1Edges=side1Edges1+side1Edges2)
mdb.models['Model-1'].Tie(name='Constraint-13', main=region1,
    secondary=region2, positionToleranceMethod=COMPUTED, adjust=ON,
    tieRotations=ON, thickness=ON)
session.viewports['Viewport: 1'].view.setValues(nearPlane=326100,
    farPlane=468132, width=10615.5, height=4210.61, viewOffsetX=-42399.7,
    viewOffsetY=33596.5)
leaf = dgm.Leaf(leafType=DEFAULT_MODEL)
session.viewports['Viewport: 1'].assemblyDisplay.displayGroup.replace(
    leaf=leaf)
a = mdb.models['Model-1'].rootAssembly
s1 = a.instances['P-23-1'].edges
side1Edges1 = s1.getSequenceFromMask(mask=('[#4 ]', ), )
s2 = a.instances['P-17-1'].edges
side1Edges2 = s2.getSequenceFromMask(mask=('[#2002 ]', ), )
region1=regionToolset.Region(side1Edges=side1Edges1+side1Edges2)
a = mdb.models['Model-1'].rootAssembly
s1 = a.instances['P-1-1'].faces
side2Faces1 = s1.getSequenceFromMask(mask=('[#2 ]', ), )
region2=regionToolset.Region(side2Faces=side2Faces1)
mdb.models['Model-1'].Tie(name='Constraint-14', main=region1,
    secondary=region2, positionToleranceMethod=COMPUTED, adjust=ON,
    tieRotations=ON, thickness=ON)
session.viewports['Viewport: 1'].view.setValues(nearPlane=325418,
    farPlane=468929, width=18760, height=7441.13, viewOffsetX=-42870.2,
    viewOffsetY=33346.8)
session.viewports['Viewport: 1'].view.setValues(nearPlane=325541,
    farPlane=468805, width=15939.8, height=6322.49, viewOffsetX=-43435.5,
    viewOffsetY=33020.3)
a = mdb.models['Model-1'].rootAssembly
f1 = a.instances['P-1-1'].faces
faces1 = f1.getSequenceFromMask(mask=('[#2 ]', ), )
leaf = dgm.LeafFromGeometry(faceSeq=faces1)
session.viewports['Viewport: 1'].assemblyDisplay.displayGroup.remove(leaf=leaf)
session.viewports['Viewport: 1'].view.setValues(width=15304.9, height=6070.67,
    viewOffsetX=-43454.2, viewOffsetY=32918.9)
a = mdb.models['Model-1'].rootAssembly
f1 = a.instances['P-1-1'].faces
faces1 = f1.getSequenceFromMask(mask=('[#1 ]', ), )
leaf = dgm.LeafFromGeometry(faceSeq=faces1)
session.viewports['Viewport: 1'].assemblyDisplay.displayGroup.remove(leaf=leaf)
session.viewports['Viewport: 1'].view.setValues(nearPlane=326263,
    farPlane=467897, width=7994.87, height=3171.15, viewOffsetX=-45311.5,
    viewOffsetY=32112.8)
leaf = dgm.Leaf(leafType=DEFAULT_MODEL)
session.viewports['Viewport: 1'].assemblyDisplay.displayGroup.replace(
    leaf=leaf)
a = mdb.models['Model-1'].rootAssembly
f1 = a.instances['P-26-1'].faces
faces1 = f1.getSequenceFromMask(mask=('[#ffffffff ]', ), )
leaf = dgm.LeafFromGeometry(faceSeq=faces1)
session.viewports['Viewport: 1'].assemblyDisplay.displayGroup.remove(leaf=leaf)
session.viewports['Viewport: 1'].view.setValues(nearPlane=326099,
    farPlane=468248, width=10633.9, height=4217.93, viewOffsetX=-45045.1,
    viewOffsetY=32155.4)
a = mdb.models['Model-1'].rootAssembly
f1 = a.instances['P-1-1'].faces
faces1 = f1.getSequenceFromMask(mask=('[#2 ]', ), )
leaf = dgm.LeafFromGeometry(faceSeq=faces1)
session.viewports['Viewport: 1'].assemblyDisplay.displayGroup.remove(leaf=leaf)
a = mdb.models['Model-1'].rootAssembly
f1 = a.instances['P-1-1'].faces
faces1 = f1.getSequenceFromMask(mask=('[#1 ]', ), )
leaf = dgm.LeafFromGeometry(faceSeq=faces1)
session.viewports['Viewport: 1'].assemblyDisplay.displayGroup.remove(leaf=leaf)
session.viewports['Viewport: 1'].view.setValues(nearPlane=326292,
    farPlane=467868, width=7675.76, height=3044.58, viewOffsetX=-45834.8,
    viewOffsetY=31847)
leaf = dgm.Leaf(leafType=DEFAULT_MODEL)
session.viewports['Viewport: 1'].assemblyDisplay.displayGroup.replace(
    leaf=leaf)
a = mdb.models['Model-1'].rootAssembly
f1 = a.instances['P-1-1'].faces
faces1 = f1.getSequenceFromMask(mask=('[#2 ]', ), )
leaf = dgm.LeafFromGeometry(faceSeq=faces1)
session.viewports['Viewport: 1'].assemblyDisplay.displayGroup.remove(leaf=leaf)
session.viewports['Viewport: 1'].view.setValues(width=7369.36, height=2923.04,
    viewOffsetX=-45801.7, viewOffsetY=31822.9)
a = mdb.models['Model-1'].rootAssembly
f1 = a.instances['P-1-1'].faces
faces1 = f1.getSequenceFromMask(mask=('[#1 ]', ), )
leaf = dgm.LeafFromGeometry(faceSeq=faces1)
session.viewports['Viewport: 1'].assemblyDisplay.displayGroup.remove(leaf=leaf)
session.viewports['Viewport: 1'].view.setValues(nearPlane=326465,
    farPlane=467695, width=5770.99, height=2289.05, viewOffsetX=-46301.8,
    viewOffsetY=31792.7)
i1 = mdb.models['Model-1'].rootAssembly.allInstances['P-25-1']
i2 = mdb.models['Model-1'].rootAssembly.allInstances['P-26-1']
leaf = dgm.LeafFromInstance(instances=(i1, i2, ))
session.viewports['Viewport: 1'].assemblyDisplay.displayGroup.replace(
    leaf=leaf)
i1 = mdb.models['Model-1'].rootAssembly.allInstances['P-24-1']
i2 = mdb.models['Model-1'].rootAssembly.allInstances['P-25-1']
leaf = dgm.LeafFromInstance(instances=(i1, i2, ))
session.viewports['Viewport: 1'].assemblyDisplay.displayGroup.replace(
    leaf=leaf)
a = mdb.models['Model-1'].rootAssembly
s1 = a.instances['P-26-1'].faces
side1Faces1 = s1.getSequenceFromMask(mask=('[#ffffffff ]', ), )
region1=regionToolset.Region(side1Faces=side1Faces1)
a = mdb.models['Model-1'].rootAssembly
s1 = a.instances['P-25-1'].edges
side1Edges1 = s1.getSequenceFromMask(mask=('[#44 ]', ), )
s2 = a.instances['P-24-1'].edges
side1Edges2 = s2.getSequenceFromMask(mask=('[#11 ]', ), )
region2=regionToolset.Region(side1Edges=side1Edges1+side1Edges2)
mdb.models['Model-1'].Tie(name='Constraint-15', main=region1,
    secondary=region2, positionToleranceMethod=COMPUTED, adjust=ON,
    tieRotations=ON, thickness=ON)
leaf = dgm.Leaf(leafType=DEFAULT_MODEL)
session.viewports['Viewport: 1'].assemblyDisplay.displayGroup.replace(
    leaf=leaf)
session.viewports['Viewport: 1'].view.setValues(nearPlane=325703,
    farPlane=468644, width=15363.2, height=6093.77, viewOffsetX=-43114.7,
    viewOffsetY=31213.3)
session.viewports['Viewport: 1'].view.setValues(nearPlane=332179,
    farPlane=456859, width=15668.7, height=6214.94, cameraPosition=(121544,
    317561, -84935.5), cameraUpVector=(-0.887051, 0.275026, 0.370811),
    cameraTarget=(-116599, -5760.01, -52679.9), viewOffsetX=-43972,
    viewOffsetY=31833.9)
session.viewports['Viewport: 1'].view.setValues(nearPlane=331001,
    farPlane=458037, width=30054.3, height=11921, viewOffsetX=-40722.2,
    viewOffsetY=32668.9)
session.viewports['Viewport: 1'].view.setValues(session.views['Iso'])
session.viewports['Viewport: 1'].view.setValues(nearPlane=311132,
    farPlane=494565, width=256099, height=101581, viewOffsetX=7101.07,
    viewOffsetY=-139.177)
session.viewports['Viewport: 1'].view.setValues(nearPlane=310298,
    farPlane=495399, width=255412, height=101309, cameraPosition=(151593,
    218898, 255229), cameraUpVector=(-0.517756, 0.574418, -0.634013),
    cameraTarget=(-80991.9, -13687, 22644.3), viewOffsetX=7082.02,
    viewOffsetY=-138.804)
session.viewports['Viewport: 1'].view.setValues(nearPlane=301079,
    farPlane=515467, width=247824, height=98299.1, cameraPosition=(243734,
    159485, 192847), cameraUpVector=(-0.41953, 0.643896, -0.639838),
    cameraTarget=(-79440, -11054.8, 23253.3), viewOffsetX=6871.61,
    viewOffsetY=-134.68)
session.viewports['Viewport: 1'].view.setValues(nearPlane=322035,
    farPlane=494511, width=14609.1, height=5794.69, viewOffsetX=-38007.6,
    viewOffsetY=-2525.7)
session.viewports['Viewport: 1'].view.setValues(nearPlane=323653,
    farPlane=495800, width=14682.5, height=5823.8, cameraPosition=(240335,
    150392, 210921), cameraUpVector=(-0.392876, 0.67388, -0.625727),
    cameraTarget=(-78399.8, -9890.04, 23824.2), viewOffsetX=-38198.6,
    viewOffsetY=-2538.39)
session.viewports['Viewport: 1'].view.setValues(nearPlane=324074,
    farPlane=495380, width=10199.1, height=4045.45, viewOffsetX=-40466.2,
    viewOffsetY=-3760.4)
session.viewports['Viewport: 1'].view.setValues(session.views['Iso'])
session.viewports['Viewport: 1'].view.setValues(nearPlane=311132,
    farPlane=494565, width=256099, height=101581, viewOffsetX=-2454.97,
    viewOffsetY=4845.39)
session.viewports['Viewport: 1'].view.setValues(nearPlane=291897,
    farPlane=520515, width=240266, height=95301, cameraPosition=(295438,
    5641.91, -107669), cameraUpVector=(-0.525184, 0.76537, -0.372009),
    cameraTarget=(-84880.2, -16191.8, 23358.4), viewOffsetX=-2303.19,
    viewOffsetY=4545.83)
session.viewports['Viewport: 1'].view.setValues(nearPlane=312783,
    farPlane=499629, width=16038, height=6361.43, viewOffsetX=-1393.16,
    viewOffsetY=2324.09)
i1 = mdb.models['Model-1'].rootAssembly.allInstances['P-1-1']
leaf = dgm.LeafFromInstance(instances=(i1, ))
session.viewports['Viewport: 1'].assemblyDisplay.displayGroup.remove(leaf=leaf)
session.viewports['Viewport: 1'].view.setValues(nearPlane=313447,
    farPlane=498873, width=8727.58, height=3461.78, viewOffsetX=-2043.3,
    viewOffsetY=2813.36)
a = mdb.models['Model-1'].rootAssembly
s1 = a.instances['P-1-1'].faces
side1Faces1 = s1.getSequenceFromMask(mask=('[#3 ]', ), )
region1=regionToolset.Region(side1Faces=side1Faces1)
a = mdb.models['Model-1'].rootAssembly
s1 = a.instances['P-25-1'].edges
side1Edges1 = s1.getSequenceFromMask(mask=('[#11 ]', ), )
s2 = a.instances['P-24-1'].edges
side1Edges2 = s2.getSequenceFromMask(mask=('[#44 ]', ), )
region2=regionToolset.Region(side1Edges=side1Edges1+side1Edges2)
mdb.models['Model-1'].Tie(name='Constraint-16', main=region1,
    secondary=region2, positionToleranceMethod=COMPUTED, adjust=ON,
    tieRotations=ON, thickness=ON)
session.viewports['Viewport: 1'].view.setValues(nearPlane=312948,
    farPlane=499373, width=15431.4, height=6120.82, viewOffsetX=302.775,
    viewOffsetY=3144.04)
session.viewports['Viewport: 1'].view.setValues(width=14811.6, height=5874.98,
    viewOffsetX=596.17, viewOffsetY=3100.51)
i1 = mdb.models['Model-1'].rootAssembly.allInstances['P-24-1']
i2 = mdb.models['Model-1'].rootAssembly.allInstances['P-25-1']
i3 = mdb.models['Model-1'].rootAssembly.allInstances['P-26-1']
leaf = dgm.LeafFromInstance(instances=(i1, i2, i3, ))
session.viewports['Viewport: 1'].assemblyDisplay.displayGroup.replace(
    leaf=leaf)
session.viewports['Viewport: 1'].view.setValues(nearPlane=469015,
    farPlane=476572, width=18857.1, height=7479.65, viewOffsetX=500.285,
    viewOffsetY=4763.91)
i1 = mdb.models['Model-1'].rootAssembly.allInstances['P-27-1']
leaf = dgm.LeafFromInstance(instances=(i1, ))
session.viewports['Viewport: 1'].assemblyDisplay.displayGroup.add(leaf=leaf)
i1 = mdb.models['Model-1'].rootAssembly.allInstances['P-28-1']
leaf = dgm.LeafFromInstance(instances=(i1, ))
session.viewports['Viewport: 1'].assemblyDisplay.displayGroup.add(leaf=leaf)
session.viewports['Viewport: 1'].view.setValues(nearPlane=470084,
    farPlane=475503, width=7095.35, height=2814.36, viewOffsetX=-2800.93,
    viewOffsetY=4958.97)
i1 = mdb.models['Model-1'].rootAssembly.allInstances['P-29-1']
leaf = dgm.LeafFromInstance(instances=(i1, ))
session.viewports['Viewport: 1'].assemblyDisplay.displayGroup.add(leaf=leaf)
session.viewports['Viewport: 1'].view.setValues(nearPlane=470333,
    farPlane=475254, width=4349.7, height=1725.3, viewOffsetX=-3764.4,
    viewOffsetY=4926.92)
i1 = mdb.models['Model-1'].rootAssembly.allInstances['P-26-1']
i2 = mdb.models['Model-1'].rootAssembly.allInstances['P-27-1']
i3 = mdb.models['Model-1'].rootAssembly.allInstances['P-28-1']
leaf = dgm.LeafFromInstance(instances=(i1, i2, i3, ))
session.viewports['Viewport: 1'].assemblyDisplay.displayGroup.replace(
    leaf=leaf)
i1 = mdb.models['Model-1'].rootAssembly.allInstances['P-27-1']
i2 = mdb.models['Model-1'].rootAssembly.allInstances['P-28-1']
i3 = mdb.models['Model-1'].rootAssembly.allInstances['P-29-1']
leaf = dgm.LeafFromInstance(instances=(i1, i2, i3, ))
session.viewports['Viewport: 1'].assemblyDisplay.displayGroup.replace(
    leaf=leaf)
session.viewports['Viewport: 1'].view.setValues(nearPlane=470651,
    farPlane=474996, width=7775.53, height=3084.15, viewOffsetX=-3351.89,
    viewOffsetY=5613.05)
session.viewports['Viewport: 1'].view.setValues(nearPlane=469656,
    farPlane=473964, width=7759.1, height=3077.63, cameraPosition=(-84660.9,
    247137, 434843), cameraUpVector=(-0.672725, 0.437542, -0.596655),
    cameraTarget=(-136196, 23405.6, 103822), viewOffsetX=-3344.8,
    viewOffsetY=5601.18)
session.viewports['Viewport: 1'].view.setValues(nearPlane=469683,
    farPlane=473936, width=7773.06, height=3083.17, viewOffsetX=-2999.14,
    viewOffsetY=5349.95)
session.viewports['Viewport: 1'].view.setValues(nearPlane=469909,
    farPlane=474455, width=7776.79, height=3084.65, cameraPosition=(239191,
    200546, -111394), cameraUpVector=(-0.812807, 0.459405, -0.358178),
    cameraTarget=(-91154.1, 13792.6, 23814.6), viewOffsetX=-3000.58,
    viewOffsetY=5352.52)
session.viewports['Viewport: 1'].view.setValues(nearPlane=469763,
    farPlane=474650, width=7774.37, height=3083.69, cameraPosition=(124720,
    54193.1, -330524), cameraUpVector=(-0.74875, 0.662852, 0.00129479),
    cameraTarget=(-109365, -8271.69, -8671.7), viewOffsetX=-2999.65,
    viewOffsetY=5350.85)
session.viewports['Viewport: 1'].view.setValues(nearPlane=469932,
    farPlane=474482, width=6087.65, height=2414.65, viewOffsetX=-2406.51,
    viewOffsetY=5178.94)
session.viewports['Viewport: 1'].view.setValues(nearPlane=469815,
    farPlane=473683, width=6086.13, height=2414.05, cameraPosition=(151920,
    328201, -72735.8), cameraUpVector=(-0.922226, 0.37558, 0.0918647),
    cameraTarget=(-103829, 33357.9, 26999.1), viewOffsetX=-2405.91,
    viewOffsetY=5177.65)
session.viewports['Viewport: 1'].view.setValues(nearPlane=469518,
    farPlane=473233, width=6082.29, height=2412.53, cameraPosition=(-205041,
    351422, 340907), cameraUpVector=(-0.849952, -0.16694, -0.499712),
    cameraTarget=(-154144, 40914.6, 89348.8), viewOffsetX=-2404.39,
    viewOffsetY=5174.38)
session.viewports['Viewport: 1'].view.setValues(nearPlane=469784,
    farPlane=472967, width=2918.74, height=1157.71, viewOffsetX=-2827.62,
    viewOffsetY=5534.53)
a = mdb.models['Model-1'].rootAssembly
s1 = a.instances['P-26-1'].faces
side2Faces1 = s1.getSequenceFromMask(mask=('[#ffffffff ]', ), )
region1=regionToolset.Region(side2Faces=side2Faces1)
a = mdb.models['Model-1'].rootAssembly
s1 = a.instances['P-29-1'].edges
side1Edges1 = s1.getSequenceFromMask(mask=('[#c0700700 #600 ]', ), )
s2 = a.instances['P-28-1'].edges
side1Edges2 = s2.getSequenceFromMask(mask=('[#ab6ad4a ]', ), )
region2=regionToolset.Region(side1Edges=side1Edges1+side1Edges2)
mdb.models['Model-1'].Tie(name='Constraint-17', main=region1,
    secondary=region2, positionToleranceMethod=COMPUTED, adjust=ON,
    tieRotations=ON, thickness=ON)
session.viewports['Viewport: 1'].view.setValues(nearPlane=469049,
    farPlane=473703, width=5599.85, height=4519.74, viewOffsetX=-2979.63,
    viewOffsetY=5392.87)
leaf = dgm.Leaf(leafType=DEFAULT_MODEL)
session.viewports['Viewport: 1'].assemblyDisplay.displayGroup.replace(
    leaf=leaf)
session.viewports['Viewport: 1'].view.setValues(nearPlane=454434,
    farPlane=524576, width=23058.6, height=9146.17, viewOffsetX=1265.46,
    viewOffsetY=6197.76)
session.viewports['Viewport: 1'].view.setValues(nearPlane=450299,
    farPlane=549220, width=22848.8, height=9062.96, cameraPosition=(-310071,
    389778, 237676), cameraUpVector=(-0.7453, -0.458833, -0.483736),
    cameraTarget=(-172858, 49406.6, 71523.2), viewOffsetX=1253.95,
    viewOffsetY=6141.37)
session.viewports['Viewport: 1'].view.setValues(nearPlane=446089,
    farPlane=553431, width=74204.4, height=29433.1, viewOffsetX=6639.89,
    viewOffsetY=11477.8)
session.viewports['Viewport: 1'].view.setValues(nearPlane=433785,
    farPlane=506530, width=72157.7, height=28621.2, cameraPosition=(-72690.3,
    405124, 252320), cameraUpVector=(-0.925572, -0.337271, 0.171943),
    cameraTarget=(-123208, 51077.7, 66884.5), viewOffsetX=6456.75,
    viewOffsetY=11161.2)
session.viewports['Viewport: 1'].view.setValues(nearPlane=426745,
    farPlane=513572, width=161162, height=63924.5, viewOffsetX=12465.4,
    viewOffsetY=20928.8)
session.viewports['Viewport: 1'].view.setValues(nearPlane=350956,
    farPlane=520743, width=132540, height=52571.7, cameraPosition=(146773,
    282459, 251184), cameraUpVector=(-0.758921, -0.269747, 0.592685),
    cameraTarget=(-96145.8, 30309.6, 51939.4), viewOffsetX=10251.6,
    viewOffsetY=17211.9)
session.viewports['Viewport: 1'].view.setValues(nearPlane=361224,
    farPlane=510476, width=41757.7, height=16563.1, viewOffsetX=3889.72,
    viewOffsetY=21555.4)
session.viewports['Viewport: 1'].view.setValues(nearPlane=341025,
    farPlane=509430, width=39422.7, height=15636.9, cameraPosition=(203581,
    235451, 218166), cameraUpVector=(-0.66314, -0.268169, 0.698807),
    cameraTarget=(-95607.8, 27322.5, 46539), viewOffsetX=3672.22,
    viewOffsetY=20350.1)
session.viewports['Viewport: 1'].view.setValues(nearPlane=341423,
    farPlane=512206, width=39468.8, height=15655.2, cameraPosition=(201888,
    180046, 277100), cameraUpVector=(-0.764592, -0.265628, 0.587231),
    cameraTarget=(-93492.5, 25199.4, 51135.2), viewOffsetX=3676.51,
    viewOffsetY=20373.9)
session.viewports['Viewport: 1'].view.setValues(nearPlane=343125,
    farPlane=510505, width=19126.1, height=7586.34, viewOffsetX=-4708.72,
    viewOffsetY=24674.6)
session.viewports['Viewport: 1'].view.setValues(nearPlane=348532,
    farPlane=511039, width=19427.5, height=7705.89, cameraPosition=(186677,
    189468, 291521), cameraUpVector=(-0.784322, -0.283752, 0.551656),
    cameraTarget=(-93454.9, 26003.9, 52580.3), viewOffsetX=-4782.92,
    viewOffsetY=25063.5)
session.viewports['Viewport: 1'].view.setValues(nearPlane=348433,
    farPlane=511138, width=19455.8, height=7717.11, viewOffsetX=-1011.93,
    viewOffsetY=27633.5)
session.viewports['Viewport: 1'].view.setValues(nearPlane=348698,
    farPlane=510873, width=16537.3, height=6559.48, viewOffsetX=-1694.12,
    viewOffsetY=27490.6)
a = mdb.models['Model-1'].rootAssembly
f1 = a.instances['P-1-1'].faces
faces1 = f1.getSequenceFromMask(mask=('[#1 ]', ), )
leaf = dgm.LeafFromGeometry(faceSeq=faces1)
session.viewports['Viewport: 1'].assemblyDisplay.displayGroup.remove(leaf=leaf)
a = mdb.models['Model-1'].rootAssembly
f1 = a.instances['P-1-1'].faces
faces1 = f1.getSequenceFromMask(mask=('[#2 ]', ), )
leaf = dgm.LeafFromGeometry(faceSeq=faces1)
session.viewports['Viewport: 1'].assemblyDisplay.displayGroup.remove(leaf=leaf)
session.viewports['Viewport: 1'].view.setValues(nearPlane=348516,
    farPlane=511178, width=21995.8, height=8724.59, viewOffsetX=-3135.08,
    viewOffsetY=27936.6)
session.viewports['Viewport: 1'].view.setValues(nearPlane=336572,
    farPlane=502785, width=21242, height=8425.58, cameraPosition=(211377,
    236145, 190839), cameraUpVector=(-0.662119, -0.179008, 0.727705),
    cameraTarget=(-97113.4, 23779, 42443), viewOffsetX=-3027.64,
    viewOffsetY=26979.2)
session.viewports['Viewport: 1'].view.setValues(nearPlane=333167,
    farPlane=506190, width=63528.1, height=25198.3, viewOffsetX=1466.63,
    viewOffsetY=27201)
session.viewports['Viewport: 1'].view.setValues(nearPlane=331587,
    farPlane=485654, width=63226.9, height=25078.9, cameraPosition=(204403,
    277029, 46472.8), cameraUpVector=(-0.711743, 0.290362, 0.639618),
    cameraTarget=(-95457.2, 8015.34, 44865.6), viewOffsetX=1459.68,
    viewOffsetY=27072)
session.viewports['Viewport: 1'].view.setValues(nearPlane=327847,
    farPlane=489394, width=110708, height=43912.3, viewOffsetX=64.8926,
    viewOffsetY=25147.8)
session.viewports['Viewport: 1'].view.setValues(nearPlane=324544,
    farPlane=470378, width=109593, height=43469.8, cameraPosition=(118682,
    296258, -127879), cameraUpVector=(-0.800226, 0.395678, 0.450641),
    cameraTarget=(-91324.5, 4263.05, 53569), viewOffsetX=64.2388,
    viewOffsetY=24894.5)
session.viewports['Viewport: 1'].view.setValues(nearPlane=332114,
    farPlane=462809, width=24937.4, height=9891.38, viewOffsetX=32893,
    viewOffsetY=20791.7)
session.viewports['Viewport: 1'].view.setValues(nearPlane=305184,
    farPlane=464187, width=22915.4, height=9089.34, cameraPosition=(175095,
    194755, -170685), cameraUpVector=(-0.671177, 0.654917, 0.347283),
    cameraTarget=(-95550.7, 1755.7, 56887.7), viewOffsetX=30225.9,
    viewOffsetY=19105.8)
session.viewports['Viewport: 1'].view.setValues(nearPlane=299411,
    farPlane=469961, width=94813.1, height=37607.4, viewOffsetX=40054.5,
    viewOffsetY=15250.2)
session.viewports['Viewport: 1'].view.setValues(nearPlane=267469,
    farPlane=452004, width=84698.2, height=33595.4, cameraPosition=(206192,
    -90757.4, -168324), cameraUpVector=(-0.342589, 0.871987, -0.349674),
    cameraTarget=(-100988, 34260.5, 60363.4), viewOffsetX=35781.4,
    viewOffsetY=13623.3)
session.viewports['Viewport: 1'].view.setValues(nearPlane=274124,
    farPlane=445349, width=19302, height=7656.11, viewOffsetX=43792.8,
    viewOffsetY=-16219.7)
session.viewports['Viewport: 1'].view.setValues(nearPlane=279017,
    farPlane=442480, width=19646.6, height=7792.79, cameraPosition=(184007,
    -67246, -207412), cameraUpVector=(-0.367354, 0.908298, -0.200115),
    cameraTarget=(-95300.7, 28046.5, 66802.6), viewOffsetX=44574.5,
    viewOffsetY=-16509.2)
session.viewports['Viewport: 1'].view.setValues(nearPlane=275970,
    farPlane=445528, width=56458.7, height=22394.2, viewOffsetX=46596.6,
    viewOffsetY=-11041.8)
session.viewports['Viewport: 1'].view.setValues(nearPlane=272364,
    farPlane=443610, width=55721, height=22101.6, cameraPosition=(187523,
    12465.3, -205474), cameraUpVector=(-0.482465, 0.87526, -0.0338889),
    cameraTarget=(-101559, 17400.2, 75051.3), viewOffsetX=45987.9,
    viewOffsetY=-10897.5)
session.viewports['Viewport: 1'].view.setValues(nearPlane=276244,
    farPlane=439730, width=12479.5, height=4949.99, viewOffsetX=44207.1,
    viewOffsetY=-4354.49)
session.viewports['Viewport: 1'].view.setValues(nearPlane=273565,
    farPlane=440532, width=12358.5, height=4901.97, cameraPosition=(192601,
    40396.2, -193285), cameraUpVector=(-0.52169, 0.853078, 0.00985695),
    cameraTarget=(-104952, 12721, 76869.3), viewOffsetX=43778.2,
    viewOffsetY=-4312.25)
session.viewports['Viewport: 1'].view.setValues(nearPlane=272660,
    farPlane=441437, width=23793.1, height=9437.49, viewOffsetX=42842.3,
    viewOffsetY=-3439.85)
session.viewports['Viewport: 1'].view.setValues(nearPlane=271688,
    farPlane=441524, width=23708.3, height=9403.86, cameraPosition=(190368,
    81112.3, -182181), cameraUpVector=(-0.583797, 0.807762, 0.0818695),
    cameraTarget=(-107324, 5774.82, 78570.2), viewOffsetX=42689.7,
    viewOffsetY=-3427.6)
session.viewports['Viewport: 1'].view.setValues(nearPlane=272863,
    farPlane=440349, width=9920.99, height=3935.14, viewOffsetX=40070.9,
    viewOffsetY=2695.08)
leaf = dgm.Leaf(leafType=DEFAULT_MODEL)
session.viewports['Viewport: 1'].assemblyDisplay.displayGroup.replace(
    leaf=leaf)
session.viewports['Viewport: 1'].view.setValues(nearPlane=272786,
    farPlane=440614, width=10762, height=4268.71, viewOffsetX=39523.8,
    viewOffsetY=2613.86)
i1 = mdb.models['Model-1'].rootAssembly.allInstances['P-1-1']
leaf = dgm.LeafFromInstance(instances=(i1, ))
session.viewports['Viewport: 1'].assemblyDisplay.displayGroup.remove(leaf=leaf)
session.viewports['Viewport: 1'].view.setValues(nearPlane=273396,
    farPlane=439816, width=4393.68, height=1742.74, viewOffsetX=37814.4,
    viewOffsetY=1977.69)
a = mdb.models['Model-1'].rootAssembly
s1 = a.instances['P-1-1'].faces
side1Faces1 = s1.getSequenceFromMask(mask=('[#2 ]', ), )
region1=regionToolset.Region(side1Faces=side1Faces1)
a = mdb.models['Model-1'].rootAssembly
s1 = a.instances['P-30-1'].edges
side1Edges1 = s1.getSequenceFromMask(mask=('[#92288 ]', ), )
region2=regionToolset.Region(side1Edges=side1Edges1)
mdb.models['Model-1'].Tie(name='Constraint-18', main=region1,
    secondary=region2, positionToleranceMethod=COMPUTED, adjust=ON,
    tieRotations=ON, thickness=ON)
session.viewports['Viewport: 1'].view.setValues(nearPlane=273086,
    farPlane=440126, width=7461.25, height=2959.49, viewOffsetX=42650.8,
    viewOffsetY=3783.25)
i1 = mdb.models['Model-1'].rootAssembly.allInstances['P-36-1']
i2 = mdb.models['Model-1'].rootAssembly.allInstances['P-37-1']
i3 = mdb.models['Model-1'].rootAssembly.allInstances['P-38-1']
leaf = dgm.LeafFromInstance(instances=(i1, i2, i3, ))
session.viewports['Viewport: 1'].assemblyDisplay.displayGroup.replace(
    leaf=leaf)
session.viewports['Viewport: 1'].view.setValues(nearPlane=418733,
    farPlane=426417, width=8597.02, height=3409.99, viewOffsetX=64481.9,
    viewOffsetY=6019.68)
i1 = mdb.models['Model-1'].rootAssembly.allInstances['P-36-1']
i2 = mdb.models['Model-1'].rootAssembly.allInstances['P-37-1']
leaf = dgm.LeafFromInstance(instances=(i1, i2, ))
session.viewports['Viewport: 1'].assemblyDisplay.displayGroup.replace(
    leaf=leaf)
a = mdb.models['Model-1'].rootAssembly
s1 = a.instances['P-38-1'].faces
side1Faces1 = s1.getSequenceFromMask(mask=('[#ffff ]', ), )
region1=regionToolset.Region(side1Faces=side1Faces1)
a = mdb.models['Model-1'].rootAssembly
s1 = a.instances['P-36-1'].edges
side1Edges1 = s1.getSequenceFromMask(mask=('[#11 ]', ), )
s2 = a.instances['P-37-1'].edges
side1Edges2 = s2.getSequenceFromMask(mask=('[#88 ]', ), )
region2=regionToolset.Region(side1Edges=side1Edges1+side1Edges2)
mdb.models['Model-1'].Tie(name='Constraint-19', main=region1,
    secondary=region2, positionToleranceMethod=COMPUTED, adjust=ON,
    tieRotations=ON, thickness=ON)
leaf = dgm.Leaf(leafType=DEFAULT_MODEL)
session.viewports['Viewport: 1'].assemblyDisplay.displayGroup.replace(
    leaf=leaf)
session.viewports['Viewport: 1'].view.setValues(nearPlane=272861,
    farPlane=440540, width=10783.7, height=4277.34, viewOffsetX=42319.3,
    viewOffsetY=4546.47)
i1 = mdb.models['Model-1'].rootAssembly.allInstances['P-1-1']
leaf = dgm.LeafFromInstance(instances=(i1, ))
session.viewports['Viewport: 1'].assemblyDisplay.displayGroup.remove(leaf=leaf)
session.viewports['Viewport: 1'].view.setValues(nearPlane=273085,
    farPlane=440127, width=7474.21, height=2964.63, viewOffsetX=42313.9,
    viewOffsetY=4302.84)
a = mdb.models['Model-1'].rootAssembly
s1 = a.instances['P-1-1'].faces
side1Faces1 = s1.getSequenceFromMask(mask=('[#3 ]', ), )
region1=regionToolset.Region(side1Faces=side1Faces1)
a = mdb.models['Model-1'].rootAssembly
s1 = a.instances['P-37-1'].edges
side1Edges1 = s1.getSequenceFromMask(mask=('[#22 ]', ), )
s2 = a.instances['P-36-1'].edges
side1Edges2 = s2.getSequenceFromMask(mask=('[#44 ]', ), )
region2=regionToolset.Region(side1Edges=side1Edges1+side1Edges2)
mdb.models['Model-1'].Tie(name='Constraint-20', main=region1,
    secondary=region2, positionToleranceMethod=COMPUTED, adjust=ON,
    tieRotations=ON, thickness=ON)
session.viewports['Viewport: 1'].view.setValues(nearPlane=272996,
    farPlane=440217, width=8459.88, height=3355.6, viewOffsetX=43096.9,
    viewOffsetY=4066.45)
session.viewports['Viewport: 1'].view.setValues(nearPlane=273056,
    farPlane=440157, width=7798.34, height=3093.2, viewOffsetX=43062.7,
    viewOffsetY=3984.43)
i1 = mdb.models['Model-1'].rootAssembly.allInstances['P-35-1']
i2 = mdb.models['Model-1'].rootAssembly.allInstances['P-36-1']
i3 = mdb.models['Model-1'].rootAssembly.allInstances['P-37-1']
i4 = mdb.models['Model-1'].rootAssembly.allInstances['P-38-1']
i5 = mdb.models['Model-1'].rootAssembly.allInstances['P-39-1']
i6 = mdb.models['Model-1'].rootAssembly.allInstances['P-40-1']
i7 = mdb.models['Model-1'].rootAssembly.allInstances['P-41-1']
leaf = dgm.LeafFromInstance(instances=(i1, i2, i3, i4, i5, i6, i7, ))
session.viewports['Viewport: 1'].assemblyDisplay.displayGroup.replace(
    leaf=leaf)
session.viewports['Viewport: 1'].view.setValues(nearPlane=414775,
    farPlane=426935, width=7560.45, height=2998.84, viewOffsetX=64370.2,
    viewOffsetY=5749.09)
i1 = mdb.models['Model-1'].rootAssembly.allInstances['P-35-1']
i2 = mdb.models['Model-1'].rootAssembly.allInstances['P-36-1']
leaf = dgm.LeafFromInstance(instances=(i1, i2, ))
session.viewports['Viewport: 1'].assemblyDisplay.displayGroup.remove(leaf=leaf)
i1 = mdb.models['Model-1'].rootAssembly.allInstances['P-37-1']
leaf = dgm.LeafFromInstance(instances=(i1, ))
session.viewports['Viewport: 1'].assemblyDisplay.displayGroup.remove(leaf=leaf)
i1 = mdb.models['Model-1'].rootAssembly.allInstances['P-38-1']
leaf = dgm.LeafFromInstance(instances=(i1, ))
session.viewports['Viewport: 1'].assemblyDisplay.displayGroup.remove(leaf=leaf)
session.viewports['Viewport: 1'].view.setValues(nearPlane=420222,
    farPlane=424820, width=10618, height=4211.62, viewOffsetX=66048.6,
    viewOffsetY=5736.53)
session.viewports['Viewport: 1'].view.setValues(nearPlane=419110,
    farPlane=424110, width=10589.9, height=4200.47, cameraPosition=(183535,
    224994, -37500.7), cameraUpVector=(-0.827497, 0.495096, -0.264819),
    cameraTarget=(-140504, 24778.2, 93648.4), viewOffsetX=65873.8,
    viewOffsetY=5721.35)
session.viewports['Viewport: 1'].view.setValues(nearPlane=419242,
    farPlane=423979, width=9486.97, height=3762.99, viewOffsetX=65805,
    viewOffsetY=4653.74)
session.viewports['Viewport: 1'].view.setValues(nearPlane=418745,
    farPlane=423643, width=9475.73, height=3758.53, cameraPosition=(101378,
    318346, -7911.44), cameraUpVector=(-0.892392, 0.207079, -0.400942),
    cameraTarget=(-161351, 30139.8, 93076.7), viewOffsetX=65727,
    viewOffsetY=4648.22)
session.viewports['Viewport: 1'].view.setValues(nearPlane=418427,
    farPlane=423960, width=13672.3, height=5423.1, viewOffsetX=66226.4,
    viewOffsetY=4488.03)
session.viewports['Viewport: 1'].view.setValues(nearPlane=417296,
    farPlane=422195, width=13635.4, height=5408.44, cameraPosition=(-235304,
    397937, 115111), cameraUpVector=(-0.754526, -0.393142, -0.525481),
    cameraTarget=(-193911, -2484.35, 99706), viewOffsetX=66047.4,
    viewOffsetY=4475.9)
session.viewports['Viewport: 1'].view.setValues(nearPlane=417519,
    farPlane=421973, width=10678.9, height=4235.77, viewOffsetX=65882.4,
    viewOffsetY=4508.73)
session.viewports['Viewport: 1'].view.setValues(nearPlane=418021,
    farPlane=422719, width=10691.8, height=4240.86, cameraPosition=(-224665,
    380616, -103589), cameraUpVector=(-0.682987, -0.619176, -0.387491),
    cameraTarget=(-201982, 23234.2, 80942.1), viewOffsetX=65961.6,
    viewOffsetY=4514.16)
session.viewports['Viewport: 1'].view.setValues(nearPlane=418155,
    farPlane=422586, width=9528.49, height=3779.46, viewOffsetX=65624.2,
    viewOffsetY=3941.47)
session.viewports['Viewport: 1'].view.setValues(nearPlane=418628,
    farPlane=423416, width=9539.27, height=3783.73, cameraPosition=(-47513.3,
    -237580, -302295), cameraUpVector=(-0.9463, -0.21053, 0.245345),
    cameraTarget=(-172395, 18160.7, -17181.8), viewOffsetX=65698.5,
    viewOffsetY=3945.93)
session.viewports['Viewport: 1'].view.setValues(nearPlane=418592,
    farPlane=423343, width=9538.44, height=3783.4, cameraPosition=(-67600.3,
    -353724, -197267), cameraUpVector=(-0.985778, 0.0402258, 0.163168),
    cameraTarget=(-160972, -1650.04, -25180.8), viewOffsetX=65692.8,
    viewOffsetY=3945.59)
session.viewports['Viewport: 1'].view.setValues(nearPlane=419097,
    farPlane=422838, width=3597.66, height=1427, viewOffsetX=65949.1,
    viewOffsetY=4979.59)
a = mdb.models['Model-1'].rootAssembly
s1 = a.instances['P-38-1'].faces
side2Faces1 = s1.getSequenceFromMask(mask=('[#ffff ]', ), )
region1=regionToolset.Region(side2Faces=side2Faces1)
a = mdb.models['Model-1'].rootAssembly
s1 = a.instances['P-41-1'].edges
side1Edges1 = s1.getSequenceFromMask(mask=('[#c00600c0 #1c01 ]', ), )
s2 = a.instances['P-40-1'].edges
side1Edges2 = s2.getSequenceFromMask(mask=('[#ab6ad5a ]', ), )
region2=regionToolset.Region(side1Edges=side1Edges1+side1Edges2)
mdb.models['Model-1'].Tie(name='Constraint-21', main=region1,
    secondary=region2, positionToleranceMethod=COMPUTED, adjust=ON,
    tieRotations=ON, thickness=ON)
session.viewports['Viewport: 1'].view.setValues(nearPlane=419054,
    farPlane=422881, width=4419.51, height=1752.99, viewOffsetX=65934.3,
    viewOffsetY=4969.11)
leaf = dgm.Leaf(leafType=DEFAULT_MODEL)
session.viewports['Viewport: 1'].assemblyDisplay.displayGroup.replace(
    leaf=leaf)
session.viewports['Viewport: 1'].view.setValues(nearPlane=358242,
    farPlane=444654, width=56884.7, height=22563.2, viewOffsetX=64415.6,
    viewOffsetY=2888.08)
session.viewports['Viewport: 1'].view.setValues(nearPlane=317373,
    farPlane=461386, width=50395.1, height=19989.1, cameraPosition=(60394.3,
    -255971, 305373), cameraUpVector=(-0.974242, -0.200381, 0.103445),
    cameraTarget=(-143668, -92073.7, -869.445), viewOffsetX=57066.9,
    viewOffsetY=2558.6)
session.viewports['Viewport: 1'].view.setValues(nearPlane=317499,
    farPlane=439641, width=50415.1, height=19997, cameraPosition=(19893.4,
    10225.6, 402405), cameraUpVector=(-0.945263, -0.305233, 0.11537),
    cameraTarget=(-127358, -108180, 46616.9), viewOffsetX=57089.5,
    viewOffsetY=2559.62)
session.viewports['Viewport: 1'].view.setValues(nearPlane=313497,
    farPlane=443642, width=100163, height=39729.3, viewOffsetX=76569.3,
    viewOffsetY=5495)
session.viewports['Viewport: 1'].view.setValues(nearPlane=333149,
    farPlane=424830, width=106441, height=42219.8, cameraPosition=(-21454.5,
    227755, 327901), cameraUpVector=(-0.743752, -0.555135, 0.372369),
    cameraTarget=(-92079.2, -83986.7, 82712.8), viewOffsetX=81369.2,
    viewOffsetY=5839.46)
session.viewports['Viewport: 1'].view.setValues(nearPlane=343871,
    farPlane=444005, width=109867, height=43578.6, cameraPosition=(-222974,
    365069, 95783.1), cameraUpVector=(-0.465377, -0.509646, 0.723661),
    cameraTarget=(-77121.7, -10146.5, 110893), viewOffsetX=83988,
    viewOffsetY=6027.4)
session.viewports['Viewport: 1'].view.setValues(nearPlane=346736,
    farPlane=441140, width=70705.8, height=28045.3, viewOffsetX=90696.1,
    viewOffsetY=3812.64)
session.viewports['Viewport: 1'].view.setValues(nearPlane=349210,
    farPlane=439782, width=71210.2, height=28245.4, cameraPosition=(-198213,
    349416, 178377), cameraUpVector=(-0.480223, -0.621954, 0.618514),
    cameraTarget=(-74607.1, -28171.5, 111768), viewOffsetX=91343,
    viewOffsetY=3839.84)
session.viewports['Viewport: 1'].view.setValues(nearPlane=352474,
    farPlane=436117, width=71875.8, height=28509.4, cameraPosition=(-145480,
    308617, 267301), cameraUpVector=(-0.424865, -0.73024, 0.535013),
    cameraTarget=(-65011.4, -47241, 96485.7), viewOffsetX=92196.8,
    viewOffsetY=3875.73)
session.viewports['Viewport: 1'].view.setValues(nearPlane=353553,
    farPlane=435039, width=56531.7, height=22423.2, viewOffsetX=106326,
    viewOffsetY=-1870.16)
session.viewports['Viewport: 1'].view.setValues(nearPlane=351271,
    farPlane=388066, width=56166.8, height=22278.5, cameraPosition=(-74371.7,
    358265, 138583), cameraUpVector=(-0.767124, -0.30944, 0.561933),
    cameraTarget=(-94566.6, -43951.8, 128495), viewOffsetX=105640,
    viewOffsetY=-1858.09)
session.viewports['Viewport: 1'].view.setValues(nearPlane=347242,
    farPlane=392094, width=106878, height=42392.8, viewOffsetX=100360,
    viewOffsetY=4529.82)
session.viewports['Viewport: 1'].view.setValues(nearPlane=214122,
    farPlane=391904, width=65904.4, height=26140.9, cameraPosition=(159670,
    27235.1, -162736), cameraUpVector=(-0.618122, 0.754959, -0.219002),
    cameraTarget=(-118603, 61193.4, 126572), viewOffsetX=61885.4,
    viewOffsetY=2793.25)
session.viewports['Viewport: 1'].view.setValues(nearPlane=220210,
    farPlane=380946, width=67778.4, height=26884.2, cameraPosition=(149164,
    -73075.1, -164786), cameraUpVector=(-0.462656, 0.789541, -0.403206),
    cameraTarget=(-99086.9, 90396, 107127), viewOffsetX=63645.1,
    viewOffsetY=2872.67)
session.viewports['Viewport: 1'].view.setValues(nearPlane=211685,
    farPlane=390158, width=65154.6, height=25843.5, cameraPosition=(176513,
    9791.5, -135662), cameraUpVector=(-0.52558, 0.816964, -0.237353),
    cameraTarget=(-125036, 56574.4, 127334), viewOffsetX=61181.3,
    viewOffsetY=2761.47)
session.viewports['Viewport: 1'].view.setValues(nearPlane=216463,
    farPlane=385380, width=12495.7, height=4956.39, viewOffsetX=66451.4,
    viewOffsetY=-3595.67)
leaf = dgm.Leaf(leafType=DEFAULT_MODEL)
session.viewports['Viewport: 1'].assemblyDisplay.displayGroup.replace(
    leaf=leaf)
a = mdb.models['Model-1'].rootAssembly
f1 = a.instances['P-1-1'].faces
faces1 = f1.getSequenceFromMask(mask=('[#2 ]', ), )
leaf = dgm.LeafFromGeometry(faceSeq=faces1)
session.viewports['Viewport: 1'].assemblyDisplay.displayGroup.remove(leaf=leaf)
session.viewports['Viewport: 1'].view.setValues(nearPlane=215253,
    farPlane=386522, width=28112.6, height=11150.8, viewOffsetX=68154.9,
    viewOffsetY=-3739.48)
session.viewports['Viewport: 1'].view.setValues(nearPlane=215615,
    farPlane=386110, width=28159.9, height=11169.6, cameraPosition=(173928,
    28823.3, -136509), cameraUpVector=(-0.561189, 0.805447, -0.19058),
    cameraTarget=(-126667, 49379.7, 130900), viewOffsetX=68269.5,
    viewOffsetY=-3745.77)
session.viewports['Viewport: 1'].view.setValues(nearPlane=217562,
    farPlane=384163, width=5560.85, height=2205.7, viewOffsetX=64800.6,
    viewOffsetY=-662.204)
leaf = dgm.Leaf(leafType=DEFAULT_MODEL)
session.viewports['Viewport: 1'].assemblyDisplay.displayGroup.replace(
    leaf=leaf)
session.viewports['Viewport: 1'].view.setValues(nearPlane=215879,
    farPlane=385921, width=26074.5, height=10342.4, viewOffsetX=67531.8,
    viewOffsetY=-2599.76)
session.viewports['Viewport: 1'].view.setValues(nearPlane=206560,
    farPlane=387396, width=24948.9, height=9895.94, cameraPosition=(184380,
    80933.2, -82254.6), cameraUpVector=(-0.627727, 0.761414, -0.161884),
    cameraTarget=(-151795, 25864.4, 132783), viewOffsetX=64616.6,
    viewOffsetY=-2487.53)
session.viewports['Viewport: 1'].view.setValues(nearPlane=204835,
    farPlane=389120, width=47706.8, height=18922.8, viewOffsetX=63201.9,
    viewOffsetY=-1019.85)
session.viewports['Viewport: 1'].view.setValues(nearPlane=199917,
    farPlane=386138, width=46561.2, height=18468.4, cameraPosition=(171596,
    142686, -13311.6), cameraUpVector=(-0.724417, 0.626768, -0.287022),
    cameraTarget=(-183900, 6304.34, 118255), viewOffsetX=61684.2,
    viewOffsetY=-995.356)
session.viewports['Viewport: 1'].view.setValues(nearPlane=201755,
    farPlane=384300, width=27735.3, height=11001.2, viewOffsetX=44239.6,
    viewOffsetY=1507.86)
session.viewports['Viewport: 1'].view.setValues(nearPlane=194915,
    farPlane=382602, width=26795.1, height=10628.2, cameraPosition=(186540,
    93810.3, -34852.5), cameraUpVector=(-0.634257, 0.660935, -0.401102),
    cameraTarget=(-181956, 35623.9, 117175), viewOffsetX=42739.8,
    viewOffsetY=1456.74)
session.viewports['Viewport: 1'].view.setValues(nearPlane=196486,
    farPlane=381032, width=9345.31, height=3706.8, viewOffsetX=45396.9,
    viewOffsetY=68.5123)
i1 = mdb.models['Model-1'].rootAssembly.allInstances['P-1-1']
leaf = dgm.LeafFromInstance(instances=(i1, ))
session.viewports['Viewport: 1'].assemblyDisplay.displayGroup.remove(leaf=leaf)
session.viewports['Viewport: 1'].view.setValues(nearPlane=196943,
    farPlane=380463, width=4320.27, height=1713.63, viewOffsetX=45320.3,
    viewOffsetY=-648.855)
a = mdb.models['Model-1'].rootAssembly
s1 = a.instances['P-1-1'].faces
side1Faces1 = s1.getSequenceFromMask(mask=('[#3 ]', ), )
region1=regionToolset.Region(side1Faces=side1Faces1)
a = mdb.models['Model-1'].rootAssembly
s1 = a.instances['P-42-1'].edges
side1Edges1 = s1.getSequenceFromMask(mask=('[#888 ]', ), )
region2=regionToolset.Region(side1Edges=side1Edges1)
mdb.models['Model-1'].Tie(name='Constraint-22', main=region1,
    secondary=region2, positionToleranceMethod=COMPUTED, adjust=ON,
    tieRotations=ON, thickness=ON)
session.viewports['Viewport: 1'].view.setValues(nearPlane=196579,
    farPlane=380826, width=9022.7, height=3578.84, viewOffsetX=45898,
    viewOffsetY=-438.533)
leaf = dgm.Leaf(leafType=DEFAULT_MODEL)
session.viewports['Viewport: 1'].assemblyDisplay.displayGroup.replace(
    leaf=leaf)
session.viewports['Viewport: 1'].view.setValues(nearPlane=196718,
    farPlane=380800, width=7362.07, height=2920.15, viewOffsetX=44976.5,
    viewOffsetY=-823.748)
a = mdb.models['Model-1'].rootAssembly
f1 = a.instances['P-43-1'].faces
faces1 = f1.getSequenceFromMask(mask=('[#10 ]', ), )
leaf = dgm.LeafFromGeometry(faceSeq=faces1)
session.viewports['Viewport: 1'].assemblyDisplay.displayGroup.remove(leaf=leaf)
session.viewports['Viewport: 1'].view.setValues(width=7066.67, height=2802.98,
    viewOffsetX=44935.2, viewOffsetY=-775.963)
a = mdb.models['Model-1'].rootAssembly
f1 = a.instances['P-35-1'].faces
faces1 = f1.getSequenceFromMask(mask=('[#4 ]', ), )
leaf = dgm.LeafFromGeometry(faceSeq=faces1)
session.viewports['Viewport: 1'].assemblyDisplay.displayGroup.remove(leaf=leaf)
a = mdb.models['Model-1'].rootAssembly
f1 = a.instances['P-47-1'].faces
faces1 = f1.getSequenceFromMask(mask=('[#2 ]', ), )
leaf = dgm.LeafFromGeometry(faceSeq=faces1)
session.viewports['Viewport: 1'].assemblyDisplay.displayGroup.remove(leaf=leaf)
a = mdb.models['Model-1'].rootAssembly
f1 = a.instances['P-35-1'].faces
faces1 = f1.getSequenceFromMask(mask=('[#1 ]', ), )
leaf = dgm.LeafFromGeometry(faceSeq=faces1)
session.viewports['Viewport: 1'].assemblyDisplay.displayGroup.remove(leaf=leaf)
a = mdb.models['Model-1'].rootAssembly
f1 = a.instances['P-44-1'].faces
faces1 = f1.getSequenceFromMask(mask=('[#20 ]', ), )
leaf = dgm.LeafFromGeometry(faceSeq=faces1)
session.viewports['Viewport: 1'].assemblyDisplay.displayGroup.remove(leaf=leaf)
a = mdb.models['Model-1'].rootAssembly
f1 = a.instances['P-35-1'].faces
faces1 = f1.getSequenceFromMask(mask=('[#8 ]', ), )
leaf = dgm.LeafFromGeometry(faceSeq=faces1)
session.viewports['Viewport: 1'].assemblyDisplay.displayGroup.remove(leaf=leaf)
a = mdb.models['Model-1'].rootAssembly
f1 = a.instances['P-44-1'].faces
faces1 = f1.getSequenceFromMask(mask=('[#4 ]', ), )
leaf = dgm.LeafFromGeometry(faceSeq=faces1)
session.viewports['Viewport: 1'].assemblyDisplay.displayGroup.remove(leaf=leaf)
session.viewports['Viewport: 1'].view.setValues(width=6784.89, height=2691.22,
    viewOffsetX=44909.6, viewOffsetY=-739.515)
a = mdb.models['Model-1'].rootAssembly
f1 = a.instances['P-44-1'].faces
faces1 = f1.getSequenceFromMask(mask=('[#1 ]', ), )
leaf = dgm.LeafFromGeometry(faceSeq=faces1)
session.viewports['Viewport: 1'].assemblyDisplay.displayGroup.remove(leaf=leaf)
a = mdb.models['Model-1'].rootAssembly
f1 = a.instances['P-44-1'].faces
faces1 = f1.getSequenceFromMask(mask=('[#10 ]', ), )
leaf = dgm.LeafFromGeometry(faceSeq=faces1)
session.viewports['Viewport: 1'].assemblyDisplay.displayGroup.remove(leaf=leaf)
a = mdb.models['Model-1'].rootAssembly
f1 = a.instances['P-47-1'].faces
faces1 = f1.getSequenceFromMask(mask=('[#1 ]', ), )
leaf = dgm.LeafFromGeometry(faceSeq=faces1)
session.viewports['Viewport: 1'].assemblyDisplay.displayGroup.remove(leaf=leaf)
session.viewports['Viewport: 1'].view.setValues(nearPlane=197073,
    farPlane=380445, width=2884.17, height=1144, viewOffsetX=44594.3,
    viewOffsetY=-598.554)
a = mdb.models['Model-1'].rootAssembly
f1 = a.instances['P-46-1'].faces
faces1 = f1.getSequenceFromMask(mask=('[#fffffff ]', ), )
leaf = dgm.LeafFromGeometry(faceSeq=faces1)
session.viewports['Viewport: 1'].assemblyDisplay.displayGroup.remove(leaf=leaf)
session.viewports['Viewport: 1'].view.setValues(nearPlane=197130,
    farPlane=380388, width=2258.25, height=895.733, viewOffsetX=44415.5,
    viewOffsetY=-596.032)
a = mdb.models['Model-1'].rootAssembly
s1 = a.instances['P-46-1'].faces
side1Faces1 = s1.getSequenceFromMask(mask=('[#fffffff ]', ), )
region1=regionToolset.Region(side1Faces=side1Faces1)
a = mdb.models['Model-1'].rootAssembly
s1 = a.instances['P-45-1'].edges
side1Edges1 = s1.getSequenceFromMask(mask=('[#210 ]', ), )
region2=regionToolset.Region(side1Edges=side1Edges1)
mdb.models['Model-1'].Tie(name='Constraint-23', main=region1,
    secondary=region2, positionToleranceMethod=COMPUTED, adjust=ON,
    tieRotations=ON, thickness=ON)
session.viewports['Viewport: 1'].view.setValues(nearPlane=197103,
    farPlane=380415, width=2769.22, height=1098.41, viewOffsetX=44510,
    viewOffsetY=-593.275)
leaf = dgm.Leaf(leafType=DEFAULT_MODEL)
session.viewports['Viewport: 1'].assemblyDisplay.displayGroup.replace(
    leaf=leaf)
session.viewports['Viewport: 1'].view.setValues(nearPlane=196908,
    farPlane=380610, width=4703.3, height=1865.55, viewOffsetX=45092.5,
    viewOffsetY=-938.821)
i1 = mdb.models['Model-1'].rootAssembly.allInstances['P-1-1']
leaf = dgm.LeafFromInstance(instances=(i1, ))
session.viewports['Viewport: 1'].assemblyDisplay.displayGroup.remove(leaf=leaf)
i1 = mdb.models['Model-1'].rootAssembly.allInstances['P-2-1']
leaf = dgm.LeafFromInstance(instances=(i1, ))
session.viewports['Viewport: 1'].assemblyDisplay.displayGroup.remove(leaf=leaf)
session.viewports['Viewport: 1'].view.setValues(nearPlane=196285,
    farPlane=379998, width=12532.2, height=4970.88, viewOffsetX=45670.9,
    viewOffsetY=-928.668)
session.viewports['Viewport: 1'].view.setValues(nearPlane=207706,
    farPlane=378293, width=13261.4, height=5260.11, cameraPosition=(153572,
    171896, 60753.2), cameraUpVector=(-0.633608, 0.493688, -0.595662),
    cameraTarget=(-210580, 790.234, 80850.9), viewOffsetX=48328.2,
    viewOffsetY=-982.702)
session.viewports['Viewport: 1'].view.setValues(nearPlane=204371,
    farPlane=381628, width=52828.5, height=20954.3, viewOffsetX=35485.7,
    viewOffsetY=1842.69)
session.viewports['Viewport: 1'].view.setValues(nearPlane=247833,
    farPlane=376445, width=64062.9, height=25410.4, cameraPosition=(4522.34,
    241742, 201457), cameraUpVector=(-0.585188, 0.364809, -0.724202),
    cameraTarget=(-189953, -61167.1, 20589.6), viewOffsetX=43032,
    viewOffsetY=2234.55)
session.viewports['Viewport: 1'].view.setValues(nearPlane=251759,
    farPlane=372520, width=7517.47, height=2981.79, viewOffsetX=3578.63,
    viewOffsetY=4088.6)
a = mdb.models['Model-1'].rootAssembly
s1 = a.instances['P-1-1'].faces
side2Faces1 = s1.getSequenceFromMask(mask=('[#3 ]', ), )
region1=regionToolset.Region(side2Faces=side2Faces1)
a = mdb.models['Model-1'].rootAssembly
s1 = a.instances['P-43-1'].edges
side1Edges1 = s1.getSequenceFromMask(mask=('[#88489 ]', ), )
region2=regionToolset.Region(side1Edges=side1Edges1)
mdb.models['Model-1'].Tie(name='Constraint-24', main=region1,
    secondary=region2, positionToleranceMethod=COMPUTED, adjust=ON,
    tieRotations=ON, thickness=ON)
a = mdb.models['Model-1'].rootAssembly
f1 = a.instances['P-47-1'].faces
faces1 = f1.getSequenceFromMask(mask=('[#2 ]', ), )
leaf = dgm.LeafFromGeometry(faceSeq=faces1)
session.viewports['Viewport: 1'].assemblyDisplay.displayGroup.remove(leaf=leaf)
a = mdb.models['Model-1'].rootAssembly
f1 = a.instances['P-35-1'].faces
faces1 = f1.getSequenceFromMask(mask=('[#1 ]', ), )
leaf = dgm.LeafFromGeometry(faceSeq=faces1)
session.viewports['Viewport: 1'].assemblyDisplay.displayGroup.remove(leaf=leaf)
a = mdb.models['Model-1'].rootAssembly
f1 = a.instances['P-44-1'].faces
faces1 = f1.getSequenceFromMask(mask=('[#1 ]', ), )
leaf = dgm.LeafFromGeometry(faceSeq=faces1)
session.viewports['Viewport: 1'].assemblyDisplay.displayGroup.remove(leaf=leaf)
a = mdb.models['Model-1'].rootAssembly
f1 = a.instances['P-44-1'].faces
faces1 = f1.getSequenceFromMask(mask=('[#4 ]', ), )
leaf = dgm.LeafFromGeometry(faceSeq=faces1)
session.viewports['Viewport: 1'].assemblyDisplay.displayGroup.remove(leaf=leaf)
a = mdb.models['Model-1'].rootAssembly
f1 = a.instances['P-44-1'].faces
faces1 = f1.getSequenceFromMask(mask=('[#2 ]', ), )
leaf = dgm.LeafFromGeometry(faceSeq=faces1)
session.viewports['Viewport: 1'].assemblyDisplay.displayGroup.remove(leaf=leaf)
a = mdb.models['Model-1'].rootAssembly
f1 = a.instances['P-35-1'].faces
faces1 = f1.getSequenceFromMask(mask=('[#8 ]', ), )
leaf = dgm.LeafFromGeometry(faceSeq=faces1)
session.viewports['Viewport: 1'].assemblyDisplay.displayGroup.remove(leaf=leaf)
a = mdb.models['Model-1'].rootAssembly
f1 = a.instances['P-44-1'].faces
faces1 = f1.getSequenceFromMask(mask=('[#20 ]', ), )
leaf = dgm.LeafFromGeometry(faceSeq=faces1)
session.viewports['Viewport: 1'].assemblyDisplay.displayGroup.remove(leaf=leaf)
session.viewports['Viewport: 1'].view.setValues(nearPlane=251701,
    farPlane=372578, width=8848.84, height=3509.88, viewOffsetX=3552.41,
    viewOffsetY=4076.59)
a = mdb.models['Model-1'].rootAssembly
f1 = a.instances['P-44-1'].faces
faces1 = f1.getSequenceFromMask(mask=('[#10 ]', ), )
leaf = dgm.LeafFromGeometry(faceSeq=faces1)
session.viewports['Viewport: 1'].assemblyDisplay.displayGroup.remove(leaf=leaf)
session.viewports['Viewport: 1'].view.setValues(nearPlane=250835,
    farPlane=373444, width=19186.3, height=7610.21, viewOffsetX=5068.1,
    viewOffsetY=3664.55)
session.viewports['Viewport: 1'].view.setValues(nearPlane=302276,
    farPlane=370970, width=23121, height=9170.92, cameraPosition=(-106915,
    255411, 243229), cameraUpVector=(-0.31424, 0.298096, -0.901328),
    cameraTarget=(-160139, -66135.8, 6453.58), viewOffsetX=6107.46,
    viewOffsetY=4416.08)
session.viewports['Viewport: 1'].view.setValues(nearPlane=302975,
    farPlane=370271, width=10725.8, height=4254.36, viewOffsetX=-4813.74,
    viewOffsetY=5908.03)
a = mdb.models['Model-1'].rootAssembly
f1 = a.instances['P-47-1'].faces
faces1 = f1.getSequenceFromMask(mask=('[#1 ]', ), )
leaf = dgm.LeafFromGeometry(faceSeq=faces1)
session.viewports['Viewport: 1'].assemblyDisplay.displayGroup.remove(leaf=leaf)
session.viewports['Viewport: 1'].view.setValues(nearPlane=301650,
    farPlane=371596, width=27450.5, height=10888.2, viewOffsetX=-2938.56,
    viewOffsetY=5856.65)
session.viewports['Viewport: 1'].view.setValues(nearPlane=194549,
    farPlane=375871, width=17704.2, height=7022.33, cameraPosition=(134243,
    73455.6, 189866), cameraUpVector=(-0.411501, 0.798771, -0.438898),
    cameraTarget=(-210542, -34100.8, 11421.2), viewOffsetX=-1895.22,
    viewOffsetY=3777.24)
session.viewports['Viewport: 1'].view.setValues(nearPlane=196518,
    farPlane=374233, width=17883.4, height=7093.42, cameraPosition=(131355,
    90914.2, 184385), cameraUpVector=(-0.451089, 0.756392, -0.473698),
    cameraTarget=(-208975, -41185.8, 14053.7), viewOffsetX=-1914.4,
    viewOffsetY=3815.48)
session.viewports['Viewport: 1'].view.setValues(nearPlane=197474,
    farPlane=373277, width=6476.48, height=2568.88, viewOffsetX=-3198.01,
    viewOffsetY=4867.53)
session.viewports['Viewport: 1'].view.setValues(nearPlane=204716,
    farPlane=375455, width=6713.97, height=2663.08, cameraPosition=(117067,
    97287.6, 206092), cameraUpVector=(-0.45971, 0.755843, -0.466227),
    cameraTarget=(-202370, -43399, 4958.22), viewOffsetX=-3315.28,
    viewOffsetY=5046.02)
session.viewports['Viewport: 1'].view.setValues(nearPlane=204152,
    farPlane=376019, width=13472.1, height=5343.69, viewOffsetX=-4063.47,
    viewOffsetY=5551.94)
session.viewports['Viewport: 1'].view.setValues(nearPlane=184872,
    farPlane=365464, width=12199.8, height=4839.03, cameraPosition=(152994,
    87285.7, 126249), cameraUpVector=(-0.525869, 0.755781, -0.390202),
    cameraTarget=(-218157, -40239.3, 35296.1), viewOffsetX=-3679.71,
    viewOffsetY=5027.61)
session.viewports['Viewport: 1'].view.setValues(nearPlane=184622,
    farPlane=365714, width=17006.5, height=6745.6, viewOffsetX=2230.24,
    viewOffsetY=6099)
session.viewports['Viewport: 1'].view.setValues(nearPlane=200670,
    farPlane=371986, width=18484.7, height=7331.94, cameraPosition=(115782,
    109845, 192625), cameraUpVector=(-0.449506, 0.702025, -0.552363),
    cameraTarget=(-202656, -50400.4, 4990.28), viewOffsetX=2424.1,
    viewOffsetY=6629.13)
session.viewports['Viewport: 1'].view.setValues(nearPlane=199729,
    farPlane=372926, width=28926.7, height=11473.7, viewOffsetX=880.34,
    viewOffsetY=7246.25)
session.viewports['Viewport: 1'].view.setValues(nearPlane=208960,
    farPlane=373468, width=30263.5, height=12004, cameraPosition=(93161.2,
    119971, 217617), cameraUpVector=(-0.409189, 0.67991, -0.608511),
    cameraTarget=(-193846, -54396.7, -4893.38), viewOffsetX=921.024,
    viewOffsetY=7581.13)
session.viewports['Viewport: 1'].view.setValues(nearPlane=208237,
    farPlane=374191, width=38736.4, height=15364.7, viewOffsetX=-733.424,
    viewOffsetY=8121.72)
session.viewports['Viewport: 1'].view.setValues(nearPlane=257412,
    farPlane=365895, width=47883.9, height=18993.1, cameraPosition=(-29757.4,
    96525.2, 314605), cameraUpVector=(-0.0528259, 0.750999, -0.658187),
    cameraTarget=(-149973, -46068.2, -42471.1), viewOffsetX=-906.622,
    viewOffsetY=10039.7)
session.viewports['Viewport: 1'].view.setValues(nearPlane=256588,
    farPlane=366719, width=50153.6, height=19893.3, viewOffsetX=-24063.5,
    viewOffsetY=-859.892)
session.viewports['Viewport: 1'].view.setValues(nearPlane=281447,
    farPlane=424069, width=55012.5, height=21820.6, cameraPosition=(-357900,
    223726, 65201.5), cameraUpVector=(0.893723, 0.372223, -0.250418),
    cameraTarget=(-82190.4, -69770.2, 76686.5), viewOffsetX=-26394.8,
    viewOffsetY=-943.199)
session.viewports['Viewport: 1'].view.setValues(nearPlane=283190,
    farPlane=422326, width=31419.8, height=12462.6, viewOffsetX=-27315,
    viewOffsetY=-7473.65)
session.viewports['Viewport: 1'].view.setValues(nearPlane=273311,
    farPlane=425344, width=30323.8, height=12027.9, cameraPosition=(-366354,
    203626, -38067.5), cameraUpVector=(0.910843, 0.40824, -0.0608636),
    cameraTarget=(-91619.9, -61135.1, 91200.8), viewOffsetX=-26362.2,
    viewOffsetY=-7212.95)
session.viewports['Viewport: 1'].view.setValues(nearPlane=269059,
    farPlane=429595, width=83409.2, height=33084.1, viewOffsetX=-11903.4,
    viewOffsetY=-9248.15)
session.viewports['Viewport: 1'].view.setValues(nearPlane=258846,
    farPlane=387687, width=80242.9, height=31828.2, cameraPosition=(-269713,
    150094, -199822), cameraUpVector=(0.834425, 0.458693, 0.305509),
    cameraTarget=(-113989, -49253.1, 113704), viewOffsetX=-11451.6,
    viewOffsetY=-8897.09)
session.viewports['Viewport: 1'].view.setValues(nearPlane=264982,
    farPlane=381552, width=12562, height=4982.68, viewOffsetX=1107.68,
    viewOffsetY=-12477.5)
a = mdb.models['Model-1'].rootAssembly
f1 = a.instances['P-43-1'].faces
faces1 = f1.getSequenceFromMask(mask=('[#3f ]', ), )
leaf = dgm.LeafFromGeometry(faceSeq=faces1)
session.viewports['Viewport: 1'].assemblyDisplay.displayGroup.remove(leaf=leaf)
session.viewports['Viewport: 1'].view.setValues(nearPlane=265192,
    farPlane=381342, width=10250.8, height=4065.96, viewOffsetX=1486.32,
    viewOffsetY=-12248.5)
a = mdb.models['Model-1'].rootAssembly
s1 = a.instances['P-43-1'].faces
side1Faces1 = s1.getSequenceFromMask(mask=('[#3f ]', ), )
region1=regionToolset.Region(side1Faces=side1Faces1)
a = mdb.models['Model-1'].rootAssembly
s1 = a.instances['P-45-1'].edges
side1Edges1 = s1.getSequenceFromMask(mask=('[#aa ]', ), )
region2=regionToolset.Region(side1Edges=side1Edges1)
mdb.models['Model-1'].Tie(name='Constraint-25', main=region1,
    secondary=region2, positionToleranceMethod=COMPUTED, adjust=ON,
    tieRotations=ON, thickness=ON)
leaf = dgm.Leaf(leafType=DEFAULT_MODEL)
session.viewports['Viewport: 1'].assemblyDisplay.displayGroup.replace(
    leaf=leaf)
a = mdb.models['Model-1'].rootAssembly
f1 = a.instances['P-47-1'].faces
faces1 = f1.getSequenceFromMask(mask=('[#1 ]', ), )
leaf = dgm.LeafFromGeometry(faceSeq=faces1)
session.viewports['Viewport: 1'].assemblyDisplay.displayGroup.remove(leaf=leaf)
a = mdb.models['Model-1'].rootAssembly
f1 = a.instances['P-44-1'].faces
faces1 = f1.getSequenceFromMask(mask=('[#20 ]', ), )
leaf = dgm.LeafFromGeometry(faceSeq=faces1)
session.viewports['Viewport: 1'].assemblyDisplay.displayGroup.remove(leaf=leaf)
leaf = dgm.Leaf(leafType=DEFAULT_MODEL)
session.viewports['Viewport: 1'].assemblyDisplay.displayGroup.replace(
    leaf=leaf)
session.viewports['Viewport: 1'].view.setValues(nearPlane=264569,
    farPlane=382107, width=13633.1, height=5407.53, viewOffsetX=2307.08,
    viewOffsetY=-12257)
a = mdb.models['Model-1'].rootAssembly
f1 = a.instances['P-47-1'].faces
faces1 = f1.getSequenceFromMask(mask=('[#1 ]', ), )
leaf = dgm.LeafFromGeometry(faceSeq=faces1)
session.viewports['Viewport: 1'].assemblyDisplay.displayGroup.remove(leaf=leaf)
session.viewports['Viewport: 1'].view.setValues(nearPlane=263612,
    farPlane=383064, width=25058.3, height=9939.31, viewOffsetX=4763.04,
    viewOffsetY=-11749.7)
session.viewports['Viewport: 1'].view.setValues(nearPlane=294871,
    farPlane=428132, width=28029.7, height=11117.9, cameraPosition=(-355684,
    240052, 36565.9), cameraUpVector=(0.931617, 0.354483, 0.080199),
    cameraTarget=(-95972.7, -67451.9, 53263), viewOffsetX=5327.84,
    viewOffsetY=-13143)
session.viewports['Viewport: 1'].view.setValues(nearPlane=293067,
    farPlane=429935, width=47609.2, height=18884.1, viewOffsetX=3977.02,
    viewOffsetY=-10832.6)
session.viewports['Viewport: 1'].view.setValues(nearPlane=313662,
    farPlane=435459, width=50955, height=20211.2, cameraPosition=(-273494,
    207741, 273507), cameraUpVector=(0.739933, 0.43044, -0.516934),
    cameraTarget=(-111133, -61657.9, 21812), viewOffsetX=4256.5,
    viewOffsetY=-11593.8)
session.viewports['Viewport: 1'].view.setValues(nearPlane=308297,
    farPlane=440823, width=113508, height=45022.7, viewOffsetX=-7749.12,
    viewOffsetY=-18.7422)
session.viewports['Viewport: 1'].view.setValues(nearPlane=289719,
    farPlane=392146, width=106668, height=42309.6, cameraPosition=(-25428.9,
    278948, 199714), cameraUpVector=(-0.661978, 0.20066, -0.722164),
    cameraTarget=(-128920, -63020.8, 13612.1), viewOffsetX=-7282.16,
    viewOffsetY=-17.6128)
session.viewports['Viewport: 1'].view.setValues(nearPlane=280739,
    farPlane=401126, width=224886, height=89200.5, viewOffsetX=-20729.3,
    viewOffsetY=14726.3)
session.viewports['Viewport: 1'].view.setValues(nearPlane=196632,
    farPlane=393863, width=157512, height=62476.9, cameraPosition=(130774,
    169334, -62332.5), cameraUpVector=(-0.826892, 0.223551, -0.516017),
    cameraTarget=(-172221, -65680.6, 61154.3), viewOffsetX=-14519,
    viewOffsetY=10314.5)
session.viewports['Viewport: 1'].view.setValues(nearPlane=215576,
    farPlane=374920, width=7449.8, height=2954.95, viewOffsetX=-12499.9,
    viewOffsetY=17068.8)
a = mdb.models['Model-1'].rootAssembly
f1 = a.instances['P-47-1'].faces
faces1 = f1.getSequenceFromMask(mask=('[#2 ]', ), )
leaf = dgm.LeafFromGeometry(faceSeq=faces1)
session.viewports['Viewport: 1'].assemblyDisplay.displayGroup.remove(leaf=leaf)
session.viewports['Viewport: 1'].view.setValues(nearPlane=215548,
    farPlane=374948, width=8419.27, height=3339.49, viewOffsetX=-11999.8,
    viewOffsetY=17445.6)
leaf = dgm.Leaf(leafType=DEFAULT_MODEL)
session.viewports['Viewport: 1'].assemblyDisplay.displayGroup.replace(
    leaf=leaf)
a = mdb.models['Model-1'].rootAssembly
e1 = a.instances['P-35-1'].edges
edges1 = e1.getSequenceFromMask(mask=('[#1 ]', ), )
leaf = dgm.LeafFromGeometry(edgeSeq=edges1)
session.viewports['Viewport: 1'].assemblyDisplay.displayGroup.remove(leaf=leaf)
a = mdb.models['Model-1'].rootAssembly
f1 = a.instances['P-35-1'].faces
faces1 = f1.getSequenceFromMask(mask=('[#4 ]', ), )
leaf = dgm.LeafFromGeometry(faceSeq=faces1)
session.viewports['Viewport: 1'].assemblyDisplay.displayGroup.remove(leaf=leaf)
a = mdb.models['Model-1'].rootAssembly
f1 = a.instances['P-35-1'].faces
faces1 = f1.getSequenceFromMask(mask=('[#2 ]', ), )
leaf = dgm.LeafFromGeometry(faceSeq=faces1)
session.viewports['Viewport: 1'].assemblyDisplay.displayGroup.remove(leaf=leaf)
a = mdb.models['Model-1'].rootAssembly
f1 = a.instances['P-35-1'].faces
faces1 = f1.getSequenceFromMask(mask=('[#1 ]', ), )
leaf = dgm.LeafFromGeometry(faceSeq=faces1)
session.viewports['Viewport: 1'].assemblyDisplay.displayGroup.remove(leaf=leaf)
a = mdb.models['Model-1'].rootAssembly
f1 = a.instances['P-35-1'].faces
faces1 = f1.getSequenceFromMask(mask=('[#8 ]', ), )
leaf = dgm.LeafFromGeometry(faceSeq=faces1)
session.viewports['Viewport: 1'].assemblyDisplay.displayGroup.remove(leaf=leaf)
a = mdb.models['Model-1'].rootAssembly
f1 = a.instances['P-47-1'].faces
faces1 = f1.getSequenceFromMask(mask=('[#2 ]', ), )
leaf = dgm.LeafFromGeometry(faceSeq=faces1)
session.viewports['Viewport: 1'].assemblyDisplay.displayGroup.remove(leaf=leaf)
session.viewports['Viewport: 1'].view.setValues(nearPlane=214652,
    farPlane=375843, width=19101.3, height=7576.48, viewOffsetX=-8321.69,
    viewOffsetY=17738.4)
session.viewports['Viewport: 1'].view.setValues(nearPlane=238501,
    farPlane=366405, width=21223.5, height=8418.25, cameraPosition=(89584.7,
    234629, -2759.15), cameraUpVector=(-0.81393, 0.1246, -0.567444),
    cameraTarget=(-152493, -84823.9, 37676.8), viewOffsetX=-9246.25,
    viewOffsetY=19709.1)
session.viewports['Viewport: 1'].view.setValues(nearPlane=236477,
    farPlane=368429, width=44029.5, height=17464.2, viewOffsetX=-13238.2,
    viewOffsetY=22124.8)
session.viewports['Viewport: 1'].view.setValues(nearPlane=256388,
    farPlane=362734, width=47736.7, height=18934.7, cameraPosition=(29954.1,
    263521, 113663), cameraUpVector=(-0.667988, 0.152435, -0.728392),
    cameraTarget=(-130027, -89010.5, 2242.1), viewOffsetX=-14352.8,
    viewOffsetY=23987.7)
session.viewports['Viewport: 1'].view.setValues(nearPlane=256803,
    farPlane=362320, width=40893.9, height=16220.5, viewOffsetX=-38723.2,
    viewOffsetY=21460.4)
session.viewports['Viewport: 1'].view.setValues(nearPlane=291049,
    farPlane=360620, width=46347.4, height=18383.6, cameraPosition=(-43509.7,
    281497, 166584), cameraUpVector=(-0.607665, 0.108506, -0.786747),
    cameraTarget=(-102740, -76804.2, -7768.6), viewOffsetX=-43887.2,
    viewOffsetY=24322.2)
session.viewports['Viewport: 1'].view.setValues(nearPlane=294127,
    farPlane=357541, width=5382.32, height=2134.89, viewOffsetX=-56574.5,
    viewOffsetY=25320.1)
a = mdb.models['Model-1'].rootAssembly
f1 = a.instances['P-45-1'].faces
faces1 = f1.getSequenceFromMask(mask=('[#1 ]', ), )
leaf = dgm.LeafFromGeometry(faceSeq=faces1)
session.viewports['Viewport: 1'].assemblyDisplay.displayGroup.remove(leaf=leaf)
a = mdb.models['Model-1'].rootAssembly
f1 = a.instances['P-45-1'].faces
faces1 = f1.getSequenceFromMask(mask=('[#2 ]', ), )
leaf = dgm.LeafFromGeometry(faceSeq=faces1)
session.viewports['Viewport: 1'].assemblyDisplay.displayGroup.remove(leaf=leaf)
session.viewports['Viewport: 1'].view.setValues(nearPlane=293414,
    farPlane=358254, width=14352.1, height=5692.74, viewOffsetX=-56524.7,
    viewOffsetY=25240.6)
session.viewports['Viewport: 1'].view.setValues(nearPlane=249878,
    farPlane=347078, width=12222.6, height=4848.06, cameraPosition=(44326.1,
    258574, 38619), cameraUpVector=(-0.68505, -0.00066632, -0.728495),
    cameraTarget=(-131820, -103257, 20258), viewOffsetX=-48137.6,
    viewOffsetY=21495.5)
session.viewports['Viewport: 1'].view.setValues(nearPlane=250142,
    farPlane=346813, width=11787, height=4675.29, viewOffsetX=-46678.4,
    viewOffsetY=21625)
session.viewports['Viewport: 1'].view.setValues(nearPlane=278469,
    farPlane=349955, width=13121.8, height=5204.73, cameraPosition=(-14034.5,
    284897, 109571), cameraUpVector=(-0.628784, 0.0288581, -0.777045),
    cameraTarget=(-104604, -90875.5, -3912.31), viewOffsetX=-51964.4,
    viewOffsetY=24073.9)
session.viewports['Viewport: 1'].view.setValues(nearPlane=277117,
    farPlane=351307, width=28410.6, height=11269, viewOffsetX=-53748.8,
    viewOffsetY=24193.4)
session.viewports['Viewport: 1'].view.setValues(nearPlane=300995,
    farPlane=352992, width=30858.7, height=12240, cameraPosition=(-66609.3,
    279565, 178228), cameraUpVector=(-0.524423, 0.105623, -0.844881),
    cameraTarget=(-86516.2, -74639.1, -12637.9), viewOffsetX=-58380.2,
    viewOffsetY=26278.1)
session.viewports['Viewport: 1'].view.setValues(nearPlane=302677,
    farPlane=351310, width=9515.22, height=3774.2, viewOffsetX=-68356.6,
    viewOffsetY=25050.5)
a = mdb.models['Model-1'].rootAssembly
f1 = a.instances['P-43-1'].faces
faces1 = f1.getSequenceFromMask(mask=('[#36 ]', ), )
leaf = dgm.LeafFromGeometry(faceSeq=faces1)
session.viewports['Viewport: 1'].assemblyDisplay.displayGroup.remove(leaf=leaf)
session.viewports['Viewport: 1'].view.setValues(nearPlane=301999,
    farPlane=351988, width=17605.2, height=6983.08, viewOffsetX=-68924.9,
    viewOffsetY=25231.2)
session.viewports['Viewport: 1'].view.setValues(nearPlane=202548,
    farPlane=344635, width=11807.7, height=4683.49, cameraPosition=(105410,
    166544, -62247.8), cameraUpVector=(-0.70098, -0.11551, -0.703765),
    cameraTarget=(-152175, -121812, 50834), viewOffsetX=-46227.4,
    viewOffsetY=16922.4)
session.viewports['Viewport: 1'].view.setValues(nearPlane=203476,
    farPlane=343708, width=7267.84, height=2882.77, viewOffsetX=-46736.2,
    viewOffsetY=16714)
a = mdb.models['Model-1'].rootAssembly
s1 = a.instances['P-43-1'].faces
side1Faces1 = s1.getSequenceFromMask(mask=('[#36 ]', ), )
region1=regionToolset.Region(side1Faces=side1Faces1)
a = mdb.models['Model-1'].rootAssembly
s1 = a.instances['P-43-1'].edges
side1Edges1 = s1.getSequenceFromMask(mask=('[#1004 ]', ), )
s2 = a.instances['P-44-1'].edges
side1Edges2 = s2.getSequenceFromMask(mask=('[#c03aa ]', ), )
region2=regionToolset.Region(side1Edges=side1Edges1+side1Edges2)
mdb.models['Model-1'].Tie(name='Constraint-26', main=region1,
    secondary=region2, positionToleranceMethod=COMPUTED, adjust=ON,
    tieRotations=ON, thickness=ON)
leaf = dgm.Leaf(leafType=DEFAULT_MODEL)
session.viewports['Viewport: 1'].assemblyDisplay.displayGroup.replace(
    leaf=leaf)
session.viewports['Viewport: 1'].view.setValues(nearPlane=202465,
    farPlane=344718, width=19330.5, height=7667.42, viewOffsetX=-45685.3,
    viewOffsetY=15836.6)
session.viewports['Viewport: 1'].view.setValues(nearPlane=205611,
    farPlane=344002, width=19630.9, height=7786.57, cameraPosition=(87450.5,
    159950, -106234), cameraUpVector=(-0.786112, -0.196239, -0.586104),
    cameraTarget=(-144481, -118898, 69089.7), viewOffsetX=-46395.2,
    viewOffsetY=16082.7)
session.viewports['Viewport: 1'].view.setValues(nearPlane=198008,
    farPlane=351605, width=110713, height=43914.1, viewOffsetX=-46668,
    viewOffsetY=27586.8)
session.viewports['Viewport: 1'].view.setValues(nearPlane=273291,
    farPlane=326661, width=152806, height=60610.3, cameraPosition=(-105871,
    278529, -99360.7), cameraUpVector=(-0.868387, -0.222525, 0.443156),
    cameraTarget=(-129684, -119636, -42931.7), viewOffsetX=-64411.3,
    viewOffsetY=38075.3)
session.viewports['Viewport: 1'].view.setValues(nearPlane=281853,
    farPlane=318100, width=12081.9, height=4792.27, viewOffsetX=-66377.5,
    viewOffsetY=68773.3)
a = mdb.models['Model-1'].rootAssembly
f1 = a.instances['P-47-1'].faces
faces1 = f1.getSequenceFromMask(mask=('[#1 ]', ), )
leaf = dgm.LeafFromGeometry(faceSeq=faces1)
session.viewports['Viewport: 1'].assemblyDisplay.displayGroup.remove(leaf=leaf)
session.viewports['Viewport: 1'].view.setValues(nearPlane=280576,
    farPlane=319376, width=28344.5, height=11242.8, viewOffsetX=-63321.1,
    viewOffsetY=68195.7)
session.viewports['Viewport: 1'].view.setValues(nearPlane=285625,
    farPlane=354782, width=28854.6, height=11445.1, cameraPosition=(-172420,
    309253, 82295.2), cameraUpVector=(-0.781793, -0.59869, 0.174269),
    cameraTarget=(-108978, -48525.6, -91648.9), viewOffsetX=-64460.7,
    viewOffsetY=69423)
session.viewports['Viewport: 1'].view.setValues(nearPlane=286485,
    farPlane=353924, width=17763.5, height=7045.88, viewOffsetX=-70329.4,
    viewOffsetY=73759.3)
session.viewports['Viewport: 1'].view.setValues(nearPlane=286544,
    farPlane=364066, width=17767.3, height=7047.35, cameraPosition=(-187883,
    300671, 121837), cameraUpVector=(-0.748668, -0.653426, 0.111937),
    cameraTarget=(-110351, -30621.9, -93849.7), viewOffsetX=-70344.1,
    viewOffsetY=73774.7)
session.viewports['Viewport: 1'].view.setValues(nearPlane=286824,
    farPlane=363786, width=15158, height=6012.39, viewOffsetX=-69571.3,
    viewOffsetY=74491)
session.viewports['Viewport: 1'].view.setValues(nearPlane=286269,
    farPlane=355463, width=15128.6, height=6000.74, cameraPosition=(-183712,
    311655, 49030.6), cameraUpVector=(-0.765254, -0.605078, 0.219697),
    cameraTarget=(-106197, -58604.8, -89484.9), viewOffsetX=-69436.5,
    viewOffsetY=74346.7)
session.viewports['Viewport: 1'].view.setValues(nearPlane=284847,
    farPlane=356886, width=32752.1, height=12991.1, viewOffsetX=-71324.5,
    viewOffsetY=75761)
session.viewports['Viewport: 1'].view.setValues(nearPlane=273096,
    farPlane=367921, width=31401, height=12455.1, cameraPosition=(-203370,
    225999, -184579), cameraUpVector=(-0.762003, -0.450621, 0.465073),
    cameraTarget=(-77516, -123162, -27943), viewOffsetX=-68382.1,
    viewOffsetY=72635.6)
session.viewports['Viewport: 1'].view.setValues(nearPlane=274633,
    farPlane=366384, width=14539, height=5766.86, viewOffsetX=-76110.4,
    viewOffsetY=73953.2)
a = mdb.models['Model-1'].rootAssembly
s1 = a.instances['P-43-1'].faces
side1Faces1 = s1.getSequenceFromMask(mask=('[#3f ]', ), )
region1=regionToolset.Region(side1Faces=side1Faces1)
mdb.models['Model-1'].constraints['Constraint-26'].setValues(main=region1)
session.viewports['Viewport: 1'].view.setValues(nearPlane=273967,
    farPlane=367050, width=23712.7, height=9405.59, viewOffsetX=-79000.3,
    viewOffsetY=73979.9)
leaf = dgm.Leaf(leafType=DEFAULT_MODEL)
session.viewports['Viewport: 1'].assemblyDisplay.displayGroup.replace(
    leaf=leaf)
session.viewports['Viewport: 1'].view.setValues(nearPlane=271836,
    farPlane=369182, width=49142.9, height=19492.5, viewOffsetX=-75649.7,
    viewOffsetY=74996.4)
session.viewports['Viewport: 1'].view.setValues(nearPlane=299666,
    farPlane=358734, width=54174.2, height=21488.1, cameraPosition=(-58406.3,
    216511, 269028), cameraUpVector=(-0.925316, -0.0410365, -0.376971),
    cameraTarget=(-58965.3, -15056.9, -60613.8), viewOffsetX=-83394.7,
    viewOffsetY=82674.6)
session.viewports['Viewport: 1'].view.setValues(nearPlane=299228,
    farPlane=359174, width=54094.9, height=21456.7, cameraPosition=(-58786,
    216968, 268707), cameraUpVector=(-0.926262, -0.0450005, -0.374185),
    cameraTarget=(-59345, -14599.4, -60934.5), viewOffsetX=-83272.7,
    viewOffsetY=82553.6)
session.viewports['Viewport: 1'].view.setValues(nearPlane=291291,
    farPlane=340381, width=52660.1, height=20887.6, cameraPosition=(-67957.8,
    304836, 87850.9), cameraUpVector=(-0.889594, -0.271125, -0.367577),
    cameraTarget=(-49808.3, -76783.2, -39916.3), viewOffsetX=-81064,
    viewOffsetY=80364)
session.viewports['Viewport: 1'].view.setValues(nearPlane=291696,
    farPlane=333649, width=52733.4, height=20916.7, cameraPosition=(-69520.1,
    308124, 30874.7), cameraUpVector=(-0.887644, -0.335444, -0.315541),
    cameraTarget=(-49382.9, -89850.2, -28266.5), viewOffsetX=-81176.8,
    viewOffsetY=80475.8)
session.viewports['Viewport: 1'].view.setValues(nearPlane=294239,
    farPlane=331104, width=22571.2, height=8952.81, viewOffsetX=-83590,
    viewOffsetY=80998.1)
session.viewports['Viewport: 1'].view.setValues(nearPlane=294616,
    farPlane=330728, width=18427.5, height=7309.22, viewOffsetX=-83018.4,
    viewOffsetY=80969.4)
a = mdb.models['Model-1'].rootAssembly
f1 = a.instances['P-35-1'].faces
faces1 = f1.getSequenceFromMask(mask=('[#8 ]', ), )
leaf = dgm.LeafFromGeometry(faceSeq=faces1)
session.viewports['Viewport: 1'].assemblyDisplay.displayGroup.remove(leaf=leaf)
a = mdb.models['Model-1'].rootAssembly
f1 = a.instances['P-35-1'].faces
faces1 = f1.getSequenceFromMask(mask=('[#4 ]', ), )
leaf = dgm.LeafFromGeometry(faceSeq=faces1)
session.viewports['Viewport: 1'].assemblyDisplay.displayGroup.remove(leaf=leaf)
session.viewports['Viewport: 1'].view.setValues(width=17694.4, height=7018.44,
    viewOffsetX=-83156.1, viewOffsetY=81004.3)
a = mdb.models['Model-1'].rootAssembly
f1 = a.instances['P-35-1'].faces
faces1 = f1.getSequenceFromMask(mask=('[#2 ]', ), )
leaf = dgm.LeafFromGeometry(faceSeq=faces1)
session.viewports['Viewport: 1'].assemblyDisplay.displayGroup.remove(leaf=leaf)
a = mdb.models['Model-1'].rootAssembly
f1 = a.instances['P-35-1'].faces
faces1 = f1.getSequenceFromMask(mask=('[#1 ]', ), )
leaf = dgm.LeafFromGeometry(faceSeq=faces1)
session.viewports['Viewport: 1'].assemblyDisplay.displayGroup.remove(leaf=leaf)
session.viewports['Viewport: 1'].view.setValues(nearPlane=293873,
    farPlane=331471, width=28849.7, height=11443.2, viewOffsetX=-80958.4,
    viewOffsetY=82656.6)
session.viewports['Viewport: 1'].view.setValues(nearPlane=232428,
    farPlane=337856, width=22817.6, height=9050.57, cameraPosition=(57651.1,
    235742, 84868.8), cameraUpVector=(-0.966451, 0.138504, -0.216307),
    cameraTarget=(-97369.3, -105837, -62030.3), viewOffsetX=-64031.2,
    viewOffsetY=65374.3)
session.viewports['Viewport: 1'].view.setValues(nearPlane=234095,
    farPlane=336189, width=9361.39, height=3713.18, viewOffsetX=-64340.1,
    viewOffsetY=66956.6)
session.viewports['Viewport: 1'].view.setValues(nearPlane=244079,
    farPlane=334061, width=9760.68, height=3871.56, cameraPosition=(41650,
    249123, 83909.6), cameraUpVector=(-0.964437, 0.0704312, -0.254757),
    cameraTarget=(-86501, -106141, -56275.1), viewOffsetX=-67084.4,
    viewOffsetY=69812.5)
session.viewports['Viewport: 1'].view.setValues(nearPlane=244503,
    farPlane=333638, width=4329.26, height=1717.19, viewOffsetX=-67442.8,
    viewOffsetY=71506.7)
a = mdb.models['Model-1'].rootAssembly
f1 = a.instances['P-45-1'].faces
faces1 = f1.getSequenceFromMask(mask=('[#1 ]', ), )
leaf = dgm.LeafFromGeometry(faceSeq=faces1)
session.viewports['Viewport: 1'].assemblyDisplay.displayGroup.remove(leaf=leaf)
a = mdb.models['Model-1'].rootAssembly
f1 = a.instances['P-45-1'].faces
faces1 = f1.getSequenceFromMask(mask=('[#2 ]', ), )
leaf = dgm.LeafFromGeometry(faceSeq=faces1)
session.viewports['Viewport: 1'].assemblyDisplay.displayGroup.remove(leaf=leaf)
session.viewports['Viewport: 1'].view.setValues(nearPlane=243186,
    farPlane=334956, width=20418.6, height=8099.01, viewOffsetX=-66467.4,
    viewOffsetY=71249.5)
session.viewports['Viewport: 1'].view.setValues(nearPlane=282059,
    farPlane=319749, width=23682.6, height=9393.65, cameraPosition=(-33988.4,
    292976, 7613.68), cameraUpVector=(-0.954724, -0.253178, -0.156213),
    cameraTarget=(-61677.9, -106642, -35113.1), viewOffsetX=-77092.3,
    viewOffsetY=82638.8)
session.viewports['Viewport: 1'].view.setValues(nearPlane=276907,
    farPlane=324901, width=82703.8, height=32804.3, viewOffsetX=-76637.1,
    viewOffsetY=89562.2)
session.viewports['Viewport: 1'].view.setValues(nearPlane=275215,
    farPlane=380895, width=82198.4, height=32603.8, cameraPosition=(-168364,
    301800, -66335.6), cameraUpVector=(-0.70797, -0.691461, -0.143738),
    cameraTarget=(-15003.8, -64030.9, 3917.49), viewOffsetX=-76168.8,
    viewOffsetY=89014.9)
session.viewports['Viewport: 1'].view.setValues(nearPlane=280531,
    farPlane=375579, width=20911.9, height=8294.67, viewOffsetX=-73369.1,
    viewOffsetY=91013.4)
session.viewports['Viewport: 1'].view.setValues(nearPlane=283782,
    farPlane=356655, width=21154.2, height=8390.79, cameraPosition=(-126589,
    307513, -42729.6), cameraUpVector=(-0.78092, -0.591548, -0.200586),
    cameraTarget=(-18613.9, -77800.6, 3765.22), viewOffsetX=-74219.3,
    viewOffsetY=92068)
session.viewports['Viewport: 1'].view.setValues(nearPlane=284097,
    farPlane=356339, width=16605.9, height=6586.68, viewOffsetX=-74215.9,
    viewOffsetY=95096.7)
session.viewports['Viewport: 1'].view.setValues(nearPlane=292054,
    farPlane=313807, width=17070.9, height=6771.15, cameraPosition=(-36424.4,
    295298, 8960.78), cameraUpVector=(-0.906219, -0.32251, -0.273411),
    cameraTarget=(-36687.9, -107254, -6470.82), viewOffsetX=-76294.4,
    viewOffsetY=97760)
session.viewports['Viewport: 1'].view.setValues(nearPlane=292545,
    farPlane=313315, width=10531.9, height=4177.44, viewOffsetX=-75171.4,
    viewOffsetY=102070)
session.viewports['Viewport: 1'].view.setValues(nearPlane=268434,
    farPlane=347816, width=9663.83, height=3833.14, cameraPosition=(10658.9,
    145307, 279805), cameraUpVector=(-0.916828, 0.221819, -0.331998),
    cameraTarget=(-49064.5, -30928.8, -77490.4), viewOffsetX=-68975.8,
    viewOffsetY=93657.8)
session.viewports['Viewport: 1'].view.setValues(nearPlane=218883,
    farPlane=349636, width=7879.96, height=3125.57, cameraPosition=(96136.7,
    83612.1, 230416), cameraUpVector=(-0.926639, 0.375952, -0.000564009),
    cameraTarget=(-92592, -24884.5, -108547), viewOffsetX=-56243.4,
    viewOffsetY=76369.3)
session.viewports['Viewport: 1'].view.setValues(nearPlane=217746,
    farPlane=350774, width=23642.5, height=9377.77, viewOffsetX=-53491.1,
    viewOffsetY=75997.5)
session.viewports['Viewport: 1'].view.setValues(nearPlane=204180,
    farPlane=339208, width=22169.6, height=8793.52, cameraPosition=(115108,
    154207, 125370), cameraUpVector=(-0.888647, 0.377477, -0.260419),
    cameraTarget=(-106812, -133034, -49358.4), viewOffsetX=-50158.6,
    viewOffsetY=71262.7)
session.viewports['Viewport: 1'].view.setValues(nearPlane=190451,
    farPlane=305669, width=20678.9, height=8202.25, cameraPosition=(24422.5,
    126564, -165069), cameraUpVector=(-0.878221, 0.305189, 0.368222),
    cameraTarget=(-139921, -169557, 53081.4), viewOffsetX=-46786,
    viewOffsetY=66471)
session.viewports['Viewport: 1'].view.setValues(nearPlane=190712,
    farPlane=305408, width=18416.2, height=7304.77, viewOffsetX=-25457.2,
    viewOffsetY=71050)
session.viewports['Viewport: 1'].view.setValues(nearPlane=231969,
    farPlane=294754, width=22400.2, height=8885.02, cameraPosition=(-84638.7,
    46105.1, -244868), cameraUpVector=(-0.654494, 0.466662, 0.594865),
    cameraTarget=(-102803, -143861, 109912), viewOffsetX=-30964.4,
    viewOffsetY=86420.4)
session.viewports['Viewport: 1'].view.setValues(nearPlane=226210,
    farPlane=300513, width=87826.2, height=34836.1, viewOffsetX=-23588.2,
    viewOffsetY=79827.8)
session.viewports['Viewport: 1'].view.setValues(nearPlane=222309,
    farPlane=339287, width=86311.4, height=34235.2, cameraPosition=(-231106,
    35340.4, -236404), cameraUpVector=(-0.0269127, 0.643592, 0.764896),
    cameraTarget=(-111594, -151013, 100160), viewOffsetX=-23181.4,
    viewOffsetY=78451)
session.viewports['Viewport: 1'].view.setValues(nearPlane=236943,
    farPlane=335890, width=91993, height=36488.8, cameraPosition=(-278682,
    171786, -150813), cameraUpVector=(0.572573, 0.26854, 0.774626),
    cameraTarget=(-178317, -155358, 61766.5), viewOffsetX=-24707.4,
    viewOffsetY=83615.2)
session.viewports['Viewport: 1'].view.setValues(nearPlane=234675,
    farPlane=338158, width=116805, height=46330.4, viewOffsetX=-24854.5,
    viewOffsetY=81709.9)
session.viewports['Viewport: 1'].view.setValues(nearPlane=246547,
    farPlane=313662, width=122714, height=48674.1, cameraPosition=(-248936,
    235926, -94101.7), cameraUpVector=(0.858259, -0.0678842, 0.508708),
    cameraTarget=(-226905, -124439, 84611.4), viewOffsetX=-26111.8,
    viewOffsetY=85843.5)
session.viewports['Viewport: 1'].view.setValues(nearPlane=247955,
    farPlane=312254, width=96772.1, height=38384.5, viewOffsetX=-18019.8,
    viewOffsetY=64408)
session.viewports['Viewport: 1'].view.setValues(nearPlane=204993,
    farPlane=307452, width=80004.6, height=31733.7, cameraPosition=(-138356,
    270112, -49653.1), cameraUpVector=(0.68852, -0.455899, 0.564),
    cameraTarget=(-269789, -96787.1, 52314.5), viewOffsetX=-14897.5,
    viewOffsetY=53248.2)
session.viewports['Viewport: 1'].view.setValues(nearPlane=211897,
    farPlane=300547, width=18357, height=7281.28, viewOffsetX=-14768,
    viewOffsetY=53585.9)
session.viewports['Viewport: 1'].view.setValues(nearPlane=264643,
    farPlane=308702, width=22926.5, height=9093.74, cameraPosition=(-244606,
    260601, -35916.7), cameraUpVector=(0.869326, -0.167335, 0.46505),
    cameraTarget=(-214532, -130491, 55894.7), viewOffsetX=-18444.1,
    viewOffsetY=66924.5)
session.viewports['Viewport: 1'].view.setValues(nearPlane=259219,
    farPlane=314126, width=83790.4, height=33235.3, viewOffsetX=-20862.4,
    viewOffsetY=64941.9)
session.viewports['Viewport: 1'].view.setValues(nearPlane=213222,
    farPlane=311829, width=68922.1, height=27337.8, cameraPosition=(-149924,
    71887.6, -246242), cameraUpVector=(0.395814, 0.556126, 0.730791),
    cameraTarget=(-225003, -101041, 109771), viewOffsetX=-17160.5,
    viewOffsetY=53418.2)
session.viewports['Viewport: 1'].view.setValues(nearPlane=196817,
    farPlane=311406, width=63619.4, height=25234.5, cameraPosition=(-99435.1,
    114459, -225024), cameraUpVector=(0.0968654, 0.473456, 0.875475),
    cameraTarget=(-226898, -125623, 72298.1), viewOffsetX=-15840.2,
    viewOffsetY=49308.3)
session.viewports['Viewport: 1'].view.setValues(nearPlane=201960,
    farPlane=306264, width=9583.83, height=3801.41, viewOffsetX=-9312.11,
    viewOffsetY=52319.3)
leaf = dgm.Leaf(leafType=DEFAULT_MODEL)
session.viewports['Viewport: 1'].assemblyDisplay.displayGroup.replace(
    leaf=leaf)
a = mdb.models['Model-1'].rootAssembly
f1 = a.instances['P-44-1'].faces
faces1 = f1.getSequenceFromMask(mask=('[#3d ]', ), )
leaf = dgm.LeafFromGeometry(faceSeq=faces1)
session.viewports['Viewport: 1'].assemblyDisplay.displayGroup.remove(leaf=leaf)
session.viewports['Viewport: 1'].view.setValues(nearPlane=201609,
    farPlane=306614, width=14575.8, height=5781.48, viewOffsetX=-8904.41,
    viewOffsetY=52420.2)
session.viewports['Viewport: 1'].view.setValues(nearPlane=231433,
    farPlane=303652, width=16732, height=6636.74, cameraPosition=(-141769,
    137929, -219135), cameraUpVector=(0.0749054, 0.427349, 0.900979),
    cameraTarget=(-193808, -141206, 66630.9), viewOffsetX=-10221.6,
    viewOffsetY=60174.7)
session.viewports['Viewport: 1'].view.setValues(nearPlane=231692,
    farPlane=303393, width=12083.9, height=4793.04, viewOffsetX=-6509.9,
    viewOffsetY=61220.3)
leaf = dgm.Leaf(leafType=DEFAULT_MODEL)
session.viewports['Viewport: 1'].assemblyDisplay.displayGroup.replace(
    leaf=leaf)
i1 = mdb.models['Model-1'].rootAssembly.allInstances['P-44-1']
i2 = mdb.models['Model-1'].rootAssembly.allInstances['P-45-1']
leaf = dgm.LeafFromInstance(instances=(i1, i2, ))
session.viewports['Viewport: 1'].assemblyDisplay.displayGroup.replace(
    leaf=leaf)
session.viewports['Viewport: 1'].view.setValues(nearPlane=288438,
    farPlane=294701, width=16351.6, height=6485.82, viewOffsetX=-6815.32,
    viewOffsetY=77378.2)
session.viewports['Viewport: 1'].view.setValues(nearPlane=286987,
    farPlane=293430, width=16269.3, height=6453.19, cameraPosition=(119941,
    94188.1, 56642.4), cameraUpVector=(-0.739379, 0.28353, 0.61068),
    cameraTarget=(-220474, -93953.7, -48271.6), viewOffsetX=-6781.04,
    viewOffsetY=76989)
session.viewports['Viewport: 1'].view.setValues(nearPlane=287388,
    farPlane=293030, width=12242.6, height=4856.02, viewOffsetX=-6725.85,
    viewOffsetY=76946.1)
session.viewports['Viewport: 1'].view.setValues(nearPlane=288107,
    farPlane=293836, width=12273.3, height=4868.16, cameraPosition=(-48876.5,
    237260, -85143.1), cameraUpVector=(-0.517232, -0.00924158, 0.855796),
    cameraTarget=(-165005, -139528, -2488.56), viewOffsetX=-6742.67,
    viewOffsetY=77138.6)
session.viewports['Viewport: 1'].view.setValues(nearPlane=288185,
    farPlane=293759, width=11826.6, height=4690.99, viewOffsetX=-6818.61,
    viewOffsetY=76786.9)
session.viewports['Viewport: 1'].view.setValues(nearPlane=288476,
    farPlane=293918, width=11838.5, height=4695.73, cameraPosition=(-157064,
    242846, -119185), cameraUpVector=(-0.378853, -0.074615, 0.922444),
    cameraTarget=(-125779, -137971, 8432.92), viewOffsetX=-6825.5,
    viewOffsetY=76864.4)
session.viewports['Viewport: 1'].view.setValues(nearPlane=288730,
    farPlane=293664, width=9290.98, height=3685.25, viewOffsetX=-6832.36,
    viewOffsetY=76572.3)
session.viewports['Viewport: 1'].view.setValues(nearPlane=288129,
    farPlane=293502, width=9271.66, height=3677.59, cameraPosition=(57746.9,
    194015, 17815.9), cameraUpVector=(-0.570176, -0.120559, 0.812628),
    cameraTarget=(-212280, -97233.3, -49611.3), viewOffsetX=-6818.15,
    viewOffsetY=76413)
session.viewports['Viewport: 1'].view.setValues(nearPlane=288332,
    farPlane=293300, width=6693.19, height=2654.84, viewOffsetX=-6682.75,
    viewOffsetY=76459.7)
a = mdb.models['Model-1'].rootAssembly
s1 = a.instances['P-44-1'].faces
side1Faces1 = s1.getSequenceFromMask(mask=('[#3f ]', ), )
region1=regionToolset.Region(side1Faces=side1Faces1)
a = mdb.models['Model-1'].rootAssembly
s1 = a.instances['P-45-1'].edges
side1Edges1 = s1.getSequenceFromMask(mask=('[#145 ]', ), )
region2=regionToolset.Region(side1Edges=side1Edges1)
mdb.models['Model-1'].Tie(name='Constraint-27', main=region1,
    secondary=region2, positionToleranceMethod=COMPUTED, adjust=ON,
    tieRotations=ON, thickness=ON)
session.viewports['Viewport: 1'].view.setValues(nearPlane=288280,
    farPlane=293351, width=7878.99, height=3125.19, viewOffsetX=-6831.88,
    viewOffsetY=76559.1)
leaf = dgm.Leaf(leafType=DEFAULT_MODEL)
session.viewports['Viewport: 1'].assemblyDisplay.displayGroup.replace(
    leaf=leaf)
session.viewports['Viewport: 1'].view.setValues(nearPlane=172836,
    farPlane=313464, width=9849.36, height=3906.73, viewOffsetX=-3821.05,
    viewOffsetY=45421.4)
a = mdb.models['Model-1'].rootAssembly
f1 = a.instances['P-1-1'].faces
faces1 = f1.getSequenceFromMask(mask=('[#3 ]', ), )
leaf = dgm.LeafFromGeometry(faceSeq=faces1)
session.viewports['Viewport: 1'].assemblyDisplay.displayGroup.remove(leaf=leaf)
session.viewports['Viewport: 1'].view.setValues(nearPlane=172516,
    farPlane=313765, width=14195.9, height=5630.78, viewOffsetX=-3201.08,
    viewOffsetY=45698.5)
session.viewports['Viewport: 1'].view.setValues(nearPlane=175924,
    farPlane=308527, width=14476.4, height=5742.03, cameraPosition=(45422.1,
    187437, -45561.8), cameraUpVector=(-0.510182, 0.103989, 0.853757),
    cameraTarget=(-210067, -121159, -3363.71), viewOffsetX=-3264.32,
    viewOffsetY=46601.4)
session.viewports['Viewport: 1'].view.setValues(nearPlane=174529,
    farPlane=309922, width=28998, height=11502, viewOffsetX=4316.58,
    viewOffsetY=36702.9)
session.viewports['Viewport: 1'].view.setValues(nearPlane=155003,
    farPlane=314081, width=25753.6, height=10215.1, cameraPosition=(58488.6,
    131150, -100991), cameraUpVector=(-0.44024, 0.4525, 0.775521),
    cameraTarget=(-227646, -108982, 49842), viewOffsetX=3833.64,
    viewOffsetY=32596.5)
session.viewports['Viewport: 1'].view.setValues(nearPlane=153733,
    farPlane=315350, width=45313.1, height=17973.4, viewOffsetX=5517.32,
    viewOffsetY=31056.3)
session.viewports['Viewport: 1'].view.setValues(nearPlane=154135,
    farPlane=296048, width=45431.5, height=18020.3, cameraPosition=(-9785.5,
    -18534.2, -191033), cameraUpVector=(0.111868, 0.879099, 0.463325),
    cameraTarget=(-218940, -20626.2, 153259), viewOffsetX=5531.74,
    viewOffsetY=31137.5)
session.viewports['Viewport: 1'].view.setValues(nearPlane=157516,
    farPlane=292667, width=6303.47, height=2500.26, viewOffsetX=7302.89,
    viewOffsetY=2971.27)
i1 = mdb.models['Model-1'].rootAssembly.allInstances['P-2-1']
leaf = dgm.LeafFromInstance(instances=(i1, ))
session.viewports['Viewport: 1'].assemblyDisplay.displayGroup.replace(
    leaf=leaf)
session.viewports['Viewport: 1'].view.setValues(nearPlane=262643,
    farPlane=293316, width=14595.1, height=5789.11, viewOffsetX=12526.2,
    viewOffsetY=5040.31)
session.viewports['Viewport: 1'].assemblyDisplay.displayGroup.undoLast()
i1 = mdb.models['Model-1'].rootAssembly.allInstances['P-2-1']
leaf = dgm.LeafFromInstance(instances=(i1, ))
session.viewports['Viewport: 1'].assemblyDisplay.displayGroup.remove(leaf=leaf)
session.viewports['Viewport: 1'].view.setValues(nearPlane=157919,
    farPlane=291376, width=1866.78, height=740.454, viewOffsetX=5841.01,
    viewOffsetY=2579.88)
a = mdb.models['Model-1'].rootAssembly
s1 = a.instances['P-1-1'].faces
side2Faces1 = s1.getSequenceFromMask(mask=('[#3 ]', ), )
region1=regionToolset.Region(side2Faces=side2Faces1)
a = mdb.models['Model-1'].rootAssembly
s1 = a.instances['P-48-1'].edges
side1Edges1 = s1.getSequenceFromMask(mask=('[#4 ]', ), )
s2 = a.instances['P-44-1'].edges
side1Edges2 = s2.getSequenceFromMask(mask=('[#840 ]', ), )
region2=regionToolset.Region(side1Edges=side1Edges1+side1Edges2)
mdb.models['Model-1'].Tie(name='Constraint-28', main=region1,
    secondary=region2, positionToleranceMethod=COMPUTED, adjust=ON,
    tieRotations=ON, thickness=ON)
session.viewports['Viewport: 1'].view.setValues(nearPlane=157871,
    farPlane=291424, width=2600.89, height=1031.64, viewOffsetX=5956.62,
    viewOffsetY=2530.67)
leaf = dgm.Leaf(leafType=DEFAULT_MODEL)
session.viewports['Viewport: 1'].assemblyDisplay.displayGroup.replace(
    leaf=leaf)
session.viewports['Viewport: 1'].view.setValues(nearPlane=157254,
    farPlane=293157, width=9964.86, height=3952.54, viewOffsetX=7246.48,
    viewOffsetY=2264.52)
session.viewports['Viewport: 1'].view.setValues(nearPlane=169701,
    farPlane=291735, width=10753.6, height=4265.4, cameraPosition=(-31862.9,
    4991.05, -203155), cameraUpVector=(0.101826, 0.849044, 0.518417),
    cameraTarget=(-199903, -38657.8, 160361), viewOffsetX=7820.06,
    viewOffsetY=2443.76)
session.viewports['Viewport: 1'].view.setValues(nearPlane=168618,
    farPlane=292817, width=23287.9, height=9237.12, viewOffsetX=9086.32,
    viewOffsetY=3716.21)
session.viewports['Viewport: 1'].view.setValues(nearPlane=202690,
    farPlane=286089, width=27993.6, height=11103.6, cameraPosition=(-90597.3,
    37753.1, -219231), cameraUpVector=(0.161453, 0.797811, 0.580888),
    cameraTarget=(-153897, -61613.9, 166004), viewOffsetX=10922.4,
    viewOffsetY=4467.13)
session.viewports['Viewport: 1'].view.setValues(nearPlane=195639,
    farPlane=293141, width=108258, height=42940.5, viewOffsetX=22546.5,
    viewOffsetY=5648.18)
session.viewports['Viewport: 1'].view.setValues(nearPlane=211419,
    farPlane=343820, width=116990, height=46404, cameraPosition=(-224597,
    143518, -166427), cameraUpVector=(0.162564, 0.502317, 0.849265),
    cameraTarget=(-66710.9, -105043, 108484), viewOffsetX=24365.1,
    viewOffsetY=6103.75)
session.viewports['Viewport: 1'].view.setValues(nearPlane=226002,
    farPlane=422566, width=125059, height=49604.7, cameraPosition=(-399908,
    79556.1, 2308.48), cameraUpVector=(0.381173, 0.266774, 0.885177),
    cameraTarget=(-16733.1, -42557.5, 25810.4), viewOffsetX=26045.7,
    viewOffsetY=6524.76)
session.viewports['Viewport: 1'].view.setValues(nearPlane=229157,
    farPlane=419411, width=77695, height=30817.6, viewOffsetX=25819.9,
    viewOffsetY=12376.4)
session.viewports['Viewport: 1'].view.setValues(nearPlane=248090,
    farPlane=445074, width=84114.3, height=33363.8, cameraPosition=(-426206,
    -67893.8, 76778.3), cameraUpVector=(0.398734, 0.55432, 0.730576),
    cameraTarget=(-33981, -11817, 3965.04), viewOffsetX=27953.2,
    viewOffsetY=13399)
session.viewports['Viewport: 1'].view.setValues(nearPlane=250289,
    farPlane=442874, width=54633.8, height=21670.4, viewOffsetX=-3678.46,
    viewOffsetY=21163.3)
session.viewports['Viewport: 1'].view.setValues(nearPlane=255381,
    farPlane=441751, width=55745.2, height=22111.2, cameraPosition=(-385097,
    -116893, 172914), cameraUpVector=(0.495749, 0.643425, 0.583299),
    cameraTarget=(-44106.6, -5008.46, -10101), viewOffsetX=-3753.29,
    viewOffsetY=21593.8)
session.viewports['Viewport: 1'].view.setValues(nearPlane=248450,
    farPlane=448682, width=139407, height=55295.6, viewOffsetX=-14444,
    viewOffsetY=18671.7)
session.viewports['Viewport: 1'].view.setValues(nearPlane=237218,
    farPlane=445766, width=133105, height=52795.7, cameraPosition=(240519,
    -55107.2, 106494), cameraUpVector=(-0.235638, 0.971575, 0.022713),
    cameraTarget=(-141354, -6734.69, -12334.4), viewOffsetX=-13791,
    viewOffsetY=17827.6)
session.viewports['Viewport: 1'].view.setValues(nearPlane=241358,
    farPlane=446113, width=135428, height=53717.1, cameraPosition=(250757,
    13915.4, -31331.6), cameraUpVector=(-0.371323, 0.885003, 0.280873),
    cameraTarget=(-149145, -14636.9, 8040.61), viewOffsetX=-14031.7,
    viewOffsetY=18138.7)
session.viewports['Viewport: 1'].view.setValues(nearPlane=242487,
    farPlane=444985, width=115563, height=45838, viewOffsetX=-14424.3,
    viewOffsetY=16316.8)
session.viewports['Viewport: 1'].view.setValues(nearPlane=294524,
    farPlane=398205, width=140363, height=55674.6, cameraPosition=(-47764.6,
    117378, -296243), cameraUpVector=(-0.0182348, 0.740802, 0.671476),
    cameraTarget=(-121023, -34703.8, 69532), viewOffsetX=-17519.7,
    viewOffsetY=19818.3)
session.viewports['Viewport: 1'].view.setValues(nearPlane=297601,
    farPlane=395128, width=77151.6, height=30602, viewOffsetX=21876.6,
    viewOffsetY=5989.21)
session.viewports['Viewport: 1'].view.setValues(nearPlane=247201,
    farPlane=402883, width=64085.6, height=25419.4, cameraPosition=(89185.4,
    199381, -152531), cameraUpVector=(-0.736594, 0.546117, 0.398981),
    cameraTarget=(-150712, -38562.6, 66830), viewOffsetX=18171.7,
    viewOffsetY=4974.9)
session.viewports['Viewport: 1'].view.setValues(nearPlane=253372,
    farPlane=396712, width=6165.3, height=2445.46, viewOffsetX=15004.4,
    viewOffsetY=14709.2)
session.viewports['Viewport: 1'].view.setValues(nearPlane=253527,
    farPlane=396556, width=4450.32, height=1765.21, viewOffsetX=14951.2,
    viewOffsetY=14680.3)
a = mdb.models['Model-1'].rootAssembly
f1 = a.instances['P-47-1'].faces
faces1 = f1.getSequenceFromMask(mask=('[#1 ]', ), )
leaf = dgm.LeafFromGeometry(faceSeq=faces1)
session.viewports['Viewport: 1'].assemblyDisplay.displayGroup.remove(leaf=leaf)
session.viewports['Viewport: 1'].view.setValues(nearPlane=251867,
    farPlane=398216, width=24640.9, height=9773.78, viewOffsetX=15980.4,
    viewOffsetY=13773.4)
session.viewports['Viewport: 1'].view.setValues(nearPlane=270020,
    farPlane=395433, width=26416.9, height=10478.2, cameraPosition=(49344.7,
    237512, -153362), cameraUpVector=(-0.781671, 0.409213, 0.470675),
    cameraTarget=(-138638, -44253.6, 64716), viewOffsetX=17132.1,
    viewOffsetY=14766.1)
session.viewports['Viewport: 1'].view.setValues(nearPlane=267196,
    farPlane=398258, width=59347.3, height=23540, viewOffsetX=17113.5,
    viewOffsetY=17793.9)
session.viewports['Viewport: 1'].view.setValues(nearPlane=327941,
    farPlane=379963, width=72839.5, height=28891.7, cameraPosition=(-75813.8,
    336192, -56540.2), cameraUpVector=(-0.721938, -0.126171, 0.680357),
    cameraTarget=(-108061, -55009, 34064.6), viewOffsetX=21004.1,
    viewOffsetY=21839.3)
session.viewports['Viewport: 1'].view.setValues(nearPlane=326759,
    farPlane=381145, width=70038.2, height=27780.5, viewOffsetX=23436.4,
    viewOffsetY=40940.1)
session.viewports['Viewport: 1'].view.setValues(nearPlane=341886,
    farPlane=402808, width=73280.4, height=29066.5, cameraPosition=(-163811,
    356260, 40630), cameraUpVector=(-0.564933, -0.477292, 0.673085),
    cameraTarget=(-98078.5, -40303.2, 14095.4), viewOffsetX=24521.3,
    viewOffsetY=42835.3)
session.viewports['Viewport: 1'].view.setValues(nearPlane=344049,
    farPlane=400644, width=43451.8, height=17235.1, viewOffsetX=25756.1,
    viewOffsetY=51571.4)
session.viewports['Viewport: 1'].view.setValues(nearPlane=340921,
    farPlane=433700, width=43056.7, height=17078.3, cameraPosition=(-213057,
    326597, 175415), cameraUpVector=(-0.400005, -0.766551, 0.502389),
    cameraTarget=(-100038, -19958.1, 3910.12), viewOffsetX=25521.9,
    viewOffsetY=51102.5)
session.viewports['Viewport: 1'].view.setValues(nearPlane=343908,
    farPlane=430712, width=9591.05, height=3804.27, viewOffsetX=26157.2,
    viewOffsetY=51198.8)
session.viewports['Viewport: 1'].view.setValues(nearPlane=343863,
    farPlane=430547, width=9589.79, height=3803.77, cameraPosition=(-218578,
    335254, 148498), cameraUpVector=(-0.414759, -0.732296, 0.540109),
    cameraTarget=(-99155.9, -21678.7, 4884.31), viewOffsetX=26153.8,
    viewOffsetY=51192.1)
session.viewports['Viewport: 1'].view.setValues(nearPlane=342875,
    farPlane=431535, width=21784.8, height=8640.92, viewOffsetX=27052.8,
    viewOffsetY=52779)
session.viewports['Viewport: 1'].view.setValues(nearPlane=344112,
    farPlane=417097, width=21863.4, height=8672.09, cameraPosition=(-199151,
    352803, 76263.6), cameraUpVector=(-0.453635, -0.595619, 0.662913),
    cameraTarget=(-98448.2, -30398, 3437.55), viewOffsetX=27150.4,
    viewOffsetY=52969.4)
session.viewports['Viewport: 1'].view.setValues(nearPlane=342648,
    farPlane=418562, width=40160.5, height=15929.6, viewOffsetX=26652.2,
    viewOffsetY=54542.9)
session.viewports['Viewport: 1'].view.setValues(nearPlane=344601,
    farPlane=408883, width=40389.4, height=16020.4, cameraPosition=(-191048,
    354523, 6252.28), cameraUpVector=(-0.467426, -0.456453, 0.757076),
    cameraTarget=(-98418.7, -37528.4, 4438.33), viewOffsetX=26804.1,
    viewOffsetY=54853.8)
session.viewports['Viewport: 1'].view.setValues(nearPlane=345755,
    farPlane=407729, width=25864.5, height=10259.1, viewOffsetX=24459.7,
    viewOffsetY=58858.1)
session.viewports['Viewport: 1'].view.setValues(nearPlane=337024,
    farPlane=393638, width=25211.4, height=10000, cameraPosition=(-150158,
    332376, -94584.8), cameraUpVector=(-0.545906, -0.193764, 0.815133),
    cameraTarget=(-98380, -52263, 13396.6), viewOffsetX=23842,
    viewOffsetY=57371.8)
session.viewports['Viewport: 1'].view.setValues(nearPlane=338991,
    farPlane=391672, width=3195.11, height=1267.34, viewOffsetX=20691.8,
    viewOffsetY=62341.3)
a = mdb.models['Model-1'].rootAssembly
s1 = a.instances['P-43-1'].faces
side1Faces1 = s1.getSequenceFromMask(mask=('[#9 ]', ), )
region1=regionToolset.Region(side1Faces=side1Faces1)
a = mdb.models['Model-1'].rootAssembly
s1 = a.instances['P-48-1'].edges
side1Edges1 = s1.getSequenceFromMask(mask=('[#a ]', ), )
region2=regionToolset.Region(side1Edges=side1Edges1)
mdb.models['Model-1'].Tie(name='Constraint-29', main=region1,
    secondary=region2, positionToleranceMethod=COMPUTED, adjust=ON,
    tieRotations=ON, thickness=ON)
session.viewports['Viewport: 1'].view.setValues(nearPlane=338878,
    farPlane=391785, width=4821.01, height=1912.24, viewOffsetX=20628.1,
    viewOffsetY=62307.1)
leaf = dgm.Leaf(leafType=DEFAULT_MODEL)
session.viewports['Viewport: 1'].assemblyDisplay.displayGroup.replace(
    leaf=leaf)
session.viewports['Viewport: 1'].view.setValues(nearPlane=337793,
    farPlane=392871, width=17775.5, height=7050.61, viewOffsetX=19926.5,
    viewOffsetY=61554.3)
session.viewports['Viewport: 1'].view.setValues(nearPlane=338721,
    farPlane=391942, width=6166.88, height=2446.08, viewOffsetX=18905.3,
    viewOffsetY=62167.3)
leaf = dgm.Leaf(leafType=DEFAULT_MODEL)
session.viewports['Viewport: 1'].assemblyDisplay.displayGroup.replace(
    leaf=leaf)
leaf = dgm.Leaf(leafType=DEFAULT_MODEL)
session.viewports['Viewport: 1'].assemblyDisplay.displayGroup.replace(
    leaf=leaf)
a = mdb.models['Model-1'].rootAssembly
i1 = a.instances['P-35-1']
leaf = dgm.LeafFromInstance((i1, ))
session.viewports['Viewport: 1'].assemblyDisplay.displayGroup.replace(
    leaf=leaf)
session.viewports['Viewport: 1'].view.setValues(nearPlane=352192,
    farPlane=365379, width=15768.5, height=6254.56, viewOffsetX=19479.3,
    viewOffsetY=65233.4)
session.viewports['Viewport: 1'].view.setValues(nearPlane=353944,
    farPlane=367718, width=15846.9, height=6285.66, cameraPosition=(-428750,
    -169200, -146767), cameraUpVector=(-0.135831, 0.230699, 0.963498),
    cameraTarget=(-105226, 27249.6, -8825.09), viewOffsetX=19576.2,
    viewOffsetY=65557.9)
session.viewports['Viewport: 1'].view.setValues(nearPlane=354436,
    farPlane=367225, width=9723.07, height=3856.64, viewOffsetX=21282,
    viewOffsetY=66226.2)
leaf = dgm.Leaf(leafType=DEFAULT_MODEL)
session.viewports['Viewport: 1'].assemblyDisplay.displayGroup.replace(
    leaf=leaf)
session.viewports['Viewport: 1'].view.setValues(nearPlane=325817,
    farPlane=495143, width=12906.2, height=5119.23, viewOffsetX=21061.3,
    viewOffsetY=60907.6)
session.viewports['Viewport: 1'].view.setValues(nearPlane=347743,
    farPlane=525774, width=13774.7, height=5463.73, cameraPosition=(-455028,
    197759, -101748), cameraUpVector=(0.040963, -0.138597, 0.989501),
    cameraTarget=(-97115.2, 41611.8, -2728.46), viewOffsetX=22478.6,
    viewOffsetY=65006.4)
session.viewports['Viewport: 1'].view.setValues(session.views['Iso'])
session.viewports['Viewport: 1'].view.setValues(nearPlane=332167,
    farPlane=473529, width=5213.5, height=2067.93, viewOffsetX=-53649.6,
    viewOffsetY=20963.8)
a = mdb.models['Model-1'].rootAssembly
s1 = a.instances['P-35-1'].edges
side1Edges1 = s1.getSequenceFromMask(mask=('[#8c8 ]', ), )
region1=regionToolset.Region(side1Edges=side1Edges1)
a = mdb.models['Model-1'].rootAssembly
s1 = a.instances['P-47-1'].edges
side1Edges1 = s1.getSequenceFromMask(mask=('[#80 ]', ), )
region2=regionToolset.Region(side1Edges=side1Edges1)
mdb.models['Model-1'].Tie(name='Constraint-30', main=region1,
    secondary=region2, positionToleranceMethod=COMPUTED, adjust=ON,
    tieRotations=ON, thickness=ON)
a = mdb.models['Model-1'].rootAssembly
i1 = a.instances['P-35-1']
leaf = dgm.LeafFromInstance((i1, ))
session.viewports['Viewport: 1'].assemblyDisplay.displayGroup.remove(leaf=leaf)
session.viewports['Viewport: 1'].view.setValues(nearPlane=332239,
    farPlane=473458, width=4429.02, height=1756.76, viewOffsetX=-53638.8,
    viewOffsetY=20938.1)
a = mdb.models['Model-1'].rootAssembly
s1 = a.instances['P-43-1'].edges
side1Edges1 = s1.getSequenceFromMask(mask=('[#20200 ]', ), )
s2 = a.instances['P-44-1'].edges
side1Edges2 = s2.getSequenceFromMask(mask=('[#20001 ]', ), )
region2=regionToolset.Region(side1Edges=side1Edges1+side1Edges2)
mdb.models['Model-1'].constraints['Constraint-30'].setValues(secondary=region2)
leaf = dgm.Leaf(leafType=DEFAULT_MODEL)
session.viewports['Viewport: 1'].assemblyDisplay.displayGroup.replace(
    leaf=leaf)
session.viewports['Viewport: 1'].view.setValues(nearPlane=330413,
    farPlane=475283, width=26591.2, height=10547.3, viewOffsetX=-50556.5,
    viewOffsetY=21283.5)
session.viewports['Viewport: 1'].view.setValues(nearPlane=286551,
    farPlane=455510, width=23061.2, height=9147.19, cameraPosition=(241495,
    162385, 25850.9), cameraUpVector=(-0.700563, 0.599612, -0.386881),
    cameraTarget=(-109675, -34354.8, 9739.17), viewOffsetX=-43845.2,
    viewOffsetY=18458.2)
session.viewports['Viewport: 1'].view.setValues(nearPlane=285322,
    farPlane=456739, width=42359.2, height=16801.7, viewOffsetX=-36128.9,
    viewOffsetY=18552.6)
session.viewports['Viewport: 1'].view.setValues(nearPlane=285176,
    farPlane=456885, width=42337.5, height=16793.1, cameraPosition=(238004,
    169238, 18260.3), cameraUpVector=(-0.735317, 0.646591, -0.20305),
    cameraTarget=(-113166, -27502.2, 2148.56), viewOffsetX=-36110.4,
    viewOffsetY=18543.1)
session.viewports['Viewport: 1'].view.setValues(nearPlane=268736,
    farPlane=454792, width=39896.8, height=15825, cameraPosition=(249299,
    95483.9, -55493.9), cameraUpVector=(-0.654903, 0.69837, -0.28876),
    cameraTarget=(-125386, -33926.3, 16274.2), viewOffsetX=-34028.7,
    viewOffsetY=17474.1)
session.viewports['Viewport: 1'].view.setValues(nearPlane=270933,
    farPlane=452596, width=17871.6, height=7088.73, viewOffsetX=-16871,
    viewOffsetY=14443.1)
session.viewports['Viewport: 1'].view.setValues(nearPlane=267349,
    farPlane=453393, width=17635.2, height=6994.98, cameraPosition=(241354,
    43533.1, -112362), cameraUpVector=(-0.620052, 0.723364, -0.303776),
    cameraTarget=(-129512, -30427, 26471.1), viewOffsetX=-16647.8,
    viewOffsetY=14252)
session.viewports['Viewport: 1'].view.setValues(nearPlane=267876,
    farPlane=452866, width=12322.4, height=4887.67, viewOffsetX=-8328.02,
    viewOffsetY=12610.8)
session.viewports['Viewport: 1'].view.setValues(nearPlane=271358,
    farPlane=451365, width=12482.6, height=4951.21, cameraPosition=(229368,
    99560.8, -110664), cameraUpVector=(-0.717726, 0.657092, -0.230433),
    cameraTarget=(-125184, -36056.3, 24196), viewOffsetX=-8436.27,
    viewOffsetY=12774.7)
session.viewports['Viewport: 1'].view.setValues(nearPlane=269022,
    farPlane=453701, width=40710.3, height=16147.7, viewOffsetX=-10563.3,
    viewOffsetY=15991.6)
session.viewports['Viewport: 1'].view.setValues(nearPlane=271960,
    farPlane=452460, width=41154.9, height=16324, cameraPosition=(221217,
    129417, -104665), cameraUpVector=(-0.762366, 0.619332, -0.187685),
    cameraTarget=(-122446, -38471.2, 21806.8), viewOffsetX=-10678.7,
    viewOffsetY=16166.3)
session.viewports['Viewport: 1'].view.setValues(nearPlane=274857,
    farPlane=449562, width=7201.79, height=2856.58, viewOffsetX=-13262.1,
    viewOffsetY=22688.9)
a = mdb.models['Model-1'].rootAssembly
i1 = a.instances['P-1-1']
leaf = dgm.LeafFromInstance((i1, ))
session.viewports['Viewport: 1'].assemblyDisplay.displayGroup.remove(leaf=leaf)
session.viewports['Viewport: 1'].view.setValues(nearPlane=275007,
    farPlane=449292, width=5548.13, height=2200.66, viewOffsetX=-10383.5,
    viewOffsetY=24143.7)
a = mdb.models['Model-1'].rootAssembly
s1 = a.instances['P-4-1'].faces
side1Faces1 = s1.getSequenceFromMask(mask=('[#f00 ]', ), )
region1=regionToolset.Region(side1Faces=side1Faces1)
a = mdb.models['Model-1'].rootAssembly
s1 = a.instances['P-13-1'].faces
side1Faces1 = s1.getSequenceFromMask(mask=('[#2 ]', ), )
s2 = a.instances['P-14-1'].faces
side1Faces2 = s2.getSequenceFromMask(mask=('[#c ]', ), )
region2=regionToolset.Region(side1Faces=side1Faces1+side1Faces2)
mdb.models['Model-1'].Tie(name='Constraint-31', main=region1,
    secondary=region2, positionToleranceMethod=COMPUTED, adjust=ON,
    tieRotations=ON, thickness=ON)
session.viewports['Viewport: 1'].view.setValues(nearPlane=275044,
    farPlane=449255, width=5140.6, height=2039.01, viewOffsetX=-15153.6,
    viewOffsetY=19804.9)
a = mdb.models['Model-1'].rootAssembly
s1 = a.instances['P-4-1'].faces
side1Faces1 = s1.getSequenceFromMask(mask=('[#e8 ]', ), )
region1=regionToolset.Region(side1Faces=side1Faces1)
a = mdb.models['Model-1'].rootAssembly
s1 = a.instances['P-14-1'].faces
side1Faces1 = s1.getSequenceFromMask(mask=('[#1 ]', ), )
s2 = a.instances['P-13-1'].faces
side1Faces2 = s2.getSequenceFromMask(mask=('[#1 ]', ), )
region2=regionToolset.Region(side1Faces=side1Faces1+side1Faces2)
mdb.models['Model-1'].Tie(name='Constraint-32', main=region1,
    secondary=region2, positionToleranceMethod=COMPUTED, adjust=ON,
    tieRotations=ON, thickness=ON)
session.viewports['Viewport: 1'].view.setValues(nearPlane=275293,
    farPlane=449006, width=2397.98, height=951.154, viewOffsetX=-17760.8,
    viewOffsetY=17812)
leaf = dgm.Leaf(leafType=DEFAULT_MODEL)
session.viewports['Viewport: 1'].assemblyDisplay.displayGroup.replace(
    leaf=leaf)
session.viewports['Viewport: 1'].view.setValues(nearPlane=274632,
    farPlane=449786, width=9669.89, height=3835.54, viewOffsetX=-14877,
    viewOffsetY=19146.8)
a = mdb.models['Model-1'].rootAssembly
i1 = a.instances['P-1-1']
leaf = dgm.LeafFromInstance((i1, ))
session.viewports['Viewport: 1'].assemblyDisplay.displayGroup.remove(leaf=leaf)
session.viewports['Viewport: 1'].view.setValues(nearPlane=275138,
    farPlane=449161, width=4110.7, height=1630.5, viewOffsetX=-15327,
    viewOffsetY=20161.1)
leaf = dgm.Leaf(leafType=DEFAULT_MODEL)
session.viewports['Viewport: 1'].assemblyDisplay.displayGroup.replace(
    leaf=leaf)
session.viewports['Viewport: 1'].view.setValues(nearPlane=275004,
    farPlane=449415, width=5582.96, height=2214.47, viewOffsetX=-15312,
    viewOffsetY=20012.3)
a = mdb.models['Model-1'].rootAssembly
s1 = a.instances['P-1-1'].faces
side1Faces1 = s1.getSequenceFromMask(mask=('[#2 ]', ), )
region1=regionToolset.Region(side1Faces=side1Faces1)
a = mdb.models['Model-1'].rootAssembly
s1 = a.instances['P-13-1'].faces
side1Faces1 = s1.getSequenceFromMask(mask=('[#1 ]', ), )
region2=regionToolset.Region(side1Faces=side1Faces1)
mdb.models['Model-1'].Tie(name='Constraint-33', main=region1,
    secondary=region2, positionToleranceMethod=COMPUTED, adjust=ON,
    tieRotations=ON, thickness=ON)
session.viewports['Viewport: 1'].view.setValues(nearPlane=275127,
    farPlane=449291, width=4226.46, height=1676.42, viewOffsetX=-10924.1,
    viewOffsetY=24090.2)
a = mdb.models['Model-1'].rootAssembly
s1 = a.instances['P-1-1'].faces
side1Faces1 = s1.getSequenceFromMask(mask=('[#2 ]', ), )
region1=regionToolset.Region(side1Faces=side1Faces1)
a = mdb.models['Model-1'].rootAssembly
s1 = a.instances['P-13-1'].faces
side1Faces1 = s1.getSequenceFromMask(mask=('[#2 ]', ), )
region2=regionToolset.Region(side1Faces=side1Faces1)
mdb.models['Model-1'].Tie(name='Constraint-34', main=region1,
    secondary=region2, positionToleranceMethod=COMPUTED, adjust=ON,
    tieRotations=ON, thickness=ON)
session.viewports['Viewport: 1'].view.setValues(nearPlane=274093,
    farPlane=450326, width=16929, height=6714.84, viewOffsetX=-11872.3,
    viewOffsetY=23615.4)
session.viewports['Viewport: 1'].view.setValues(nearPlane=274567,
    farPlane=449852, width=10390.5, height=4121.36, viewOffsetX=-13146.1,
    viewOffsetY=22529.3)
a = mdb.models['Model-1'].rootAssembly
a.features['P-47-1'].suppress()

mdb.models['Model-1'].constraints['Constraint-27'].swapSurfaces()
mdb.models['Model-1'].constraints['Constraint-31'].suppress()