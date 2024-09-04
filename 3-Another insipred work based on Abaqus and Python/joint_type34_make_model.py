# -*- coding: mbcs -*-
from abaqus import *
from abaqusConstants import *
from caeModules import *
from driverUtils import executeOnCaeStartup
import numpy as np


def get_circle(r, h):
    l_third = (r ** 2 - h ** 2) ** 0.5
    return l_third


def get_cross_line1_line2(k1, point1, k2, point2):
    x1, y1 = point1
    x2, y2 = point2
    y = ((x2 - x1) * k1 * k2 + (y1 * k2 - y2 * k1)) / (k2 - k1)
    x = x2 + y / k2 - y2 / k2
    cross_point = (x, y)
    return cross_point


def get_cross_line_circle(point, k, r):
    """
    :param point:
    :param k:
    :param r:
    :return: larger, small
    """
    a, b = point
    core_function = ((r ** 2) / (k ** 2 + 1)) ** 0.5
    x1 = a + core_function
    y1 = b + k * core_function
    x2 = a - core_function
    y2 = b - k * core_function
    point_1 = (x1, y1)
    point_2 = (x2, y2)
    return point_1, point_2


def get_support_board_point(debut_point, r2, h_web, l1, l2, l3, l4, l5, l6, alpha, h_deep, h_web_support):
    alpha_pi = np.tan(np.pi * alpha / 180.0)
    beta_pi = (-1) / alpha_pi
    point1 = (r2, h_web / 2)
    point2 = (r2 + l1, h_web / 2)
    point3 = (r2 + l4, h_web / 2 + l3)
    point4 = (r2, h_web / 2 + l2)
    point5 = (r2 + l5, h_web / 2 + l6)
    point6 = get_cross_line1_line2(alpha_pi, debut_point, beta_pi, point3)
    point7, point8 = get_cross_line_circle(point6, beta_pi, h_web_support / 2)
    point9 = get_cross_line_circle(point7, alpha_pi, h_deep)[1]
    point10 = get_cross_line_circle(point8, alpha_pi, h_deep)[1]

    point_anticlockwise_circle = \
        (point1, point2, point3, point7, point9, point10, point8, point5, point4)

    point_support = (point9, point10)

    return point_anticlockwise_circle, point_support


def get_area_h_section(web_thickness, flange_thickness, width, height):
    return flange_thickness * 2 * width + web_thickness * height


class joint32_model():

    def __init__(self, geometry_column, geometry_plate, num_beams,
                 geometry_beam1, geometry_beam2, geometry_beam3, geometry_beam4,
                 num_supports, geometry_support_board, support_compress,
                 material_property, material_support, mesh_size, compute_set):

        self.num_beams = num_beams
        self.h_column, self.circle1, self.circle2, self.circle3, self.t_tube, self.slope = geometry_column
        self.h_web, self.t_plate = geometry_plate
        self.l_flange1, self.w_flange1, self.t_web1 = geometry_beam1
        self.l_flange2, self.w_flange2, self.t_web2 = geometry_beam2
        self.l_flange3, self.w_flange3, self.t_web3 = geometry_beam3
        self.l_flange4, self.w_flange4, self.t_web4 = geometry_beam4
        self.mesh_size_steel, self.mesh_size_concrete = mesh_size
        self.steel_plastic_tuple, self.concrete_elastic_modu, self.concrete_compres_tuple = material_property
        self.memory_percent, self.num_Cpus, self.num_GPUS = compute_set

        self.cross1 = get_circle(self.circle3, self.w_flange1 / 2)
        self.cross2 = get_circle(self.circle3, self.w_flange2 / 2)
        self.cross3 = get_circle(self.circle3, self.w_flange3 / 2)
        self.cross4 = get_circle(self.circle3, self.w_flange4 / 2)

        # add cross
        self.cross1_2 = get_circle(self.circle2, self.w_flange1 / 2)
        self.cross2_2 = get_circle(self.circle2, self.w_flange2 / 2)

        # slope cross
        self.length_mid = self.h_web / 2 * np.tan(self.slope/180.0 * np.pi)
        self.length_displace = self.length_mid * 2
        self.length_down = self.length_mid - self.w_flange1 / 2
        self.length_up = self.length_mid + self.w_flange1 / 2
        self.cross_down = get_circle(self.circle3, self.length_down)
        self.cross_up = get_circle(self.circle3, self.length_up)

        # support
        self.num_supports = num_supports
        self.r4, self.r5, self.debut_point, self.l1, self.l2, self.l3, self.l4, self.l5, self.l6,\
        self.alpha, self.t_support_board, self.w_flange_support, self.t_support_flange\
            = geometry_support_board
        self.steel_strength_support, self.support_steel_plastic_tuple = material_support
        self.r2 = self.circle2
        self.h_web = self.h_web

        self.cross5 = get_circle(self.r5, self.w_flange_support/2)
        self.support_compress = support_compress

    def step1_part(self):

        # circle-1
        s = mdb.models['Model-1'].ConstrainedSketch(name='__profile__', sheetSize=9000.0)
        g, v, d, c = s.geometry, s.vertices, s.dimensions, s.constraints
        s.setPrimaryObject(option=STANDALONE)
        s.CircleByCenterPerimeter(center=(0.0, 0.0), point1=(self.circle1, 0.0))

        # the 1st arc
        s.ArcByCenterEnds(center=(0.0, 0.0), point1=(self.cross1, -self.w_flange1 / 2),
                          point2=(-self.length_down, -self.cross_down), direction=CLOCKWISE)

        # the 2nd arc
        s.ArcByCenterEnds(center=(0.0, 0.0), point1=(-self.length_up, -self.cross_up),
                          point2=(-self.cross1, -self.w_flange1 / 2), direction=CLOCKWISE)
        #
        # the 3rd arc
        s.ArcByCenterEnds(center=(0.0, 0.0), point1=(-self.cross1, self.w_flange1 / 2),
                          point2=(self.cross1, self.w_flange1 / 2), direction=CLOCKWISE)

        # # the 4th arc
        # s.ArcByCenterEnds(center=(0.0, 0.0), point1=(-self.length_down, self.cross_down),
        #                   point2=(self.cross1, self.w_flange1 / 2), direction=CLOCKWISE)

        # the 1st 3-lines
        s.Line(point1=(self.cross1, self.w_flange1 / 2), point2=(self.l_flange1, self.w_flange1 / 2))
        s.Line(point1=(self.l_flange1, self.w_flange1 / 2), point2=(self.l_flange1, -self.w_flange1 / 2))
        s.Line(point1=(self.l_flange1, -self.w_flange1 / 2), point2=(self.cross1, -self.w_flange1 / 2))

        # the 2nd 3-lines
        s.Line(point1=(-self.length_down, -self.cross_down), point2=(-self.length_down, -self.l_flange2))
        s.Line(point1=(-self.length_down, -self.l_flange2), point2=(-self.length_up, -self.l_flange2))
        s.Line(point1=(-self.length_up, -self.l_flange2), point2=(-self.length_up, -self.cross_up))


        # the 3rd 3-lines
        s.Line(point1=(-self.cross1, self.w_flange1 / 2),
               point2=(- (self.l_flange1 + self.length_displace), self.w_flange1 / 2))
        s.Line(point1=(-(self.l_flange1 + self.length_displace), self.w_flange1 / 2),
               point2=(-(self.l_flange1 + self.length_displace), -self.w_flange1 / 2))
        s.Line(point1=(-(self.l_flange1 + self.length_displace), -self.w_flange1 / 2),
               point2=(-self.cross1, -self.w_flange1 / 2))


        # part-plate-get
        p = mdb.models['Model-1'].Part(name='Part-plate', dimensionality=THREE_D, type=DEFORMABLE_BODY)
        p = mdb.models['Model-1'].parts['Part-plate']
        p.BaseShell(sketch=s)
        s.unsetPrimaryObject()
        p = mdb.models['Model-1'].parts['Part-plate']
        session.viewports['Viewport: 1'].setValues(displayedObject=p)
        del mdb.models['Model-1'].sketches['__profile__']

        # add plate2
        # circle-1
        s = mdb.models['Model-1'].ConstrainedSketch(name='__profile__', sheetSize=9000.0)
        g, v, d, c = s.geometry, s.vertices, s.dimensions, s.constraints
        s.setPrimaryObject(option=STANDALONE)

        s.CircleByCenterPerimeter(center=(0.0, 0.0), point1=(self.circle1, 0.0))

        # the 1st arc
        s.ArcByCenterEnds(center=(0.0, 0.0), point1=(self.cross1, -self.w_flange1 / 2),
                          point2=(-self.cross1, -self.w_flange1 / 2), direction=CLOCKWISE)

        # # the 2nd arc
        # s.ArcByCenterEnds(center=(0.0, 0.0), point1=(-self.length_up, -self.cross_up),
        #                   point2=(-self.cross1, -self.w_flange1 / 2), direction=CLOCKWISE)
        #
        # the 3rd arc
        s.ArcByCenterEnds(center=(0.0, 0.0), point1=(-self.cross1, self.w_flange1 / 2),
                          point2=(-self.length_up, self.cross_up), direction=CLOCKWISE)
        #
        # the 4th arc
        s.ArcByCenterEnds(center=(0.0, 0.0), point1=(-self.length_down, self.cross_down),
                          point2=(self.cross1, self.w_flange1 / 2), direction=CLOCKWISE)

        # the 1st 3-lines
        s.Line(point1=(self.cross1, self.w_flange1 / 2), point2=(self.l_flange1, self.w_flange1 / 2))
        s.Line(point1=(self.l_flange1, self.w_flange1 / 2), point2=(self.l_flange1, -self.w_flange1 / 2))
        s.Line(point1=(self.l_flange1, -self.w_flange1 / 2), point2=(self.cross1, -self.w_flange1 / 2))


        # the 3rd 3-lines
        s.Line(point1=(-self.cross1, self.w_flange1 / 2),
               point2=(- (self.l_flange1 + self.length_displace), self.w_flange1 / 2))
        s.Line(point1=(-(self.l_flange1 + self.length_displace), self.w_flange1 / 2),
               point2=(-(self.l_flange1 + self.length_displace), -self.w_flange1 / 2))
        s.Line(point1=(-(self.l_flange1 + self.length_displace), -self.w_flange1 / 2),
               point2=(-self.cross1, -self.w_flange1 / 2))

        # the 4th 3-lines
        s.Line(point1=(-self.length_up, self.cross_up), point2=(-self.length_up, self.l_flange2))
        s.Line(point1=(-self.length_up, self.l_flange2), point2=(-self.length_down, self.l_flange2))
        s.Line(point1=(-self.length_down, self.l_flange2), point2=(-self.length_down, self.cross_down))

        # part-plate-get
        p = mdb.models['Model-1'].Part(name='Part-plate2', dimensionality=THREE_D, type=DEFORMABLE_BODY)
        p = mdb.models['Model-1'].parts['Part-plate2']
        p.BaseShell(sketch=s)
        s.unsetPrimaryObject()
        p = mdb.models['Model-1'].parts['Part-plate2']
        session.viewports['Viewport: 1'].setValues(displayedObject=p)
        del mdb.models['Model-1'].sketches['__profile__']

        # part-web1
        x_web_dis = self.circle2 / np.cos(self.slope / 180.0 * np.pi)  # The elliptical cross line
        point_web1_1 = (x_web_dis - self.length_displace / 2, self.w_flange1 / 2)
        point_web1_2 = (x_web_dis - self.length_displace - self.length_displace / 2, -self.w_flange1 / 2)
        point_web1_3 = (self.l_flange1 - self.length_displace / 2, -self.w_flange1 / 2)
        point_web1_4 = (self.l_flange1 - self.length_displace / 2, self.w_flange1 / 2)
        p = mdb.models['Model-1'].parts['Part-plate']
        s = mdb.models['Model-1'].ConstrainedSketch(name='__profile__', sheetSize=8000.0)
        g, v, d, c = s.geometry, s.vertices, s.dimensions, s.constraints
        s.setPrimaryObject(option=STANDALONE)
        s.Line(point1=point_web1_1, point2=point_web1_2)
        s.Line(point1=point_web1_2, point2=point_web1_3)
        s.HorizontalConstraint(entity=g[3], addUndoState=False)
        s.Line(point1=point_web1_3, point2=point_web1_4)
        s.VerticalConstraint(entity=g[4], addUndoState=False)
        s.PerpendicularConstraint(entity1=g[3], entity2=g[4], addUndoState=False)
        s.Line(point1=point_web1_4, point2=point_web1_1)
        s.HorizontalConstraint(entity=g[5], addUndoState=False)
        s.PerpendicularConstraint(entity1=g[4], entity2=g[5], addUndoState=False)
        p = mdb.models['Model-1'].Part(name='Part-web1', dimensionality=THREE_D,
                                       type=DEFORMABLE_BODY)
        p = mdb.models['Model-1'].parts['Part-web1']
        p.BaseShell(sketch=s)
        s.unsetPrimaryObject()
        p = mdb.models['Model-1'].parts['Part-web1']
        del mdb.models['Model-1'].sketches['__profile__']


        # part-web2
        ellipse_b = self.circle2
        ellipse_a = self.circle2 / np.sin(self.slope/180.0 * np.pi)
        ellipse_random_x = ellipse_a / 2.0
        ellipse_random_y = ((1.0 - (ellipse_random_x ** 2.0 / ellipse_a ** 2.0)) * (ellipse_b ** 2)) ** 0.5

        ellipse_cross_x_abs = self.w_flange2 / 2.0
        ellipse_cross_y_abs = ((1.0 - (ellipse_cross_x_abs ** 2.0 / ellipse_a ** 2.0)) * (ellipse_b ** 2)) ** 0.5

        s1 = mdb.models['Model-1'].ConstrainedSketch(name='__profile__',sheetSize=8000.0)
        g, v, d, c = s1.geometry, s1.vertices, s1.dimensions, s1.constraints
        s1.setPrimaryObject(option=STANDALONE)
        s1.EllipseByCenterPerimeter(center=(0.0, 0.0), axisPoint1=(ellipse_a, 0.0), axisPoint2=(0.0, -ellipse_b))

        s1.Line(point1=(-ellipse_cross_x_abs, -ellipse_cross_y_abs),
                point2=(-ellipse_cross_x_abs, -self.l_flange2))
        s1.VerticalConstraint(entity=g[4], addUndoState=False)
        s1.CoincidentConstraint(entity1=v[3], entity2=g[2], addUndoState=False)
        s1.Line(point1=(-ellipse_cross_x_abs, -self.l_flange2),
                point2=(ellipse_cross_x_abs, -self.l_flange2))
        s1.HorizontalConstraint(entity=g[5], addUndoState=False)
        s1.PerpendicularConstraint(entity1=g[4], entity2=g[5], addUndoState=False)
        s1.Line(point1=(ellipse_cross_x_abs, -self.l_flange2),
                point2=(ellipse_cross_x_abs, -ellipse_cross_y_abs))
        s1.VerticalConstraint(entity=g[6], addUndoState=False)
        s1.PerpendicularConstraint(entity1=g[5], entity2=g[6], addUndoState=False)
        s1.CoincidentConstraint(entity1=v[6], entity2=g[2], addUndoState=False)
        s1.autoTrimCurve(curve1=g[2], point1=(-ellipse_a, 0))
        s1.autoTrimCurve(curve1=g[7], point1=(ellipse_random_x, -ellipse_random_y))
        p = mdb.models['Model-1'].Part(name='Part-web2', dimensionality=THREE_D,type=DEFORMABLE_BODY)
        p = mdb.models['Model-1'].parts['Part-web2']
        p.BaseShell(sketch=s1)
        s1.unsetPrimaryObject()
        p = mdb.models['Model-1'].parts['Part-web2']
        del mdb.models['Model-1'].sketches['__profile__']

        # part-tube
        s = mdb.models['Model-1'].ConstrainedSketch(name='__profile__', sheetSize=9000.0)
        g, v, d, c = s.geometry, s.vertices, s.dimensions, s.constraints
        s.setPrimaryObject(option=STANDALONE)
        s.CircleByCenterPerimeter(center=(0.0, 0.0), point1=(self.circle2, 0.0))
        p = mdb.models['Model-1'].Part(name='Part-tube', dimensionality=THREE_D, type=DEFORMABLE_BODY)
        p = mdb.models['Model-1'].parts['Part-tube']
        p.BaseShellExtrude(sketch=s, depth=self.h_column)
        s.unsetPrimaryObject()
        p = mdb.models['Model-1'].parts['Part-tube']
        session.viewports['Viewport: 1'].setValues(displayedObject=p)
        del mdb.models['Model-1'].sketches['__profile__']

        # part-column
        s1 = mdb.models['Model-1'].ConstrainedSketch(name='__profile__', sheetSize=9000.0)
        g, v, d, c = s1.geometry, s1.vertices, s1.dimensions, s1.constraints
        s1.setPrimaryObject(option=STANDALONE)
        s1.CircleByCenterPerimeter(center=(0.0, 0.0), point1=(self.circle2, 0.0))
        p = mdb.models['Model-1'].Part(name='Part-column', dimensionality=THREE_D, type=DEFORMABLE_BODY)
        p = mdb.models['Model-1'].parts['Part-column']
        p.BaseSolidExtrude(sketch=s1, depth=self.h_column)
        s1.unsetPrimaryObject()
        p = mdb.models['Model-1'].parts['Part-column']
        session.viewports['Viewport: 1'].setValues(displayedObject=p)
        del mdb.models['Model-1'].sketches['__profile__']

        # part-support-plate
        s = mdb.models['Model-1'].ConstrainedSketch(name='__profile__',
                                                    sheetSize=8000.0)
        g, v, d, c = s.geometry, s.vertices, s.dimensions, s.constraints
        s.setPrimaryObject(option=STANDALONE)
        s.CircleByCenterPerimeter(center=(0.0, 0.0), point1=(self.r4, 0.0))
        s.ArcByCenterEnds(center=(0.0, 0.0), point1=(self.cross5, -self.w_flange_support/2), point2=(
            self.cross5, self.w_flange_support/2), direction=CLOCKWISE)

        s.Line(point1=(self.cross5, self.w_flange_support/2),
               point2=(self.l6 + self.r2, self.w_flange_support/2))
        s.HorizontalConstraint(entity=g[4], addUndoState=False)
        s.Line(point1=(self.l6 + self.r2, self.w_flange_support/2),
        point2=(self.l6 + self.r2, - self.w_flange_support/2))
        s.VerticalConstraint(entity=g[5], addUndoState=False)

        s.PerpendicularConstraint(entity1=g[4], entity2=g[5], addUndoState=False)
        s.Line(point1=(self.l6 + self.r2, -self.w_flange_support/2),
        point2=(self.cross5, -self.w_flange_support/2))
        p = mdb.models['Model-1'].Part(name='Part-support-plate',
                                       dimensionality=THREE_D, type=DEFORMABLE_BODY)
        p = mdb.models['Model-1'].parts['Part-support-plate']
        p.BaseShell(sketch=s)
        s.unsetPrimaryObject()
        p = mdb.models['Model-1'].parts['Part-support-plate']
        del mdb.models['Model-1'].sketches['__profile__']

        # support-board
        cross_right_bottom, cross_right_bottom2 \
            = get_cross_line_circle((self.r2 + self.l5, self.h_web / 2 + self.l4),
                                    np.tan(self.alpha / 180.0 * np.pi), self.l3)

        cross_right_up, cross_right_up2 \
            = get_cross_line_circle((self.r2 + self.l6, self.h_web / 2 + self.l2),
                                    np.tan(self.alpha / 180.0 * np.pi), self.l3)

        s = mdb.models['Model-1'].ConstrainedSketch(name='__profile__',sheetSize=8000.0)
        g, v, d, c = s.geometry, s.vertices, s.dimensions, s.constraints
        s.setPrimaryObject(option=STANDALONE)
        x_dis_board = self.l2 / np.tan((90.0 - self.slope) / 180.0 * np.pi)
        s.Line(point1=(self.r2 - x_dis_board, self.h_web/2), point2=(self.r2 + self.l1, self.h_web/2))

        s.HorizontalConstraint(entity=g[2], addUndoState=False)
        s.Line(point1=(self.r2 + self.l1, self.h_web/2),
               point2=(self.r2 + self.l5, self.h_web/2 + self.l4))
        #
        s.Line(point1=(self.r2 + self.l5, self.h_web/2 + self.l4),
               point2=cross_right_bottom)

        s.Line(point1=cross_right_bottom, point2=cross_right_up)

        s.Line(point1=cross_right_up, point2=(self.r2 + self.l6, self.h_web / 2 + self.l2))
        s.Line(point1=(self.r2 + self.l6, self.h_web / 2 + self.l2), point2=(self.r2, self.h_web / 2 + self.l2))
        s.HorizontalConstraint(entity=g[7], addUndoState=False)
        s.Line(point1=(self.r2, self.h_web / 2 + self.l2), point2=(self.r2 - x_dis_board, self.h_web/2))
        # s.VerticalConstraint(entity=g[8], addUndoState=False)
        # s.PerpendicularConstraint(entity1=g[7], entity2=g[8], addUndoState=False)
        p = mdb.models['Model-1'].Part(name='Part-support-board', dimensionality=THREE_D, type=DEFORMABLE_BODY)
        p = mdb.models['Model-1'].parts['Part-support-board']
        p.BaseShell(sketch=s)
        s.unsetPrimaryObject()
        p = mdb.models['Model-1'].parts['Part-support-board']
        del mdb.models['Model-1'].sketches['__profile__']

        # support-flange-1
        point_flange1_point1, point_flange1_point2\
            = get_cross_line_circle((self.r2 + self.l1, self.h_web/2), 0, self.w_flange_support)
        point_flange1_point3, point_flange1_point4 \
            = get_cross_line_circle((self.r2 + self.l1, -self.h_web / 2), 0, self.w_flange_support)

        s1 = mdb.models['Model-1'].ConstrainedSketch(name='__profile__',sheetSize=8000.0)
        g, v, d, c = s1.geometry, s1.vertices, s1.dimensions, s1.constraints
        s1.setPrimaryObject(option=STANDALONE)
        s1.Line(point1=(self.r2 + self.l1, self.h_web/2), point2=(self.r2 + self.l1, -self.h_web/2))
        s1.Line(point1=(self.r2 + self.l1, -self.h_web/2), point2=point_flange1_point3)
        s1.PerpendicularConstraint(entity1=g[2], entity2=g[3], addUndoState=False)
        s1.Line(point1=point_flange1_point3, point2=point_flange1_point1)
        s1.PerpendicularConstraint(entity1=g[3], entity2=g[4], addUndoState=False)
        s1.Line(point1=point_flange1_point1, point2=(self.r2 + self.l1, self.h_web/2))
        s1.PerpendicularConstraint(entity1=g[4], entity2=g[5], addUndoState=False)
        p = mdb.models['Model-1'].Part(name='Part-flange-1', dimensionality=THREE_D, type=DEFORMABLE_BODY)
        p = mdb.models['Model-1'].parts['Part-flange-1']
        p.BaseShell(sketch=s1)
        s1.unsetPrimaryObject()
        p = mdb.models['Model-1'].parts['Part-flange-1']
        session.viewports['Viewport: 1'].setValues(displayedObject=p)
        del mdb.models['Model-1'].sketches['__profile__']

        # support-flange-2
        k_flange2 = self.l4 / (self.l5 - self.l1)
        k_flange2_vertical = - 1 / k_flange2

        point_flange2_point1, point_flange2_point2 \
            = get_cross_line_circle((self.r2 + self.l1, self.h_web / 2),
                                    k_flange2_vertical, self.w_flange_support)
        point_flange2_point3, point_flange2_point4 \
            = get_cross_line_circle((self.r2 + self.l5, self.h_web / 2 + self.l4),
                                    k_flange2_vertical, self.w_flange_support)

        s1 = mdb.models['Model-1'].ConstrainedSketch(name='__profile__', sheetSize=8000.0)
        g, v, d, c = s1.geometry, s1.vertices, s1.dimensions, s1.constraints
        s1.setPrimaryObject(option=STANDALONE)
        s1.Line(point1=(self.r2 + self.l1, self.h_web / 2), point2=(self.r2 + self.l5, self.h_web / 2 + self.l4))
        s1.Line(point1=(self.r2 + self.l5, self.h_web / 2 + self.l4), point2=point_flange2_point3)
        s1.PerpendicularConstraint(entity1=g[2], entity2=g[3], addUndoState=False)
        s1.Line(point1=point_flange2_point3, point2=point_flange2_point1)
        s1.PerpendicularConstraint(entity1=g[3], entity2=g[4], addUndoState=False)
        s1.Line(point1=point_flange2_point1, point2=(self.r2 + self.l1, self.h_web / 2))
        s1.PerpendicularConstraint(entity1=g[4], entity2=g[5], addUndoState=False)
        p = mdb.models['Model-1'].Part(name='Part-flange-2', dimensionality=THREE_D, type=DEFORMABLE_BODY)
        p = mdb.models['Model-1'].parts['Part-flange-2']
        p.BaseShell(sketch=s1)
        s1.unsetPrimaryObject()
        p = mdb.models['Model-1'].parts['Part-flange-2']
        session.viewports['Viewport: 1'].setValues(displayedObject=p)
        del mdb.models['Model-1'].sketches['__profile__']

        # support-flange-3-4
        k_flange3_4 = np.tan(self.alpha / 180.0 * np.pi)
        k_flange3_4_vertical = - 1 / k_flange3_4

        support_flange_point_bottom, support_flange_point_bottom2 = \
            get_cross_line_circle((self.r2 + self.l5, self.h_web/2 + self.l4), k_flange3_4, self.l3)

        support_flange_point_up, support_flange_point_up2 = \
            get_cross_line_circle((self.r2 + self.l6, self.h_web / 2 + self.l2), k_flange3_4, self.l3)

        point_flange3_point1, point_flange3_point2 \
            = get_cross_line_circle((self.r2 + self.l5, self.h_web / 2 + self.l4),
                                    k_flange3_4_vertical, self.w_flange_support)
        point_flange3_point3, point_flange3_point4 \
            = get_cross_line_circle(support_flange_point_bottom,
                                    k_flange3_4_vertical, self.w_flange_support)

        point_flange4_point1, point_flange4_point2 \
            = get_cross_line_circle((self.r2 + self.l6, self.h_web / 2 + self.l2),
                                    k_flange3_4_vertical, self.w_flange_support)
        point_flange4_point3, point_flange4_point4 \
            = get_cross_line_circle(support_flange_point_up,
                                    k_flange3_4_vertical, self.w_flange_support)
        # 3
        s1 = mdb.models['Model-1'].ConstrainedSketch(name='__profile__', sheetSize=8000.0)
        g, v, d, c = s1.geometry, s1.vertices, s1.dimensions, s1.constraints
        s1.setPrimaryObject(option=STANDALONE)
        s1.Line(point1=(self.r2 + self.l5, self.h_web/2 + self.l4), point2=support_flange_point_bottom)
        s1.Line(point1=support_flange_point_bottom, point2=point_flange3_point3)
        # s1.PerpendicularConstraint(entity1=g[2], entity2=g[3], addUndoState=False)
        s1.Line(point1=point_flange3_point3, point2=point_flange3_point1)
        # s1.PerpendicularConstraint(entity1=g[3], entity2=g[4], addUndoState=False)
        s1.Line(point1=point_flange3_point1, point2=(self.r2 + self.l5, self.h_web/2 + self.l4))
        # s1.PerpendicularConstraint(entity1=g[4], entity2=g[5], addUndoState=False)
        p = mdb.models['Model-1'].Part(name='Part-flange-3', dimensionality=THREE_D, type=DEFORMABLE_BODY)
        p = mdb.models['Model-1'].parts['Part-flange-3']
        p.BaseShell(sketch=s1)
        s1.unsetPrimaryObject()
        p = mdb.models['Model-1'].parts['Part-flange-3']
        session.viewports['Viewport: 1'].setValues(displayedObject=p)
        del mdb.models['Model-1'].sketches['__profile__']
        # 4
        s1 = mdb.models['Model-1'].ConstrainedSketch(name='__profile__', sheetSize=8000.0)
        g, v, d, c = s1.geometry, s1.vertices, s1.dimensions, s1.constraints
        s1.setPrimaryObject(option=STANDALONE)
        s1.Line(point1=(self.r2 + self.l6, self.h_web / 2 + self.l2), point2=support_flange_point_up)
        s1.Line(point1=support_flange_point_up, point2=point_flange4_point3)
        # s1.PerpendicularConstraint(entity1=g[2], entity2=g[3], addUndoState=False)
        s1.Line(point1=point_flange4_point3, point2=point_flange4_point1)
        # s1.PerpendicularConstraint(entity1=g[3], entity2=g[4], addUndoState=False)
        s1.Line(point1=point_flange4_point1, point2=(self.r2 + self.l6, self.h_web / 2 + self.l2))
        # s1.PerpendicularConstraint(entity1=g[4], entity2=g[5], addUndoState=False)
        p = mdb.models['Model-1'].Part(name='Part-flange-4', dimensionality=THREE_D, type=DEFORMABLE_BODY)
        p = mdb.models['Model-1'].parts['Part-flange-4']
        p.BaseShell(sketch=s1)
        s1.unsetPrimaryObject()
        p = mdb.models['Model-1'].parts['Part-flange-4']
        session.viewports['Viewport: 1'].setValues(displayedObject=p)
        del mdb.models['Model-1'].sketches['__profile__']

        # support-flange��5
        point_board_bottom = (self.r2 + self.l5, self.h_web/2 + self.l4)
        point_board_up = (self.r2 + self.l6, self.h_web / 2 + self.l2)
        k_flange5 = (point_board_up[1] - point_board_bottom[1]) / (point_board_up[0] - point_board_bottom[0])
        point_flange5_point1,point_flange5_point2 = \
            get_cross_line_circle(point_board_bottom, -1 / k_flange5, self.w_flange_support)
        point_flange5_point3, point_flange5_point4 = \
            get_cross_line_circle(point_board_up, -1 / k_flange5, self.w_flange_support)

        s1 = mdb.models['Model-1'].ConstrainedSketch(name='__profile__', sheetSize=8000.0)
        g, v, d, c = s1.geometry, s1.vertices, s1.dimensions, s1.constraints
        s1.setPrimaryObject(option=STANDALONE)
        s1.Line(point1=point_board_bottom, point2=point_board_up)
        s1.Line(point1=point_board_up, point2=point_flange5_point3)
        # s1.PerpendicularConstraint(entity1=g[2], entity2=g[3], addUndoState=False)
        s1.Line(point1=point_flange5_point3, point2=point_flange5_point1)
        # s1.PerpendicularConstraint(entity1=g[3], entity2=g[4], addUndoState=False)
        s1.Line(point1=point_flange5_point1, point2=point_board_bottom)
        # s1.PerpendicularConstraint(entity1=g[4], entity2=g[5], addUndoState=False)
        p = mdb.models['Model-1'].Part(name='Part-flange-5', dimensionality=THREE_D, type=DEFORMABLE_BODY)
        p = mdb.models['Model-1'].parts['Part-flange-5']
        p.BaseShell(sketch=s1)
        s1.unsetPrimaryObject()
        p = mdb.models['Model-1'].parts['Part-flange-5']
        session.viewports['Viewport: 1'].setValues(displayedObject=p)
        del mdb.models['Model-1'].sketches['__profile__']

    def step2_assembly(self):
        print('assembly!')
        a = mdb.models['Model-1'].rootAssembly
        a.DatumCsysByDefault(CARTESIAN)
        p = mdb.models['Model-1'].parts['Part-column']
        a.Instance(name='Part-column-1', part=p, dependent=ON)
        p = mdb.models['Model-1'].parts['Part-plate']
        a.Instance(name='Part-plate-1', part=p, dependent=ON)

        a = mdb.models['Model-1'].rootAssembly
        a.translate(instanceList=('Part-column-1',), vector=(0.0, 0.0, -self.h_column/2))
        #: The instance Part-column-1 was translated by 0., 0., -1.835E+03 with respect to the assembly coordinate system

        a = mdb.models['Model-1'].rootAssembly
        a.translate(instanceList=('Part-plate-1',), vector=(0.0, 0.0, self.h_web/2))
        #: The instance Part-plate-1 was translated by 0., 0., 150. with respect to the assembly coordinate system

        a = mdb.models['Model-1'].rootAssembly
        p = mdb.models['Model-1'].parts['Part-plate2']
        a.Instance(name='Part-plate2-1', part=p, dependent=ON)

        a = mdb.models['Model-1'].rootAssembly
        a.rotate(instanceList=('Part-plate2-1',), axisPoint=(0.0, 0.0, 0.0),
                 axisDirection=(0.0, 0.0, 1.0), angle=180.0)
        #: The instance Part-plate-2 was rotated by 180. degrees about the axis defined by the point 0., 0., 0. and the vector 0., 0., 10.

        a = mdb.models['Model-1'].rootAssembly
        a.translate(instanceList=('Part-plate2-1',), vector=(0.0, 0.0, -self.h_web/2))
        #: The instance Part-plate-2 was translated by 0., 0., -150. with respect to the assembly coordinate system

        a = mdb.models['Model-1'].rootAssembly
        a.rotate(instanceList=('Part-column-1',), axisPoint=(0.0, 0.0, 0.0),
                 axisDirection=(0.0, 1.0, 0.0), angle=self.slope)
        #: The instance Part-column-1 was rotated by 30. degrees about the axis defined by the point 0., 0., 0. and the vector 0., 10., 0.

        a = mdb.models['Model-1'].rootAssembly
        a.translate(instanceList=('Part-plate-1',), vector=(self.length_mid, 0.0, 0.0))
        #: The instance Part-plate-1 was translated by 86.6, 0., 0. with respect to the assembly coordinate system

        # a = mdb.models['Model-1'].rootAssembly
        # a.translate(instanceList=('Part-plate-2',), vector=(-self.length_mid, 0.0, 0.0))
        # #: The instance Part-plate-2 was translated by -86.6, 0., 0. with respect to the assembly coordinate system


        a = mdb.models['Model-1'].rootAssembly
        a.translate(instanceList=('Part-plate2-1',), vector=(-self.length_mid, 0.0, 0.0))
        #: The instance Part-plate-2 was translated by -86.6, 0., 0. with respect to the assembly coordinate

        a = mdb.models['Model-1'].rootAssembly
        p = mdb.models['Model-1'].parts['Part-web1']
        a.Instance(name='Part-web1-1', part=p, dependent=ON)

        a = mdb.models['Model-1'].rootAssembly
        a.rotate(instanceList=('Part-web1-1',), axisPoint=(0.0, 0.0, 0.0),
                 axisDirection=(10.0, 0.0, 0.0), angle=90.0)
        #: The instance Part-web1-1 was rotated by 90. degrees about the axis defined by the point 0., 0., 0. and the vector 10., 0., 0.

        a = mdb.models['Model-1'].rootAssembly
        a.translate(instanceList=('Part-web1-1',), vector=(self.length_mid * 2, 0.0, 0.0))
        #: The instance Part-web1-1 was translated by 173.2, 0., 0. with respect to the assembly coordinate system

        a = mdb.models['Model-1'].rootAssembly
        p = mdb.models['Model-1'].parts['Part-web1']
        a.Instance(name='Part-web1-2', part=p, dependent=ON)

        a = mdb.models['Model-1'].rootAssembly
        a.rotate(instanceList=('Part-web1-2',), axisPoint=(0.0, 0.0, 0.0),
                 axisDirection=(0.0, 1.0, 0.0), angle=180.0)
        #: The instance Part-web1-2 was rotated by 180. degrees about the axis defined by the point 0., 0., 0. and the vector 0., 10., 0.

        a = mdb.models['Model-1'].rootAssembly
        a.rotate(instanceList=('Part-web1-2',), axisPoint=(0.0, 0.0, 0.0),
                 axisDirection=(1.0, 0.0, 0.0), angle=270.0)
        #: The instance Part-web1-2 was rotated by 270. degrees about the axis defined by the point 0., 0., 0. and the vector 10., 0., 0.
        a = mdb.models['Model-1'].rootAssembly
        a.translate(instanceList=('Part-web1-2',), vector=(-self.length_mid * 2, 0.0, 0.0))
        #: The instance Part-web1-2 was translated by -173.2, 0., 0. with respect to the assembly coordinate system

        a = mdb.models['Model-1'].rootAssembly
        p = mdb.models['Model-1'].parts['Part-web2']
        a.Instance(name='Part-web2-1', part=p, dependent=ON)

        a = mdb.models['Model-1'].rootAssembly
        a.rotate(instanceList=('Part-web2-1',), axisPoint=(0.0, 0.0, 0.0),
                 axisDirection=(0.0, 1.0, 0.0), angle=90.0)
        #: The instance Part-web2-1 was rotated by 90. degrees about the axis defined by the point 0., 0., 0. and the vector 0., 10., 0.


        # tube
        a = mdb.models['Model-1'].rootAssembly
        p = mdb.models['Model-1'].parts['Part-tube']
        a.Instance(name='Part-tube-1', part=p, dependent=ON)
        a = mdb.models['Model-1'].rootAssembly
        a.translate(instanceList=('Part-tube-1',), vector=(0.0, 0.0, -self.h_column/2))
        #: The instance Part-tube-1 was translated by 0., 0., -1.835E+03 with respect to the assembly coordinate system
        a = mdb.models['Model-1'].rootAssembly
        a.rotate(instanceList=('Part-tube-1',), axisPoint=(0.0, 0.0, 0.0),
                 axisDirection=(0.0, 10.0, 0.0), angle=self.slope)
        #: The instance Part-tube-1 was rotated by 30. degrees about the axis defined by the point 0., 0., 0. and the vector 0., 10., 0.

        # assembly-support
        a = mdb.models['Model-1'].rootAssembly
        p = mdb.models['Model-1'].parts['Part-flange-1']
        a.Instance(name='Part-flange-1-1', part=p, dependent=ON)
        p = mdb.models['Model-1'].parts['Part-flange-2']
        a.Instance(name='Part-flange-2-1', part=p, dependent=ON)
        p = mdb.models['Model-1'].parts['Part-flange-3']
        a.Instance(name='Part-flange-3-1', part=p, dependent=ON)
        p = mdb.models['Model-1'].parts['Part-flange-4']
        a.Instance(name='Part-flange-4-1', part=p, dependent=ON)
        p = mdb.models['Model-1'].parts['Part-flange-5']
        a.Instance(name='Part-flange-5-1', part=p, dependent=ON)
        p = mdb.models['Model-1'].parts['Part-support-board']
        a.Instance(name='Part-support-board-1', part=p, dependent=ON)

        point_1 = (self.r2 + self.l1, self.h_web / 2, 0)
        point_2 = (self.r2 + self.l5, self.h_web / 2 + self.l4, 0)
        point_3 = (self.r2 + self.l6, self.h_web / 2 + self.l2, 0)
        k_support = np.tan(self.alpha / 180.0 * np.pi)
        k_support_vertical = -1 / k_support
        k_2_3 = (point_3[1] - point_2[1]) / (point_3[0] - point_2[0])
        k_1_2 = (point_2[1] - point_1[1]) / (point_2[0] - point_1[0])

        a = mdb.models['Model-1'].rootAssembly
        a.rotate(instanceList=('Part-flange-4-1',), axisPoint=point_3, axisDirection=(1.0, k_support, 0.0), angle=90.0)
        a = mdb.models['Model-1'].rootAssembly
        a.translate(instanceList=('Part-flange-4-1',), vector=(0.0, 0.0, self.w_flange_support / 2))
        # #: The instance Part-flange-4-1 was translated by 0., 0., -50. with respect to the assembly coordinate system

        a = mdb.models['Model-1'].rootAssembly
        a.rotate(instanceList=('Part-flange-3-1',), axisPoint=point_2, axisDirection=(1.0, k_support, 0.0), angle=90.0)
        a = mdb.models['Model-1'].rootAssembly
        a.translate(instanceList=('Part-flange-3-1',), vector=(0.0, 0.0, self.w_flange_support / 2))
        # #: The instance Part-flange-3-1 was translated by 0., 0., -50. with respect to the assembly coordinate system

        a = mdb.models['Model-1'].rootAssembly
        a.rotate(instanceList=('Part-flange-5-1',), axisPoint=point_2, axisDirection=(1.0, k_2_3, 0.0), angle=90.0)
        a = mdb.models['Model-1'].rootAssembly
        a.translate(instanceList=('Part-flange-5-1',), vector=(0.0, 0.0, -self.w_flange_support / 2))
        # #: The instance Part-flange-3-1 was translated by 0., 0., -50. with respect to the assembly coordinate system

        a = mdb.models['Model-1'].rootAssembly
        a.rotate(instanceList=('Part-flange-2-1',), axisPoint=point_1, axisDirection=(1.0, k_1_2, 0.0), angle=90.0)
        a = mdb.models['Model-1'].rootAssembly
        a.translate(instanceList=('Part-flange-2-1',), vector=(0.0, 0.0, self.w_flange_support / 2))
        # #: The instance Part-flange-3-1 was translated by 0., 0., -50. with respect to the assembly coordinate sys

        a = mdb.models['Model-1'].rootAssembly
        a.rotate(instanceList=('Part-flange-1-1',), axisPoint=(self.r2 + self.l1, self.h_web / 2, 0.0),
                 axisDirection=(0.0, -1.0, 0.0), angle=90.0)
        a = mdb.models['Model-1'].rootAssembly
        a.rotate(instanceList=('Part-flange-1-1',), axisPoint=(0.0, 0.0, 0.0), axisDirection=(1.0, 0.0, 0.0),
                 angle=90.0)
        # #: The instance Part-flange-1-1 was rotated by 90. degrees about the axis defined by the point 0., 0., 0. and the vector 10., 0., 0.
        a = mdb.models['Model-1'].rootAssembly
        a.translate(instanceList=('Part-flange-1-1',), vector=(0.0, self.w_flange_support / 2, 0.0))
        #: The instance Part-flange-1-1 was translated by 0., 50., 0. with respect to the assembly coordinate system

        a = mdb.models['Model-1'].rootAssembly
        p = mdb.models['Model-1'].parts['Part-support-plate']
        a.Instance(name='Part-support-plate-1', part=p, dependent=ON)
        a = mdb.models['Model-1'].rootAssembly
        a.translate(instanceList=('Part-support-plate-1',), vector=(0.0, 0.0, self.l2 + self.h_web / 2))
        #: The instance Part-support-plate-1 was translated by 0., 0., 123. with respect to the assembly coordinate system

        a = mdb.models['Model-1'].rootAssembly
        a.rotate(instanceList=('Part-flange-2-1', 'Part-flange-3-1', 'Part-flange-4-1',
                               'Part-flange-5-1', 'Part-support-board-1'), axisPoint=(0.0, 0.0, 0.0),
                 axisDirection=(10.0, 0.0, 0.0), angle=90.0)
        #: The instances were rotated by 90. degrees about the axis defined by the point 0., 0., 0. and the vector 10., 0., 0.

        a = mdb.models['Model-1'].rootAssembly
        a.InstanceFromBooleanMerge(name='Part-support1', instances=(
            a.instances['Part-support-board-1'], a.instances['Part-support-plate-1'],
            a.instances['Part-flange-3-1'], a.instances['Part-flange-4-1'],a.instances['Part-flange-5-1'],
            a.instances['Part-flange-1-1'], a.instances['Part-flange-2-1'],),
                                   originalInstances=SUPPRESS, domain=GEOMETRY)

        x_displace_support = np.tan(self.slope / 180.0 * np.pi) * (self.l2 + self.h_web / 2)
        x_displace_support_2 = self.circle2 / np.cos(self.slope / 180.0 * np.pi) - self.circle2
        a = mdb.models['Model-1'].rootAssembly
        a.translate(instanceList=('Part-support1-1',), vector=(x_displace_support + x_displace_support_2, 0.0, 0.0))
        #: The instance Part-support1-1 was translated by 375., 0., 0. with respect to the assembly coordinate system
        #
        # support2
        a = mdb.models['Model-1'].rootAssembly
        a.rotate(instanceList=('Part-support1-1',), axisPoint=(0.0, 0.0, 0.0),
                 axisDirection=(0.0, 0.0, 10.0), angle=180.0)
        #: The instance Part-support1-1 was rotated by 180. degrees about the axis defined by the point 0., 0., 0. and the vector 0., 0., 10.

        a = mdb.models['Model-1'].rootAssembly
        a.rotate(instanceList=('Part-support1-1',), axisPoint=(0.0, 0.0, 0.0),
                 axisDirection=(10.0, 0.0, 0.0), angle=180.0)
        #: The instance Part-support1-1 was rotated by 180. degrees about the axis defined by the point 0., 0., 0. and the vector 10., 0., 0.

        a = mdb.models['Model-1'].rootAssembly
        p = mdb.models['Model-1'].parts['Part-support1']
        a.Instance(name='Part-support1-2', part=p, dependent=ON)

        a = mdb.models['Model-1'].rootAssembly
        a.translate(instanceList=('Part-support1-2',), vector=(x_displace_support + x_displace_support_2, 0.0, 0.0))
        #: The instance Part-support1-2 was translated by 10., 0., 0. with respect to the assembly coordinate system

        a = mdb.models['Model-1'].rootAssembly
        a.InstanceFromBooleanMerge(name='Part-steel', instances=(
            a.instances['Part-plate-1'], a.instances['Part-plate2-1'],
            a.instances['Part-web1-1'], a.instances['Part-web1-2'],
            a.instances['Part-web2-1'], a.instances['Part-tube-1'],
            a.instances['Part-support1-1'], a.instances['Part-support1-2'],),
                                   originalInstances=SUPPRESS, domain=GEOMETRY)
        a = mdb.models['Model-1'].rootAssembly
        a.makeIndependent(instances=(a.instances['Part-steel-1'],))

    def step3_property(self):
        concreteElasticModu = self.concrete_elastic_modu
        concreteCompres = self.concrete_compres_tuple
        steelPlastic = self.steel_plastic_tuple
        steelPlastic_support = self.support_steel_plastic_tuple

        mdb.models['Model-1'].Material(name='CONCRETE')
        mdb.models['Model-1'].materials['CONCRETE'].Elastic(table=((concreteElasticModu, 0.2),))
        mdb.models['Model-1'].materials['CONCRETE'].ConcreteDamagedPlasticity(
            table=((40.0, 0.1, 1.16, 0.6667, 0.0005),))  # not change
        mdb.models['Model-1'].materials['CONCRETE'].concreteDamagedPlasticity.ConcreteCompressionHardening(
            table=concreteCompres)
        mdb.models['Model-1'].materials['CONCRETE'].concreteDamagedPlasticity.ConcreteTensionStiffening(
            table=((2.04, 51.0),), type=GFI)  # not change

        mdb.models['Model-1'].Material(name='STEEL')
        mdb.models['Model-1'].materials['STEEL'].Elastic(table=((206000.0, 0.3),))  # not change
        mdb.models['Model-1'].materials['STEEL'].Plastic(table=(steelPlastic,))

        mdb.models['Model-1'].Material(name='STEEL-SUPPORT')
        mdb.models['Model-1'].materials['STEEL-SUPPORT'].Elastic(table=((206000.0, 0.3),))  # not change
        mdb.models['Model-1'].materials['STEEL-SUPPORT'].Plastic(table=(steelPlastic_support,))

        # section
        mdb.models['Model-1'].HomogeneousSolidSection(name='Section-column',
                                                      material='CONCRETE', thickness=None)
        mdb.models['Model-1'].HomogeneousShellSection(name='Section-tube',
                                                      preIntegrate=OFF, material='STEEL', thicknessType=UNIFORM,
                                                      thickness=self.t_tube,
                                                      thicknessField='', nodalThicknessField='',
                                                      idealization=NO_IDEALIZATION,
                                                      poissonDefinition=DEFAULT, thicknessModulus=None,
                                                      temperature=GRADIENT,
                                                      useDensity=OFF, integrationRule=SIMPSON, numIntPts=5)
        mdb.models['Model-1'].HomogeneousShellSection(name='Section-flate',
                                                      preIntegrate=OFF, material='STEEL', thicknessType=UNIFORM,
                                                      thickness=self.t_plate,
                                                      thicknessField='', nodalThicknessField='',
                                                      idealization=NO_IDEALIZATION,
                                                      poissonDefinition=DEFAULT, thicknessModulus=None,
                                                      temperature=GRADIENT,
                                                      useDensity=OFF, integrationRule=SIMPSON, numIntPts=5)

        mdb.models['Model-1'].HomogeneousShellSection(name='Section-web1',
                                                      preIntegrate=OFF, material='STEEL', thicknessType=UNIFORM,
                                                      thickness=self.t_web1,
                                                      thicknessField='', nodalThicknessField='',
                                                      idealization=NO_IDEALIZATION,
                                                      poissonDefinition=DEFAULT, thicknessModulus=None,
                                                      temperature=GRADIENT,
                                                      useDensity=OFF, integrationRule=SIMPSON, numIntPts=5)
        mdb.models['Model-1'].HomogeneousShellSection(name='Section-web2',
                                                      preIntegrate=OFF, material='STEEL', thicknessType=UNIFORM,
                                                      thickness=self.t_web2,
                                                      thicknessField='', nodalThicknessField='',
                                                      idealization=NO_IDEALIZATION,
                                                      poissonDefinition=DEFAULT, thicknessModulus=None,
                                                      temperature=GRADIENT,
                                                      useDensity=OFF, integrationRule=SIMPSON, numIntPts=5)
        mdb.models['Model-1'].HomogeneousShellSection(name='Section-web3',
                                                      preIntegrate=OFF, material='STEEL', thicknessType=UNIFORM,
                                                      thickness=self.t_web3,
                                                      thicknessField='', nodalThicknessField='',
                                                      idealization=NO_IDEALIZATION,
                                                      poissonDefinition=DEFAULT, thicknessModulus=None,
                                                      temperature=GRADIENT,
                                                      useDensity=OFF, integrationRule=SIMPSON, numIntPts=5)
        mdb.models['Model-1'].HomogeneousShellSection(name='Section-web4',
                                                      preIntegrate=OFF, material='STEEL', thicknessType=UNIFORM,
                                                      thickness=self.t_web4,
                                                      thicknessField='', nodalThicknessField='',
                                                      idealization=NO_IDEALIZATION,
                                                      poissonDefinition=DEFAULT, thicknessModulus=None,
                                                      temperature=GRADIENT,
                                                      useDensity=OFF, integrationRule=SIMPSON, numIntPts=5)

        mdb.models['Model-1'].HomogeneousShellSection(name='Section-support-board',
                                                      preIntegrate=OFF, material='STEEL-SUPPORT', thicknessType=UNIFORM,
                                                      thickness=self.t_support_board,
                                                      thicknessField='', nodalThicknessField='',
                                                      idealization=NO_IDEALIZATION,
                                                      poissonDefinition=DEFAULT, thicknessModulus=None,
                                                      temperature=GRADIENT,
                                                      useDensity=OFF, integrationRule=SIMPSON, numIntPts=5)
        mdb.models['Model-1'].HomogeneousShellSection(name='Section-support-flange',
                                                      preIntegrate=OFF, material='STEEL-SUPPORT', thicknessType=UNIFORM,
                                                      thickness=self.t_support_flange,
                                                      thicknessField='', nodalThicknessField='',
                                                      idealization=NO_IDEALIZATION,
                                                      poissonDefinition=DEFAULT, thicknessModulus=None,
                                                      temperature=GRADIENT,
                                                      useDensity=OFF, integrationRule=SIMPSON, numIntPts=5)

        p = mdb.models['Model-1'].parts['Part-steel']
        f = p.faces
        faces = f.getSequenceFromMask(mask=('[#10021002 ]',), )
        region = regionToolset.Region(faces=faces)
        p = mdb.models['Model-1'].parts['Part-steel']
        p.SectionAssignment(region=region, sectionName='Section-support-flange',
                            offset=0.0, offsetType=MIDDLE_SURFACE, offsetField='',
                            thicknessAssignment=FROM_SECTION)

        p = mdb.models['Model-1'].parts['Part-steel']
        f = p.faces
        faces = f.getSequenceFromMask(mask=('[#f6c0f6c ]',), )
        region = regionToolset.Region(faces=faces)
        p = mdb.models['Model-1'].parts['Part-steel']
        p.SectionAssignment(region=region, sectionName='Section-support-flange',
                            offset=0.0, offsetType=MIDDLE_SURFACE, offsetField='',
                            thicknessAssignment=FROM_SECTION)

        p = mdb.models['Model-1'].parts['Part-steel']
        f = p.faces
        faces = f.getSequenceFromMask(mask=('[#110011 ]',), )
        region = regionToolset.Region(faces=faces)
        p = mdb.models['Model-1'].parts['Part-steel']
        p.SectionAssignment(region=region, sectionName='Section-support-flange',
                            offset=0.0, offsetType=MIDDLE_SURFACE, offsetField='',
                            thicknessAssignment=FROM_SECTION)

        p = mdb.models['Model-1'].parts['Part-steel']
        f = p.faces
        faces = f.getSequenceFromMask(mask=('[#20802080 ]',), )
        region = regionToolset.Region(faces=faces)
        p = mdb.models['Model-1'].parts['Part-steel']
        p.SectionAssignment(region=region, sectionName='Section-support-board',
                            offset=0.0, offsetType=MIDDLE_SURFACE, offsetField='',
                            thicknessAssignment=FROM_SECTION)

        p = mdb.models['Model-1'].parts['Part-steel']
        f = p.faces
        faces = f.getSequenceFromMask(mask=('[#40004000 #3000 ]',), )
        region = regionToolset.Region(faces=faces)
        p = mdb.models['Model-1'].parts['Part-steel']
        p.SectionAssignment(region=region, sectionName='Section-web1', offset=0.0,
                            offsetType=MIDDLE_SURFACE, offsetField='',
                            thicknessAssignment=FROM_SECTION)

        p = mdb.models['Model-1'].parts['Part-steel']
        f = p.faces
        faces = f.getSequenceFromMask(mask=('[#0 #800 ]',), )
        region = regionToolset.Region(faces=faces)
        p = mdb.models['Model-1'].parts['Part-steel']
        p.SectionAssignment(region=region, sectionName='Section-web2', offset=0.0,
                            offsetType=MIDDLE_SURFACE, offsetField='',
                            thicknessAssignment=FROM_SECTION)

        p = mdb.models['Model-1'].parts['Part-steel']
        f = p.faces
        faces = f.getSequenceFromMask(mask=('[#0 #c7e0 ]',), )
        region = regionToolset.Region(faces=faces)
        p = mdb.models['Model-1'].parts['Part-steel']
        p.SectionAssignment(region=region, sectionName='Section-flate', offset=0.0,
                            offsetType=MIDDLE_SURFACE, offsetField='',
                            thicknessAssignment=FROM_SECTION)

        p = mdb.models['Model-1'].parts['Part-steel']
        f = p.faces
        faces = f.getSequenceFromMask(mask=('[#80008000 #1f ]',), )
        region = regionToolset.Region(faces=faces)
        p = mdb.models['Model-1'].parts['Part-steel']
        p.SectionAssignment(region=region, sectionName='Section-tube', offset=0.0,
                            offsetType=MIDDLE_SURFACE, offsetField='',
                            thicknessAssignment=FROM_SECTION)

        p = mdb.models['Model-1'].parts['Part-column']
        c = p.cells
        cells = c.getSequenceFromMask(mask=('[#1 ]',), )
        region = regionToolset.Region(cells=cells)
        p = mdb.models['Model-1'].parts['Part-column']
        p.SectionAssignment(region=region, sectionName='Section-column', offset=0.0,
                            offsetType=MIDDLE_SURFACE, offsetField='',
                            thicknessAssignment=FROM_SECTION)

    def step4_mesh(self):
        # DatumPoint
        a = mdb.models['Model-1'].rootAssembly
        a.DatumPointByCoordinate(coords=(self.circle3 - self.length_displace / 2, 0.0, -self.h_web / 2))
        a = mdb.models['Model-1'].rootAssembly
        a.DatumPointByCoordinate(coords=(-self.circle3 - self.length_displace / 2, 0.0, -self.h_web / 2))
        a = mdb.models['Model-1'].rootAssembly
        a.DatumPointByCoordinate(coords=(0.0, -self.circle3, -self.h_web / 2))
        a = mdb.models['Model-1'].rootAssembly
        a.DatumPointByCoordinate(coords=(0.0, self.circle3, -self.h_web / 2))

        a = mdb.models['Model-1'].rootAssembly
        a.DatumPointByCoordinate(coords=(self.circle3 + self.length_displace / 2, 0.0, self.h_web / 2))
        a = mdb.models['Model-1'].rootAssembly
        a.DatumPointByCoordinate(coords=(-self.circle3 + self.length_displace / 2, 0.0, self.h_web / 2))
        a = mdb.models['Model-1'].rootAssembly
        a.DatumPointByCoordinate(coords=(0.0, -self.circle3, self.h_web / 2))
        a = mdb.models['Model-1'].rootAssembly
        a.DatumPointByCoordinate(coords=(0.0, self.circle3, self.h_web / 2))

        # add support plate
        a = mdb.models['Model-1'].rootAssembly
        dis_x_support = (self.l2 + self.h_web / 2.0) * np.tan(self.slope / 180.0 * np.pi)
        a.DatumPointByCoordinate(coords=(self.circle3 + dis_x_support, 0.0, self.h_web / 2 + self.l2))

        a = mdb.models['Model-1'].rootAssembly
        a.DatumPointByCoordinate(coords=(-(self.circle3 + dis_x_support), 0.0, -(self.h_web / 2 + self.l2)))

        # partition circle
        a = mdb.models['Model-1'].rootAssembly
        f1 = a.instances['Part-steel-1'].faces
        pickedFaces = f1.getSequenceFromMask(mask=('[#0 #200 ]',), )
        v1 = a.instances['Part-steel-1'].vertices
        d1 = a.datums
        a.PartitionFaceByShortestPath(point1=v1[75], point2=d1[41], faces=pickedFaces)
        #: Warning: Cannot continue yet--complete the step or cancel the procedure.

        a = mdb.models['Model-1'].rootAssembly
        f1 = a.instances['Part-steel-1'].faces
        pickedFaces = f1.getSequenceFromMask(mask=('[#0 #800 ]',), )
        d11 = a.datums
        v11 = a.instances['Part-steel-1'].vertices
        a.PartitionFaceByShortestPath(point1=d11[41], point2=v11[81],
                                      faces=pickedFaces)

        a = mdb.models['Model-1'].rootAssembly
        f1 = a.instances['Part-steel-1'].faces
        pickedFaces = f1.getSequenceFromMask(mask=('[#0 #800 ]',), )
        v1 = a.instances['Part-steel-1'].vertices
        d1 = a.datums
        a.PartitionFaceByShortestPath(point1=v1[79], point2=d1[42], faces=pickedFaces)

        a = mdb.models['Model-1'].rootAssembly
        f1 = a.instances['Part-steel-1'].faces
        pickedFaces = f1.getSequenceFromMask(mask=('[#0 #800 ]',), )
        d11 = a.datums
        v11 = a.instances['Part-steel-1'].vertices
        a.PartitionFaceByShortestPath(point1=d11[42], point2=v11[77],
                                      faces=pickedFaces)

        a = mdb.models['Model-1'].rootAssembly
        f1 = a.instances['Part-steel-1'].faces
        pickedFaces = f1.getSequenceFromMask(mask=('[#1 ]',), )
        v1 = a.instances['Part-steel-1'].vertices
        d1 = a.datums
        a.PartitionFaceByShortestPath(point1=v1[2], point2=d1[40], faces=pickedFaces)

        a = mdb.models['Model-1'].rootAssembly
        f1 = a.instances['Part-steel-1'].faces
        pickedFaces = f1.getSequenceFromMask(mask=('[#0 #8000 ]',), )
        d11 = a.datums
        v11 = a.instances['Part-steel-1'].vertices
        a.PartitionFaceByShortestPath(point1=d11[40], point2=v11[84],
                                      faces=pickedFaces)

        a = mdb.models['Model-1'].rootAssembly
        f1 = a.instances['Part-steel-1'].faces
        pickedFaces = f1.getSequenceFromMask(mask=('[#0 #1000 ]',), )
        v1 = a.instances['Part-steel-1'].vertices
        d1 = a.datums
        a.PartitionFaceByShortestPath(point1=v1[75], point2=d1[38], faces=pickedFaces)

        a = mdb.models['Model-1'].rootAssembly
        f1 = a.instances['Part-steel-1'].faces
        pickedFaces = f1.getSequenceFromMask(mask=('[#0 #1000 ]',), )
        v11 = a.instances['Part-steel-1'].vertices
        d11 = a.datums
        a.PartitionFaceByShortestPath(point1=v11[73], point2=d11[38],
                                      faces=pickedFaces)

        a = mdb.models['Model-1'].rootAssembly
        f1 = a.instances['Part-steel-1'].faces
        pickedFaces = f1.getSequenceFromMask(mask=('[#2 ]',), )
        v1 = a.instances['Part-steel-1'].vertices
        d1 = a.datums
        a.PartitionFaceByShortestPath(point1=v1[11], point2=d1[37], faces=pickedFaces)

        a = mdb.models['Model-1'].rootAssembly
        f1 = a.instances['Part-steel-1'].faces
        pickedFaces = f1.getSequenceFromMask(mask=('[#0 #10000 ]',), )
        d11 = a.datums
        v11 = a.instances['Part-steel-1'].vertices
        a.PartitionFaceByShortestPath(point1=d11[37], point2=v11[81],
                                      faces=pickedFaces)

        a = mdb.models['Model-1'].rootAssembly
        f1 = a.instances['Part-steel-1'].faces
        pickedFaces = f1.getSequenceFromMask(mask=('[#0 #8000 ]',), )
        v1 = a.instances['Part-steel-1'].vertices
        d1 = a.datums
        a.PartitionFaceByShortestPath(point1=v1[77], point2=d1[36], faces=pickedFaces)

        a = mdb.models['Model-1'].rootAssembly
        f1 = a.instances['Part-steel-1'].faces
        pickedFaces = f1.getSequenceFromMask(mask=('[#0 #40000 ]',), )
        d11 = a.datums
        v11 = a.instances['Part-steel-1'].vertices
        a.PartitionFaceByShortestPath(point1=d11[36], point2=v11[83],
                                      faces=pickedFaces)

        # partition column
        a1 = mdb.models['Model-1'].rootAssembly
        a1.makeIndependent(instances=(a1.instances['Part-column-1'],))

        a = mdb.models['Model-1'].rootAssembly
        e1 = a.instances['Part-column-1'].edges
        v1 = a.instances['Part-column-1'].vertices
        a.DatumPlaneByThreePoints(point2=v1[0], point3=v1[1],
                                  point1=a.instances['Part-column-1'].InterestingPoint(edge=e1[0],
                                                                                       rule=MIDDLE))
        # escape the beam
        a = mdb.models['Model-1'].rootAssembly
        f1 = a.instances['Part-column-1'].faces
        faces1 = f1.getSequenceFromMask(mask=('[#7 ]',), )
        f2 = a.instances['Part-steel-1'].faces
        faces2 = f2.getSequenceFromMask(mask=('[#ffffffff #fffffff ]',), )
        pickedFaces = faces1 + faces2
        d1 = a.datums
        a.PartitionFaceByDatumPlane(datumPlane=d1[58], faces=pickedFaces)

        a = mdb.models['Model-1'].rootAssembly
        c1 = a.instances['Part-column-1'].cells
        pickedCells = c1.getSequenceFromMask(mask=('[#1 ]',), )
        d11 = a.datums
        a.PartitionCellByDatumPlane(datumPlane=d11[58], cells=pickedCells)

        a = mdb.models['Model-1'].rootAssembly
        e1 = a.instances['Part-column-1'].edges
        a.DatumPlaneByThreePoints(point1=a.instances['Part-column-1'].InterestingPoint(
            edge=e1[4], rule=MIDDLE),
            point2=a.instances['Part-column-1'].InterestingPoint(edge=e1[6],
                                                                 rule=MIDDLE),
            point3=a.instances['Part-column-1'].InterestingPoint(
                edge=e1[7], rule=MIDDLE))

        a = mdb.models['Model-1'].rootAssembly
        c1 = a.instances['Part-column-1'].cells
        pickedCells = c1.getSequenceFromMask(mask=('[#3 ]',), )
        d1 = a.datums
        a.PartitionCellByDatumPlane(datumPlane=d1[61], cells=pickedCells)

        a = mdb.models['Model-1'].rootAssembly
        f1 = a.instances['Part-steel-1'].faces
        pickedFaces = f1.getSequenceFromMask(mask=('[#249 #7e00020 ]',), )
        d11 = a.datums
        a.PartitionFaceByDatumPlane(datumPlane=d11[61], faces=pickedFaces)

        # partition the beam
        a = mdb.models['Model-1'].rootAssembly
        v1 = a.instances['Part-steel-1'].vertices
        a.DatumPlaneByThreePoints(point1=v1[111], point2=v1[110], point3=v1[71])
        a = mdb.models['Model-1'].rootAssembly
        v11 = a.instances['Part-steel-1'].vertices
        a.DatumPlaneByThreePoints(point1=v11[59], point2=v11[107], point3=v11[58])

        a = mdb.models['Model-1'].rootAssembly
        v1 = a.instances['Part-steel-1'].vertices
        a.DatumPlaneByThreePoints(point1=v1[82], point2=v1[30], point3=v1[83])

        a = mdb.models['Model-1'].rootAssembly
        v11 = a.instances['Part-steel-1'].vertices
        a.DatumPlaneByThreePoints(point1=v11[23], point2=v11[24], point3=v11[25])

        a = mdb.models['Model-1'].rootAssembly
        v1 = a.instances['Part-steel-1'].vertices
        a.DatumPlaneByThreePoints(point1=v1[24], point2=v1[25], point3=v1[23])

        a = mdb.models['Model-1'].rootAssembly
        v11 = a.instances['Part-steel-1'].vertices
        a.DatumPlaneByThreePoints(point1=v11[55], point2=v11[52], point3=v11[77])

        a = mdb.models['Model-1'].rootAssembly
        v1 = a.instances['Part-steel-1'].vertices
        a.DatumPlaneByThreePoints(point1=v1[70], point2=v1[69], point3=v1[79])

        a = mdb.models['Model-1'].rootAssembly
        c1 = a.instances['Part-column-1'].cells
        pickedCells = c1.getSequenceFromMask(mask=('[#f ]',), )
        d1 = a.datums
        a.PartitionCellByDatumPlane(datumPlane=d1[66], cells=pickedCells)

        a = mdb.models['Model-1'].rootAssembly
        c1 = a.instances['Part-column-1'].cells
        pickedCells = c1.getSequenceFromMask(mask=('[#b8 ]',), )
        d11 = a.datums
        a.PartitionCellByDatumPlane(datumPlane=d11[64], cells=pickedCells)

        a = mdb.models['Model-1'].rootAssembly
        c1 = a.instances['Part-column-1'].cells
        pickedCells = c1.getSequenceFromMask(mask=('[#47 ]',), )
        d1 = a.datums
        a.PartitionCellByDatumPlane(datumPlane=d1[65], cells=pickedCells)
        a = mdb.models['Model-1'].rootAssembly
        c1 = a.instances['Part-column-1'].cells
        pickedCells = c1.getSequenceFromMask(mask=('[#47 ]',), )
        d11 = a.datums
        a.PartitionCellByDatumPlane(datumPlane=d11[68], cells=pickedCells)

        a = mdb.models['Model-1'].rootAssembly
        f1 = a.instances['Part-steel-1'].faces
        pickedFaces = f1.getSequenceFromMask(mask=('[#20000000 #0 #4940 ]',), )
        d1 = a.datums
        a.PartitionFaceByDatumPlane(datumPlane=d1[70], faces=pickedFaces)
        a = mdb.models['Model-1'].rootAssembly
        f1 = a.instances['Part-steel-1'].faces
        pickedFaces = f1.getSequenceFromMask(mask=('[#18000000 #18 #20000 ]',), )
        d11 = a.datums
        a.PartitionFaceByDatumPlane(datumPlane=d11[69], faces=pickedFaces)

        # partition support
        a = mdb.models['Model-1'].rootAssembly
        f1 = a.instances['Part-steel-1'].faces
        pickedFaces = f1.getSequenceFromMask(mask=('[#0 #400 ]',), )
        d1 = a.datums
        v1 = a.instances['Part-steel-1'].vertices
        a.PartitionFaceByShortestPath(point1=d1[44], point2=v1[95], faces=pickedFaces)

        a = mdb.models['Model-1'].rootAssembly
        f1 = a.instances['Part-steel-1'].faces
        pickedFaces = f1.getSequenceFromMask(mask=('[#400000 ]',), )
        v11 = a.instances['Part-steel-1'].vertices
        d11 = a.datums
        a.PartitionFaceByShortestPath(point1=v11[67], point2=d11[44],
                                      faces=pickedFaces)

        a = mdb.models['Model-1'].rootAssembly
        f1 = a.instances['Part-steel-1'].faces
        pickedFaces = f1.getSequenceFromMask(mask=('[#400000 ]',), )
        v1 = a.instances['Part-steel-1'].vertices
        d1 = a.datums
        a.PartitionFaceByShortestPath(point1=v1[63], point2=d1[45], faces=pickedFaces)
        a = mdb.models['Model-1'].rootAssembly
        f1 = a.instances['Part-steel-1'].faces
        pickedFaces = f1.getSequenceFromMask(mask=('[#0 #20000000 ]',), )
        v11 = a.instances['Part-steel-1'].vertices
        d11 = a.datums
        a.PartitionFaceByShortestPath(point1=v11[109], point2=d11[45],
                                      faces=pickedFaces)

        #add
        a = mdb.models['Model-1'].rootAssembly
        f1 = a.instances['Part-steel-1'].faces
        pickedFaces = f1.getSequenceFromMask(mask=('[#da000002 #42004082 #18000200 ]',
                                                   ), )
        d1 = a.datums
        a.PartitionFaceByDatumPlane(datumPlane=d1[61], faces=pickedFaces)

        # mesh
        a = mdb.models['Model-1'].rootAssembly
        partInstances = (a.instances['Part-column-1'],)
        a.seedPartInstance(regions=partInstances, size=self.mesh_size_concrete, deviationFactor=0.1,
                           minSizeFactor=0.1)
        a = mdb.models['Model-1'].rootAssembly
        partInstances = (a.instances['Part-column-1'],)
        a.generateMesh(regions=partInstances)

        a = mdb.models['Model-1'].rootAssembly
        partInstances = (a.instances['Part-steel-1'],)
        a.seedPartInstance(regions=partInstances, size=self.mesh_size_steel, deviationFactor=0.1,
                           minSizeFactor=0.1)
        a = mdb.models['Model-1'].rootAssembly
        partInstances = (a.instances['Part-steel-1'],)
        a.generateMesh(regions=partInstances)

    def step5_RP(self):
        dis_x_column = (self.h_column / 2.0) * np.sin(self.slope / 180.0 * np.pi)
        dis_z_column = (self.h_column / 2.0) * np.cos(self.slope / 180.0 * np.pi)
        dis_x_beam = (self.h_web / 2.0) * np.tan(self.slope / 180.0 * np.pi)
        # RP
        a = mdb.models['Model-1'].rootAssembly
        a.ReferencePoint(point=(dis_x_column, 0.0, dis_z_column))
        a = mdb.models['Model-1'].rootAssembly
        a.ReferencePoint(point=(-dis_x_column, 0.0, - dis_z_column))
        a = mdb.models['Model-1'].rootAssembly
        a.ReferencePoint(point=(self.l_flange1 + dis_x_beam, 0.0, 0.0))
        a = mdb.models['Model-1'].rootAssembly
        a.ReferencePoint(point=(0.0, -self.l_flange2, 0.0))
        a = mdb.models['Model-1'].rootAssembly
        a.ReferencePoint(point=(-self.l_flange3 - dis_x_beam, 0.0, 0.0))
        # a = mdb.models['Model-1'].rootAssembly
        # a.ReferencePoint(point=(0.0, self.l_flange4, 0.0))
        a = mdb.models['Model-1'].rootAssembly
        a.ReferencePoint(point=(self.circle3 + dis_x_beam, 0.0, self.h_web / 2))
        a = mdb.models['Model-1'].rootAssembly
        a.ReferencePoint(point=(self.circle3 - dis_x_beam, 0.0, -self.h_web / 2))
        a = mdb.models['Model-1'].rootAssembly
        a.ReferencePoint(point=(0.0, - self.circle3, self.h_web / 2))
        a = mdb.models['Model-1'].rootAssembly
        a.ReferencePoint(point=(0.0, - self.circle3, -self.h_web / 2))
        a = mdb.models['Model-1'].rootAssembly
        a.ReferencePoint(point=(- self.circle3 + dis_x_beam, 0.0, self.h_web / 2.0))
        a = mdb.models['Model-1'].rootAssembly
        a.ReferencePoint(point=(- self.circle3 - dis_x_beam, 0.0, -self.h_web / 2.0))
        a = mdb.models['Model-1'].rootAssembly
        a.ReferencePoint(point=(dis_x_beam, self.circle3, self.h_web / 2.0))
        a = mdb.models['Model-1'].rootAssembly
        a.ReferencePoint(point=(-dis_x_beam, self.circle3, -self.h_web / 2.0))



        # set-section
        #: The set 'Set-section-column-top' has been created (4 faces, 2 edges).
        #: The set 'Set-section-column-bottom' has been created (4 faces).
        #: The set 'Set-section-beam1' has been created (5 edges).
        #: The set 'Set-section-beam2' has been created (5 edges).
        #: The set 'Set-section-beam3' has been created (5 edges).
        #: The set 'Set-section-beam4' has been created (5 edges).
        # set-part
        #: The set 'Set-part-beam2' has been created (5 faces, 1 reference point).
        #: The set 'Set-part-beam3' has been created (5 faces, 1 reference point).
        #: The set 'Set-part-beam4' has been created (5 faces, 1 reference point).
        # set-plate
        a = mdb.models['Model-1'].rootAssembly
        e1 = a.instances['Part-steel-1'].edges
        edges1 = e1.getSequenceFromMask(mask=('[#0:3 #120000 #10 #0:2 #4 ]',), )
        f2 = a.instances['Part-column-1'].faces
        faces2 = f2.getSequenceFromMask(mask=('[#0 #44840000 ]',), )
        a.Set(edges=edges1, faces=faces2, name='Set-section-column-top')
        #: The set 'Set-section-column-top' has been created (4 faces, 4 edges).

        a = mdb.models['Model-1'].rootAssembly
        e1 = a.instances['Part-steel-1'].edges
        edges1 = e1.getSequenceFromMask(mask=('[#0:3 #8000200 #20000 #0:2 #10 ]',), )
        f2 = a.instances['Part-column-1'].faces
        faces2 = f2.getSequenceFromMask(mask=('[#0 #88500000 ]',), )
        a.Set(edges=edges1, faces=faces2, name='Set-section-column-bottom')
        #: The set 'Set-section-column-bottom' has been created (4 faces, 4 edges).

        a = mdb.models['Model-1'].rootAssembly
        e1 = a.instances['Part-steel-1'].edges
        edges1 = e1.getSequenceFromMask(mask=('[#0:2 #44200 #0 #2000000 #0:2 #10000 ]',
                                              ), )
        a.Set(edges=edges1, name='Set-section-beam1')
        #: The set 'Set-section-column-beam1' has been created (5 edges).
        a = mdb.models['Model-1'].rootAssembly
        e1 = a.instances['Part-steel-1'].edges
        edges1 = e1.getSequenceFromMask(mask=('[#0:4 #20000000 #0:2 #a480 ]',), )
        a.Set(edges=edges1, name='Set-section-beam2')
        #: The set 'Set-section-beam2' has been created (5 edges).

        a = mdb.models['Model-1'].rootAssembly
        e1 = a.instances['Part-steel-1'].edges
        edges1 = e1.getSequenceFromMask(mask=(
            '[#0:2 #10000000 #22 #0 #200 #0 #20000 ]',), )
        a.Set(edges=edges1, name='Set-section-beam3')
        #: The set 'Set-section-beam3' has been created (5 edges).

        a = mdb.models['Model-1'].rootAssembly
        f1 = a.instances['Part-steel-1'].faces
        faces1 = f1.getSequenceFromMask(mask=('[#30f0 #1719400 #0 #600 ]',), )
        a.Set(faces=faces1, name='Set-part-plate')
        #: The set 'Set-section-plate' has been created (16 faces).

        a = mdb.models['Model-1'].rootAssembly
        e1 = a.instances['Part-steel-1'].edges
        edges1 = e1.getSequenceFromMask(mask=('[#0:5 #20000000 #4b ]',), )
        a.Set(edges=edges1, name='Set-section-support1')
        #: The set 'Set-section-support1' has been created (5 edges).

        a = mdb.models['Model-1'].rootAssembly
        e1 = a.instances['Part-steel-1'].edges
        edges1 = e1.getSequenceFromMask(mask=('[#0:6 #96400000 ]',), )
        a.Set(edges=edges1, name='Set-section-support2')
        #: The set 'Set-section-support2' has been created (5 edges).

        a = mdb.models['Model-1'].rootAssembly
        f1 = a.instances['Part-steel-1'].faces
        faces1 = f1.getSequenceFromMask(mask=('[#3c0000 #6060000 #2000000 #80 ]',), )
        r2 = a.referencePoints
        refPoints2 = (r2[88],)
        a.Set(faces=faces1, referencePoints=refPoints2, name='Set-part-beam1')
        #: The set 'Set-part-beam1' has been created (10 faces, 1 reference point).

        a = mdb.models['Model-1'].rootAssembly
        f1 = a.instances['Part-steel-1'].faces
        faces1 = f1.getSequenceFromMask(mask=('[#0 #80000 #0 #5a ]',), )
        r2 = a.referencePoints
        refPoints2 = (r2[87],)
        a.Set(faces=faces1, referencePoints=refPoints2, name='Set-part-beam2')
        #: The set 'Set-part-beam2' has been created (5 faces, 1 reference point).

        a = mdb.models['Model-1'].rootAssembly
        f1 = a.instances['Part-steel-1'].faces
        faces1 = f1.getSequenceFromMask(mask=('[#3c00000 #800000 #200 #125 ]',), )
        r2 = a.referencePoints
        refPoints2 = (r2[86],)
        a.Set(faces=faces1, referencePoints=refPoints2, name='Set-part-beam3')
        #: The set 'Set-part-beam3' has been created (10 faces, 1 reference point).

        # set-RP
        #: The set 'Set-rp-column-top' has been created (1 reference point).
        #: The set 'Set-rp-column-bottom' has been created (1 reference point).
        #: The set 'Set-rp-beam1-edge' has been created (1 reference point).
        #: The set 'Set-rp-beam-up' has been created (1 reference point).
        #: The set 'Set-rp-beam1-down' has been created (1 reference point).
        #: The set 'Set-beam2-up' has been created (1 reference point).
        #: The set 'Set-rp-beam2-down' has been created (1 reference point).
        #: The set 'Set-rp-beam3-edge' has been created (1 reference point).
        #: The set 'Set-beam3-up' has been created (1 reference point).
        #: The set 'Set-rp-beam3-down' has been created (1 reference point).
        #: The set 'Set-rp-beam4-edge' has been created (1 reference point).
        #: The set 'Set-rp-beam4-up' has been created (1 reference point).
        #: The set 'Set-rp-beam4-down' has been created (1 reference point).
        a = mdb.models['Model-1'].rootAssembly
        r1 = a.referencePoints
        refPoints1 = (r1[84],)
        a.Set(referencePoints=refPoints1, name='Set-rp-column-top')
        #: The set 'Set-rp-column-top' has been created (1 reference point).
        a = mdb.models['Model-1'].rootAssembly
        r1 = a.referencePoints
        refPoints1 = (r1[85],)
        a.Set(referencePoints=refPoints1, name='Set-rp-column-bottom')
        #: The set 'Set-rp-column-bottom' has been created (1 reference point).
        a = mdb.models['Model-1'].rootAssembly
        r1 = a.referencePoints
        refPoints1 = (r1[86],)
        a.Set(referencePoints=refPoints1, name='Set-rp-beam1-edge')
        #: The set 'Set-rp-beam1-edge' has been created (1 reference point).
        a = mdb.models['Model-1'].rootAssembly
        r1 = a.referencePoints
        refPoints1 = (r1[87],)
        a.Set(referencePoints=refPoints1, name='Set-rp-beam2-edge')
        #: The set 'Set-rp-beam2-edge' has been created (1 reference point).
        a = mdb.models['Model-1'].rootAssembly
        r1 = a.referencePoints
        refPoints1 = (r1[88],)
        a.Set(referencePoints=refPoints1, name='Set-rp-beam3-edge')
        #: The set 'Set-rp-beam3-edge' has been created (1 reference point).

        a = mdb.models['Model-1'].rootAssembly
        r1 = a.referencePoints
        refPoints1 = (r1[89],)
        a.Set(referencePoints=refPoints1, name='Set-rp-beam1-up')
        #: The set 'Set-rp-beam1-up' has been created (1 reference point).
        a = mdb.models['Model-1'].rootAssembly
        r1 = a.referencePoints
        refPoints1 = (r1[90],)
        a.Set(referencePoints=refPoints1, name='Set-rp-beam1-down')
        #: The set 'Set-rp-beam1-down' has been created (1 reference point).

        a = mdb.models['Model-1'].rootAssembly
        r1 = a.referencePoints
        refPoints1 = (r1[91],)
        a.Set(referencePoints=refPoints1, name='Set-rp-beam2-up')
        #: The set 'Set-rp-beam2-up' has been created (1 reference point).
        a = mdb.models['Model-1'].rootAssembly
        r1 = a.referencePoints
        refPoints1 = (r1[92],)
        a.Set(referencePoints=refPoints1, name='Set-rp-beam2-down')
        #: The set 'Set-rp-beam2-down' has been created (1 reference point).

        a = mdb.models['Model-1'].rootAssembly
        r1 = a.referencePoints
        refPoints1 = (r1[93],)
        a.Set(referencePoints=refPoints1, name='Set-rp-beam3-up')
        #: The set 'Set-rp-beam3-up' has been created (1 reference point).
        a = mdb.models['Model-1'].rootAssembly
        r1 = a.referencePoints
        refPoints1 = (r1[94],)
        a.Set(referencePoints=refPoints1, name='Set-rp-beam3-down')
        #: The set 'Set-rp-beam3-down' has been created (1 reference point).

        a = mdb.models['Model-1'].rootAssembly
        r1 = a.referencePoints
        refPoints1 = (r1[95],)
        a.Set(referencePoints=refPoints1, name='Set-rp-beam4-up')
        #: The set 'Set-rp-beam4-up' has been created (1 reference point).
        a = mdb.models['Model-1'].rootAssembly
        r1 = a.referencePoints
        refPoints1 = (r1[96],)
        a.Set(referencePoints=refPoints1, name='Set-rp-beam4-down')
        #: The set 'Set-rp-beam4-down' has been created (1 reference point).

        # surface
        #: The surface 'Surf-tube' has been created (12 faces).
        #: The surface 'Surf-column' has been created (12 faces).
        a = mdb.models['Model-1'].rootAssembly
        s1 = a.instances['Part-steel-1'].faces
        side2Faces1 = s1.getSequenceFromMask(mask=('[#fc000000 #493b #bc000400 ]',), )
        a.Surface(side2Faces=side2Faces1, name='Surf-tube')
        #: The surface 'Surf-tube' has been created (20 faces).

        a = mdb.models['Model-1'].rootAssembly
        s1 = a.instances['Part-column-1'].faces
        side1Faces1 = s1.getSequenceFromMask(mask=('[#e0360960 #30284b02 ]',), )
        a.Surface(side1Faces=side1Faces1, name='Surf-column')
        #: The surface 'Surf-column' has been created (20 faces).

        # rp-support
        a = mdb.models['Model-1'].rootAssembly
        e1 = a.instances['Part-steel-1'].edges
        a.ReferencePoint(point=a.instances['Part-steel-1'].InterestingPoint(
            edge=e1[189], rule=MIDDLE))
        a = mdb.models['Model-1'].rootAssembly
        e11 = a.instances['Part-steel-1'].edges
        a.ReferencePoint(point=a.instances['Part-steel-1'].InterestingPoint(
            edge=e11[214], rule=MIDDLE))

        a = mdb.models['Model-1'].rootAssembly
        r1 = a.referencePoints
        refPoints1 = (r1[123],)
        a.Set(referencePoints=refPoints1, name='Set-rp-support1')
        #: The set 'Set-rp-support1' has been created (1 reference point).
        a = mdb.models['Model-1'].rootAssembly
        r1 = a.referencePoints
        refPoints1 = (r1[124],)
        a.Set(referencePoints=refPoints1, name='Set-rp-support2')
        #: The set 'Set-rp-support2' has been created (1 reference point).

    def step6_interation(self):
        # surface-surface
        mdb.models['Model-1'].ContactProperty('IntProp-1')
        mdb.models['Model-1'].interactionProperties['IntProp-1'].TangentialBehavior(
            formulation=PENALTY, directionality=ISOTROPIC, slipRateDependency=OFF,
            pressureDependency=OFF, temperatureDependency=OFF, dependencies=0, table=((
                                                                                          0.4,),), shearStressLimit=0.6,
            maximumElasticSlip=FRACTION,
            fraction=0.005, elasticSlipStiffness=None)
        mdb.models['Model-1'].interactionProperties['IntProp-1'].NormalBehavior(
            pressureOverclosure=HARD, allowSeparation=ON,
            constraintEnforcementMethod=DEFAULT)
        mdb.models['Model-1'].interactionProperties['IntProp-1'].GeometricProperties(
            contactArea=1.0, padThickness=None)
        #: The interaction property "IntProp-1" has been created.

        a = mdb.models['Model-1'].rootAssembly
        region1 = a.surfaces['Surf-tube']
        a = mdb.models['Model-1'].rootAssembly
        region2 = a.surfaces['Surf-column']
        mdb.models['Model-1'].SurfaceToSurfaceContactStd(name='Int-1',
                                                         createStepName='Initial', master=region1, slave=region2,
                                                         sliding=FINITE,
                                                         thickness=ON, interactionProperty='IntProp-1',
                                                         adjustMethod=OVERCLOSED,
                                                         initialClearance=OMIT, datumAxis=None, clearanceRegion=None,
                                                         tied=OFF)
        #: The interaction "Int-1" has been created.

        # constrain-COLUMN
        a = mdb.models['Model-1'].rootAssembly
        region4 = a.sets['Set-section-column-top']
        a = mdb.models['Model-1'].rootAssembly
        region1 = a.sets['Set-rp-column-top']
        mdb.models['Model-1'].RigidBody(name='Constraint-1', refPointRegion=region1, tieRegion=region4)

        a = mdb.models['Model-1'].rootAssembly
        region4 = a.sets['Set-section-column-bottom']
        a = mdb.models['Model-1'].rootAssembly
        region1 = a.sets['Set-rp-column-bottom']
        mdb.models['Model-1'].RigidBody(name='Constraint-2', refPointRegion=region1, tieRegion=region4)

        # constrain-edge
        a = mdb.models['Model-1'].rootAssembly
        region4 = a.sets['Set-section-beam3']
        a = mdb.models['Model-1'].rootAssembly
        region1 = a.sets['Set-rp-beam1-edge']
        mdb.models['Model-1'].RigidBody(name='Constraint-3', refPointRegion=region1, tieRegion=region4)

        a = mdb.models['Model-1'].rootAssembly
        region4 = a.sets['Set-section-beam2']
        a = mdb.models['Model-1'].rootAssembly
        region1 = a.sets['Set-rp-beam2-edge']
        mdb.models['Model-1'].RigidBody(name='Constraint-4', refPointRegion=region1, tieRegion=region4)

        a = mdb.models['Model-1'].rootAssembly
        region4 = a.sets['Set-section-beam1']
        a = mdb.models['Model-1'].rootAssembly
        region1 = a.sets['Set-rp-beam3-edge']
        mdb.models['Model-1'].RigidBody(name='Constraint-5', refPointRegion=region1, tieRegion=region4)

        # constrain-outNeed
        a = mdb.models['Model-1'].rootAssembly
        a.features['RP-6'].suppress()
        a.features['RP-7'].suppress()
        a.features['RP-8'].suppress()
        a.features['RP-9'].suppress()
        a.features['RP-10'].suppress()
        a.features['RP-11'].suppress()
        a.features['RP-12'].suppress()
        a.features['RP-13'].suppress()

        a = mdb.models['Model-1'].rootAssembly
        v1 = a.instances['Part-steel-1'].vertices
        verts1 = v1.getSequenceFromMask(mask=('[#40000 ]',), )
        region4 = regionToolset.Region(vertices=verts1)
        a = mdb.models['Model-1'].rootAssembly
        region1 = a.sets['Set-rp-beam1-up']
        mdb.models['Model-1'].RigidBody(name='Constraint-6', refPointRegion=region1,
                                        tieRegion=region4)
        a = mdb.models['Model-1'].rootAssembly
        v1 = a.instances['Part-steel-1'].vertices
        verts1 = v1.getSequenceFromMask(mask=('[#2000000 ]',), )
        region4 = regionToolset.Region(vertices=verts1)
        a = mdb.models['Model-1'].rootAssembly
        region1 = a.sets['Set-rp-beam1-down']
        mdb.models['Model-1'].RigidBody(name='Constraint-7', refPointRegion=region1,
                                        tieRegion=region4)
        a = mdb.models['Model-1'].rootAssembly
        v1 = a.instances['Part-steel-1'].vertices
        verts1 = v1.getSequenceFromMask(mask=('[#0:3 #4000 ]',), )
        region4 = regionToolset.Region(vertices=verts1)
        a = mdb.models['Model-1'].rootAssembly
        region1 = a.sets['Set-rp-beam2-up']
        mdb.models['Model-1'].RigidBody(name='Constraint-8', refPointRegion=region1,
                                        tieRegion=region4)

        a = mdb.models['Model-1'].rootAssembly
        v1 = a.instances['Part-steel-1'].vertices
        verts1 = v1.getSequenceFromMask(mask=('[#0:3 #20 ]',), )
        region4 = regionToolset.Region(vertices=verts1)
        a = mdb.models['Model-1'].rootAssembly
        region1 = a.sets['Set-rp-beam2-down']
        mdb.models['Model-1'].RigidBody(name='Constraint-9', refPointRegion=region1,
                                        tieRegion=region4)
        a = mdb.models['Model-1'].rootAssembly
        v1 = a.instances['Part-steel-1'].vertices
        verts1 = v1.getSequenceFromMask(mask=('[#0:3 #2000 ]',), )
        region4 = regionToolset.Region(vertices=verts1)
        a = mdb.models['Model-1'].rootAssembly
        region1 = a.sets['Set-rp-beam3-up']
        mdb.models['Model-1'].RigidBody(name='Constraint-10', refPointRegion=region1,
                                        tieRegion=region4)
        a = mdb.models['Model-1'].rootAssembly
        v1 = a.instances['Part-steel-1'].vertices
        verts1 = v1.getSequenceFromMask(mask=('[#0 #400000 ]',), )
        region4 = regionToolset.Region(vertices=verts1)
        a = mdb.models['Model-1'].rootAssembly
        region1 = a.sets['Set-rp-beam3-down']
        mdb.models['Model-1'].RigidBody(name='Constraint-11', refPointRegion=region1,
                                        tieRegion=region4)

        a = mdb.models['Model-1'].rootAssembly
        v1 = a.instances['Part-steel-1'].vertices
        verts1 = v1.getSequenceFromMask(mask=('[#8000 ]',), )
        region4 = regionToolset.Region(vertices=verts1)
        a = mdb.models['Model-1'].rootAssembly
        region1 = a.sets['Set-rp-beam4-up']
        mdb.models['Model-1'].RigidBody(name='Constraint-12', refPointRegion=region1,
                                        tieRegion=region4)

        a = mdb.models['Model-1'].rootAssembly
        v1 = a.instances['Part-steel-1'].vertices
        verts1 = v1.getSequenceFromMask(mask=('[#400000 ]',), )
        region4 = regionToolset.Region(vertices=verts1)
        a = mdb.models['Model-1'].rootAssembly
        region1 = a.sets['Set-rp-beam4-down']
        mdb.models['Model-1'].RigidBody(name='Constraint-13', refPointRegion=region1,
                                        tieRegion=region4)

        a = mdb.models['Model-1'].rootAssembly
        a.features['RP-6'].resume()
        a.features['RP-7'].resume()
        a.features['RP-8'].resume()
        a.features['RP-9'].resume()
        a.features['RP-10'].resume()
        a.features['RP-11'].resume()
        a.features['RP-12'].resume()
        a.features['RP-13'].resume()

        a = mdb.models['Model-1'].rootAssembly
        region4 = a.sets['Set-section-support1']
        a = mdb.models['Model-1'].rootAssembly
        region1 = a.sets['Set-rp-support1']
        mdb.models['Model-1'].RigidBody(name='Constraint-14', refPointRegion=region1,
                                        tieRegion=region4)
        a = mdb.models['Model-1'].rootAssembly
        region4 = a.sets['Set-section-support2']
        a = mdb.models['Model-1'].rootAssembly
        region1 = a.sets['Set-rp-support2']
        mdb.models['Model-1'].RigidBody(name='Constraint-15', refPointRegion=region1,
                                        tieRegion=region4)

    def step7_step_out(self):
        # step
        mdb.models['Model-1'].StaticStep(name='Step-1', previous='Initial',
                                         maxNumInc=1000, initialInc=0.005, minInc=1e-05, maxInc=0.02, nlgeom=ON)

        # field out
        regionDef = mdb.models['Model-1'].rootAssembly.sets['Set-part-beam1']
        mdb.models['Model-1'].FieldOutputRequest(name='F-Output-2',
                                                 createStepName='Step-1', variables=('S', 'MISES'), region=regionDef,
                                                 sectionPoints=DEFAULT, rebar=EXCLUDE)
        regionDef = mdb.models['Model-1'].rootAssembly.sets['Set-part-beam2']
        mdb.models['Model-1'].FieldOutputRequest(name='F-Output-3',
                                                 createStepName='Step-1', variables=('S', 'MISES'), region=regionDef,
                                                 sectionPoints=DEFAULT, rebar=EXCLUDE)
        regionDef = mdb.models['Model-1'].rootAssembly.sets['Set-part-beam3']
        mdb.models['Model-1'].FieldOutputRequest(name='F-Output-4',
                                                 createStepName='Step-1', variables=('S', 'MISES'), region=regionDef,
                                                 sectionPoints=DEFAULT, rebar=EXCLUDE)

        regionDef = mdb.models['Model-1'].rootAssembly.sets['Set-part-plate']
        mdb.models['Model-1'].FieldOutputRequest(name='F-Output-6',
                                                 createStepName='Step-1', variables=('S', 'MISES'), region=regionDef,
                                                 sectionPoints=DEFAULT, rebar=EXCLUDE)

        # history out-beam1
        regionDef = mdb.models['Model-1'].rootAssembly.sets['Set-rp-beam1-edge']
        mdb.models['Model-1'].HistoryOutputRequest(name='H-Output-2',
                                                   createStepName='Step-1',
                                                   variables=('U1', 'U2', 'U3', 'UR1', 'UR2', 'UR3',
                                                              'UT', 'RF1', 'RF2', 'RF3', 'RM1', 'RM2',
                                                              'RM3', 'RM'), region=regionDef,
                                                   sectionPoints=DEFAULT, rebar=EXCLUDE)

        regionDef = mdb.models['Model-1'].rootAssembly.sets['Set-rp-beam1-up']
        mdb.models['Model-1'].HistoryOutputRequest(name='H-Output-3',
                                                   createStepName='Step-1',
                                                   variables=('U1', 'U2', 'U3', 'UR1', 'UR2', 'UR3',
                                                              'UT'), region=regionDef,
                                                   sectionPoints=DEFAULT, rebar=EXCLUDE)

        regionDef = mdb.models['Model-1'].rootAssembly.sets['Set-rp-beam1-down']
        mdb.models['Model-1'].HistoryOutputRequest(name='H-Output-4',
                                                   createStepName='Step-1',
                                                   variables=('U1', 'U2', 'U3', 'UR1', 'UR2', 'UR3',
                                                              'UT'), region=regionDef,
                                                   sectionPoints=DEFAULT, rebar=EXCLUDE)

        # history out-beam2
        regionDef = mdb.models['Model-1'].rootAssembly.sets['Set-rp-beam2-edge']
        mdb.models['Model-1'].HistoryOutputRequest(name='H-Output-5',
                                                   createStepName='Step-1',
                                                   variables=('U1', 'U2', 'U3', 'UR1', 'UR2', 'UR3',
                                                              'UT', 'RF1', 'RF2', 'RF3', 'RM1', 'RM2',
                                                              'RM3', 'RM'), region=regionDef,
                                                   sectionPoints=DEFAULT, rebar=EXCLUDE)

        regionDef = mdb.models['Model-1'].rootAssembly.sets['Set-rp-beam2-up']
        mdb.models['Model-1'].HistoryOutputRequest(name='H-Output-6',
                                                   createStepName='Step-1',
                                                   variables=('U1', 'U2', 'U3', 'UR1', 'UR2', 'UR3',
                                                              'UT'), region=regionDef,
                                                   sectionPoints=DEFAULT, rebar=EXCLUDE)

        regionDef = mdb.models['Model-1'].rootAssembly.sets['Set-rp-beam2-down']
        mdb.models['Model-1'].HistoryOutputRequest(name='H-Output-7',
                                                   createStepName='Step-1',
                                                   variables=('U1', 'U2', 'U3', 'UR1', 'UR2', 'UR3',
                                                              'UT'), region=regionDef,
                                                   sectionPoints=DEFAULT, rebar=EXCLUDE)

        # history out-beam3
        regionDef = mdb.models['Model-1'].rootAssembly.sets['Set-rp-beam3-edge']
        mdb.models['Model-1'].HistoryOutputRequest(name='H-Output-8',
                                                   createStepName='Step-1',
                                                   variables=('U1', 'U2', 'U3', 'UR1', 'UR2', 'UR3',
                                                              'UT', 'RF1', 'RF2', 'RF3', 'RM1', 'RM2',
                                                              'RM3', 'RM'), region=regionDef,
                                                   sectionPoints=DEFAULT, rebar=EXCLUDE)

        regionDef = mdb.models['Model-1'].rootAssembly.sets['Set-rp-beam3-up']
        mdb.models['Model-1'].HistoryOutputRequest(name='H-Output-9',
                                                   createStepName='Step-1',
                                                   variables=('U1', 'U2', 'U3', 'UR1', 'UR2', 'UR3',
                                                              'UT'), region=regionDef,
                                                   sectionPoints=DEFAULT, rebar=EXCLUDE)

        regionDef = mdb.models['Model-1'].rootAssembly.sets['Set-rp-beam3-down']
        mdb.models['Model-1'].HistoryOutputRequest(name='H-Output-10',
                                                   createStepName='Step-1',
                                                   variables=('U1', 'U2', 'U3', 'UR1', 'UR2', 'UR3',
                                                              'UT'), region=regionDef,
                                                   sectionPoints=DEFAULT, rebar=EXCLUDE)

        # history out-beam4
        regionDef = mdb.models['Model-1'].rootAssembly.sets['Set-rp-beam4-up']
        mdb.models['Model-1'].HistoryOutputRequest(name='H-Output-12',
                                                   createStepName='Step-1',
                                                   variables=('U1', 'U2', 'U3', 'UR1', 'UR2', 'UR3',
                                                              'UT'), region=regionDef,
                                                   sectionPoints=DEFAULT, rebar=EXCLUDE)

        regionDef = mdb.models['Model-1'].rootAssembly.sets['Set-rp-beam4-down']
        mdb.models['Model-1'].HistoryOutputRequest(name='H-Output-13',
                                                   createStepName='Step-1',
                                                   variables=('U1', 'U2', 'U3', 'UR1', 'UR2', 'UR3',
                                                              'UT', 'RT', 'RM'), region=regionDef,
                                                   sectionPoints=DEFAULT, rebar=EXCLUDE)

        regionDef = mdb.models['Model-1'].rootAssembly.sets['Set-rp-support1']
        mdb.models['Model-1'].HistoryOutputRequest(name='H-Output-14',
                                                   createStepName='Step-1',
                                                   variables=('U1', 'U2', 'U3', 'UR1', 'UR2', 'UR3',
                                                              'UT', 'RT', 'RM', 'RF1', 'RF2', 'RF3', 'RM1', 'RM2',
                                                              'RM3', 'RM'), region=regionDef,
                                                   sectionPoints=DEFAULT, rebar=EXCLUDE)

        regionDef = mdb.models['Model-1'].rootAssembly.sets['Set-rp-support2']
        mdb.models['Model-1'].HistoryOutputRequest(name='H-Output-15',
                                                   createStepName='Step-1',
                                                   variables=('U1', 'U2', 'U3', 'UR1', 'UR2', 'UR3',
                                                              'UT', 'RT', 'RM', 'RF1', 'RF2', 'RF3', 'RM1', 'RM2',
                                                              'RM3', 'RM'), region=regionDef,
                                                   sectionPoints=DEFAULT, rebar=EXCLUDE)

    def step8_load(self):
        # load-top-bottom
        a = mdb.models['Model-1'].rootAssembly
        region = a.sets['Set-rp-column-top']
        mdb.models['Model-1'].DisplacementBC(name='BC-column-top',
                                             createStepName='Initial', region=region, u1=SET, u2=SET, u3=SET, ur1=UNSET,
                                             ur2=UNSET, ur3=SET, amplitude=UNSET, distributionType=UNIFORM,
                                             fieldName='', localCsys=None)

        a = mdb.models['Model-1'].rootAssembly
        region = a.sets['Set-rp-column-bottom']
        mdb.models['Model-1'].DisplacementBC(name='BC-column-bottom',
                                             createStepName='Initial', region=region, u1=SET, u2=SET, u3=SET, ur1=UNSET,
                                             ur2=UNSET, ur3=SET, amplitude=UNSET, distributionType=UNIFORM,
                                             fieldName='', localCsys=None)

        # load-edge
        a = mdb.models['Model-1'].rootAssembly
        region = a.sets['Set-rp-beam1-edge']
        mdb.models['Model-1'].DisplacementBC(name='BC-edge-beam1',
                                             createStepName='Step-1', region=region, u1=UNSET, u2=0.0, u3=-150.0,
                                             ur1=0.0, ur2=UNSET, ur3=0.0, amplitude=UNSET, fixed=OFF,
                                             distributionType=UNIFORM, fieldName='', localCsys=None)

        a = mdb.models['Model-1'].rootAssembly
        region = a.sets['Set-rp-beam2-edge']
        mdb.models['Model-1'].DisplacementBC(name='BC-edge-beam2',
                                             createStepName='Step-1', region=region, u1=0.0, u2=UNSET, u3=-150.0,
                                             ur1=UNSET, ur2=0.0, ur3=0.0, amplitude=UNSET, fixed=OFF,
                                             distributionType=UNIFORM, fieldName='', localCsys=None)

        a = mdb.models['Model-1'].rootAssembly
        region = a.sets['Set-rp-beam3-edge']
        mdb.models['Model-1'].DisplacementBC(name='BC-edge-beam3', createStepName='Step-1',
                                             region=region, u1=UNSET, u2=0.0, u3=-150.0, ur1=0.0, ur2=UNSET, ur3=0.0,
                                             amplitude=UNSET, fixed=OFF, distributionType=UNIFORM, fieldName='',
                                             localCsys=None)

        # support
        a = mdb.models['Model-1'].rootAssembly
        r1 = a.referencePoints
        v1 = a.instances['Part-steel-1'].vertices
        a.DatumCsysByThreePoints(origin=r1[123], point1=v1[118], point2=v1[123],
                                 name='Datum csys-support1', coordSysType=CARTESIAN)

        a = mdb.models['Model-1'].rootAssembly
        r11 = a.referencePoints
        v11 = a.instances['Part-steel-1'].vertices
        a.DatumCsysByThreePoints(origin=r11[124], point1=v11[128], point2=v11[130],
                                 name='Datum csys-support2', coordSysType=CARTESIAN)

        a = mdb.models['Model-1'].rootAssembly
        region = a.sets['Set-rp-support1']
        datum = mdb.models['Model-1'].rootAssembly.datums[135]
        mdb.models['Model-1'].DisplacementBC(name='BC-support1',
                                             createStepName='Step-1', region=region, u1=UNSET, u2=0.0, u3=-10.0,
                                             ur1=0.0, ur2=UNSET, ur3=0.0, amplitude=UNSET, fixed=OFF,
                                             distributionType=UNIFORM, fieldName='', localCsys=datum)

        a = mdb.models['Model-1'].rootAssembly
        region = a.sets['Set-rp-support2']
        datum = mdb.models['Model-1'].rootAssembly.datums[136]
        mdb.models['Model-1'].DisplacementBC(name='BC-support2',
                                             createStepName='Step-1', region=region, u1=UNSET, u2=0.0, u3=-10.0,
                                             ur1=0.0, ur2=UNSET, ur3=0.0, amplitude=UNSET, fixed=OFF,
                                             distributionType=UNIFORM, fieldName='', localCsys=datum)

        # close the boundary
        if self.num_beams == 1:
            # mdb.models['Model-1'].boundaryConditions['BC-edge-beam1'].suppress()
            mdb.models['Model-1'].boundaryConditions['BC-edge-beam2'].suppress()
            mdb.models['Model-1'].boundaryConditions['BC-edge-beam3'].suppress()
            mdb.models['Model-1'].boundaryConditions['BC-edge-beam4'].suppress()
        elif self.num_beams == 2:
            mdb.models['Model-1'].boundaryConditions['BC-edge-beam3'].suppress()
            mdb.models['Model-1'].boundaryConditions['BC-edge-beam4'].suppress()
        elif self.num_beams == 3:
            print('ok!')
        elif self.num_beams == 4:
            mdb.models['Model-1'].boundaryConditions['BC-edge-beam2'].suppress()
            mdb.models['Model-1'].boundaryConditions['BC-edge-beam4'].suppress()

        # load column
        a = mdb.models['Model-1'].rootAssembly
        r1 = a.referencePoints
        v1 = a.instances['Part-steel-1'].vertices
        a.DatumCsysByThreePoints(origin=r1[84], point1=v1[86], point2=v1[87],
                                     name='Datum csys-column', coordSysType=CARTESIAN)

        datum = mdb.models['Model-1'].rootAssembly.datums[137]
        mdb.models['Model-1'].boundaryConditions['BC-column-bottom'].setValues(
                localCsys=datum)

        datum = mdb.models['Model-1'].rootAssembly.datums[137]
        mdb.models['Model-1'].boundaryConditions['BC-column-top'].setValues(
                localCsys=datum)


    def step9_job_submit(self):
        mdb.Job(name='Job-1', model='Model-1', description='', type=ANALYSIS,
                atTime=None, waitMinutes=0, waitHours=0, queue=None, memory=50,
                memoryUnits=PERCENTAGE, getMemoryFromAnalysis=True,
                explicitPrecision=SINGLE, nodalOutputPrecision=SINGLE, echoPrint=OFF,
                modelPrint=OFF, contactPrint=OFF, historyPrint=OFF, userSubroutine='',
                scratch='', resultsFormat=ODB, multiprocessingMode=DEFAULT, numCpus=self.num_Cpus,
                numDomains=self.num_Cpus, numGPUs=self.num_GPUS)

        mdb.jobs['Job-1'].writeInput(consistencyChecking=OFF)
        #: The job input file has been written to "Job-1.inp".
        mdb.jobs['Job-1'].submit(consistencyChecking=OFF)



if __name__ == '__main__':
    table_tuple_steel_plastic = (345.0, 0.0)
    concrete_Elastic_Modu = 36000
    tuple_ConcreteCompres = (
        (10.982159009444045, 0), (19.391566321708993, 0.00010193040531817721),
        (24.508179320264276, 0.00027994096389845726),
        (26.918034904628875, 0.0005330367724423602), (27.544054329259225, 0.0008355811949952625),
        (26.47890896338067, 0.0011850000923518355), (24.196877814132492, 0.0015681191130796513),
        (21.644744904415024, 0.001958638766356623), (19.25083578573562, 0.0023446611855040267),
        (17.152688260249768, 0.002722365941261889), (15.36209086872523, 0.0030914256393465038),
        (13.846524669505321, 0.0034527436488124208), (12.563208845002526, 0.0038075083907610392),
        (11.471614149874592, 0.004156845742557793), (10.537146779016444, 0.004501716708166676),
        (9.731498640369004, 0.0048429076883487465), (9.031898590614999, 0.005181051279671543),
        (8.420125796051742, 0.0055166536811513634), (7.881588962639291, 0.005850120271196233),
        (7.404556636964908, 0.006181776988135625), (6.97954309013444, 0.006511887389000017),
        (6.598828467974566, 0.006840665978682895), (6.256087008809019, 0.00716828853722461),
        (5.946099517184168, 0.007494900106653188), (5.664530578899386, 0.007820621179456668),
        (5.407755244798146, 0.008145552512921003), (5.172723491433353, 0.008469778894112523),
        (4.9568535974985375, 0.008793372101643604), (4.7579477435587885, 0.009116393250124442),
        (4.574124778602643, 0.009438894657759789), (4.403766322702903, 0.009760921343496022),
        (4.2454732917679125, 0.010082512234667896), (4.0980306166819505, 0.010403701147022286),
        (3.9603784445020658, 0.010724517584685013), (3.8315884979733164, 0.011044987396840832))

    geometry_column_1 = [3570, 200, 250, 400, 6, 10]
    geometry_plate_1 = [300, 12]

    geometry_beam_add = np.array([geometry_column_1[3] + 2, 2, 2])
    num_beams_1 = 3
    geometry_beam1_1 = [2200, 300, 8]
    geometry_beam2_1 = [2200, 300, 8]
    geometry_beam3_1 = [2200, 300, 8]
    # geometry_beam4_1 = geometry_beam_add
    geometry_beam4_1 = [420, 20, 8]

    material_property_1 = [table_tuple_steel_plastic, concrete_Elastic_Modu, tuple_ConcreteCompres]
    mesh_size_1 = [50, 50]
    compute_set_1 = [60, 10, 2]

    num_supports = 2
    geometry_support_board = [200.0, 400.0, (0.0, 0.0),
                              300.0, 800.0, 400.0, 600.0, 600.0, 400.0,
                              45, 4.0, 100.0, 4.0]

    support_compress_1 = 45000
    material_support_1 = [360, (420.0, 0.0)]

    # example
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
    # joint_example.step9_job_submit()
