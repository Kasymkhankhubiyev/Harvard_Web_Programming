import unittest

from prime import is_prime

class Tests(unittest.TestCase):

    def test1(self):
        """Check that 1 is not prime."""
        self.assertFalse(is_prime(1))

    def test2(self):
        """Check that 2 is prime."""
        self.assertTrue(is_prime(2))

    def test3(self):
        """Check that 3 is prime."""
        self.assertTrue(is_prime(3))

    def test11(self):
        """Check that 11 is prime."""
        self.assertTrue(is_prime(11))

    def test12(self):
        """Check that 12 is not prime."""
        self.assertFalse(is_prime(12))

    def test99(self):
        """Check that 99 is not prime."""
        self.assertFalse(is_prime(99))

    def test18(self):
        """Check that 18 is not prime."""
        self.assertFalse(is_prime(18))

    
if __name__ == "__main__":
    unittest.main()