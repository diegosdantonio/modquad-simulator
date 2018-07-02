from scipy import linalg
from math import sin, cos, sqrt, pi



def trajhandle(t):
    """
    Circular trajectory.
    :param t:
    :return:
    """
    t_max = 30

    A = [[1, 0, 0, 0, 0, 0],
         [1, t_max, (t_max) ** 2, (t_max) ** 3, (t_max) ** 4, (t_max) ** 5],
         [0, 1, 0, 0, 0, 0],
         [0, 1, 2 * t_max, 3 * (t_max) ** 2, 4 * (t_max) ** 3, 5 * (t_max) ** 4],
         [0, 0, 2, 0, 0, 0],
         [0, 0, 2, 6 * t_max, 12 * (t_max) ** 2, 20 * (t_max) ** 3]]

    b = [0, 1, 0, 0, 0, 0]
    a = linalg.solve(A, b)

    q = a[0] + a[1] * t + a[2] * (t ** 2) + a[3] * (t ** 3) + a[4] * (t ** 4) + a[5] * (t ** 5)
    qv = a[1] + 2 * a[2] * t + 3 * a[3] * (t ** 2) + 4 * a[4] * t ** 3 + 5 * a[5] * t ** 4
    qa = 2 * a[2] + 6 * a[3] * t + 12 * a[4] * t ** 2 + 20 * a[5] * t ** 3

    pos = [5 * cos(2 * pi * q), 5 * sin(2 * pi * q), 2.5 * q]
    vel = [-5 * 2 * pi * sin(2 * pi * q) * qv, 5 * 2 * pi * cos(2 * pi * q) * qv, 2.5 * qv]
    acc = [5 * (-2 * pi * sin(2 * pi * q) * qa - 4 * pi ** 2 * cos(2 * pi * q) * qv ** 2),
           5 * (2 * pi * cos(2 * pi * q) * qa - 4 * pi ** 2 * sin(2 * pi * q) * qv ** 2), 2.5 * qa]

    yaw = 0
    yawdot = 0
    return [pos, vel, acc, yaw, yawdot]