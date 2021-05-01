from math import tan
import numpy as np

PI_OVER_360 = 0.0087266

def create_perspective_projection_matrix(fov: float , aspect: float , znear:float , zfar: float):
    xymax = float(znear * tan(fov * PI_OVER_360))
    ymin  = float(-xymax)
    xmin  = float(-xymax)

    width  = float(xymax - xmin)
    height = float(xymax - ymin)

    depth = float(zfar - znear)
    q     = float(-(zfar + znear) / depth)
    qn    = float(-2 * (zfar * znear) / depth)

    w = float(2 * znear / width)
    w = w / aspect
    h = float(2 * znear / height)

    m1 = 4 * [0]
    m2 = 4 * [0]
    m3 = 4 * [0]
    m4 = 4 * [0]

    m1[0] = w
    m2[1] = h
    m3[2] = q
    m3[3] = -1
    m4[2] = qn

    return np.array([m1,m2,m3,m4], dtype=np.float32)