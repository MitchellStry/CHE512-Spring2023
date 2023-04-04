import numpy as np

class Hamiltonian:
    def __init__(self, x0, y0, px, py, omega_x, omega_y, delta, delta_12, cx, cy):
        self.x0 = x0
        self.y0 = y0
        self.px = px
        self.py = py
        self.omega_x = omega_x
        self.omega_y = omega_y
        self.delta = delta
        self.delta_12 = delta_12
        self.cx = cx
        self.cy = cy

    def compute_hamiltonian(self, x, y):
        TS = 0.5 * (self.px**2 + self.py**2)
        TS = np.array([[TS, 0], [0, TS]])
        
        VD = 0.5 * ((self.omega_x**2) * (x + self.x0)**2 + (self.omega_y**2) * (y + self.y0)**2 + self.delta)
        VA = 0.5 * ((self.omega_x**2) * (x - self.x0)**2 + (self.omega_y**2) * (y - self.y0)**2 - self.delta)
        VC = self.cx * x + self.cy * y + self.delta_12
        HS = TS + np.array([[VA, VC], [VC, VD]])

        q = [1, 2, 3, 4, 5, 6]
        omega = [1, 2, 3, 4, 5, 6]
        p = [1, 2, 3, 4, 5, 6]
        N = 6
        valueb = 0
        for j in range(0, N - 2):
            valueb = valueb + (p[j]**2 + (omega[j]**2) * (q[j]**2))
        valueb = 0.5 * valueb
        HB = np.array([[valueb, 0], [0, valueb]])

        lmbdax = [1, 2, 3, 4, 5, 6]
        lmbday = [1, 2, 3, 4, 5, 6]
        N = 6
        valuesb = 0
        for j in range(0, N - 2):
            valuesb = valuesb + (lmbdax[j] * x + lmbday[j] * y) * q[j]
        HSB = np.array([[valuesb, 0], [0, valuesb]])

        H = HS + HSB + HB
        return H

# Example
hamiltonian = Hamiltonian(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
H = hamiltonian.compute_hamiltonian(1, 2)
print(H)
