import numpy as np

def compute_hamiltonian(x, y, x0, y0, px, py, omega_x, omega_y, delta, delta_12, cx, cy):
    '''
    This function computes Hamiltonian matrix
    x0 (float): initial position in x direction
    y0 (float): initial position in y direction
    px (float): momentum in x direction
    py (float): momentum in y direction
    Vector omega = (omega_x, omega_y) : is a normal vector to the degeneracy line where VD = VA
    delta (float): energy difference between V_D and V_A
    delta_12 (float): determines the displacement of the zero coupling line along the C vector
    Vector C = (CX, CY) : determines a coupling directionand is a normal vector to a zero coupling...
    line where Vc = 0
    Returns:
    H (matrix): Hamiltonian matrix'''
    
    TS = 0.5*(px**2+py**2)
    TS = np.array([[TS, 0],[0, TS]])
    VD = 0.5 * ((omega_x**2)*(x+x0)**2+(omega_y**2)*(y+y0)**2+delta)
    VA = 0.5 * ((omega_x**2)*(x-x0)**2+(omega_y**2)*(y-y0)**2-delta)
    VC = cx*x+cy*y+delta_12
    HS = TS+np.array([[VA,VC],[VC,VD]])


    q = [1,2,3,4,5,6]
    omega = [1,2,3,4,5,6]
    p = [1,2,3,4,5,6]
    N = 6
    valueb = 0
    for j in range(0,N-2):
        valueb = valueb + (p[j]**2+(omega[j]**2)*(q[j]**2))
    valueb = 0.5*valueb
    HB = np.array([[valueb,0],[0,valueb]])


    lmbdax = [1,2,3,4,5,6]
    lmbday = [1,2,3,4,5,6]
    N = 6
    valuesb = 0
    for j in range(0,N-2):
        valuesb = valuesb + (lmbdax[j]*x+lmbday[j]*y)*q[j]
    HSB = np.array([[valuesb,0],[0,valuesb]])
    
    H = HS+HSB+HB
    return H


