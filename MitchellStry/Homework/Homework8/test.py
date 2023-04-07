import homework8 as h8
import unittest
""" 
Summary of the tests:
Args:
    1 - Making matrixes
    2 - Energies
    3 - Matrix Solving
    4 - Solve Hamiltonian
Returns:
    Please note that I can't actually sove the math for this by hand so I don't know the answers to these for the computer to compare to.
    Please fill in the correct numbers when doing your own tests.
"""
class TestmEigen(unittest.TestCase):
    def test_f1(self):
        """Testing function matrixmaking"""
        print("Det")
        self.assertAlmostEqual(h8.matrixmaking(1.0,1.0),1.0,1.0,1.0,1.0 )
    def test_f1_2(self):
        self.assertEqual(h8.energies(1,1,1),1,1)
    def test_f2_1(self):
        self.assertEqual(h8.matrixsolve(1,1,1,1,1,1),1,1 )
    def test_f2_2(self):
        self.assertAlmostEqual(h8.finishedhamil(1,1),1 )
if __name__=='__main__':
    unittest.main()
