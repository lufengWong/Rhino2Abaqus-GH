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
executeOnCaeStartup()
session.viewports['Viewport: 1'].partDisplay.geometryOptions.setValues(
    referenceRepresentation=ON)
# openMdb(pathName='F:/temp/A-abaqus-2.cae')
#: The model database "F:\temp\A-abaqus-2.cae" has been opened.




session.viewports['Viewport: 1'].view.setValues(nearPlane=405699, 
    farPlane=591854, width=72581.2, height=28789.2, viewOffsetX=-116196, 
    viewOffsetY=103421)
session.viewports['Viewport: 1'].view.setValues(nearPlane=405130, 
    farPlane=587886, width=72479.4, height=28748.8, cameraPosition=(-467348, 
    -361074, 52958.2), cameraUpVector=(0.343251, 0.442794, 0.828319), 
    cameraTarget=(-120727, -172925, -29146.5), viewOffsetX=-116033, 
    viewOffsetY=103275)
session.viewports['Viewport: 1'].view.setValues(nearPlane=407069, 
    farPlane=585947, width=48417.2, height=19204.6, viewOffsetX=-120842, 
    viewOffsetY=106981)
session.viewports['Viewport: 1'].view.setValues(nearPlane=407384, 
    farPlane=587284, width=48454.7, height=19219.5, cameraPosition=(-477201, 
    -351990, 44587.4), cameraUpVector=(0.343343, 0.426427, 0.836825), 
    cameraTarget=(-124943, -171859, -31268.1), viewOffsetX=-120936, 
    viewOffsetY=107063)
session.viewports['Viewport: 1'].view.setValues(nearPlane=407380, 
    farPlane=587286, width=48454.2, height=19219.3, cameraPosition=(-472539, 
    -356144, 56372), cameraUpVector=(0.312503, 0.479625, 0.81994), 
    cameraTarget=(-120281, -176013, -19483.5), viewOffsetX=-120935, 
    viewOffsetY=107062)
session.viewports['Viewport: 1'].view.setValues(nearPlane=407133, 
    farPlane=586206, width=48424.8, height=19207.7, cameraPosition=(-474048, 
    -354899, 31888.4), cameraUpVector=(0.281603, 0.456946, 0.843742), 
    cameraTarget=(-118534, -174310, -25419.4), viewOffsetX=-120862, 
    viewOffsetY=106997)
session.viewports['Viewport: 1'].view.setValues(nearPlane=410850, 
    farPlane=582489, width=6093.27, height=2416.88, viewOffsetX=-138585, 
    viewOffsetY=109081)
a = mdb.models['Model-1'].rootAssembly
v1 = a.instances['FZX-1'].vertices
e1 = a.instances['FZX-1'].edges
a.DatumCsysByThreePoints(origin=v1[15], point1=v1[14], name='Datum csys-2', 
    coordSysType=CARTESIAN, point2=a.instances['FZX-1'].InterestingPoint(
    edge=e1[13], rule=MIDDLE))
session.viewports['Viewport: 1'].view.setValues(nearPlane=407728, 
    farPlane=585611, width=43355.9, height=17197, viewOffsetX=-122090, 
    viewOffsetY=112331)
session.viewports['Viewport: 1'].view.setValues(nearPlane=408195, 
    farPlane=567051, width=43405.5, height=17216.7, cameraPosition=(-365707, 
    -432212, 85230.4), cameraUpVector=(0.260587, 0.550209, 0.793325), 
    cameraTarget=(-75121.6, -173862, -20135.2), viewOffsetX=-122230, 
    viewOffsetY=112460)
session.viewports['Viewport: 1'].view.setValues(nearPlane=401593, 
    farPlane=573652, width=123857, height=49127.7, viewOffsetX=-138777, 
    viewOffsetY=112841)
session.viewports['Viewport: 1'].view.setValues(nearPlane=410743, 
    farPlane=481653, width=126679, height=50247.1, cameraPosition=(-4283.81, 
    -475482, 45632.1), cameraUpVector=(-0.093133, 0.541259, 0.835682), 
    cameraTarget=(46643.8, -85307.2, -40719.6), viewOffsetX=-141939, 
    viewOffsetY=115412)
session.viewports['Viewport: 1'].view.setValues(nearPlane=420352, 
    farPlane=472044, width=13180.7, height=5228.08, viewOffsetX=-176951, 
    viewOffsetY=126851)
session.viewports['Viewport: 1'].view.setValues(nearPlane=417296, 
    farPlane=489842, width=13084.8, height=5190.08, cameraPosition=(-62741, 
    -489525, 37149), cameraUpVector=(-0.142521, 0.51346, 0.846195), 
    cameraTarget=(44946.5, -105432, -19089.2), viewOffsetX=-175665, 
    viewOffsetY=125929)
session.viewports['Viewport: 1'].view.setValues(nearPlane=417168, 
    farPlane=496178, width=13080.8, height=5188.49, cameraPosition=(-76567.6, 
    -491745, 61884.3), cameraUpVector=(-0.113071, 0.560325, 0.820519), 
    cameraTarget=(40407.4, -114233, -16142.9), viewOffsetX=-175611, 
    viewOffsetY=125890)
session.viewports['Viewport: 1'].view.setValues(nearPlane=417739, 
    farPlane=495608, width=6282.2, height=2491.82, viewOffsetX=-175845, 
    viewOffsetY=125357)
a = mdb.models['Model-1'].rootAssembly
v11 = a.instances['FZX-1'].vertices
e11 = a.instances['FZX-1'].edges
a.DatumCsysByThreePoints(origin=v11[9], point1=v11[13], name='Datum csys-3', 
    coordSysType=CARTESIAN, point2=a.instances['FZX-1'].InterestingPoint(
    edge=e11[8], rule=MIDDLE))
session.viewports['Viewport: 1'].view.setValues(nearPlane=411170, 
    farPlane=502177, width=85192, height=33791.3, viewOffsetX=-184734, 
    viewOffsetY=117452)
session.viewports['Viewport: 1'].view.setValues(nearPlane=411764, 
    farPlane=480846, width=85315.1, height=33840.1, cameraPosition=(25738, 
    -437428, 194379), cameraUpVector=(-0.293319, 0.705196, 0.645494), 
    cameraTarget=(67084.6, -74436.8, 24630.2), viewOffsetX=-185001, 
    viewOffsetY=117622)
session.viewports['Viewport: 1'].view.setValues(nearPlane=410797, 
    farPlane=481814, width=104569, height=41477.1, viewOffsetX=-187322, 
    viewOffsetY=116029)
session.viewports['Viewport: 1'].view.setValues(nearPlane=408647, 
    farPlane=570135, width=104022, height=41260.1, cameraPosition=(-248104, 
    -404489, 321896), cameraUpVector=(-0.000680365, 0.920527, 0.390679), 
    cameraTarget=(-4900.18, -166784, 105944), viewOffsetX=-186341, 
    viewOffsetY=115422)
session.viewports['Viewport: 1'].view.setValues(nearPlane=413180, 
    farPlane=565602, width=50530.5, height=20042.8, viewOffsetX=-187236, 
    viewOffsetY=105175)
session.viewports['Viewport: 1'].view.setValues(nearPlane=416344, 
    farPlane=580503, width=50917.4, height=20196.3, cameraPosition=(-313180, 
    -403102, 295935), cameraUpVector=(0.0532879, 0.903419, 0.425434), 
    cameraTarget=(-32716.4, -182794, 108608), viewOffsetX=-188670, 
    viewOffsetY=105980)
session.viewports['Viewport: 1'].view.setValues(nearPlane=415701, 
    farPlane=581145, width=60274, height=23907.6, viewOffsetX=-180390, 
    viewOffsetY=103189)
session.viewports['Viewport: 1'].view.setValues(nearPlane=418330, 
    farPlane=593712, width=60655.2, height=24058.8, cameraPosition=(-364333, 
    -358403, 323641), cameraUpVector=(0.223826, 0.896496, 0.382358), 
    cameraTarget=(-63631.2, -193538, 112254), viewOffsetX=-181531, 
    viewOffsetY=103842)
session.viewports['Viewport: 1'].view.setValues(nearPlane=419172, 
    farPlane=597198, width=60777.3, height=24107.2, cameraPosition=(-380779, 
    -365078, 302718), cameraUpVector=(0.171024, 0.899537, 0.401976), 
    cameraTarget=(-67729.2, -192368, 117090), viewOffsetX=-181896, 
    viewOffsetY=104051)
session.viewports['Viewport: 1'].view.setValues(nearPlane=419760, 
    farPlane=596610, width=51783.4, height=20539.8, viewOffsetX=-181760, 
    viewOffsetY=101060)
session.viewports['Viewport: 1'].view.setValues(nearPlane=416523, 
    farPlane=583552, width=51384, height=20381.4, cameraPosition=(-329616, 
    -400854, 289756), cameraUpVector=(0.165794, 0.873869, 0.457018), 
    cameraTarget=(-44858.6, -197057, 90591.3), viewOffsetX=-180358, 
    viewOffsetY=100280)
session.viewports['Viewport: 1'].view.setValues(nearPlane=414302, 
    farPlane=585773, width=80358.6, height=31874.1, viewOffsetX=-183333, 
    viewOffsetY=103236)
session.viewports['Viewport: 1'].view.setValues(nearPlane=413069, 
    farPlane=570384, width=80119.4, height=31779.2, cameraPosition=(-271519, 
    -459013, 218792), cameraUpVector=(-0.00715084, 0.821394, 0.570317), 
    cameraTarget=(-12775.4, -189129, 68788.4), viewOffsetX=-182787, 
    viewOffsetY=102929)
session.viewports['Viewport: 1'].view.setValues(nearPlane=414356, 
    farPlane=569097, width=63018.9, height=24996.3, viewOffsetX=-185550, 
    viewOffsetY=115097)
session.viewports['Viewport: 1'].view.setValues(nearPlane=415312, 
    farPlane=560028, width=63164.4, height=25054, cameraPosition=(-250319, 
    -490141, 136014), cameraUpVector=(-0.0502781, 0.720807, 0.69131), 
    cameraTarget=(-2842.34, -188996, 34260.2), viewOffsetX=-185979, 
    viewOffsetY=115362)
session.viewports['Viewport: 1'].view.setValues(nearPlane=419581, 
    farPlane=555759, width=13527.6, height=5365.7, viewOffsetX=-190620, 
    viewOffsetY=130241)
a = mdb.models['Model-1'].rootAssembly
v1 = a.instances['FZX-1'].vertices
e1 = a.instances['FZX-1'].edges
a.DatumCsysByThreePoints(origin=v1[3], name='Datum csys-4', 
    coordSysType=CARTESIAN, point1=a.instances['FZX-1'].InterestingPoint(
    edge=e1[1], rule=MIDDLE), line2=(0.0, 2310588.731019, 232977.782374))
session.viewports['Viewport: 1'].view.setValues(nearPlane=419358, 
    farPlane=555982, width=17333, height=6875.1, viewOffsetX=-177398, 
    viewOffsetY=130283)
a = mdb.models['Model-1'].rootAssembly
v11 = a.instances['FZX-1'].vertices
e11 = a.instances['FZX-1'].edges
a.DatumCsysByThreePoints(origin=v11[21], name='Datum csys-5', 
    coordSysType=CARTESIAN, point1=a.instances['FZX-1'].InterestingPoint(
    edge=e11[15], rule=MIDDLE), line2=(-6617.101558, 30958430.113157, 
    -11695.687409))
#: Warning: Cannot continue yet--complete the step or cancel the procedure.
session.viewports['Viewport: 1'].view.setValues(nearPlane=419096, 
    farPlane=556245, width=20465.7, height=8117.68, viewOffsetX=-179821, 
    viewOffsetY=129738)
a = mdb.models['Model-1'].rootAssembly
v1 = a.instances['FZX-1'].vertices
e1 = a.instances['FZX-1'].edges
a.DatumCsysByThreePoints(origin=v1[23], name='Datum csys-6', 
    coordSysType=CARTESIAN, point1=a.instances['FZX-1'].InterestingPoint(
    edge=e1[16], rule=MIDDLE), line2=(-466320.92081, 9224271.72301, 
    807691.527475))
session.viewports['Viewport: 1'].view.setValues(nearPlane=418116, 
    farPlane=557224, width=32158.2, height=12755.5, viewOffsetX=-174409, 
    viewOffsetY=129324)
a = mdb.models['Model-1'].rootAssembly
v11 = a.instances['FZX-1'].vertices
e11 = a.instances['FZX-1'].edges
a.DatumCsysByThreePoints(origin=v11[1], name='Datum csys-7', 
    coordSysType=CARTESIAN, point1=a.instances['FZX-1'].InterestingPoint(
    edge=e11[0], rule=MIDDLE), line2=(-117457.278503, 22995081.515399, 
    199402.889811))
session.viewports['Viewport: 1'].view.setValues(nearPlane=415954, 
    farPlane=559387, width=57959.1, height=22989.4, viewOffsetX=-178261, 
    viewOffsetY=129690)
session.viewports['Viewport: 1'].view.setValues(nearPlane=416584, 
    farPlane=508247, width=58046.9, height=23024.2, cameraPosition=(-47876.4, 
    -482404, 173010), cameraUpVector=(-0.0588369, 0.750326, 0.658445), 
    cameraTarget=(54440.1, -137068, -7435.96), viewOffsetX=-178531, 
    viewOffsetY=129886)
session.viewports['Viewport: 1'].view.setValues(nearPlane=411580, 
    farPlane=513250, width=119994, height=47595.3, viewOffsetX=-189170, 
    viewOffsetY=127966)
session.viewports['Viewport: 1'].view.setValues(nearPlane=339542, 
    farPlane=513452, width=98991.5, height=39264.8, cameraPosition=(330020, 
    102451, 226419), cameraUpVector=(-0.789637, 0.567188, 0.234031), 
    cameraTarget=(67345.8, 99524.2, -78998.4), viewOffsetX=-156060, 
    viewOffsetY=105568)
session.viewports['Viewport: 1'].view.setValues(nearPlane=373131, 
    farPlane=519166, width=108784, height=43149, cameraPosition=(200927, 
    359886, 201687), cameraUpVector=(-0.987705, 0.0803788, 0.134081), 
    cameraTarget=(8973.13, 164610, -93790.2), viewOffsetX=-171498, 
    viewOffsetY=116011)
session.viewports['Viewport: 1'].view.setValues(nearPlane=379694, 
    farPlane=512602, width=24743.3, height=9814.38, viewOffsetX=-179347, 
    viewOffsetY=121616)
a = mdb.models['Model-1'].rootAssembly
v1 = a.instances['FZX-1'].vertices
e1 = a.instances['FZX-1'].edges
a.DatumCsysByThreePoints(origin=v1[19], name='Datum csys-8', 
    coordSysType=CARTESIAN, point1=a.instances['FZX-1'].InterestingPoint(
    edge=e1[14], rule=MIDDLE), line2=(34263.533043, 46230518.626663, 
    -60560.589629))
session.viewports['Viewport: 1'].view.setValues(nearPlane=378111, 
    farPlane=514185, width=43636.1, height=17308.2, viewOffsetX=-172710, 
    viewOffsetY=121825)
session.viewports['Viewport: 1'].view.setValues(nearPlane=385590, 
    farPlane=491582, width=44499.2, height=17650.5, cameraPosition=(154394, 
    -41819.7, 460816), cameraUpVector=(-0.987934, 0.152488, 0.0270826), 
    cameraTarget=(41513, 165432, 134335), viewOffsetX=-176126, 
    viewOffsetY=124235)
session.viewports['Viewport: 1'].view.setValues(nearPlane=380332, 
    farPlane=496840, width=108127, height=42888.2, viewOffsetX=-179799, 
    viewOffsetY=132229)
session.viewports['Viewport: 1'].view.setValues(nearPlane=337238, 
    farPlane=457224, width=95875.1, height=38028.7, cameraPosition=(253126, 
    -296831, -55948.6), cameraUpVector=(-0.769527, -0.259015, 0.583729), 
    cameraTarget=(104401, 31604.5, 123762), viewOffsetX=-159426, 
    viewOffsetY=117247)
session.viewports['Viewport: 1'].view.setValues(nearPlane=368122, 
    farPlane=445081, width=104655, height=41511.4, cameraPosition=(74413.2, 
    -407321, -142352), cameraUpVector=(-0.570922, 0.0239531, 0.820655), 
    cameraTarget=(125177, -55020.4, 46306.5), viewOffsetX=-174026, 
    viewOffsetY=127985)
session.viewports['Viewport: 1'].view.setValues(nearPlane=356342, 
    farPlane=456860, width=239997, height=95194.4, viewOffsetX=-181710, 
    viewOffsetY=142964)
session.viewports['Viewport: 1'].view.setValues(nearPlane=367093, 
    farPlane=507045, width=247238, height=98066.3, cameraPosition=(-121982, 
    -488815, -55312.3), cameraUpVector=(0.0792493, 0.407006, 0.909981), 
    cameraTarget=(59292.9, -130200, -83933), viewOffsetX=-187192, 
    viewOffsetY=147277)
session.viewports['Viewport: 1'].view.setValues(nearPlane=373278, 
    farPlane=546854, width=251404, height=99718.6, cameraPosition=(-194098, 
    -488822, 162549), cameraUpVector=(0.212891, 0.720875, 0.659558), 
    cameraTarget=(25462.2, -202895, -17238.3), viewOffsetX=-190346, 
    viewOffsetY=149758)
session.viewports['Viewport: 1'].view.setValues(nearPlane=379768, 
    farPlane=569223, width=255775, height=101452, cameraPosition=(-208624, 
    -426531, 324080), cameraUpVector=(0.0725004, 0.911869, 0.404027), 
    cameraTarget=(39037.9, -200176, 101120), viewOffsetX=-193656, 
    viewOffsetY=152362)
session.viewports['Viewport: 1'].view.setValues(nearPlane=393678, 
    farPlane=555312, width=95723.3, height=37968.5, viewOffsetX=-226760, 
    viewOffsetY=131448)
session.viewports['Viewport: 1'].view.setValues(nearPlane=423661, 
    farPlane=544920, width=103014, height=40860.2, cameraPosition=(-90606.7, 
    -135848, 546671), cameraUpVector=(0.333764, 0.890308, -0.309763), 
    cameraTarget=(38103.4, -165684, 166109), viewOffsetX=-244030, 
    viewOffsetY=141459)
session.viewports['Viewport: 1'].view.setValues(nearPlane=406793, 
    farPlane=561788, width=300401, height=119154, viewOffsetX=-230640, 
    viewOffsetY=119154)
session.viewports['Viewport: 1'].view.setValues(nearPlane=450152, 
    farPlane=615043, width=332420, height=131854, cameraPosition=(-131151, 
    445369, 395072), cameraUpVector=(0.201026, 0.192049, -0.960576), 
    cameraTarget=(47986.2, 125164, 228751), viewOffsetX=-255224, 
    viewOffsetY=131854)
session.viewports['Viewport: 1'].view.setValues(nearPlane=472409, 
    farPlane=592786, width=43499, height=17253.8, viewOffsetX=-266444, 
    viewOffsetY=89070.3)
i1 = mdb.models['Model-1'].rootAssembly.allInstances['FZX-1']
leaf = dgm.LeafFromInstance(instances=(i1, ))
session.viewports['Viewport: 1'].assemblyDisplay.displayGroup.replace(
    leaf=leaf)
session.viewports['Viewport: 1'].view.setValues(nearPlane=475847, 
    farPlane=511634, width=22801.8, height=9044.28, viewOffsetX=-270318, 
    viewOffsetY=85337.2)
a = mdb.models['Model-1'].rootAssembly
v11 = a.instances['FZX-1'].vertices
e11 = a.instances['FZX-1'].edges
a.DatumCsysByThreePoints(origin=v11[5], point2=v11[7], name='Datum csys-9', 
    coordSysType=CARTESIAN, point1=a.instances['FZX-1'].InterestingPoint(
    edge=e11[2], rule=MIDDLE))
session.viewports['Viewport: 1'].view.setValues(nearPlane=473784, 
    farPlane=513697, width=47419.3, height=18808.8, viewOffsetX=-267167, 
    viewOffsetY=85645.6)
session.viewports['Viewport: 1'].view.setValues(nearPlane=468806, 
    farPlane=511571, width=46921.1, height=18611.2, cameraPosition=(-216456, 
    -56839, 609159), cameraUpVector=(-0.208317, 0.901852, -0.378507), 
    cameraTarget=(20349.6, 13169.3, 290872), viewOffsetX=-264360, 
    viewOffsetY=84745.8)
session.viewports['Viewport: 1'].view.setValues(nearPlane=467604, 
    farPlane=508455, width=46800.8, height=18563.5, cameraPosition=(-198217, 
    -358248, 490590), cameraUpVector=(-0.591075, 0.806154, 0.0273196), 
    cameraTarget=(-13307.5, -49942.4, 308819), viewOffsetX=-263682, 
    viewOffsetY=84528.4)
session.viewports['Viewport: 1'].view.setValues(nearPlane=467614, 
    farPlane=508444, width=46801.8, height=18563.9, cameraPosition=(-135501, 
    -445160, 406976), cameraUpVector=(-0.332905, 0.861392, 0.383638), 
    cameraTarget=(49408.8, -136854, 225205), viewOffsetX=-263687, 
    viewOffsetY=84530.2)
leaf = dgm.Leaf(leafType=DEFAULT_MODEL)
session.viewports['Viewport: 1'].assemblyDisplay.displayGroup.replace(
    leaf=leaf)
session.viewports['Viewport: 1'].view.setValues(nearPlane=464244, 
    farPlane=592387, width=70010.9, height=27769.7, viewOffsetX=-268259, 
    viewOffsetY=84295.7)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(loads=ON, bcs=ON, 
    predefinedFields=ON, connectors=ON)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(loads=OFF, bcs=OFF, 
    predefinedFields=OFF, connectors=OFF, adaptiveMeshConstraints=ON)
mdb.models['Model-1'].StaticStep(name='Step-1', previous='Initial', 
    maxNumInc=1000000, initialInc=0.1, minInc=1e-09, nlgeom=ON)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(step='Step-1')



session.viewports['Viewport: 1'].assemblyDisplay.setValues(loads=ON, bcs=ON, 
    predefinedFields=ON, connectors=ON, adaptiveMeshConstraints=OFF)
session.viewports['Viewport: 1'].view.setValues(nearPlane=466346, 
    farPlane=590285, width=41438.9, height=16436.7, viewOffsetX=-269638, 
    viewOffsetY=81201.9)
a = mdb.models['Model-1'].rootAssembly
region = a.sets['SET-RP5']
datum = mdb.models['Model-1'].rootAssembly.datums[211]
mdb.models['Model-1'].ConcentratedForce(name='Load-1', createStepName='Step-1', 
    region=region, cf1=1078510.0, distributionType=UNIFORM, field='', 
    localCsys=datum)
session.viewports['Viewport: 1'].view.setValues(nearPlane=466344, 
    farPlane=590288, width=44963.9, height=17834.9, viewOffsetX=-268975, 
    viewOffsetY=81239.1)
a = mdb.models['Model-1'].rootAssembly
region = a.sets['SET-RP7']
datum = mdb.models['Model-1'].rootAssembly.datums[212]
mdb.models['Model-1'].ConcentratedForce(name='Load-2', createStepName='Step-1', 
    region=region, cf1=-16895.0, distributionType=UNIFORM, field='', 
    localCsys=datum)
a = mdb.models['Model-1'].rootAssembly
region = a.sets['SET-RP9']
datum = mdb.models['Model-1'].rootAssembly.datums[213]
mdb.models['Model-1'].ConcentratedForce(name='Load-3', createStepName='Step-1', 
    region=region, cf1=8606310.0, distributionType=UNIFORM, field='', 
    localCsys=datum)
a = mdb.models['Model-1'].rootAssembly
region = a.sets['SET-RP11']
datum = mdb.models['Model-1'].rootAssembly.datums[214]
mdb.models['Model-1'].ConcentratedForce(name='Load-4', createStepName='Step-1', 
    region=region, cf1=-58401.0, distributionType=UNIFORM, field='', 
    localCsys=datum)
a = mdb.models['Model-1'].rootAssembly
region = a.sets['SET-RP13']
datum = mdb.models['Model-1'].rootAssembly.datums[215]
mdb.models['Model-1'].ConcentratedForce(name='Load-5', createStepName='Step-1', 
    region=region, cf1=19343.0, distributionType=UNIFORM, field='', 
    localCsys=datum)
session.viewports['Viewport: 1'].view.setValues(nearPlane=466191, 
    farPlane=590441, width=43151.2, height=17115.9, viewOffsetX=-272173, 
    viewOffsetY=81758.4)
a = mdb.models['Model-1'].rootAssembly
region = a.sets['SET-RP1']
datum = mdb.models['Model-1'].rootAssembly.datums[209]
mdb.models['Model-1'].ConcentratedForce(name='Load-6', createStepName='Step-1', 
    region=region, cf1=110056600.0, cf2=341110.0, cf3=1889480.0, 
    distributionType=UNIFORM, field='', localCsys=datum)
a = mdb.models['Model-1'].rootAssembly
region = a.sets['SET-RP1']
datum = mdb.models['Model-1'].rootAssembly.datums[209]
mdb.models['Model-1'].Moment(name='Load-7', createStepName='Step-1', 
    region=region, cm1=-729530000.0, cm2=-25954400000.0, cm3=9910420000.0, 
    distributionType=UNIFORM, field='', localCsys=datum)
a = mdb.models['Model-1'].rootAssembly
region = a.sets['SET-RP3']
datum = mdb.models['Model-1'].rootAssembly.datums[1]
mdb.models['Model-1'].Moment(name='Load-8', createStepName='Step-1', 
    region=region, cm2=-44395.0, cm3=13476.0, distributionType=UNIFORM, 
    field='', localCsys=datum)
mdb.models['Model-1'].loads['Load-8'].suppress()
a = mdb.models['Model-1'].rootAssembly
region = a.sets['SET-RP15']
datum = mdb.models['Model-1'].rootAssembly.datums[216]
mdb.models['Model-1'].ConcentratedForce(name='Load-9', createStepName='Step-1', 
    region=region, cf1=52476.0, cf2=-20870.0, cf3=-17321.0, 
    distributionType=UNIFORM, field='', localCsys=datum)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(step='Initial')
a = mdb.models['Model-1'].rootAssembly
region = a.sets['SET-RP3']
datum = mdb.models['Model-1'].rootAssembly.datums[210]
mdb.models['Model-1'].DisplacementBC(name='BC-1', createStepName='Initial', 
    region=region, u1=SET, u2=SET, u3=SET, ur1=SET, ur2=SET, ur3=SET, 
    amplitude=UNSET, distributionType=UNIFORM, fieldName='', localCsys=datum)

mdb.save()
# #: The model database has been saved to "F:\temp\A-abaqus-2.cae".

session.viewports['Viewport: 1'].assemblyDisplay.setValues(step='Step-1')
session.viewports['Viewport: 1'].assemblyDisplay.setValues(loads=OFF, bcs=OFF, 
    predefinedFields=OFF, connectors=OFF)
# make job
mdb.Job(name='S31223', model='Model-1', description='', type=ANALYSIS, 
    atTime=None, waitMinutes=0, waitHours=0, queue=None, memory=90, 
    memoryUnits=PERCENTAGE, getMemoryFromAnalysis=True, 
    explicitPrecision=SINGLE, nodalOutputPrecision=SINGLE, echoPrint=OFF, 
    modelPrint=OFF, contactPrint=OFF, historyPrint=OFF, userSubroutine='', 
    scratch='', resultsFormat=ODB, numThreadsPerMpiProcess=1, 
    multiprocessingMode=DEFAULT, numCpus=1, numDomains=1, numGPUs=0)

session.viewports['Viewport: 1'].partDisplay.setValues(mesh=OFF)
session.viewports['Viewport: 1'].partDisplay.meshOptions.setValues(
    meshTechnique=OFF)
session.viewports['Viewport: 1'].partDisplay.geometryOptions.setValues(
    referenceRepresentation=ON)

p = mdb.models['Model-1'].parts['FZX']
session.viewports['Viewport: 1'].setValues(displayedObject=p)
session.viewports['Viewport: 1'].partDisplay.setValues(sectionAssignments=ON, 
    engineeringFeatures=ON)
session.viewports['Viewport: 1'].partDisplay.geometryOptions.setValues(
    referenceRepresentation=OFF)
p = mdb.models['Model-1'].parts['FZX']
e = p.edges
edges = e.getSequenceFromMask(mask=('[#1ffff ]', ), )
region=regionToolset.Region(edges=edges)
p = mdb.models['Model-1'].parts['FZX']
p.assignBeamSectionOrientation(region=region, method=N1_COSINES, n1=(0.0, 0.0, 
    -1.0))
#: Beam orientations have been assigned to the selected regions.
session.viewports['Viewport: 1'].view.setValues(nearPlane=61120.2, 
    farPlane=108403, width=61726.6, height=24483.7, viewOffsetX=-1611.36, 
    viewOffsetY=-1015.78)
a = mdb.models['Model-1'].rootAssembly
a.regenerate()
session.viewports['Viewport: 1'].setValues(displayedObject=a)


# # submit job
# mdb.jobs['S31223'].submit(consistencyChecking=OFF)
# #: The job input file "S31223.inp" has been submitted for analysis.
# #: Job S31223: Analysis Input File Processor completed successfully.
# #: Job S31223: Abaqus/Standard completed successfully.
# #: Job S31223 completed successfully.
# o3 = session.openOdb(name='E:/temp/S31223.odb')
# #: Model: E:/temp/S31223.odb
# #: Number of Assemblies:         1
# #: Number of Assembly instances: 0
# #: Number of Part instances:     50
# #: Number of Meshes:             50
# #: Number of Element Sets:       11
# #: Number of Node Sets:          30
# #: Number of Steps:              1
# session.viewports['Viewport: 1'].setValues(displayedObject=o3)
# session.viewports['Viewport: 1'].makeCurrent()
# session.viewports['Viewport: 1'].odbDisplay.display.setValues(plotState=(
#     CONTOURS_ON_DEF, ))
# session.viewports['Viewport: 1'].view.setValues(nearPlane=61045.2,
#     farPlane=112236, width=61118.7, height=24242.6, cameraPosition=(-86623.4,
#     27101.4, 13080.1), cameraUpVector=(-0.708887, 0.694564, 0.12272),
#     cameraTarget=(-158893, -10308.1, 41302.3))
# session.viewports['Viewport: 1'].view.setValues(nearPlane=63671.5,
#     farPlane=107818, width=63748.2, height=25285.6, cameraPosition=(-120513,
#     58307.5, 5940.23), cameraUpVector=(-0.643583, 0.305471, 0.701775),
#     cameraTarget=(-159092, -10125.2, 41260.5))
# session.viewports['Viewport: 1'].view.setValues(nearPlane=68645.3,
#     farPlane=102844, width=3945.66, height=1565.04, viewOffsetX=4213.79,
#     viewOffsetY=-771.261)
# session.viewports['Viewport: 1'].view.setValues(nearPlane=68184.2,
#     farPlane=102855, width=3919.15, height=1554.53, cameraPosition=(-117794,
#     57972.8, 9150.56), cameraUpVector=(-0.658439, 0.303888, 0.688557),
#     cameraTarget=(-159239, -10320.4, 41357.7), viewOffsetX=4185.48,
#     viewOffsetY=-766.08)
# session.viewports['Viewport: 1'].view.setValues(nearPlane=68157.5,
#     farPlane=102882, width=4428.02, height=1756.37, viewOffsetX=4224.45,
#     viewOffsetY=-778.353)
# session.viewports['Viewport: 1'].odbDisplay.contourOptions.setValues(
#     maxAutoCompute=OFF, maxValue=345, minValue=0)
