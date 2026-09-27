import unittest
class DeliberateFailure(unittest.TestCase):
 def test_failed_change(self):
  self.fail("deliberate CI boundary probe")
