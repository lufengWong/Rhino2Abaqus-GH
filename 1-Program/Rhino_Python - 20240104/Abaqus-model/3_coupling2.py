# -*- coding: mbcs -*-
#
# Abaqus/CAE Release 2022 replay file
# Internal Version: 2021_09_16-01.57.30 176069
# Run by Administrator on Sat Dec 23 13:25:42 2023
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
# executeOnCaeStartup()
# session.viewports['Viewport: 1'].partDisplay.geometryOptions.setValues(
#     referenceRepresentation=ON)
# openMdb(pathName='F:/temp/A-abaqus-2.cae')
# #: The model database "F:\temp\A-abaqus-2.cae" has been opened.








session.viewports['Viewport: 1'].view.setValues(nearPlane=222988,
    farPlane=361079, width=40893.5, height=16220.3, viewOffsetX=-13397,
    viewOffsetY=86931.7)
session.viewports['Viewport: 1'].view.setValues(nearPlane=213814,
    farPlane=368758, width=39211.1, height=15553, cameraPosition=(65428.9,
    8065.12, -244525), cameraUpVector=(-0.460852, 0.762283, 0.454467),
    cameraTarget=(-176592, -134157, 43705.1), viewOffsetX=-12845.9,
    viewOffsetY=83355.3)
session.viewports['Viewport: 1'].view.setValues(nearPlane=208080,
    farPlane=374492, width=110871, height=43976.6, viewOffsetX=9905.16,
    viewOffsetY=78444.3)
session.viewports['Viewport: 1'].view.setValues(nearPlane=272362,
    farPlane=452326, width=145122, height=57562.2, cameraPosition=(-427681,
    74812.1, -144945), cameraUpVector=(0.776974, 0.594925, 0.205853),
    cameraTarget=(-122651, -146750, -4430.39), viewOffsetX=12965.1,
    viewOffsetY=102678)
session.viewports['Viewport: 1'].view.setValues(nearPlane=261321,
    farPlane=463367, width=246584, height=97806.9, viewOffsetX=28830.7,
    viewOffsetY=99228)
session.viewports['Viewport: 1'].view.setValues(nearPlane=287283,
    farPlane=451943, width=271082, height=107524, cameraPosition=(-289988,
    38214.9, 363408), cameraUpVector=(0.205864, 0.662364, -0.720343),
    cameraTarget=(-118372, -150819, 52455.3), viewOffsetX=31695,
    viewOffsetY=109086)
session.viewports['Viewport: 1'].view.setValues(nearPlane=295627,
    farPlane=443600, width=145169, height=57581.1, viewOffsetX=5083.18,
    viewOffsetY=110703)
session.viewports['Viewport: 1'].view.setValues(nearPlane=305791,
    farPlane=419598, width=150160, height=59560.8, cameraPosition=(-158427,
    -64231.1, 401752), cameraUpVector=(-0.224513, 0.787366, -0.57415),
    cameraTarget=(-72791.3, -149347, 17955.8), viewOffsetX=5257.95,
    viewOffsetY=114509)
session.viewports['Viewport: 1'].view.setValues(nearPlane=308365,
    farPlane=421222, width=151424, height=60062.2, cameraPosition=(-141733,
    -194113, 362364), cameraUpVector=(-0.321335, 0.905989, -0.275548),
    cameraTarget=(-59303.8, -135276, -27021.8), viewOffsetX=5302.21,
    viewOffsetY=115473)
session.viewports['Viewport: 1'].view.setValues(nearPlane=297818,
    farPlane=431769, width=281512, height=111661, viewOffsetX=7725.07,
    viewOffsetY=127883)
session.viewports['Viewport: 1'].view.setValues(nearPlane=279961,
    farPlane=478089, width=264633, height=104966, cameraPosition=(-326624,
    -335624, 8829.61), cameraUpVector=(-0.125749, 0.848693, 0.513718),
    cameraTarget=(-42436.3, -71298.3, -97224.3), viewOffsetX=7261.87,
    viewOffsetY=120215)
session.viewports['Viewport: 1'].view.setValues(nearPlane=279950,
    farPlane=481747, width=264623, height=104962, cameraPosition=(-364773,
    -304153, 82009.3), cameraUpVector=(0.103991, 0.876775, 0.469523),
    cameraTarget=(-83796, -84675.4, -104431), viewOffsetX=7261.6,
    viewOffsetY=120210)
session.viewports['Viewport: 1'].view.setValues(nearPlane=280120,
    farPlane=479284, width=264784, height=105026, cameraPosition=(-365569,
    -308977, 38157.5), cameraUpVector=(0.106006, 0.805958, 0.582404),
    cameraTarget=(-84022.5, -67246.2, -117330), viewOffsetX=7266.02,
    viewOffsetY=120283)
session.viewports['Viewport: 1'].view.setValues(nearPlane=281465,
    farPlane=472253, width=266055, height=105530, cameraPosition=(-326709,
    -327829, 94343.2), cameraUpVector=(0.0236171, 0.890884, 0.453616),
    cameraTarget=(-76614.6, -82916.1, -104023), viewOffsetX=7300.9,
    viewOffsetY=120860)
session.viewports['Viewport: 1'].view.setValues(nearPlane=301462,
    farPlane=452255, width=34169.5, height=13553.3, viewOffsetX=-2953.29,
    viewOffsetY=152865)

# #######################
a = mdb.models['Model-1'].rootAssembly
v1 = a.instances['FZX-1'].vertices
verts1 = v1.getSequenceFromMask(mask=('[#8000 ]', ), )
a.Set(vertices=verts1, name='SET-RP1')
#: The set 'SET-RP1' has been created (1 vertex).
session.viewports['Viewport: 1'].view.setValues(nearPlane=303390,
    farPlane=450327, width=14032.4, height=5565.91, viewOffsetX=-11059.6,
    viewOffsetY=155300)
a = mdb.models['Model-1'].rootAssembly
e1 = a.instances['P-1-1'].edges
edges1 = e1.getSequenceFromMask(mask=('[#21 ]', ), )
e2 = a.instances['P-2-1'].edges
edges2 = e2.getSequenceFromMask(mask=('[#22222222:2 ]', ), )
a.Set(edges=edges1+edges2, name='SET-RP2')
#: The set 'SET-RP2' has been created (18 edges).
session.viewports['Viewport: 1'].view.setValues(nearPlane=300254,
    farPlane=453463, width=51457.5, height=20410.5, viewOffsetX=10429.1,
    viewOffsetY=153469)
session.viewports['Viewport: 1'].view.setValues(nearPlane=303690,
    farPlane=447648, width=52046.5, height=20644.1, cameraPosition=(-306131,
    -332732, 127024), cameraUpVector=(0.0354551, 0.906792, 0.420086),
    cameraTarget=(-87124.2, -86472.2, -103780), viewOffsetX=10548.5,
    viewOffsetY=155226)
session.viewports['Viewport: 1'].view.setValues(nearPlane=301384,
    farPlane=449955, width=81068.6, height=32155.7, viewOffsetX=8399.2,
    viewOffsetY=152286)
session.viewports['Viewport: 1'].view.setValues(nearPlane=306777,
    farPlane=432739, width=82519.3, height=32731.1, cameraPosition=(-252796,
    -347364, 155390), cameraUpVector=(0.00620938, 0.91388, 0.405936),
    cameraTarget=(-96860, -85154.7, -106924), viewOffsetX=8549.5,
    viewOffsetY=155011)
session.viewports['Viewport: 1'].view.setValues(nearPlane=316257,
    farPlane=437011, width=85069.4, height=33742.6, cameraPosition=(-221764,
    -313057, 252953), cameraUpVector=(-0.0601048, 0.985976, 0.155686),
    cameraTarget=(-89731.4, -117527, -72951.2), viewOffsetX=8813.7,
    viewOffsetY=159801)
session.viewports['Viewport: 1'].view.setValues(nearPlane=306649,
    farPlane=444223, width=82485.1, height=32717.5, cameraPosition=(-254229,
    -333259, 193644), cameraUpVector=(-0.0769513, 0.962476, 0.260227),
    cameraTarget=(-74660.9, -104408, -84313.7), viewOffsetX=8545.95,
    viewOffsetY=154946)
session.viewports['Viewport: 1'].view.setValues(nearPlane=304549,
    farPlane=446324, width=113559, height=45042.9, viewOffsetX=5989.79,
    viewOffsetY=154929)
session.viewports['Viewport: 1'].view.setValues(nearPlane=311994,
    farPlane=435346, width=116335, height=46144, cameraPosition=(-198721,
    -323250, 244419), cameraUpVector=(-0.151284, 0.974554, 0.165404),
    cameraTarget=(-72467.5, -112013, -73883.9), viewOffsetX=6136.22,
    viewOffsetY=158716)
session.viewports['Viewport: 1'].view.setValues(nearPlane=317227,
    farPlane=428837, width=118286, height=46918, cameraPosition=(-151576,
    -309459, 276559), cameraUpVector=(-0.263625, 0.960876, 0.0849703),
    cameraTarget=(-57405.7, -114082, -62317.4), viewOffsetX=6239.15,
    viewOffsetY=161378)
session.viewports['Viewport: 1'].view.setValues(nearPlane=323097,
    farPlane=422966, width=47112.4, height=18687.1, viewOffsetX=-7281.49,
    viewOffsetY=156888)
session.viewports['Viewport: 1'].view.setValues(nearPlane=327842,
    farPlane=413791, width=47804.3, height=18961.5, cameraPosition=(-118740,
    -290814, 299591), cameraUpVector=(-0.297157, 0.954078, 0.0378636),
    cameraTarget=(-58765.7, -117357, -58450), viewOffsetX=-7388.42,
    viewOffsetY=159192)
session.viewports['Viewport: 1'].view.setValues(nearPlane=327602,
    farPlane=414032, width=51923.1, height=20595.2, viewOffsetX=-11979.8,
    viewOffsetY=157523)
session.viewports['Viewport: 1'].view.setValues(nearPlane=333514,
    farPlane=401486, width=52860.3, height=20966.9, cameraPosition=(-71122.3,
    -257453, 326176), cameraUpVector=(-0.367401, 0.92954, -0.0311624),
    cameraTarget=(-56089.5, -119898, -51621), viewOffsetX=-12196,
    viewOffsetY=160366)
session.viewports['Viewport: 1'].view.setValues(nearPlane=331831,
    farPlane=399803, width=52593.6, height=20861.1, cameraPosition=(-33362.7,
    -223199, 344092), cameraUpVector=(-0.44994, 0.888523, -0.0898942),
    cameraTarget=(-48253.7, -119091, -44261), viewOffsetX=-12134.5,
    viewOffsetY=159557)
session.viewports['Viewport: 1'].view.setValues(nearPlane=333922,
    farPlane=397713, width=30093.8, height=11936.7, viewOffsetX=-27791.7,
    viewOffsetY=156222)
session.viewports['Viewport: 1'].view.setValues(nearPlane=311956,
    farPlane=401986, width=28114.2, height=11151.4, cameraPosition=(29464.7,
    -177304, 343544), cameraUpVector=(-0.540125, 0.834565, -0.108467),
    cameraTarget=(-48393.5, -117710, -46667.3), viewOffsetX=-25963.5,
    viewOffsetY=145946)
session.viewports['Viewport: 1'].view.setValues(nearPlane=311036,
    farPlane=402906, width=42309.7, height=16782.1, viewOffsetX=-26008.6,
    viewOffsetY=146056)
session.viewports['Viewport: 1'].view.setValues(nearPlane=305206,
    farPlane=405827, width=41516.6, height=16467.5, cameraPosition=(68110.7,
    -73291, 360429), cameraUpVector=(-0.686212, 0.685871, -0.24227),
    cameraTarget=(-31486.5, -114331, -27223.5), viewOffsetX=-25521.1,
    viewOffsetY=143319)
session.viewports['Viewport: 1'].view.setValues(nearPlane=306841,
    farPlane=404191, width=22626.2, height=8974.64, viewOffsetX=-29465.3,
    viewOffsetY=142011)
session.viewports['Viewport: 1'].view.setValues(nearPlane=329876,
    farPlane=400047, width=24324.7, height=9648.37, cameraPosition=(-5119.17,
    -205291, 346575), cameraUpVector=(-0.528519, 0.843766, -0.093414),
    cameraTarget=(-37520.8, -109762, -42915.3), viewOffsetX=-31677.3,
    viewOffsetY=152672)
session.viewports['Viewport: 1'].view.setValues(nearPlane=330870,
    farPlane=399053, width=10784, height=4277.45, viewOffsetX=-33517.6,
    viewOffsetY=152816)
a = mdb.models['Model-1'].rootAssembly
v1 = a.instances['FZX-1'].vertices
verts1 = v1.getSequenceFromMask(mask=('[#200 ]', ), )
a.Set(vertices=verts1, name='SET-RP3')
#: The set 'SET-RP3' has been created (1 vertex).
session.viewports['Viewport: 1'].view.setValues(nearPlane=330764,
    farPlane=399158, width=12960.4, height=5140.7, viewOffsetX=-31726.3,
    viewOffsetY=153205)
i1 = mdb.models['Model-1'].rootAssembly.allInstances['FZX-1']
leaf = dgm.LeafFromInstance(instances=(i1, ))
session.viewports['Viewport: 1'].assemblyDisplay.displayGroup.remove(leaf=leaf)
session.viewports['Viewport: 1'].view.setValues(nearPlane=331065,
    farPlane=398858, width=8639.3, height=3426.76, viewOffsetX=-32438.6,
    viewOffsetY=152484)
a = mdb.models['Model-1'].rootAssembly
e1 = a.instances['P-1-1'].edges
edges1 = e1.getSequenceFromMask(mask=('[#14 ]', ), )
e2 = a.instances['P-2-1'].edges
edges2 = e2.getSequenceFromMask(mask=('[#88888888:2 ]', ), )
a.Set(edges=edges1+edges2, name='SET-RP4')
#: The set 'SET-RP4' has been created (18 edges).
session.viewports['Viewport: 1'].view.setValues(nearPlane=327317,
    farPlane=402605, width=54088.3, height=21454, viewOffsetX=-32902.9,
    viewOffsetY=154736)
leaf = dgm.Leaf(leafType=DEFAULT_MODEL)
session.viewports['Viewport: 1'].assemblyDisplay.displayGroup.replace(
    leaf=leaf)
session.viewports['Viewport: 1'].view.setValues(nearPlane=324801,
    farPlane=405122, width=84094.7, height=33356, viewOffsetX=-32247.8,
    viewOffsetY=154222)
session.viewports['Viewport: 1'].view.setValues(nearPlane=252323,
    farPlane=414636, width=65329.4, height=25912.8, cameraPosition=(191916,
    21567.7, 238756), cameraUpVector=(-0.81908, 0.571648, -0.0482332),
    cameraTarget=(-49271.2, -114052, -53330.7), viewOffsetX=-25051.9,
    viewOffsetY=119809)
session.viewports['Viewport: 1'].view.setValues(nearPlane=273579,
    farPlane=388562, width=70832.8, height=28095.7, cameraPosition=(160610,
    237479, 38886.3), cameraUpVector=(-0.982904, 0.10379, 0.152077),
    cameraTarget=(-23160, -114352, -26858.8), viewOffsetX=-27162.3,
    viewOffsetY=129902)
session.viewports['Viewport: 1'].view.setValues(nearPlane=268918,
    farPlane=393223, width=123518, height=48993.1, viewOffsetX=-15534.8,
    viewOffsetY=132487)
session.viewports['Viewport: 1'].view.setValues(nearPlane=263506,
    farPlane=385709, width=121032, height=48007.2, cameraPosition=(-73798.1,
    -64136.4, -318078), cameraUpVector=(-0.749928, -0.137866, 0.646994),
    cameraTarget=(41082.3, 56656.8, 48105.4), viewOffsetX=-15222.2,
    viewOffsetY=129821)
session.viewports['Viewport: 1'].view.setValues(nearPlane=251376,
    farPlane=397839, width=272579, height=108118, viewOffsetX=5488.33,
    viewOffsetY=137222)
session.viewports['Viewport: 1'].view.setValues(nearPlane=283124,
    farPlane=415894, width=307006, height=121773, cameraPosition=(-273330,
    -292641, -163813), cameraUpVector=(0.177743, 0.185393, 0.966456),
    cameraTarget=(-126197, 79659.1, -123522), viewOffsetX=6181.5,
    viewOffsetY=154553)
session.viewports['Viewport: 1'].view.setValues(nearPlane=269906,
    farPlane=381693, width=292673, height=116088, cameraPosition=(-57272.9,
    -308537, -178650), cameraUpVector=(-0.10675, 0.180792, 0.977711),
    cameraTarget=(-136764, 81833.8, -122343), viewOffsetX=5892.91,
    viewOffsetY=147338)
session.viewports['Viewport: 1'].view.setValues(nearPlane=277172,
    farPlane=390493, width=300552, height=119213, cameraPosition=(3825.78,
    -360468, -24772.8), cameraUpVector=(-0.448689, 0.493738, 0.744917),
    cameraTarget=(-69516.9, 18042.9, -139792), viewOffsetX=6051.56,
    viewOffsetY=151305)
session.viewports['Viewport: 1'].view.setValues(nearPlane=290993,
    farPlane=402327, width=315538, height=125157, cameraPosition=(-85731.2,
    -384753, -3661.41), cameraUpVector=(-0.463366, 0.624192, 0.629028),
    cameraTarget=(-20291.1, -4937.01, -119144), viewOffsetX=6353.31,
    viewOffsetY=158850)
session.viewports['Viewport: 1'].view.setValues(nearPlane=298487,
    farPlane=394833, width=206575, height=81937.6, viewOffsetX=-654.776,
    viewOffsetY=173249)
session.viewports['Viewport: 1'].view.setValues(nearPlane=260936,
    farPlane=362693, width=180587, height=71629.4, cameraPosition=(-12942.7,
    -214336, -256726), cameraUpVector=(-0.371132, -0.115151, 0.921413),
    cameraTarget=(-82420.3, 147011, -94000.4), viewOffsetX=-572.402,
    viewOffsetY=151453)
session.viewports['Viewport: 1'].view.setValues(nearPlane=277868,
    farPlane=345760, width=12000.2, height=4759.86, viewOffsetX=-24514.8,
    viewOffsetY=177506)
a = mdb.models['Model-1'].rootAssembly
v1 = a.instances['FZX-1'].vertices
verts1 = v1.getSequenceFromMask(mask=('[#8 ]', ), )
a.Set(vertices=verts1, name='SET-RP5')
#: The set 'SET-RP5' has been created (1 vertex).
session.viewports['Viewport: 1'].view.setValues(nearPlane=277868,
    farPlane=345760, width=12000.2, height=4759.87, viewOffsetX=-23395.1,
    viewOffsetY=177997)
a = mdb.models['Model-1'].rootAssembly
e1 = a.instances['P-11-1'].edges
edges1 = e1.getSequenceFromMask(mask=('[#8 ]', ), )
a.Set(edges=edges1, name='SET-RP6')
#: The set 'SET-RP6' has been created (1 edge).
session.viewports['Viewport: 1'].view.setValues(nearPlane=278104,
    farPlane=345524, width=9401.29, height=3729.01, viewOffsetX=-12682.6,
    viewOffsetY=178492)
a = mdb.models['Model-1'].rootAssembly
v1 = a.instances['FZX-1'].vertices
verts1 = v1.getSequenceFromMask(mask=('[#200000 ]', ), )
a.Set(vertices=verts1, name='SET-RP7')
#: The set 'SET-RP7' has been created (1 vertex).
session.viewports['Viewport: 1'].view.setValues(nearPlane=278232,
    farPlane=345395, width=7988.64, height=3168.68, viewOffsetX=-12886.9,
    viewOffsetY=178500)
a = mdb.models['Model-1'].rootAssembly
e1 = a.instances['P-18-1'].edges
edges1 = e1.getSequenceFromMask(mask=('[#2 ]', ), )
a.Set(edges=edges1, name='SET-RP8')
#: The set 'SET-RP8' has been created (1 edge).
session.viewports['Viewport: 1'].view.setValues(nearPlane=278228,
    farPlane=345399, width=8030.3, height=3185.2, viewOffsetX=-19892.9,
    viewOffsetY=177474)
a = mdb.models['Model-1'].rootAssembly
v1 = a.instances['FZX-1'].vertices
verts1 = v1.getSequenceFromMask(mask=('[#800000 ]', ), )
a.Set(vertices=verts1, name='SET-RP9')
#: The set 'SET-RP9' has been created (1 vertex).
a = mdb.models['Model-1'].rootAssembly
e1 = a.instances['P-18-1'].edges
edges1 = e1.getSequenceFromMask(mask=('[#8 ]', ), )
a.Set(edges=edges1, name='SET-RP10')
#: The set 'SET-RP10' has been created (1 edge).
session.viewports['Viewport: 1'].view.setValues(nearPlane=277904,
    farPlane=345724, width=11602.2, height=4601.98, viewOffsetX=-15257.8,
    viewOffsetY=176883)
a = mdb.models['Model-1'].rootAssembly
v1 = a.instances['FZX-1'].vertices
verts1 = v1.getSequenceFromMask(mask=('[#2 ]', ), )
a.Set(vertices=verts1, name='SET-RP11')
#: The set 'SET-RP11' has been created (1 vertex).
a = mdb.models['Model-1'].rootAssembly
e1 = a.instances['P-11-1'].edges
edges1 = e1.getSequenceFromMask(mask=('[#2 ]', ), )
a.Set(edges=edges1, name='SET-RP12')
#: The set 'SET-RP12' has been created (1 edge).
session.viewports['Viewport: 1'].view.setValues(nearPlane=278897,
    farPlane=344731, width=673.122, height=266.993, viewOffsetX=-10394,
    viewOffsetY=178443)
session.viewports['Viewport: 1'].view.setValues(nearPlane=277881,
    farPlane=345746, width=12853.5, height=5098.3, viewOffsetX=-8486.75,
    viewOffsetY=177199)
session.viewports['Viewport: 1'].view.setValues(nearPlane=271490,
    farPlane=347143, width=12557.8, height=4981.04, cameraPosition=(-2189.03,
    -204834, -257907), cameraUpVector=(-0.374094, -0.143037, 0.916294),
    cameraTarget=(-88614.9, 151035, -91274.1), viewOffsetX=-8291.56,
    viewOffsetY=173124)
session.viewports['Viewport: 1'].view.setValues(nearPlane=266815,
    farPlane=351818, width=69144, height=27425.8, viewOffsetX=-1358.8,
    viewOffsetY=169283)
session.viewports['Viewport: 1'].view.setValues(nearPlane=185662,
    farPlane=365932, width=48113.5, height=19084.1, cameraPosition=(50545,
    6447.38, -284086), cameraUpVector=(0.002124, -0.495491, 0.86861),
    cameraTarget=(-256518, 132787, -56865.3), viewOffsetX=-945.517,
    viewOffsetY=117795)
session.viewports['Viewport: 1'].view.setValues(nearPlane=173085,
    farPlane=352013, width=44854.3, height=17791.4, cameraPosition=(7506.45,
    183922, -228044), cameraUpVector=(0.281686, -0.607563, 0.742644),
    cameraTarget=(-317909, 15752, -61604.3), viewOffsetX=-881.469,
    viewOffsetY=109816)
session.viewports['Viewport: 1'].view.setValues(nearPlane=167891,
    farPlane=357208, width=111647, height=44284.4, viewOffsetX=12506.5,
    viewOffsetY=101351)
session.viewports['Viewport: 1'].view.setValues(nearPlane=203899,
    farPlane=333801, width=135591, height=53782, cameraPosition=(-47075.7,
    257581, -175167), cameraUpVector=(0.316305, -0.480801, 0.817791),
    cameraTarget=(-253794, -84960.7, -132606), viewOffsetX=15188.8,
    viewOffsetY=123087)
session.viewports['Viewport: 1'].view.setValues(nearPlane=213560,
    farPlane=324140, width=871.125, height=345.53, viewOffsetX=42688.4,
    viewOffsetY=129526)
a = mdb.models['Model-1'].rootAssembly
v1 = a.instances['FZX-1'].vertices
verts1 = v1.getSequenceFromMask(mask=('[#80000 ]', ), )
a.Set(vertices=verts1, name='SET-RP13')
#: The set 'SET-RP13' has been created (1 vertex).
a = mdb.models['Model-1'].rootAssembly
e1 = a.instances['P-31-1'].edges
edges1 = e1.getSequenceFromMask(mask=('[#2 ]', ), )
a.Set(edges=edges1, name='SET-RP14')
#: The set 'SET-RP14' has been created (1 edge).
session.viewports['Viewport: 1'].view.setValues(nearPlane=213515,
    farPlane=324185, width=1485.84, height=589.356, viewOffsetX=42855.9,
    viewOffsetY=129469)
session.viewports['Viewport: 1'].view.setValues(session.views['Iso'])
session.viewports['Viewport: 1'].view.setValues(nearPlane=309429,
    farPlane=496267, width=276364, height=109619, viewOffsetX=16160.2,
    viewOffsetY=-474.792)
session.viewports['Viewport: 1'].view.setValues(nearPlane=319189,
    farPlane=471640, width=285081, height=113077, cameraPosition=(54484.2,
    248781, 289127), cameraUpVector=(-0.592106, 0.464082, -0.658816),
    cameraTarget=(-82537.9, -18210.9, 20376), viewOffsetX=16669.9,
    viewOffsetY=-489.768)
session.viewports['Viewport: 1'].view.setValues(nearPlane=342127,
    farPlane=448702, width=12148.8, height=4818.82, viewOffsetX=-56926.4,
    viewOffsetY=32430.3)
a = mdb.models['Model-1'].rootAssembly
v1 = a.instances['FZX-1'].vertices
verts1 = v1.getSequenceFromMask(mask=('[#20 ]', ), )
a.Set(vertices=verts1, name='SET-RP15')
#: The set 'SET-RP15' has been created (1 vertex).
session.viewports['Viewport: 1'].view.setValues(nearPlane=342253,
    farPlane=448575, width=10752.5, height=4264.96, viewOffsetX=-57177.7,
    viewOffsetY=32549.6)
a = mdb.models['Model-1'].rootAssembly
e1 = a.instances['P-35-1'].edges
edges1 = e1.getSequenceFromMask(mask=('[#612 ]', ), )
a.Set(edges=edges1, name='SET-RP16')
#: The set 'SET-RP16' has been created (4 edges).
session.viewports['Viewport: 1'].view.setValues(nearPlane=336887,
    farPlane=453941, width=75621.9, height=29995.3, viewOffsetX=-41342.8,
    viewOffsetY=32136.5)
session.viewports['Viewport: 1'].view.setValues(nearPlane=310164,
    farPlane=458496, width=69623.2, height=27615.9, cameraPosition=(122928,
    189017, 278122), cameraUpVector=(-0.597278, 0.614573, -0.515324),
    cameraTarget=(-89573.6, -23770.2, 10070.1), viewOffsetX=-38063.3,
    viewOffsetY=29587.3)
session.viewports['Viewport: 1'].view.setValues(nearPlane=306388,
    farPlane=450761, width=68775.7, height=27279.7, cameraPosition=(114727,
    -2735.84, 344775), cameraUpVector=(-0.594104, 0.8041, -0.0215417),
    cameraTarget=(-88318.5, 4923.96, -3076.73), viewOffsetX=-37600,
    viewOffsetY=29227.1)
session.viewports['Viewport: 1'].view.setValues(nearPlane=305690,
    farPlane=451459, width=80790.4, height=32045.4, viewOffsetX=-36913.7,
    viewOffsetY=28808)
session.viewports['Viewport: 1'].view.setValues(nearPlane=322997,
    farPlane=415286, width=85364.6, height=33859.7, cameraPosition=(8185.77,
    -277768, 260909), cameraUpVector=(-0.645929, 0.602384, 0.468944),
    cameraTarget=(-74047, 39412.7, 26556.6), viewOffsetX=-39003.6,
    viewOffsetY=30439.1)
session.viewports['Viewport: 1'].view.setValues(nearPlane=319811,
    farPlane=418472, width=122048, height=48410.2, viewOffsetX=-40416.7,
    viewOffsetY=30938.5)
session.viewports['Viewport: 1'].view.setValues(nearPlane=331204,
    farPlane=438321, width=126396, height=50134.9, cameraPosition=(-163225,
    -298752, 270196), cameraUpVector=(-0.579246, 0.77575, 0.250372),
    cameraTarget=(-60000.4, 22467, 50082.5), viewOffsetX=-41856.5,
    viewOffsetY=32040.6)
session.viewports['Viewport: 1'].view.setValues(nearPlane=330825,
    farPlane=438701, width=126251, height=50077.6, cameraPosition=(-163341,
    -310424, 253108), cameraUpVector=(-0.333615, 0.83068, 0.445725),
    cameraTarget=(-60116.2, 10794.8, 32994.6), viewOffsetX=-41808.6,
    viewOffsetY=32004)
session.viewports['Viewport: 1'].view.setValues(nearPlane=332732,
    farPlane=404228, width=126979, height=50366.3, cameraPosition=(-129124,
    -374227, 54348.2), cameraUpVector=(-0.364145, 0.44904, 0.815942),
    cameraTarget=(-60623, 22090.5, 31386.6), viewOffsetX=-42049.6,
    viewOffsetY=32188.5)
session.viewports['Viewport: 1'].view.setValues(nearPlane=337647,
    farPlane=399314, width=67173.5, height=26644.3, viewOffsetX=-70093.6,
    viewOffsetY=45789.6)
session.viewports['Viewport: 1'].view.setValues(nearPlane=337887,
    farPlane=399074, width=67221.2, height=26663.2, cameraPosition=(-130384,
    -374486, 46124.3), cameraUpVector=(-0.287019, 0.4378, 0.852028),
    cameraTarget=(-61882.5, 21831.7, 23162.7), viewOffsetX=-70143.4,
    viewOffsetY=45822.1)
session.viewports['Viewport: 1'].view.setValues(nearPlane=335228,
    farPlane=426849, width=66692.2, height=26453.4, cameraPosition=(-180241,
    -367038, 117619), cameraUpVector=(-0.135689, 0.622768, 0.770551),
    cameraTarget=(-62930.8, 3826.48, 12807.9), viewOffsetX=-69591.4,
    viewOffsetY=45461.5)
session.viewports['Viewport: 1'].view.setValues(nearPlane=333687,
    farPlane=428390, width=88344, height=35041.5, viewOffsetX=-64838.5,
    viewOffsetY=42642.2)
session.viewports['Viewport: 1'].view.setValues(nearPlane=331979,
    farPlane=447750, width=87891.7, height=34862.1, cameraPosition=(-219381,
    -349883, 161659), cameraUpVector=(-0.102278, 0.723611, 0.682588),
    cameraTarget=(-63539.3, -7137.09, 18390.5), viewOffsetX=-64506.4,
    viewOffsetY=42423.8)
session.viewports['Viewport: 1'].view.setValues(nearPlane=331930,
    farPlane=443828, width=87878.7, height=34856.9, cameraPosition=(-220528,
    -361317, 119495), cameraUpVector=(-0.17335, 0.652878, 0.73736),
    cameraTarget=(-61727.1, -4001.69, 22564.9), viewOffsetX=-64496.8,
    viewOffsetY=42417.5)
session.viewports['Viewport: 1'].view.setValues(nearPlane=332733,
    farPlane=442448, width=88091.3, height=34941.2, cameraPosition=(-197852,
    -344196, 186247), cameraUpVector=(-0.18743, 0.761358, 0.620648),
    cameraTarget=(-60911.7, -1840.88, 23989), viewOffsetX=-64652.9,
    viewOffsetY=42520.1)
session.viewports['Viewport: 1'].view.setValues(nearPlane=333342,
    farPlane=459262, width=88252.6, height=35005.2, cameraPosition=(-224296,
    -305062, 251359), cameraUpVector=(-0.174987, 0.876031, 0.449389),
    cameraTarget=(-61787.9, -7622.27, 33625.3), viewOffsetX=-64771.3,
    viewOffsetY=42598)
session.viewports['Viewport: 1'].view.setValues(nearPlane=330829,
    farPlane=461775, width=121626, height=48242.6, viewOffsetX=-63131.5,
    viewOffsetY=40893.4)
session.viewports['Viewport: 1'].view.setValues(nearPlane=330147,
    farPlane=454904, width=121375, height=48143.2, cameraPosition=(-210355,
    -320606, 230984), cameraUpVector=(-0.222061, 0.839298, 0.496253),
    cameraTarget=(-60222.9, -3673.32, 32737.9), viewOffsetX=-63001.4,
    viewOffsetY=40809.1)
session.viewports['Viewport: 1'].view.setValues(nearPlane=330084,
    farPlane=450258, width=121352, height=48134, cameraPosition=(-202898,
    -331762, 212699), cameraUpVector=(-0.233809, 0.80754, 0.541491),
    cameraTarget=(-59747.2, -2055.87, 30795.8), viewOffsetX=-62989.4,
    viewOffsetY=40801.3)
session.viewports['Viewport: 1'].view.setValues(nearPlane=330903,
    farPlane=449438, width=107631, height=42691.6, viewOffsetX=-61518.3,
    viewOffsetY=40066.4)
a = mdb.models['Model-1'].rootAssembly
f1 = a.instances['P-1-1'].faces
faces1 = f1.getSequenceFromMask(mask=('[#3 ]', ), )
f2 = a.instances['P-2-1'].faces
faces2 = f2.getSequenceFromMask(mask=('[#ffff ]', ), )
f3 = a.instances['P-3-1'].faces
faces3 = f3.getSequenceFromMask(mask=('[#3 ]', ), )
f4 = a.instances['P-50-1'].faces
faces4 = f4.getSequenceFromMask(mask=('[#ffffff ]', ), )
f5 = a.instances['P-4-1'].faces
faces5 = f5.getSequenceFromMask(mask=('[#fff ]', ), )
f6 = a.instances['P-5-1'].faces
faces6 = f6.getSequenceFromMask(mask=('[#fff ]', ), )
f7 = a.instances['P-6-1'].faces
faces7 = f7.getSequenceFromMask(mask=('[#ffffffff:6 ]', ), )
f8 = a.instances['P-7-1'].faces
faces8 = f8.getSequenceFromMask(mask=('[#fff ]', ), )
f9 = a.instances['P-8-1'].faces
faces9 = f9.getSequenceFromMask(mask=('[#ffffffff #ffff ]', ), )
f10 = a.instances['P-9-1'].faces
faces10 = f10.getSequenceFromMask(mask=('[#ffffff ]', ), )
f11 = a.instances['P-10-1'].faces
faces11 = f11.getSequenceFromMask(mask=('[#7ffff ]', ), )
f12 = a.instances['P-11-1'].faces
faces12 = f12.getSequenceFromMask(mask=('[#3 ]', ), )
f13 = a.instances['P-12-1'].faces
faces13 = f13.getSequenceFromMask(mask=('[#3 ]', ), )
f14 = a.instances['P-13-1'].faces
faces14 = f14.getSequenceFromMask(mask=('[#3 ]', ), )
f15 = a.instances['P-14-1'].faces
faces15 = f15.getSequenceFromMask(mask=('[#f ]', ), )
f16 = a.instances['P-15-1'].faces
faces16 = f16.getSequenceFromMask(mask=('[#7 ]', ), )
f17 = a.instances['P-16-1'].faces
faces17 = f17.getSequenceFromMask(mask=('[#f ]', ), )
f18 = a.instances['P-17-1'].faces
faces18 = f18.getSequenceFromMask(mask=('[#3f ]', ), )
f19 = a.instances['P-18-1'].faces
faces19 = f19.getSequenceFromMask(mask=('[#3 ]', ), )
f20 = a.instances['P-19-1'].faces
faces20 = f20.getSequenceFromMask(mask=('[#f ]', ), )
f21 = a.instances['P-20-1'].faces
faces21 = f21.getSequenceFromMask(mask=('[#f ]', ), )
f22 = a.instances['P-21-1'].faces
faces22 = f22.getSequenceFromMask(mask=('[#7 ]', ), )
f23 = a.instances['P-22-1'].faces
faces23 = f23.getSequenceFromMask(mask=('[#3 ]', ), )
f24 = a.instances['P-23-1'].faces
faces24 = f24.getSequenceFromMask(mask=('[#7 ]', ), )
f25 = a.instances['P-24-1'].faces
faces25 = f25.getSequenceFromMask(mask=('[#3 ]', ), )
f26 = a.instances['P-25-1'].faces
faces26 = f26.getSequenceFromMask(mask=('[#3 ]', ), )
f27 = a.instances['P-26-1'].faces
faces27 = f27.getSequenceFromMask(mask=('[#ffffffff ]', ), )
f28 = a.instances['P-27-1'].faces
faces28 = f28.getSequenceFromMask(mask=('[#3 ]', ), )
f29 = a.instances['P-28-1'].faces
faces29 = f29.getSequenceFromMask(mask=('[#ff ]', ), )
f30 = a.instances['P-29-1'].faces
faces30 = f30.getSequenceFromMask(mask=('[#f ]', ), )
f31 = a.instances['P-30-1'].faces
faces31 = f31.getSequenceFromMask(mask=('[#3f ]', ), )
f32 = a.instances['P-31-1'].faces
faces32 = f32.getSequenceFromMask(mask=('[#1 ]', ), )
f33 = a.instances['P-32-1'].faces
faces33 = f33.getSequenceFromMask(mask=('[#3 ]', ), )
f34 = a.instances['P-33-1'].faces
faces34 = f34.getSequenceFromMask(mask=('[#3 ]', ), )
f35 = a.instances['P-34-1'].faces
faces35 = f35.getSequenceFromMask(mask=('[#3 ]', ), )
f36 = a.instances['P-35-1'].faces
faces36 = f36.getSequenceFromMask(mask=('[#f ]', ), )
f37 = a.instances['P-36-1'].faces
faces37 = f37.getSequenceFromMask(mask=('[#3 ]', ), )
f38 = a.instances['P-37-1'].faces
faces38 = f38.getSequenceFromMask(mask=('[#3 ]', ), )
f39 = a.instances['P-38-1'].faces
faces39 = f39.getSequenceFromMask(mask=('[#ffff ]', ), )
f40 = a.instances['P-39-1'].faces
faces40 = f40.getSequenceFromMask(mask=('[#3 ]', ), )
f41 = a.instances['P-40-1'].faces
faces41 = f41.getSequenceFromMask(mask=('[#ff ]', ), )
f42 = a.instances['P-41-1'].faces
faces42 = f42.getSequenceFromMask(mask=('[#f ]', ), )
f43 = a.instances['P-42-1'].faces
faces43 = f43.getSequenceFromMask(mask=('[#7 ]', ), )
f44 = a.instances['P-43-1'].faces
faces44 = f44.getSequenceFromMask(mask=('[#3f ]', ), )
f45 = a.instances['P-44-1'].faces
faces45 = f45.getSequenceFromMask(mask=('[#3f ]', ), )
f46 = a.instances['P-45-1'].faces
faces46 = f46.getSequenceFromMask(mask=('[#3 ]', ), )
f47 = a.instances['P-46-1'].faces
faces47 = f47.getSequenceFromMask(mask=('[#fffffff ]', ), )
f48 = a.instances['P-48-1'].faces
faces48 = f48.getSequenceFromMask(mask=('[#1 ]', ), )
f49 = a.instances['P-51-1'].faces
faces49 = f49.getSequenceFromMask(mask=('[#3 ]', ), )
e50 = a.instances['FZX-1'].edges
edges50 = e50.getSequenceFromMask(mask=('[#1ffff ]', ), )
a.Set(edges=edges50, faces=faces1+faces2+faces3+faces4+faces5+faces6+faces7+\
    faces8+faces9+faces10+faces11+faces12+faces13+faces14+faces15+faces16+\
    faces17+faces18+faces19+faces20+faces21+faces22+faces23+faces24+faces25+\
    faces26+faces27+faces28+faces29+faces30+faces31+faces32+faces33+faces34+\
    faces35+faces36+faces37+faces38+faces39+faces40+faces41+faces42+faces43+\
    faces44+faces45+faces46+faces47+faces48+faces49, name='SET-ALL')
#: The set 'SET-ALL' has been created (553 faces, 17 edges).
a = mdb.models['Model-1'].rootAssembly
region1=a.sets['SET-RP1']
a = mdb.models['Model-1'].rootAssembly
region2=a.sets['SET-RP2']
mdb.models['Model-1'].Coupling(name='Constraint-35', controlPoint=region1,
    surface=region2, influenceRadius=WHOLE_SURFACE, couplingType=KINEMATIC,
    localCsys=None, u1=ON, u2=ON, u3=ON, ur1=ON, ur2=ON, ur3=ON)
session.viewports['Viewport: 1'].view.setValues(nearPlane=332648,
    farPlane=447693, width=95727.1, height=37970, viewOffsetX=-65203.7,
    viewOffsetY=41001)
session.viewports['Viewport: 1'].view.setValues(nearPlane=330955,
    farPlane=490264, width=95240.1, height=37776.8, cameraPosition=(-333388,
    -305026, 171078), cameraUpVector=(-0.040405, 0.807809, 0.588057),
    cameraTarget=(-72078, -28826.6, 37967.8), viewOffsetX=-64872,
    viewOffsetY=40792.4)
session.viewports['Viewport: 1'].view.setValues(nearPlane=353352,
    farPlane=549340, width=101685, height=40333.3, cameraPosition=(-525101,
    -123953, 61191.4), cameraUpVector=(0.258352, 0.67018, 0.695782),
    cameraTarget=(-128776, -54795.7, 40412.9), viewOffsetX=-69262.1,
    viewOffsetY=43553)
session.viewports['Viewport: 1'].view.setValues(nearPlane=348992,
    farPlane=553702, width=151062, height=59918.3, viewOffsetX=-57827.2,
    viewOffsetY=41614.5)
session.viewports['Viewport: 1'].view.setValues(nearPlane=348482,
    farPlane=554211, width=150841, height=59830.8, cameraPosition=(-525066,
    -123852, 62188.2), cameraUpVector=(0.256681, 0.677736, 0.689049),
    cameraTarget=(-128741, -54694.8, 41409.7), viewOffsetX=-57742.8,
    viewOffsetY=41553.8)
session.viewports['Viewport: 1'].view.setValues(nearPlane=343542,
    farPlane=559151, width=215470, height=85465.8, viewOffsetX=-38626,
    viewOffsetY=41693.2)
session.viewports['Viewport: 1'].view.setValues(nearPlane=338494,
    farPlane=541889, width=212304, height=84210, cameraPosition=(-450357,
    -258270, 70348.2), cameraUpVector=(0.0573802, 0.696869, 0.714899),
    cameraTarget=(-100287, -61516.6, 38292.9), viewOffsetX=-38058.4,
    viewOffsetY=41080.5)
session.viewports['Viewport: 1'].view.setValues(nearPlane=347411,
    farPlane=532972, width=108858, height=43178.5, viewOffsetX=-37059.8,
    viewOffsetY=43138)
session.viewports['Viewport: 1'].view.setValues(nearPlane=349560,
    farPlane=523922, width=109532, height=43445.6, cameraPosition=(-408878,
    -302876, 80263.9), cameraUpVector=(-0.0136582, 0.697693, 0.716267),
    cameraTarget=(-89821, -60613.5, 37842.6), viewOffsetX=-37289,
    viewOffsetY=43404.8)
session.viewports['Viewport: 1'].view.setValues(nearPlane=354942,
    farPlane=518540, width=45304.7, height=17970, viewOffsetX=-56890.2,
    viewOffsetY=45955.6)
a = mdb.models['Model-1'].rootAssembly
region1=a.sets['SET-RP3']
a = mdb.models['Model-1'].rootAssembly
region2=a.sets['SET-RP4']
mdb.models['Model-1'].Coupling(name='Constraint-36', controlPoint=region1,
    surface=region2, influenceRadius=WHOLE_SURFACE, couplingType=KINEMATIC,
    localCsys=None, u1=ON, u2=ON, u3=ON, ur1=ON, ur2=ON, ur3=ON)
session.viewports['Viewport: 1'].view.setValues(nearPlane=351221,
    farPlane=522260, width=93472.9, height=37075.9, viewOffsetX=-50843.9,
    viewOffsetY=42795.1)
session.viewports['Viewport: 1'].view.setValues(nearPlane=381556,
    farPlane=467145, width=101546, height=40278.1, cameraPosition=(-112814,
    -339794, 291919), cameraUpVector=(0.109552, 0.869042, 0.482457),
    cameraTarget=(-58199.2, -43622.9, 24359.2), viewOffsetX=-55235.2,
    viewOffsetY=46491.3)
session.viewports['Viewport: 1'].view.setValues(nearPlane=383013,
    farPlane=465689, width=79928.4, height=31703.5, viewOffsetX=-80455.6,
    viewOffsetY=32932.3)
session.viewports['Viewport: 1'].view.setValues(nearPlane=370774,
    farPlane=529440, width=77374.4, height=30690.4, cameraPosition=(-352926,
    -335182, 193987), cameraUpVector=(-0.0732407, 0.819581, 0.568263),
    cameraTarget=(-83699.2, -61946.4, 70912.1), viewOffsetX=-77884.8,
    viewOffsetY=31880)
session.viewports['Viewport: 1'].view.setValues(nearPlane=372225,
    farPlane=527989, width=60802.4, height=24117.2, viewOffsetX=-80751,
    viewOffsetY=31181.5)
session.viewports['Viewport: 1'].view.setValues(nearPlane=379187,
    farPlane=491804, width=61939.6, height=24568.2, cameraPosition=(-255539,
    -412302, 58197), cameraUpVector=(-0.241328, 0.553431, 0.797167),
    cameraTarget=(-61677.5, -59609.8, 40477.3), viewOffsetX=-82261.3,
    viewOffsetY=31764.7)
session.viewports['Viewport: 1'].view.setValues(nearPlane=377834,
    farPlane=493156, width=73300.3, height=29074.4, viewOffsetX=-84753,
    viewOffsetY=57195.6)
session.viewports['Viewport: 1'].view.setValues(nearPlane=378818,
    farPlane=476526, width=73491.1, height=29150.1, cameraPosition=(-212163,
    -420556, 31871.8), cameraUpVector=(-0.256193, 0.47338, 0.842779),
    cameraTarget=(-54211.5, -49964, 31060.3), viewOffsetX=-84973.7,
    viewOffsetY=57344.5)
session.viewports['Viewport: 1'].view.setValues(nearPlane=379855,
    farPlane=467416, width=73692.3, height=29229.9, cameraPosition=(-172769,
    -424101, 66640.2), cameraUpVector=(-0.219612, 0.510627, 0.831282),
    cameraTarget=(-50192, -42495, 26150.6), viewOffsetX=-85206.3,
    viewOffsetY=57501.5)
session.viewports['Viewport: 1'].view.setValues(nearPlane=378616,
    farPlane=477229, width=73452, height=29134.6, cameraPosition=(-212698,
    -420534, 34734.3), cameraUpVector=(-0.224746, 0.474145, 0.851279),
    cameraTarget=(-54511.2, -50104.8, 27915.4), viewOffsetX=-84928.4,
    viewOffsetY=57314)
session.viewports['Viewport: 1'].view.setValues(nearPlane=382804,
    farPlane=473040, width=24666.3, height=9783.85, viewOffsetX=-95957.8,
    viewOffsetY=56774.1)
a = mdb.models['Model-1'].rootAssembly
region1=a.sets['SET-RP5']
a = mdb.models['Model-1'].rootAssembly
region2=a.sets['SET-RP6']
mdb.models['Model-1'].Coupling(name='Constraint-37', controlPoint=region1,
    surface=region2, influenceRadius=WHOLE_SURFACE, couplingType=KINEMATIC,
    localCsys=None, u1=ON, u2=ON, u3=ON, ur1=ON, ur2=ON, ur3=ON)
a = mdb.models['Model-1'].rootAssembly
region1=a.sets['SET-RP7']
a = mdb.models['Model-1'].rootAssembly
region2=a.sets['SET-RP8']
mdb.models['Model-1'].Coupling(name='Constraint-38', controlPoint=region1,
    surface=region2, influenceRadius=WHOLE_SURFACE, couplingType=KINEMATIC,
    localCsys=None, u1=ON, u2=ON, u3=ON, ur1=ON, ur2=ON, ur3=ON)
session.viewports['Viewport: 1'].view.setValues(nearPlane=382062,
    farPlane=473783, width=35610.3, height=14124.7, viewOffsetX=-93688,
    viewOffsetY=56555.1)
a = mdb.models['Model-1'].rootAssembly
region1=a.sets['SET-RP9']
a = mdb.models['Model-1'].rootAssembly
region2=a.sets['SET-RP10']
mdb.models['Model-1'].Coupling(name='Constraint-39', controlPoint=region1,
    surface=region2, influenceRadius=WHOLE_SURFACE, couplingType=KINEMATIC,
    localCsys=None, u1=ON, u2=ON, u3=ON, ur1=ON, ur2=ON, ur3=ON)
a = mdb.models['Model-1'].rootAssembly
region1=a.sets['SET-RP11']
a = mdb.models['Model-1'].rootAssembly
region2=a.sets['SET-RP12']
mdb.models['Model-1'].Coupling(name='Constraint-40', controlPoint=region1,
    surface=region2, influenceRadius=WHOLE_SURFACE, couplingType=KINEMATIC,
    localCsys=None, u1=ON, u2=ON, u3=ON, ur1=ON, ur2=ON, ur3=ON)
session.viewports['Viewport: 1'].view.setValues(nearPlane=381935,
    farPlane=473909, width=34233.9, height=13578.8, viewOffsetX=-89520.2,
    viewOffsetY=56247.7)
a = mdb.models['Model-1'].rootAssembly
region1=a.sets['SET-RP13']
a = mdb.models['Model-1'].rootAssembly
region2=a.sets['SET-RP14']
mdb.models['Model-1'].Coupling(name='Constraint-41', controlPoint=region1,
    surface=region2, influenceRadius=WHOLE_SURFACE, couplingType=KINEMATIC,
    localCsys=None, u1=ON, u2=ON, u3=ON, ur1=ON, ur2=ON, ur3=ON)
# mdb.save()
#: The model database has been saved to "F:\temp\A-abaqus-2.cae".
a = mdb.models['Model-1'].rootAssembly
region1=a.sets['SET-RP15']
a = mdb.models['Model-1'].rootAssembly
region2=a.sets['SET-RP16']
mdb.models['Model-1'].Coupling(name='Constraint-42', controlPoint=region1,
    surface=region2, influenceRadius=WHOLE_SURFACE, couplingType=KINEMATIC,
    localCsys=None, u1=ON, u2=ON, u3=ON, ur1=ON, ur2=ON, ur3=ON)
session.viewports['Viewport: 1'].view.setValues(nearPlane=381235,
    farPlane=474609, width=45473.9, height=18037.1, viewOffsetX=-87113.4,
    viewOffsetY=57165)
mdb.models['Model-1'].constraints['Constraint-42'].suppress()
session.viewports['Viewport: 1'].view.setValues(nearPlane=382291,
    farPlane=473553, width=30316.2, height=12024.9, viewOffsetX=-92156,
    viewOffsetY=56722.8)
i1 = mdb.models['Model-1'].rootAssembly.allInstances['P-11-1']
i2 = mdb.models['Model-1'].rootAssembly.allInstances['P-12-1']
leaf = dgm.LeafFromInstance(instances=(i1, i2, ))
session.viewports['Viewport: 1'].assemblyDisplay.displayGroup.replace(
    leaf=leaf)
i1 = mdb.models['Model-1'].rootAssembly.allInstances['P-11-1']
leaf = dgm.LeafFromInstance(instances=(i1, ))
session.viewports['Viewport: 1'].assemblyDisplay.displayGroup.replace(
    leaf=leaf)
session.viewports['Viewport: 1'].view.setValues(nearPlane=389551,
    farPlane=398952, width=20538, height=8146.36, viewOffsetX=-95802.5,
    viewOffsetY=57442.9)
i1 = mdb.models['Model-1'].rootAssembly.allInstances['P-12-1']
leaf = dgm.LeafFromInstance(instances=(i1, ))
session.viewports['Viewport: 1'].assemblyDisplay.displayGroup.replace(
    leaf=leaf)
session.viewports['Viewport: 1'].view.setValues(width=21380.4, height=8480.49,
    viewOffsetX=-95619.3, viewOffsetY=57400)
a = mdb.models['Model-1'].rootAssembly
s1 = a.instances['P-11-1'].edges
side1Edges1 = s1.getSequenceFromMask(mask=('[#5 ]', ), )
region1=regionToolset.Region(side1Edges=side1Edges1)
a = mdb.models['Model-1'].rootAssembly
s1 = a.instances['P-12-1'].edges
side1Edges1 = s1.getSequenceFromMask(mask=('[#24 ]', ), )
region2=regionToolset.Region(side1Edges=side1Edges1)
mdb.models['Model-1'].Tie(name='Constraint-43', main=region1,
    secondary=region2, positionToleranceMethod=COMPUTED, adjust=ON,
    tieRotations=ON, thickness=ON)
leaf = dgm.Leaf(leafType=DEFAULT_MODEL)
session.viewports['Viewport: 1'].assemblyDisplay.displayGroup.replace(
    leaf=leaf)
i1 = mdb.models['Model-1'].rootAssembly.allInstances['P-18-1']
i2 = mdb.models['Model-1'].rootAssembly.allInstances['P-19-1']
leaf = dgm.LeafFromInstance(instances=(i1, i2, ))
session.viewports['Viewport: 1'].assemblyDisplay.displayGroup.replace(
    leaf=leaf)
session.viewports['Viewport: 1'].view.setValues(nearPlane=391125,
    farPlane=399708, width=19004.3, height=7538.04, viewOffsetX=-93401.2,
    viewOffsetY=57374.1)
i1 = mdb.models['Model-1'].rootAssembly.allInstances['P-18-1']
leaf = dgm.LeafFromInstance(instances=(i1, ))
session.viewports['Viewport: 1'].assemblyDisplay.displayGroup.replace(
    leaf=leaf)
i1 = mdb.models['Model-1'].rootAssembly.allInstances['P-19-1']
leaf = dgm.LeafFromInstance(instances=(i1, ))
session.viewports['Viewport: 1'].assemblyDisplay.displayGroup.replace(
    leaf=leaf)
a = mdb.models['Model-1'].rootAssembly
s1 = a.instances['P-18-1'].edges
side1Edges1 = s1.getSequenceFromMask(mask=('[#5 ]', ), )
region1=regionToolset.Region(side1Edges=side1Edges1)
a = mdb.models['Model-1'].rootAssembly
s1 = a.instances['P-19-1'].edges
side1Edges1 = s1.getSequenceFromMask(mask=('[#1010 ]', ), )
region2=regionToolset.Region(side1Edges=side1Edges1)
mdb.models['Model-1'].Tie(name='Constraint-44', main=region1,
    secondary=region2, positionToleranceMethod=COMPUTED, adjust=ON,
    tieRotations=ON, thickness=ON)
leaf = dgm.Leaf(leafType=DEFAULT_MODEL)
session.viewports['Viewport: 1'].assemblyDisplay.displayGroup.replace(
    leaf=leaf)
session.viewports['Viewport: 1'].view.setValues(nearPlane=382605,
    farPlane=473239, width=29127.6, height=11553.4, viewOffsetX=-89424.2,
    viewOffsetY=56845.3)
session.viewports['Viewport: 1'].view.setValues(nearPlane=384325,
    farPlane=471519, width=7923.79, height=3142.96, viewOffsetX=-80934,
    viewOffsetY=56270.6)
i1 = mdb.models['Model-1'].rootAssembly.allInstances['P-31-1']
i2 = mdb.models['Model-1'].rootAssembly.allInstances['P-32-1']
leaf = dgm.LeafFromInstance(instances=(i1, i2, ))
session.viewports['Viewport: 1'].assemblyDisplay.displayGroup.replace(
    leaf=leaf)
i1 = mdb.models['Model-1'].rootAssembly.allInstances['P-31-1']
leaf = dgm.LeafFromInstance(instances=(i1, ))
session.viewports['Viewport: 1'].assemblyDisplay.displayGroup.replace(
    leaf=leaf)
session.viewports['Viewport: 1'].view.setValues(nearPlane=398385,
    farPlane=399835, width=6697.2, height=2656.43, viewOffsetX=-84226.6,
    viewOffsetY=58219.8)
i1 = mdb.models['Model-1'].rootAssembly.allInstances['P-32-1']
leaf = dgm.LeafFromInstance(instances=(i1, ))
session.viewports['Viewport: 1'].assemblyDisplay.displayGroup.replace(
    leaf=leaf)
a = mdb.models['Model-1'].rootAssembly
s1 = a.instances['P-31-1'].edges
side1Edges1 = s1.getSequenceFromMask(mask=('[#1 ]', ), )
region1=regionToolset.Region(side1Edges=side1Edges1)
a = mdb.models['Model-1'].rootAssembly
s1 = a.instances['P-32-1'].edges
side1Edges1 = s1.getSequenceFromMask(mask=('[#10 ]', ), )
region2=regionToolset.Region(side1Edges=side1Edges1)
mdb.models['Model-1'].Tie(name='Constraint-45', main=region1,
    secondary=region2, positionToleranceMethod=COMPUTED, adjust=ON,
    tieRotations=ON, thickness=ON)
leaf = dgm.Leaf(leafType=DEFAULT_MODEL)
session.viewports['Viewport: 1'].assemblyDisplay.displayGroup.replace(
    leaf=leaf)
session.viewports['Viewport: 1'].view.setValues(nearPlane=381782,
    farPlane=474062, width=38948.6, height=15448.9, viewOffsetX=-88055.6,
    viewOffsetY=59705.9)
i1 = mdb.models['Model-1'].rootAssembly.allInstances['P-12-1']
i2 = mdb.models['Model-1'].rootAssembly.allInstances['P-13-1']
leaf = dgm.LeafFromInstance(instances=(i1, i2, ))
session.viewports['Viewport: 1'].assemblyDisplay.displayGroup.replace(
    leaf=leaf)
session.viewports['Viewport: 1'].view.setValues(nearPlane=388133,
    farPlane=400120, width=30994.5, height=12293.9, viewOffsetX=-92156.1,
    viewOffsetY=59049)
i1 = mdb.models['Model-1'].rootAssembly.allInstances['P-12-1']
leaf = dgm.LeafFromInstance(instances=(i1, ))
session.viewports['Viewport: 1'].assemblyDisplay.displayGroup.replace(
    leaf=leaf)
i1 = mdb.models['Model-1'].rootAssembly.allInstances['P-12-1']
leaf = dgm.LeafFromInstance(instances=(i1, ))
session.viewports['Viewport: 1'].assemblyDisplay.displayGroup.replace(
    leaf=leaf)
i1 = mdb.models['Model-1'].rootAssembly.allInstances['P-13-1']
leaf = dgm.LeafFromInstance(instances=(i1, ))
session.viewports['Viewport: 1'].assemblyDisplay.displayGroup.replace(
    leaf=leaf)
session.viewports['Viewport: 1'].view.setValues(nearPlane=388335,
    farPlane=399859, width=26338.8, height=10447.2, viewOffsetX=-93445.9,
    viewOffsetY=58589.5)
a = mdb.models['Model-1'].rootAssembly
s1 = a.instances['P-12-1'].edges
side1Edges1 = s1.getSequenceFromMask(mask=('[#11 ]', ), )
region1=regionToolset.Region(side1Edges=side1Edges1)
a = mdb.models['Model-1'].rootAssembly
s1 = a.instances['P-13-1'].edges
side1Edges1 = s1.getSequenceFromMask(mask=('[#1200 ]', ), )
region2=regionToolset.Region(side1Edges=side1Edges1)
mdb.models['Model-1'].Tie(name='Constraint-46', main=region1,
    secondary=region2, positionToleranceMethod=COMPUTED, adjust=ON,
    tieRotations=ON, thickness=ON)
leaf = dgm.Leaf(leafType=DEFAULT_MODEL)
session.viewports['Viewport: 1'].assemblyDisplay.displayGroup.replace(
    leaf=leaf)
session.viewports['Viewport: 1'].view.setValues(nearPlane=381499,
    farPlane=474345, width=42304.1, height=16779.9, viewOffsetX=-86860.8,
    viewOffsetY=57152.7)
session.viewports['Viewport: 1'].view.setValues(nearPlane=380878,
    farPlane=474966, width=49726.8, height=19724.1, viewOffsetX=-84774.7,
    viewOffsetY=56827.4)
i1 = mdb.models['Model-1'].rootAssembly.allInstances['P-4-1']
i2 = mdb.models['Model-1'].rootAssembly.allInstances['P-5-1']
leaf = dgm.LeafFromInstance(instances=(i1, i2, ))
session.viewports['Viewport: 1'].assemblyDisplay.displayGroup.replace(
    leaf=leaf)
session.viewports['Viewport: 1'].view.setValues(nearPlane=385073,
    farPlane=402118, width=30964.7, height=12282.1, viewOffsetX=-89512,
    viewOffsetY=57967.8)
i1 = mdb.models['Model-1'].rootAssembly.allInstances['P-4-1']
leaf = dgm.LeafFromInstance(instances=(i1, ))
session.viewports['Viewport: 1'].assemblyDisplay.displayGroup.replace(
    leaf=leaf)
session.viewports['Viewport: 1'].view.setValues(nearPlane=384959,
    farPlane=403341, width=46561.4, height=18468.5, viewOffsetX=-87605.8,
    viewOffsetY=57406.1)
session.viewports['Viewport: 1'].view.setValues(nearPlane=378303,
    farPlane=404938, width=45756.3, height=18149.2, cameraPosition=(-414901,
    -303902, 173393), cameraUpVector=(0.250194, 0.716291, 0.651406),
    cameraTarget=(-93380.8, -103805, 36013.4), viewOffsetX=-86091.1,
    viewOffsetY=56413.6)
session.viewports['Viewport: 1'].view.setValues(nearPlane=377351,
    farPlane=404687, width=45641.1, height=18103.5, cameraPosition=(-433228,
    -180843, 293775), cameraUpVector=(0.383743, 0.886135, 0.25982),
    cameraTarget=(-104366, -107025, 73120.3), viewOffsetX=-85874.4,
    viewOffsetY=56271.6)
session.viewports['Viewport: 1'].view.setValues(nearPlane=379773,
    farPlane=402265, width=18743.8, height=7434.69, viewOffsetX=-90058.7,
    viewOffsetY=59200.6)
i1 = mdb.models['Model-1'].rootAssembly.allInstances['P-5-1']
leaf = dgm.LeafFromInstance(instances=(i1, ))
session.viewports['Viewport: 1'].assemblyDisplay.displayGroup.replace(
    leaf=leaf)
session.viewports['Viewport: 1'].view.setValues(nearPlane=377252,
    farPlane=402173, width=23911.2, height=9484.34, viewOffsetX=-93450.4,
    viewOffsetY=57432.1)
session.viewports['Viewport: 1'].view.setValues(nearPlane=377212,
    farPlane=402019, width=23908.7, height=9483.35, cameraPosition=(-386442,
    -200838, 323811), cameraUpVector=(0.34638, 0.912182, 0.218965),
    cameraTarget=(-94123.7, -102425, 64672.6), viewOffsetX=-93440.5,
    viewOffsetY=57426.1)
session.viewports['Viewport: 1'].view.setValues(nearPlane=378156,
    farPlane=401075, width=13628.9, height=5405.86, viewOffsetX=-88628,
    viewOffsetY=59855.7)
session.viewports['Viewport: 1'].view.setValues(nearPlane=378934,
    farPlane=401382, width=13656.9, height=5416.98, cameraPosition=(-345132,
    -222967, 338433), cameraUpVector=(0.327231, 0.918821, 0.220653),
    cameraTarget=(-88485.4, -99774.6, 53400.4), viewOffsetX=-88810.3,
    viewOffsetY=59978.8)
session.viewports['Viewport: 1'].view.setValues(nearPlane=379362,
    farPlane=400954, width=9089.8, height=3605.45, viewOffsetX=-88398.4,
    viewOffsetY=60506)
a = mdb.models['Model-1'].rootAssembly
s1 = a.instances['P-4-1'].edges
side1Edges1 = s1.getSequenceFromMask(mask=('[#8a28a28 #88a02002 #2888 ]', ), )
region1=regionToolset.Region(side1Edges=side1Edges1)
a = mdb.models['Model-1'].rootAssembly
s1 = a.instances['P-5-1'].edges
side1Edges1 = s1.getSequenceFromMask(mask=('[#55aaaaaa #885145 ]', ), )
region2=regionToolset.Region(side1Edges=side1Edges1)
mdb.models['Model-1'].Tie(name='Constraint-47', main=region1,
    secondary=region2, positionToleranceMethod=COMPUTED, adjust=ON,
    tieRotations=ON, thickness=ON)
session.viewports['Viewport: 1'].view.setValues(nearPlane=377535,
    farPlane=402780, width=30891, height=12252.8, viewOffsetX=-90027.8,
    viewOffsetY=58835.8)
leaf = dgm.Leaf(leafType=DEFAULT_MODEL)
session.viewports['Viewport: 1'].assemblyDisplay.displayGroup.replace(
    leaf=leaf)
session.viewports['Viewport: 1'].view.setValues(nearPlane=371139,
    farPlane=531043, width=42096, height=16697.3, viewOffsetX=-89018,
    viewOffsetY=56300.1)
session.viewports['Viewport: 1'].view.setValues(nearPlane=370541,
    farPlane=528642, width=42028.2, height=16670.4, cameraPosition=(-336634,
    -243217, 328676), cameraUpVector=(0.309659, 0.914455, 0.260544),
    cameraTarget=(-85454.1, -101318, 47498.3), viewOffsetX=-88874.6,
    viewOffsetY=56209.4)
session.viewports['Viewport: 1'].view.setValues(nearPlane=369346,
    farPlane=529838, width=58072.2, height=23034.2, viewOffsetX=-83478,
    viewOffsetY=57247.4)
session.viewports['Viewport: 1'].view.setValues(nearPlane=369368,
    farPlane=544210, width=58075.7, height=23035.6, cameraPosition=(-389551,
    -252782, 279106), cameraUpVector=(0.217952, 0.92244, 0.318749),
    cameraTarget=(-91602.8, -100169, 54999.9), viewOffsetX=-83483.1,
    viewOffsetY=57250.9)
session.viewports['Viewport: 1'].view.setValues(nearPlane=370910,
    farPlane=542668, width=42070.1, height=16687, viewOffsetX=-79976.4,
    viewOffsetY=62098.1)
session.viewports['Viewport: 1'].view.setValues(nearPlane=370487,
    farPlane=540287, width=42022.1, height=16668, cameraPosition=(-379453,
    -267272, 273910), cameraUpVector=(0.183902, 0.924023, 0.335203),
    cameraTarget=(-87173.9, -99934.1, 52869.7), viewOffsetX=-79885.3,
    viewOffsetY=62027.4)
session.viewports['Viewport: 1'].view.setValues(nearPlane=371068,
    farPlane=542919, width=42088, height=16694.2, cameraPosition=(-388624,
    -237657, 294246), cameraUpVector=(0.248932, 0.92573, 0.284706),
    cameraTarget=(-93185.9, -99348.7, 57867.1), viewOffsetX=-80010.6,
    viewOffsetY=62124.7)
session.viewports['Viewport: 1'].view.setValues(nearPlane=369452,
    farPlane=544535, width=63030.8, height=25001.1, viewOffsetX=-71178.5,
    viewOffsetY=63048.8)
i1 = mdb.models['Model-1'].rootAssembly.allInstances['P-3-1']
i2 = mdb.models['Model-1'].rootAssembly.allInstances['P-50-1']
leaf = dgm.LeafFromInstance(instances=(i1, i2, ))
session.viewports['Viewport: 1'].assemblyDisplay.displayGroup.replace(
    leaf=leaf)
session.viewports['Viewport: 1'].view.setValues(nearPlane=379882,
    farPlane=391151, width=22423.1, height=8894.09, viewOffsetX=-93317.7,
    viewOffsetY=61927.1)
i1 = mdb.models['Model-1'].rootAssembly.allInstances['P-3-1']
leaf = dgm.LeafFromInstance(instances=(i1, ))
session.viewports['Viewport: 1'].assemblyDisplay.displayGroup.replace(
    leaf=leaf)
session.viewports['Viewport: 1'].view.setValues(nearPlane=380719,
    farPlane=390314, width=13218.3, height=5243.03, viewOffsetX=-96579.6,
    viewOffsetY=61037.1)
i1 = mdb.models['Model-1'].rootAssembly.allInstances['P-50-1']
leaf = dgm.LeafFromInstance(instances=(i1, ))
session.viewports['Viewport: 1'].assemblyDisplay.displayGroup.replace(
    leaf=leaf)
session.viewports['Viewport: 1'].view.setValues(nearPlane=381883,
    farPlane=389215, width=10015.4, height=3972.58, viewOffsetX=-98229.3,
    viewOffsetY=60879.9)
a = mdb.models['Model-1'].rootAssembly
s1 = a.instances['P-3-1'].edges
side1Edges1 = s1.getSequenceFromMask(mask=('[#36 ]', ), )
region1=regionToolset.Region(side1Edges=side1Edges1)
a = mdb.models['Model-1'].rootAssembly
s1 = a.instances['P-50-1'].edges
side1Edges1 = s1.getSequenceFromMask(mask=('[#82224202 #4110480 ]', ), )
region2=regionToolset.Region(side1Edges=side1Edges1)
mdb.models['Model-1'].Tie(name='Constraint-48', main=region1,
    secondary=region2, positionToleranceMethod=COMPUTED, adjust=ON,
    tieRotations=ON, thickness=ON)
leaf = dgm.Leaf(leafType=DEFAULT_MODEL)
session.viewports['Viewport: 1'].assemblyDisplay.displayGroup.replace(
    leaf=leaf)
session.viewports['Viewport: 1'].view.setValues(nearPlane=373550,
    farPlane=540438, width=14146.4, height=5611.12, viewOffsetX=-94286.1,
    viewOffsetY=59347.5)
i1 = mdb.models['Model-1'].rootAssembly.allInstances['P-8-1']
i2 = mdb.models['Model-1'].rootAssembly.allInstances['P-9-1']
leaf = dgm.LeafFromInstance(instances=(i1, i2, ))
session.viewports['Viewport: 1'].assemblyDisplay.displayGroup.replace(
    leaf=leaf)
session.viewports['Viewport: 1'].view.setValues(nearPlane=378957,
    farPlane=403301, width=34003.4, height=13487.4, viewOffsetX=-89602.9,
    viewOffsetY=61994.6)
i1 = mdb.models['Model-1'].rootAssembly.allInstances['P-7-1']
i2 = mdb.models['Model-1'].rootAssembly.allInstances['P-8-1']
i3 = mdb.models['Model-1'].rootAssembly.allInstances['P-9-1']
leaf = dgm.LeafFromInstance(instances=(i1, i2, i3, ))
session.viewports['Viewport: 1'].assemblyDisplay.displayGroup.replace(
    leaf=leaf)
i1 = mdb.models['Model-1'].rootAssembly.allInstances['P-7-1']
i2 = mdb.models['Model-1'].rootAssembly.allInstances['P-8-1']
i3 = mdb.models['Model-1'].rootAssembly.allInstances['P-9-1']
leaf = dgm.LeafFromInstance(instances=(i1, i2, i3, ))
session.viewports['Viewport: 1'].assemblyDisplay.displayGroup.replace(
    leaf=leaf)
i1 = mdb.models['Model-1'].rootAssembly.allInstances['P-7-1']
leaf = dgm.LeafFromInstance(instances=(i1, ))
session.viewports['Viewport: 1'].assemblyDisplay.displayGroup.replace(
    leaf=leaf)
session.viewports['Viewport: 1'].view.setValues(nearPlane=381507,
    farPlane=400742, width=7334, height=2909.02, viewOffsetX=-80546.6,
    viewOffsetY=64819.8)
i1 = mdb.models['Model-1'].rootAssembly.allInstances['P-8-1']
i2 = mdb.models['Model-1'].rootAssembly.allInstances['P-9-1']
leaf = dgm.LeafFromInstance(instances=(i1, i2, ))
session.viewports['Viewport: 1'].assemblyDisplay.displayGroup.replace(
    leaf=leaf)
session.viewports['Viewport: 1'].view.setValues(nearPlane=380565,
    farPlane=401693, width=14810.8, height=5874.69, viewOffsetX=-79340.6,
    viewOffsetY=65197.5)
session.viewports['Viewport: 1'].view.setValues(nearPlane=373114,
    farPlane=393878, width=14520.9, height=5759.67, cameraPosition=(-423683,
    -150071, -225774), cameraUpVector=(-0.248654, 0.789921, 0.560532),
    cameraTarget=(-164220, -115716, 80471.5), viewOffsetX=-77787.3,
    viewOffsetY=63921)
session.viewports['Viewport: 1'].view.setValues(nearPlane=373523,
    farPlane=393468, width=10541.6, height=4181.3, viewOffsetX=-77332.3,
    viewOffsetY=70199.5)
a = mdb.models['Model-1'].rootAssembly
s1 = a.instances['P-7-1'].edges
side1Edges1 = s1.getSequenceFromMask(mask=('[#ffffffff #ffff ]', ), )
region1=regionToolset.Region(side1Edges=side1Edges1)
a = mdb.models['Model-1'].rootAssembly
s1 = a.instances['P-8-1'].edges
side1Edges1 = s1.getSequenceFromMask(mask=(
    '[#10204081 #81020408 #8102040 #40810204 #4081020 #10 ]', ), )
s2 = a.instances['P-9-1'].edges
side1Edges2 = s2.getSequenceFromMask(mask=(
    '[#8104102 #10208104 #10408204 #8208204 #82082 ]', ), )
region2=regionToolset.Region(side1Edges=side1Edges1+side1Edges2)
mdb.models['Model-1'].Tie(name='Constraint-49', main=region1,
    secondary=region2, positionToleranceMethod=COMPUTED, adjust=ON,
    tieRotations=ON, thickness=ON)
session.viewports['Viewport: 1'].view.setValues(nearPlane=373132,
    farPlane=393859, width=15205.9, height=6031.37, viewOffsetX=-77323.1,
    viewOffsetY=70352.2)
leaf = dgm.Leaf(leafType=DEFAULT_MODEL)
session.viewports['Viewport: 1'].assemblyDisplay.displayGroup.replace(
    leaf=leaf)
session.viewports['Viewport: 1'].view.setValues(nearPlane=340267,
    farPlane=496741, width=20857.2, height=8272.97, viewOffsetX=-69765.1,
    viewOffsetY=64114.9)
session.viewports['Viewport: 1'].view.setValues(nearPlane=341522,
    farPlane=428816, width=20934.1, height=8303.47, cameraPosition=(-294858,
    -81620.7, -328897), cameraUpVector=(-0.0863353, 0.919941, 0.382433),
    cameraTarget=(-215982, -92418, 66007.7), viewOffsetX=-70022.3,
    viewOffsetY=64351.3)
session.viewports['Viewport: 1'].view.setValues(nearPlane=339044,
    farPlane=431294, width=51284.8, height=20342, viewOffsetX=-62370.2,
    viewOffsetY=64104)
session.viewports['Viewport: 1'].view.setValues(nearPlane=360436,
    farPlane=461469, width=54520.6, height=21625.5, cameraPosition=(-353886,
    -356775, 63978.8), cameraUpVector=(-0.125752, 0.577954, -0.806322),
    cameraTarget=(-198703, 8172.41, 134827), viewOffsetX=-66305.4,
    viewOffsetY=68148.6)
session.viewports['Viewport: 1'].view.setValues(nearPlane=374770,
    farPlane=560297, width=56688.8, height=22485.5, cameraPosition=(-486711,
    256329, -56623), cameraUpVector=(0.502789, -0.457105, -0.733661),
    cameraTarget=(-140150, 110932, 88439.8), viewOffsetX=-68942.3,
    viewOffsetY=70858.8)
session.viewports['Viewport: 1'].view.setValues(nearPlane=373930,
    farPlane=559243, width=56561.8, height=22435.1, cameraPosition=(-545995,
    18357.9, -140299), cameraUpVector=(0.80041, 0.0108436, -0.599355),
    cameraTarget=(-212686, 62674.2, 81577.3), viewOffsetX=-68787.9,
    viewOffsetY=70700.1)
session.viewports['Viewport: 1'].view.setValues(nearPlane=368651,
    farPlane=564523, width=121959, height=48374.8, viewOffsetX=-62080.8,
    viewOffsetY=63655.1)
session.viewports['Viewport: 1'].view.setValues(nearPlane=385184,
    farPlane=496158, width=127429, height=50544.3, cameraPosition=(-215515,
    203091, -360035), cameraUpVector=(0.738041, -0.674421, 0.0212739),
    cameraTarget=(-126972, 112946, 22485.3), viewOffsetX=-64865.1,
    viewOffsetY=66510)
session.viewports['Viewport: 1'].view.setValues(nearPlane=380290,
    farPlane=490554, width=125810, height=49902.1, cameraPosition=(-195384,
    -295732, -299651), cameraUpVector=(0.445009, -0.321207, 0.835938),
    cameraTarget=(-88059, 20668.2, -74573.4), viewOffsetX=-64040.9,
    viewOffsetY=65664.9)
session.viewports['Viewport: 1'].view.setValues(nearPlane=332672,
    farPlane=492937, width=110057, height=43653.7, cameraPosition=(199580,
    -220953, -201391), cameraUpVector=(-0.153825, -0.244068, 0.95748),
    cameraTarget=(-41504.7, 52615.9, -30143.4), viewOffsetX=-56022.1,
    viewOffsetY=57442.8)
session.viewports['Viewport: 1'].view.setValues(nearPlane=365174,
    farPlane=465630, width=120809, height=47918.6, cameraPosition=(113608,
    -360830, -102313), cameraUpVector=(-0.337581, 0.0589387, 0.939449),
    cameraTarget=(-15339.7, 13758.1, -29212.6), viewOffsetX=-61495.4,
    viewOffsetY=63054.9)
session.viewports['Viewport: 1'].view.setValues(nearPlane=372096,
    farPlane=458708, width=29494.9, height=11699.1, viewOffsetX=-102488,
    viewOffsetY=90721)
session.viewports['Viewport: 1'].view.setValues(nearPlane=372202,
    farPlane=458601, width=29503.4, height=11702.5, cameraPosition=(120151,
    -361739, -86112.9), cameraUpVector=(-0.434699, 0.0332127, 0.899963),
    cameraTarget=(-8796.26, 12849.2, -13012.5), viewOffsetX=-102517,
    viewOffsetY=90746.9)
session.viewports['Viewport: 1'].view.setValues(nearPlane=371069,
    farPlane=459735, width=44242.2, height=17548.6, viewOffsetX=-98394.9,
    viewOffsetY=90568.6)
session.viewports['Viewport: 1'].view.setValues(nearPlane=391626,
    farPlane=456725, width=46693.2, height=18520.8, cameraPosition=(64658.6,
    -393335, -103206), cameraUpVector=(-0.432275, 0.0557365, 0.900018),
    cameraTarget=(-3309.74, -7219.61, -10563.3), viewOffsetX=-103846,
    viewOffsetY=95586.2)
session.viewports['Viewport: 1'].view.setValues(nearPlane=393080,
    farPlane=455271, width=28715.7, height=11390, viewOffsetX=-108403,
    viewOffsetY=98756.9)
session.viewports['Viewport: 1'].view.setValues(nearPlane=387948,
    farPlane=455308, width=28340.7, height=11241.3, cameraPosition=(89273.7,
    -393768, -52115.7), cameraUpVector=(-0.423867, 0.158548, 0.891739),
    cameraTarget=(-5479.94, -3900.6, -15887.6), viewOffsetX=-106987,
    viewOffsetY=97467.4)
session.viewports['Viewport: 1'].view.setValues(nearPlane=383061,
    farPlane=455175, width=27983.7, height=11099.7, cameraPosition=(109889,
    -386247, -17515.9), cameraUpVector=(-0.455702, 0.20369, 0.866514),
    cameraTarget=(-5358.57, -251.598, -13892.6), viewOffsetX=-105639,
    viewOffsetY=96239.5)
session.viewports['Viewport: 1'].view.setValues(nearPlane=382842,
    farPlane=455394, width=32114.7, height=12738.2, viewOffsetX=-102902,
    viewOffsetY=99923.6)
session.viewports['Viewport: 1'].view.setValues(nearPlane=418091,
    farPlane=454650, width=35071.5, height=13911.1, cameraPosition=(-16185.3,
    -432965, -91288.3), cameraUpVector=(-0.368017, 0.17834, 0.912556),
    cameraTarget=(-4290.53, -37264.6, -16673.7), viewOffsetX=-112377,
    viewOffsetY=109124)
session.viewports['Viewport: 1'].view.setValues(nearPlane=415496,
    farPlane=457246, width=64407.8, height=25547.2, viewOffsetX=-117722,
    viewOffsetY=109106)
session.viewports['Viewport: 1'].view.setValues(nearPlane=415786,
    farPlane=468289, width=64452.8, height=25565.1, cameraPosition=(-45660,
    -446367, -76679), cameraUpVector=(-0.354355, 0.233925, 0.905379),
    cameraTarget=(-6574.19, -50121.6, -15444.9), viewOffsetX=-117804,
    viewOffsetY=109182)
i1 = mdb.models['Model-1'].rootAssembly.allInstances['P-39-1']
i2 = mdb.models['Model-1'].rootAssembly.allInstances['P-40-1']
i3 = mdb.models['Model-1'].rootAssembly.allInstances['P-41-1']
leaf = dgm.LeafFromInstance(instances=(i1, i2, i3, ))
session.viewports['Viewport: 1'].assemblyDisplay.displayGroup.replace(
    leaf=leaf)
session.viewports['Viewport: 1'].view.setValues(nearPlane=424530,
    farPlane=440173, width=77481.1, height=30732.7, viewOffsetX=-115923,
    viewOffsetY=111308)
session.viewports['Viewport: 1'].view.setValues(nearPlane=421879,
    farPlane=438161, width=76997.4, height=30540.9, cameraPosition=(-536790,
    -278555, 51169.7), cameraUpVector=(0.453481, 0.317382, 0.83284),
    cameraTarget=(-162322, -159051, -37035.8), viewOffsetX=-115200,
    viewOffsetY=110613)
session.viewports['Viewport: 1'].view.setValues(nearPlane=427198,
    farPlane=432843, width=15867, height=6293.62, viewOffsetX=-118526,
    viewOffsetY=110602)
i1 = mdb.models['Model-1'].rootAssembly.allInstances['P-39-1']
leaf = dgm.LeafFromInstance(instances=(i1, ))
session.viewports['Viewport: 1'].assemblyDisplay.displayGroup.replace(
    leaf=leaf)
session.viewports['Viewport: 1'].view.setValues(nearPlane=428310,
    farPlane=431730, width=6221.04, height=2467.56, viewOffsetX=-119730,
    viewOffsetY=109985)
i1 = mdb.models['Model-1'].rootAssembly.allInstances['P-40-1']
i2 = mdb.models['Model-1'].rootAssembly.allInstances['P-41-1']
leaf = dgm.LeafFromInstance(instances=(i1, i2, ))
session.viewports['Viewport: 1'].assemblyDisplay.displayGroup.replace(
    leaf=leaf)
session.viewports['Viewport: 1'].view.setValues(nearPlane=428197,
    farPlane=431844, width=4868.28, height=1931, viewOffsetX=-119683,
    viewOffsetY=109780)
a = mdb.models['Model-1'].rootAssembly
s1 = a.instances['P-39-1'].edges
side1Edges1 = s1.getSequenceFromMask(mask=('[#ff ]', ), )
region1=regionToolset.Region(side1Edges=side1Edges1)
a = mdb.models['Model-1'].rootAssembly
s1 = a.instances['P-40-1'].edges
side1Edges1 = s1.getSequenceFromMask(mask=('[#1004081 ]', ), )
s2 = a.instances['P-41-1'].edges
side1Edges2 = s2.getSequenceFromMask(mask=('[#2001002 #20 ]', ), )
region2=regionToolset.Region(side1Edges=side1Edges1+side1Edges2)
mdb.models['Model-1'].Tie(name='Constraint-50', main=region1,
    secondary=region2, positionToleranceMethod=COMPUTED, adjust=ON,
    tieRotations=ON, thickness=ON)
leaf = dgm.Leaf(leafType=DEFAULT_MODEL)
session.viewports['Viewport: 1'].assemblyDisplay.displayGroup.replace(
    leaf=leaf)
session.viewports['Viewport: 1'].view.setValues(nearPlane=409467,
    farPlane=595969, width=37726.5, height=14964.2, viewOffsetX=-112902,
    viewOffsetY=104387)
i1 = mdb.models['Model-1'].rootAssembly.allInstances['P-27-1']
i2 = mdb.models['Model-1'].rootAssembly.allInstances['P-28-1']
i3 = mdb.models['Model-1'].rootAssembly.allInstances['P-29-1']
leaf = dgm.LeafFromInstance(instances=(i1, i2, i3, ))
session.viewports['Viewport: 1'].assemblyDisplay.displayGroup.replace(
    leaf=leaf)
session.viewports['Viewport: 1'].view.setValues(nearPlane=436031,
    farPlane=440433, width=7848.65, height=3113.15, viewOffsetX=-115830,
    viewOffsetY=115713)
i1 = mdb.models['Model-1'].rootAssembly.allInstances['P-27-1']
leaf = dgm.LeafFromInstance(instances=(i1, ))
session.viewports['Viewport: 1'].assemblyDisplay.displayGroup.replace(
    leaf=leaf)
i1 = mdb.models['Model-1'].rootAssembly.allInstances['P-28-1']
i2 = mdb.models['Model-1'].rootAssembly.allInstances['P-29-1']
leaf = dgm.LeafFromInstance(instances=(i1, i2, ))
session.viewports['Viewport: 1'].assemblyDisplay.displayGroup.replace(
    leaf=leaf)
session.viewports['Viewport: 1'].view.setValues(nearPlane=436138,
    farPlane=440326, width=7235.1, height=2869.79, viewOffsetX=-115282,
    viewOffsetY=115590)
a = mdb.models['Model-1'].rootAssembly
s1 = a.instances['P-27-1'].edges
side1Edges1 = s1.getSequenceFromMask(mask=('[#ff ]', ), )
region1=regionToolset.Region(side1Edges=side1Edges1)
a = mdb.models['Model-1'].rootAssembly
s1 = a.instances['P-28-1'].edges
side1Edges1 = s1.getSequenceFromMask(mask=('[#1004081 ]', ), )
s2 = a.instances['P-29-1'].edges
side1Edges2 = s2.getSequenceFromMask(mask=('[#2008008 #10 ]', ), )
region2=regionToolset.Region(side1Edges=side1Edges1+side1Edges2)
mdb.models['Model-1'].Tie(name='Constraint-51', main=region1,
    secondary=region2, positionToleranceMethod=COMPUTED, adjust=ON,
    tieRotations=ON, thickness=ON)
leaf = dgm.Leaf(leafType=DEFAULT_MODEL)
session.viewports['Viewport: 1'].assemblyDisplay.displayGroup.replace(
    leaf=leaf)
session.viewports['Viewport: 1'].view.setValues(nearPlane=408388,
    farPlane=597048, width=50597.9, height=20069.6, viewOffsetX=-111093,
    viewOffsetY=103558)
a = mdb.models['Model-1'].rootAssembly
region1=a.sets['SET-RP15']
a = mdb.models['Model-1'].rootAssembly
region2=a.sets['SET-RP16']
mdb.models['Model-1'].Coupling(name='Constraint-52', controlPoint=region1,
    surface=region2, influenceRadius=WHOLE_SURFACE, couplingType=KINEMATIC,
    localCsys=None, u1=ON, u2=ON, u3=ON, ur1=ON, ur2=ON, ur3=ON)

# mdb.save()
#: The model database has been saved to "F:\temp\A-abaqus-2.cae".





