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

# openMdb(pathName='F:/tmp/A-abaqus-2.cae')
#: The model database "F:\temp\A-abaqus-2.cae" has been opened.

session.viewports['Viewport: 1'].setValues(displayedObject=None)
p = mdb.models['Model-1'].parts['P-1']
session.viewports['Viewport: 1'].setValues(displayedObject=p)
a = mdb.models['Model-1'].rootAssembly

# ##################
iges = mdb.openIges(r'PATH_IGS', msbo=False, trimCurve=DEFAULT,
    topology=WIRE, scaleFromFile=ON) #F:/tmp/FZX.igs
# #####################

mdb.models['Model-1'].PartFromGeometryFile(name='FZX', geometryFile=iges,
    combine=False, stitchTolerance=1.0, dimensionality=THREE_D,
    type=DEFORMABLE_BODY, topology=WIRE, convertToAnalytical=1, stitchEdges=1)
p = mdb.models['Model-1'].parts['FZX']
session.viewports['Viewport: 1'].setValues(displayedObject=p)
a = mdb.models['Model-1'].rootAssembly
session.viewports['Viewport: 1'].setValues(displayedObject=a)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(interactions=OFF,
    constraints=OFF, connectors=OFF, engineeringFeatures=OFF)
p = mdb.models['Model-1'].parts['FZX']
session.viewports['Viewport: 1'].setValues(displayedObject=p)
session.viewports['Viewport: 1'].partDisplay.setValues(sectionAssignments=ON,
    engineeringFeatures=ON)
session.viewports['Viewport: 1'].partDisplay.geometryOptions.setValues(
    referenceRepresentation=OFF)
session.viewports['Viewport: 1'].view.setValues(nearPlane=61109.9,
    farPlane=108413, width=66966.4, height=26562.1, viewOffsetX=-779.478,
    viewOffsetY=-269.385)
mdb.models['Model-1'].CircularProfile(name='Profile-1', r=50.0)
mdb.models['Model-1'].BeamSection(name='FZX', integration=DURING_ANALYSIS,
    poissonRatio=0.0, profile='Profile-1', material='Q390',
    temperatureVar=LINEAR, consistentMassMatrix=False)
p = mdb.models['Model-1'].parts['FZX']
e = p.edges
edges = e.getSequenceFromMask(mask=('[#1ffff ]', ), )
region = regionToolset.Region(edges=edges)
p = mdb.models['Model-1'].parts['FZX']
p.SectionAssignment(region=region, sectionName='FZX', offset=0.0,
    offsetType=MIDDLE_SURFACE, offsetField='',
    thicknessAssignment=FROM_SECTION)
session.viewports['Viewport: 1'].partDisplay.setValues(sectionAssignments=OFF,
    engineeringFeatures=OFF, mesh=ON)
session.viewports['Viewport: 1'].partDisplay.meshOptions.setValues(
    meshTechnique=ON)
elemType1 = mesh.ElemType(elemCode=B31, elemLibrary=STANDARD)
p = mdb.models['Model-1'].parts['FZX']
e = p.edges
edges = e.getSequenceFromMask(mask=('[#1ffff ]', ), )
pickedRegions =(edges, )
p.setElementType(regions=pickedRegions, elemTypes=(elemType1, ))
p = mdb.models['Model-1'].parts['FZX']
p.seedPart(size=50.0, deviationFactor=0.1, minSizeFactor=0.1)
p = mdb.models['Model-1'].parts['FZX']
p.generateMesh()
a = mdb.models['Model-1'].rootAssembly
session.viewports['Viewport: 1'].setValues(displayedObject=a)
a = mdb.models['Model-1'].rootAssembly
p = mdb.models['Model-1'].parts['FZX']
a.Instance(name='FZX-1', part=p, dependent=ON)