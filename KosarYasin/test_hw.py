import hw4, hw3, hw5, hw6
import unittest


class TestmEigen(unittest.TestCase):
    """ Summary of the tests:
    1 - determinant
    2 -
    """
    def test_f1_1(self):
        """
        Testing function f1
        """
        self.assertAlmostEqual( hw4.fermi_energy(1.0, [1,2,3,4], 1.0, 1.0), 2.0644297834303202  )

    def test_f1_2(self):
        """
        Testing function f2
        """
        self.assertAlmostEqual( hw3.compute_hamiltonian(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12 )[0, 0],  534)

if __name__=='__main':
    unittest.main()


