
# stp material mesh
# #import stp
step = mdb.openStep(r'Path_Stp', scaleFromFile=ON)
# #make part
mdb.models['Model-1'].PartFromGeometryFile(name='P-Part_Name',
    geometryFile=step, combine=True, dimensionality=THREE_D,
    type=DEFORMABLE_BODY)
# #make section
mdb.models['Model-1'].HomogeneousShellSection(name='Section-P-Part_Name',
    preIntegrate=OFF, material= 'Material_Q', thicknessType=UNIFORM, thickness=Thick_Section,
    thicknessField='', nodalThicknessField='', idealization=NO_IDEALIZATION,
    poissonDefinition=DEFAULT, thicknessModulus=None, temperature=GRADIENT,
    useDensity=OFF, integrationRule=SIMPSON, numIntPts=5)
# #assign
p = mdb.models['Model-1'].parts['P-Part_Name']
f = p.faces
num = len(f)
face_need = f[0:num]
region = regionToolset.Region(faces=face_need)
p = mdb.models['Model-1'].parts['P-Part_Name']
p.SectionAssignment(region=region, sectionName='Section-P-Part_Name', offset=0.0,
    offsetType=MIDDLE_SURFACE, offsetField='',
    thicknessAssignment=FROM_SECTION)
# #mesh
p = mdb.models['Model-1'].parts['P-Part_Name']
p.seedPart(size=Size_Mesh, deviationFactor=0.1, minSizeFactor=0.1)
p = mdb.models['Model-1'].parts['P-Part_Name']
p.generateMesh()