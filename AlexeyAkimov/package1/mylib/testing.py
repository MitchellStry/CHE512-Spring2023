import flib
import unittest

class Test_flib(unittest.TestCase):
    """ Summary of the tests:
    """

    def test_f1_1(self):
        """
        Testing function f1
        """
        self.assertAmostEqual( flib.f1(1.0), 1.0  )

    def test_f1_2(self):
        self.assertEqual( flib.f1(1), 1  )

    def test_f2_1(self):
        self.assertEqual( flib.f2(2), 4  )

    def test_f2_2(self):
        self.assertAlmostEqual( flib.f2(2.0), 4.0  )


if __name__=='__main__':
    unittest.main()

