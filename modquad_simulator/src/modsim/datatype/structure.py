import numpy as np

from modsim import params


class Structure:

    def __init__(self, xx=[0], yy=[0], motor_failure=[]):
        self.xx = xx
        self.yy = yy
        self.motor_failure = motor_failure  # set of tuples, (module from 0 to n-1, rotor number from 0 to 3)
        self.motor_roll = [[0, 0, 0, 0], [0, 0, 0, 0]]
        self.motor_pitch = [[0, 0, 0, 0], [0, 0, 0, 0]]

        # TMP override
        # self.xx = [0, params.cage_width]
        # self.yy = [0, 0]

        ##
        self.n = len(self.xx)  # Number of modules
        self.xx = np.array(self.xx) - np.average(self.xx)  # x-coordinates with respect to the center of mass
        self.yy = np.array(self.yy) - np.average(self.yy)  # y-coordinates with respect to the center of mass

        # Equation (4) of the Modquad paper
        # FIXME inertia with parallel axis theorem is not working. Temporary multiplied by zero
        self.inertia_tensor = self.n * np.array(params.I) + 0 * params.mass * np.diag([
            np.sum(self.yy ** 2),
            np.sum(self.xx ** 2),
            np.sum(self.yy ** 2) + np.sum(self.xx ** 2)
        ])

        # print self.n
        # self.inertia_tensor = self.n * np.array(params.I)
        # self.inertia_tensor = params.I
        self.inverse_inertia = np.linalg.inv(self.inertia_tensor)

        # self.inertia_tensor = params.I
        # self.inverse_inertia = params.invI
