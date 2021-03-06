"""
This module implements a 2-D diffusion PDE.

Note that an upper-case 'Y' is used to represent the Greek psi, which
represents the problem solution Y(x, y, t).

The equation is defined on the domain (x, y, t) in
([0, 1], [0, 1], [0, inf]).

The analytical form of the equation is:

  G([x, y, t], Y, delY, del2Y) = dY_dt - D*(d2Y_dx2 + d2Y_dy2) = 0

where:

x, y, t are the independent variables
delY is the vector (dY/dx, dY/dy, dY/dt)
del2Y is the vector (d2Y/dx2, d2Y_dy2, d2Y/dt2)
D is the diffusion coefficient

With boundary conditions:

Y(0, y, t) = 0
Y(1, y, t) = 0
Y(x, 0, t) = 0
Y(x, 1, t) = 0
Y(x, 0) = sin(pi*x)*sin(pi*y)

This equation has the analytical solution for the supplied initial
conditions:

Ya(x, y, t) = exp(-2*pi**2*D*t)*sin(pi*x)*sin(pi*y)

Todo:
    * Add function annotations.
    * Add variable annotations.
"""


from math import cos, exp, pi, sin
import numpy as np


# Diffusion coefficient
D = 0.1


def G(xyt, Y, delY, del2Y):
    """The differential equation in standard form"""
    (x, y, t) = xyt
    (dY_dx, dY_dy, dY_dt) = delY
    (d2Y_dx2, d2Y_dy2, d2Y_dt2) = del2Y
    return dY_dt - D*(d2Y_dx2 + d2Y_dy2)


def f0(xyt):
    """Boundary condition at (x, y, t) = (0, y, t)"""
    return 0


def f1(xyt):
    """Boundary condition at (x, y, t) = (1, y, t)"""
    return 0


def g0(xyt):
    """Boundary condition at (x, y, t) = (x, 0, t)"""
    return 0


def g1(xyt):
    """Boundary condition at (x, y, t) = (x, 1, t)"""
    return 0


def Y0(xyt):
    """Boundary condition at (x, y, t) = (x, y, 0)"""
    (x, y, t) = xyt
    return sin(pi*x)*sin(pi*y)


bc = [[f0, f1], [g0, g1], [Y0, None]]


def df0_dx(xyt):
    """1st derivative of BC wrt x at (x, y, t) = (0, y, t)"""
    return 0


def df0_dy(xyt):
    """1st derivative of BC wrt y at (x, y, t) = (0, y, t)"""
    return 0


def df0_dt(xyt):
    """1st derivative of BC wrt t at (x, y, t) = (0, y, t)"""
    return 0


def df1_dx(xyt):
    """1st derivative of BC wrt x at (x, y, t) = (1, y, t)"""
    return 0


def df1_dy(xyt):
    """1st derivative of BC wrt y at (x, y, t) = (1, y, t)"""
    return 0


def df1_dt(xyt):
    """1st derivative of BC wrt t at (x, y, t) = (1, y, t)"""
    return 0


def dg0_dx(xyt):
    """1st derivative of BC wrt x at (x, y, t) = (x, 0, t)"""
    return 0


def dg0_dy(xyt):
    """1st derivative of BC wrt y at (x, y, t) = (x, 0, t)"""
    return 0


def dg0_dt(xyt):
    """1st derivative of BC wrt t at (x, y, t) = (x, 0, t)"""
    return 0


def dg1_dx(xyt):
    """1st derivative of BC wrt x at (x, y, t) = (x, 1, t)"""
    return 0


def dg1_dy(xyt):
    """1st derivative of BC wrt y at (x, y, t) = (x, 1, t)"""
    return 0


def dg1_dt(xyt):
    """1st derivative of BC wrt t at (x, y, t) = (x, 1, t)"""
    return 0


def dY0_dx(xyt):
    """1st derivative of BC wrt x at (x, y, t) = (x, y, 0)"""
    (x, y, t) = xyt
    return pi*cos(pi*x)*sin(pi*y)


def dY0_dy(xyt):
    """1st derivative of BC wrt y at (x, y, t) = (x, y, 0)"""
    (x, y, t) = xyt
    return pi*sin(pi*x)*cos(pi*y)


def dY0_dt(xyt):
    """1st derivative of BC wrt t at (x, y, t) = (x, y, 0)"""
    return 0


delbc = [[[df0_dx, df0_dy, df0_dt], [df1_dx, df1_dy, df1_dt]],
         [[dg0_dx, dg0_dy, dg0_dt], [dg1_dx, dg1_dy, dg1_dt]],
         [[dY0_dx, dY0_dy, dY0_dt], [None, None, None]]]


def d2f0_dx2(xyt):
    """2nd derivative of BC wrt x at (x, y, t) = (0, y, t)"""
    return 0


def d2f0_dy2(xyt):
    """2nd derivative of BC wrt y at (x, y, t) = (0, y, t)"""
    return 0


def d2f0_dt2(xyt):
    """2nd derivative of BC wrt t at (x, y, t) = (0, y, t)"""
    return 0


def d2f1_dx2(xyt):
    """2nd derivative of BC wrt x at (x, y, t) = (1, y, t)"""
    return 0


def d2f1_dy2(xyt):
    """2nd derivative of BC wrt y at (x, y, t) = (1, y, t)"""
    return 0


def d2f1_dt2(xyt):
    """2nd derivative of BC wrt t at (x, y, t) = (1, y, t)"""
    return 0


def d2g0_dx2(xyt):
    """2nd derivative of BC wrt x at (x, y, t) = (x, 0, t)"""
    return 0


def d2g0_dy2(xyt):
    """2nd derivative of BC wrt y at (x, y, t) = (x, 0, t)"""
    return 0


def d2g0_dt2(xyt):
    """2nd derivative of BC wrt t at (x, y, t) = (x, 0, t)"""
    return 0


def d2g1_dx2(xyt):
    """2nd derivative of BC wrt x at (x, y, t) = (x, 1, t)"""
    return 0


def d2g1_dy2(xyt):
    """2nd derivative of BC wrt y at (x, y, t) = (x, 1, t)"""
    return 0


def d2g1_dt2(xyt):
    """2nd derivative of BC wrt t at (x, y, t) = (x, 1, t)"""
    return 0


def d2Y0_dx2(xyt):
    """2nd derivative of BC wrt x at (x, y, t) = (x, y, 0)"""
    (x, y, t) = xyt
    return -pi**2*sin(pi*x)*sin(pi*y)


def d2Y0_dy2(xyt):
    """2nd derivative of BC wrt y at (x, y, t) = (x, y, 0)"""
    (x, y, t) = xyt
    return -pi**2*sin(pi*x)*sin(pi*y)


def d2Y0_dt2(xyt):
    """2nd derivative of BC wrt t at (x, y, t) = (x, y, 0)"""
    return 0


del2bc = [[[d2f0_dx2, d2f0_dy2, d2f0_dt2], [d2f1_dx2, d2f1_dy2, d2f1_dt2]],
          [[d2g0_dx2, d2g0_dy2, d2g0_dt2], [d2g1_dx2, d2g1_dy2, d2g1_dt2]],
          [[d2Y0_dx2, d2Y0_dy2, d2Y0_dt2], [None, None, None]]]


def dG_dY(xyt, Y, delY, del2Y):
    """Partial of PDE wrt Y"""
    return 0


def dG_ddY_dx(xyt, Y, delY, del2Y):
    """Partial of PDE wrt dY/dx"""
    return 0


def dG_ddY_dy(xyt, Y, delY, del2Y):
    """Partial of PDE wrt dY/dy"""
    return 0


def dG_ddY_dt(xyt, Y, delY, del2Y):
    """Partial of PDE wrt dY/dt"""
    return 1


dG_ddelY = [dG_ddY_dx, dG_ddY_dy, dG_ddY_dt]


def dG_dd2Y_dx2(xyt, Y, delY, del2Y):
    """Partial of PDE wrt d2Y/dx2"""
    return -D


def dG_dd2Y_dy2(xyt, Y, delY, del2Y):
    """Partial of PDE wrt d2Y/dy2"""
    return -D


def dG_dd2Y_dt2(xyt, Y, delY, del2Y):
    """Partial of PDE wrt d2Y/dt2"""
    return 0


dG_ddel2Y = [dG_dd2Y_dx2, dG_dd2Y_dy2, dG_dd2Y_dt2]


def A(xyt):
    """Optimized version of boundary condition function"""
    (x, y, t) = xyt
    A = (1 - t)*sin(pi*x)*sin(pi*y)
    return A


def delA(xyt):
    """Optimized version of boundary condition function gradient"""
    (x, y, t) = xyt
    dA_dx = pi*(1 - t)*cos(pi*x)*sin(pi*y)
    dA_dy = pi*(1 - t)*sin(pi*x)*cos(pi*y)
    dA_dt = -sin(pi*x)*sin(pi*y)
    delA = [dA_dx, dA_dy, dA_dt]
    return delA


def del2A(xyt):
    """Optimized version of boundary condition function Laplacian"""
    (x, y, t) = xyt
    d2A_dx2 = -pi**2*(1 - t)*sin(pi*x)*sin(pi*y)
    d2A_dy2 = -pi**2*(1 - t)*sin(pi*x)*sin(pi*y)
    d2A_dt2 = 0
    del2A = [d2A_dx2, d2A_dy2,  d2A_dt2]
    return del2A


def Ya(xyt):
    """Analytical solution"""
    (x, y, t) = xyt
    return exp(-2*pi**2*D*t)*sin(pi*x)*sin(pi*y)


def dYa_dx(xyt):
    """Analytical x-gradient"""
    (x, y, t) = xyt
    return pi*exp(-2*pi**2*D*t)*cos(pi*x)*sin(pi*y)


def dYa_dy(xyt):
    """Analytical y-gradient"""
    (x, y, t) = xyt
    return pi*exp(-2*pi**2*D*t)*sin(pi*x)*cos(pi*y)


def dYa_dt(xyt):
    """Analytical t-gradient"""
    (x, y, t) = xyt
    return -2*pi**2*D*exp(-2*pi**2*D*t)*sin(pi*x)*sin(pi*y)


delYa = [dYa_dx, dYa_dy, dYa_dt]


def d2Ya_dx2(xyt):
    """Analytical x-Laplacian"""
    (x, y, t) = xyt
    return -pi**2*exp(-2*pi**2*D*t)*sin(pi*x)*sin(pi*y)


def d2Ya_dy2(xyt):
    """Analytical y-Laplacian"""
    (x, y, t) = xyt
    return -pi**2*exp(-2*pi**2*D*t)*sin(pi*x)*sin(pi*y)


def d2Ya_dt2(xyt):
    """Analytical t-Laplacian"""
    (x, y, t) = xyt
    return 4*pi**4*D**2*exp(-2*pi**2*D*t)*sin(pi*x)*sin(pi*y)


del2Ya = [d2Ya_dx2, d2Ya_dy2, d2Ya_dt2]


if __name__ == '__main__':

    # Test values
    x_test = (0.4, 0.5, 0.6)
    m = len(x_test)
    Y_test = 0.2909702304064997
    delY_test = (0.2970123234623966, 0, -0.57435221333211949)
    del2Y_test = (-2.871761066605974, -2.871761066605974, 1.133725826474056)

    # Reference values for tests.
    G_ref = 0
    bc_ref = ((0, 0), (0, 0), (0.951057, None))
    delbc_ref = (((0, 0, 0), (0, 0, 0)),
                 ((0, 0, 0), (0, 0, 0)),
                 ((0.970806, 0, 0), (None, None, None)))
    del2bc_ref = (((0, 0, 0), (0, 0, 0)),
                  ((0, 0, 0), (0, 0, 0)),
                  ((-9.386551, -9.386551, 0), (None, None, None)))
    dG_dY_ref = 0
    dG_ddelY_ref = (0, 0, 1)
    dG_ddel2Y_ref = (-D, -D, 0)
    A_ref = 0.380423
    delA_ref = (0.388322, 0, -0.951057)
    del2A_ref = (-3.75462, -3.75462, 0)
    Ya_ref = 0.290970
    delYa_ref = (0.2970123234623966, 0, -0.57435221333211949)
    del2Ya_ref = (-2.871761066605974, -2.871761066605974, 1.133725826474056)

    print("Testing differential equation.")
    assert np.isclose(G(x_test, Y_test, delY_test, del2Y_test), G_ref)

    print('Testing boundary conditions.')
    for j in range(m):
        for jj in range(2):
            if bc[j][jj] is not None:
                assert np.isclose(bc[j][jj](x_test), bc_ref[j][jj])

    print("Testing boundary condition continuity constraints.")
    assert np.isclose(f0([0, 0, 0]), g0([0, 0, 0]))
    assert np.isclose(f0([0, 1, 0]), g1([0, 1, 0]))
    assert np.isclose(f1([1, 0, 0]), g0([1, 0, 0]))
    assert np.isclose(f1([1, 1, 0]), g0([1, 1, 0]))
    assert np.isclose(f0([0, 0, 0]), Y0([0, 0, 0]))
    assert np.isclose(f0([0, 1, 0]), Y0([0, 1, 0]))
    assert np.isclose(f1([1, 0, 0]), Y0([1, 0, 0]))
    assert np.isclose(f1([1, 1, 0]), Y0([1, 1, 0]))
    # t=1 not used

    print('Testing boundary condition gradients.')
    for j in range(m):
        for jj in range(2):
            for jjj in range(m):
                if delbc[j][jj][jjj] is not None:
                    assert np.isclose(delbc[j][jj][jjj](x_test),
                                      delbc_ref[j][jj][jjj])

    print('Testing boundary condition Laplacians.')
    for j in range(m):
        for jj in range(2):
            for jjj in range(m):
                if del2bc[j][jj][jjj] is not None:
                    assert np.isclose(del2bc[j][jj][jjj](x_test),
                                      del2bc_ref[j][jj][jjj])

    print('Testing derivative of differential equation wrt solution.')
    assert np.isclose(dG_dY(x_test, Y_test, delY_test, del2Y_test),
                      dG_dY_ref)

    print('Testing derivative of differential equation wrt gradient '
          'components.')
    for j in range(m):
        assert np.isclose(dG_ddelY[j](x_test, Y_test, delY_test, del2Y_test),
                          dG_ddelY_ref[j])

    print('Testing derivative of differential equation wrt Laplacian '
          'components.')
    for j in range(m):
        assert np.isclose(dG_ddel2Y[j](x_test, Y_test, delY_test, del2Y_test),
                          dG_ddel2Y_ref[j])

    print("Testing optimized BC function.")
    A_ = A(x_test)
    assert np.isclose(A_, A_ref)

    print("Testing optimized BC function gradient.")
    delA_ = delA(x_test)
    for j in range(m):
        assert np.isclose(delA_[j], delA_ref[j])

    print("Testing optimized BC function Laplacian.")
    del2A_ = del2A(x_test)
    for j in range(m):
        assert np.isclose(del2A_[j], del2A_ref[j])

    print("Testing analytical solution.")
    assert np.isclose(Ya(x_test), Ya_ref)

    print("Testing analytical solution gradient.")
    for j in range(m):
        assert np.isclose(delYa[j](x_test), delYa_ref[j])

    print("Testing analytical solution Laplacian.")
    for j in range(m):
        assert np.isclose(del2Ya[j](x_test), del2Ya_ref[j])
