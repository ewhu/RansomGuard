# test_ransomguard.py
"""
Tests for RansomGuard module.
"""

import unittest
from ransomguard import RansomGuard

class TestRansomGuard(unittest.TestCase):
    """Test cases for RansomGuard class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = RansomGuard()
        self.assertIsInstance(instance, RansomGuard)
        
    def test_run_method(self):
        """Test the run method."""
        instance = RansomGuard()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
