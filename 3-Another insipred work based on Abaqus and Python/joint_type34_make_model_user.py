# -*- coding:utf-8 -*-
from joint_type34_make_model import *

if __name__ == '__main__':
    # to do#

    joint_example = joint32_model(geometry_column_1, geometry_plate_1, num_beams_1,
                                   geometry_beam1_1, geometry_beam2_1, geometry_beam3_1, geometry_beam4_1,
                                   num_supports, geometry_support_board, support_compress_1,
                                   material_property_1, material_support_1, mesh_size_1, compute_set_1)

    joint_example.step1_part()
    joint_example.step2_assembly()
    joint_example.step3_property()
    joint_example.step4_mesh()
    joint_example.step5_RP()
    joint_example.step6_interation()
    joint_example.step7_step_out()
    joint_example.step8_load()
    joint_example.step9_job_submit()
