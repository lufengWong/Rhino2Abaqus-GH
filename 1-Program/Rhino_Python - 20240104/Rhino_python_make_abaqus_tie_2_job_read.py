
import os
import time
from tqdm import tqdm

def make_Abaqus_txt_2(path_python_txt, path_file_cae, path_file_igs):
    # 将tmp文件储存在file_cae文件夹中
    path_file_cae_in = os.path.dirname(path_file_cae)
    path_python_txt_abs = os.path.join(path_file_cae_in, 'A-Joint_make_abaqus_tie_2_job.py')

    # path_abs = os.path.join(path_files, 'A-abaqus')  # cae文件及其所在位置
    # path_python_txt_abs = os.path.join(path_files, 'A-Joint_make_abaqus.py')

    # delete the existed script
    if os.path.exists(path_python_txt_abs):
        os.remove(path_python_txt_abs)
        print('Have deleted the script used !')

    # 1 TIE
    fileTemp = ''
    with open(os.path.join(path_python_txt, 'Function_txt_abaqus_1_tie.py'), "r", encoding="utf-8") as f:
        for line in f:
            if 'PATH_CAE' in line:
                line = line.replace('PATH_CAE', str(path_file_cae))
            fileTemp += line
    with open(path_python_txt_abs, "a", encoding="utf-8") as f:
        f.write(fileTemp)

    # 2 import igs
    fileTemp = ''
    with open(os.path.join(path_python_txt, 'Function_txt_abaqus_2_igs.py'), "r", encoding="utf-8") as f:
        for line in f:
            if 'PATH_IGS' in line:
                line = line.replace('PATH_IGS', str(path_file_igs))
            fileTemp += line
    with open(path_python_txt_abs, "a", encoding="utf-8") as f:
        f.write(fileTemp)

    # 3 couple
    fileTemp = ''
    with open(os.path.join(path_python_txt, 'Function_txt_abaqus_3_couple.py'), "r", encoding="utf-8") as f:
        for line in f:
            fileTemp += line
    with open(path_python_txt_abs, "a", encoding="utf-8") as f:
        f.write(fileTemp)

    # 4 load
    fileTemp = ''
    with open(os.path.join(path_python_txt, 'Function_txt_abaqus_4_load.py'), "r", encoding="utf-8") as f:
        for line in f:
            fileTemp += line
    with open(path_python_txt_abs, "a", encoding="utf-8") as f:
        f.write(fileTemp)
        f.close()

    os.chdir(path_file_cae_in)

    # get_odb
    order1 = 'abaqus cae nogui=' + str(path_python_txt_abs)
    d1 = os.popen(order1)
    f1 = d1.read()
    print(f1)


def read_odb(path_python_txt, path_file, job_name, set_name, value_limited):
    # ######
    py_txt = os.path.join(path_python_txt, "Function_Rhino_python_read_result.py")

    fileTemp2 = ''
    with open(py_txt, "r", encoding="utf-8") as f:
        for line in f:
            if 'PATH_FILE_RE' in line:
                line = line.replace('PATH_FILE_RE', str(path_file))
            # fileTemp2 += line

            if 'JOB_NAME_RE' in line:
                line = line.replace('JOB_NAME_RE', str(job_name))
            # fileTemp2 += line

            if 'SET_NAME_RE' in line:
                line = line.replace('SET_NAME_RE', str(set_name))
            # fileTemp2 += line

            if 'VALUE_LIMITED' in line:
                line = line.replace('VALUE_LIMITED', str(value_limited))
            fileTemp2 += line

    path_tmp_save = os.path.join(path_file, 'A-abaqus_odb_process_user_temp.py')
    with open(path_tmp_save, "w", encoding="utf-8") as f:
        f.write(fileTemp2)

    order3 = 'abaqus python ' + str(path_tmp_save)
    d3 = os.popen(order3)
    f3 = d3.read()
    print(f3)


if __name__ == '__main__':
    path_function_txt = r'C:\Users\18328\Desktop\Rhino_Python - 20240104'

    # # tset make odb
    # path_cae = r'F:\Rhino_File\wlf\28a2af8033624db6841f55efab112140\A-abaqus.cae'
    # path_igs = r'F:\tmp\FZX.igs'
    # make_Abaqus_txt_2(path_function_txt, path_cae, path_igs)

    # test 2
    # read_odb(path_function_txt, r'F:\Rhino_File\wlf\28a2af8033624db6841f55efab112140', 'S31223',
    #          'SET-ALL', '345')

    # # ###################################################33
    # make odb
    path_dirs = r'F:\Rhino_File\GA2\Result-0105'
    path_igs = r'F:\tmp\FZX.igs'
    start_index = 0  #
    for index, file_tmp in enumerate(os.listdir(path_dirs)[start_index:]):
        print(index)
        print(file_tmp)

        t = time.localtime()
        print(t.tm_year, t.tm_mon, t.tm_mday, t.tm_hour, t.tm_min)

        path_this = os.path.join(path_dirs, file_tmp)
        path_cae = os.path.join(path_this, 'A-abaqus.cae')

        make_Abaqus_txt_2(path_function_txt, path_cae, path_igs)
        print('Yep!')

    # # read odb
    # start_index = 0
    # for index, file in enumerate(os.listdir(path_dirs)[start_index:]):
    #     print(index)
    #     print(file)
    #
    #     t = time.localtime()
    #     print(t.tm_year, t.tm_mon, t.tm_mday, t.tm_hour, t.tm_min)
    #
    #     path_this = os.path.join(path_dirs, file)
    #     read_odb(path_function_txt, path_this, 'S31223', 'SET-ALL', '345')
    #
    #     print('Yep!')



