import os


def get_material_and_thick(path):
    """
    读取文件
    :param path: 文件所在的文件夹
    :return:
    """
    txt_material = os.path.join(path, 'A-material.txt')
    txt_thick = os.path.join(path, 'A-name-thick.txt')

    with open(txt_material, 'r') as file:
        content = file.read()
    material_Q = []
    for line in content.split('\n'):
        if line:
            material_Q.append(line)
    dict_material = {'name': str(material_Q[0]),
                     'elastic': [float(i) for i in material_Q[1].split(' ')],
                     'plastic': [float(j) for j in material_Q[2].split(' ')]}

    print('Material')
    print(dict_material)

    with open(txt_thick, 'r') as file:
        content = file.read()
    dict_layer_thick = {}
    for line in content.split('\n'):
        if line:
            [layer_, thick_] = (int(i) for i in line.split(' '))
            dict_layer_thick[layer_] = thick_

    print('Layer_thick')
    print(dict_layer_thick)

    return dict_material, dict_layer_thick


def pair_list(numbers):
    """make pair """
    assert len(numbers) % 2 == 0, ' Material data error！'
    return list(zip(numbers[::2], numbers[1::2]))


def make_Abaqus_txt(path_python_txt, path_files, dict_material, dict_layer_thick, size_mesh):
    path_abs = os.path.join(path_files, 'A-abaqus')  # cae文件及其所在位置

    path_python_txt_abs = os.path.join(path_files, 'A-Joint_make_abaqus.py')

    # delete the existed script
    if os.path.exists(path_python_txt_abs):
        os.remove(path_python_txt_abs)
        print('Have deleted the script used !')

    # 建立CAE文件
    fileTemp = ''
    with open(os.path.join(path_python_txt, 'Function_txt_abaqus_start.py'), "r", encoding="utf-8") as f:
        for line in f:
            if 'Path_define' in line:
                line = line.replace('Path_define', str(path_abs))

            fileTemp += line
    with open(path_python_txt_abs, "a", encoding="utf-8") as f:
        f.write(fileTemp)

    # 建立材料
    # #数据处理
    list_elastic = tuple(pair_list(dict_material['elastic']))
    list_plastic = tuple(pair_list(dict_material['plastic']))

    fileTemp = ''
    with open(os.path.join(path_python_txt, 'Function_txt_abaqus_material.py'), "r", encoding="utf-8") as f:
        for line in f:
            if 'Material_Name' in line:
                line = line.replace('Material_Name', str(dict_material['name']))
            if 'Elastic_replace' in line:
                line = line.replace('Elastic_replace', str(list_elastic))
            if 'Plastic_replace' in line:
                line = line.replace('Plastic_replace', str(list_plastic))

            fileTemp += line
    with open(path_python_txt_abs, "a", encoding="utf-8") as f:
        f.write(fileTemp)

    # 导入Stp 并赋予材料以及划分网格
    # #构件以layer_dict为准
    for layer_ele, thick_els in dict_layer_thick.items():
        path_stp_abs = os.path.join(path_files, str(layer_ele) + '.stp')

        fileTemp = ''  # avoid the repeat
        with open(os.path.join(path_python_txt, 'Function_txt_abaqus_stp_material_mesh.py'), "r",
                  encoding="utf-8") as f:
            for line in f:
                if 'Path_Stp' in line:
                    line = line.replace('Path_Stp', str(path_stp_abs))
                if 'Part_Name' in line:
                    line = line.replace('Part_Name', str(layer_ele))
                if 'Thick_Section' in line:
                    line = line.replace('Thick_Section', str(int(thick_els)))
                if 'Material_Q' in line:
                    line = line.replace('Material_Q', str(dict_material['name']))
                if 'Size_Mesh' in line:
                    line = line.replace('Size_Mesh', str(int(size_mesh)))

                fileTemp += line
        with open(path_python_txt_abs, "a", encoding="utf-8") as f:
            f.write(fileTemp)

    # 装配
    # 坐标
    fileTemp = ''
    with open(os.path.join(path_python_txt, 'Function_txt_abaqus_assembly_start.py'), "r", encoding="utf-8") as f:
        for line in f:
            fileTemp += line

    with open(path_python_txt_abs, "a", encoding="utf-8") as f:
        f.write(fileTemp)

    # 部件
    for layer_ele, thick_els in dict_layer_thick.items():

        fileTemp = ''  # avoid the repeat
        with open(os.path.join(path_python_txt, 'Function_txt_abaqus_assembly_part.py'), "r",
                  encoding="utf-8") as f:
            for line in f:
                if 'Part_Name' in line:
                    line = line.replace('Part_Name', str(layer_ele))

                fileTemp += line
        with open(path_python_txt_abs, "a", encoding="utf-8") as f:
            f.write(fileTemp)

    # 保存模型
    fileTemp = ''
    with open(os.path.join(path_python_txt, 'Function_txt_abaqus_save.py'), "r", encoding="utf-8") as f:
        for line in f:
            fileTemp += line

    with open(path_python_txt_abs, "a", encoding="utf-8") as f:
        f.write(fileTemp)

    print('Have writen the script!')

if __name__ == '__main__':
    # 测试
    path_project = r'F:\Rhino_File\Ex'
    path_python_txt = r'C:\Users\18328\Desktop\Rhino_Python'
    size_mesh = 200

    dict_material, dict_layer_thick = get_material_and_thick(path_project)
    make_Abaqus_txt(path_python_txt, path_project, dict_material, dict_layer_thick, size_mesh)
