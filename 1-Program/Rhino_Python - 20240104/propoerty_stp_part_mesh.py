# -*- coding: mbcs -*-
#
# Abaqus/CAE Release 2022 replay file
# Internal Version: 2021_09_16-01.57.30 176069
# Run by 18328 on Thu Dec 14 19:30:18 2023
#

# from driverUtils import executeOnCaeGraphicsStartup
# executeOnCaeGraphicsStartup()
#: Executing "onCaeGraphicsStartup()" in the site directory ...
from abaqus import *
from abaqusConstants import *

session.Viewport(name='Viewport: 1', origin=(0.0, 0.0), width=108.857414245605, 
    height=131.481475830078)
session.viewports['Viewport: 1'].makeCurrent()
session.viewports['Viewport: 1'].maximize()
from caeModules import *
from driverUtils import executeOnCaeStartup
executeOnCaeStartup()
session.viewports['Viewport: 1'].partDisplay.geometryOptions.setValues(
    referenceRepresentation=ON)
session.viewports['Viewport: 1'].partDisplay.setValues(sectionAssignments=ON, 
    engineeringFeatures=ON)
session.viewports['Viewport: 1'].partDisplay.geometryOptions.setValues(
    referenceRepresentation=OFF)
mdb.models['Model-1'].Material(name='Q390')
mdb.models['Model-1'].materials['Q390'].Elastic(table=((206000.0, 0.3), ))
mdb.models['Model-1'].materials['Q390'].Plastic(scaleStress=None, table=((
    390.0, 0.0), (450.0, 0.1)))

session.viewports['Viewport: 1'].partDisplay.setValues(sectionAssignments=OFF, 
    engineeringFeatures=OFF)
session.viewports['Viewport: 1'].partDisplay.geometryOptions.setValues(
    referenceRepresentation=ON)
step = mdb.openStep('F:/Rhino_File/Ex/HC18mm.stp', scaleFromFile=ON)
mdb.models['Model-1'].PartFromGeometryFile(name='HC18mm', geometryFile=step, 
    combine=True, dimensionality=THREE_D, type=DEFORMABLE_BODY)
p = mdb.models['Model-1'].parts['HC18mm']
session.viewports['Viewport: 1'].setValues(displayedObject=p)
session.viewports['Viewport: 1'].partDisplay.setValues(sectionAssignments=ON, 
    engineeringFeatures=ON)
session.viewports['Viewport: 1'].partDisplay.geometryOptions.setValues(
    referenceRepresentation=OFF)
mdb.models['Model-1'].HomogeneousShellSection(name='Section-1', 
    preIntegrate=OFF, material='Q390', thicknessType=UNIFORM, thickness=18.0, 
    thicknessField='', nodalThicknessField='', idealization=NO_IDEALIZATION, 
    poissonDefinition=DEFAULT, thicknessModulus=None, temperature=GRADIENT, 
    useDensity=OFF, integrationRule=SIMPSON, numIntPts=5)
session.viewports['Viewport: 1'].view.setValues(nearPlane=52427.9, 
    farPlane=94772.4, width=47936.1, height=22280.7, viewOffsetX=1452.34, 
    viewOffsetY=-321.868)
p = mdb.models['Model-1'].parts['HC18mm']
f = p.faces
faces = f.getSequenceFromMask(mask=('[#ff ]', ), )
region = regionToolset.Region(faces=faces)
p = mdb.models['Model-1'].parts['HC18mm']
p.SectionAssignment(region=region, sectionName='Section-1', offset=0.0, 
    offsetType=MIDDLE_SURFACE, offsetField='', 
    thicknessAssignment=FROM_SECTION)
session.viewports['Viewport: 1'].partDisplay.setValues(sectionAssignments=OFF, 
    engineeringFeatures=OFF, mesh=ON)
session.viewports['Viewport: 1'].partDisplay.meshOptions.setValues(
    meshTechnique=ON)
p = mdb.models['Model-1'].parts['HC18mm']
p.seedPart(size=200.0, deviationFactor=0.1, minSizeFactor=0.1)
p = mdb.models['Model-1'].parts['HC18mm']
p.generateMesh()
session.viewports['Viewport: 1'].partDisplay.setValues(mesh=OFF)
session.viewports['Viewport: 1'].partDisplay.meshOptions.setValues(
    meshTechnique=OFF)
session.viewports['Viewport: 1'].partDisplay.geometryOptions.setValues(
    referenceRepresentation=ON)
step = mdb.openStep('F:/Rhino_File/Ex/HCDLGB24mm.stp', scaleFromFile=ON)
mdb.models['Model-1'].PartFromGeometryFile(name='HCDLGB24mm', 
    geometryFile=step, combine=True, dimensionality=THREE_D, 
    type=DEFORMABLE_BODY)
p = mdb.models['Model-1'].parts['HCDLGB24mm']
session.viewports['Viewport: 1'].setValues(displayedObject=p)
session.viewports['Viewport: 1'].partDisplay.setValues(sectionAssignments=ON, 
    engineeringFeatures=ON)
session.viewports['Viewport: 1'].partDisplay.geometryOptions.setValues(
    referenceRepresentation=OFF)
mdb.models['Model-1'].HomogeneousShellSection(name='Section-2', 
    preIntegrate=OFF, material='Q390', thicknessType=UNIFORM, thickness=24.0, 
    thicknessField='', nodalThicknessField='', idealization=NO_IDEALIZATION, 
    poissonDefinition=DEFAULT, thicknessModulus=None, temperature=GRADIENT, 
    useDensity=OFF, integrationRule=SIMPSON, numIntPts=5)
p = mdb.models['Model-1'].parts['HCDLGB24mm']
f = p.faces
faces = f.getSequenceFromMask(mask=('[#1ff ]', ), )
region = regionToolset.Region(faces=faces)
p = mdb.models['Model-1'].parts['HCDLGB24mm']
p.SectionAssignment(region=region, sectionName='Section-2', offset=0.0, 
    offsetType=MIDDLE_SURFACE, offsetField='', 
    thicknessAssignment=FROM_SECTION)
session.viewports['Viewport: 1'].partDisplay.setValues(sectionAssignments=OFF, 
    engineeringFeatures=OFF, mesh=ON)
session.viewports['Viewport: 1'].partDisplay.meshOptions.setValues(
    meshTechnique=ON)
p = mdb.models['Model-1'].parts['HCDLGB24mm']
p.seedPart(size=200.0, deviationFactor=0.1, minSizeFactor=0.1)
p = mdb.models['Model-1'].parts['HCDLGB24mm']
p.generateMesh()
a = mdb.models['Model-1'].rootAssembly
session.viewports['Viewport: 1'].setValues(displayedObject=a)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(
    optimizationTasks=OFF, geometricRestrictions=OFF, stopConditions=OFF)
a = mdb.models['Model-1'].rootAssembly
a.DatumCsysByDefault(CARTESIAN)
p = mdb.models['Model-1'].parts['HC18mm']
a.Instance(name='HC18mm-1', part=p, dependent=ON)
p = mdb.models['Model-1'].parts['HCDLGB24mm']
a.Instance(name='HCDLGB24mm-1', part=p, dependent=ON)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(mesh=ON)
session.viewports['Viewport: 1'].assemblyDisplay.meshOptions.setValues(
    meshTechnique=ON)
