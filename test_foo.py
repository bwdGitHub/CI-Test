import unittest
import sys
# todo - this path should work for the CI
# but doesn't match my structure. Is there a way to support both?
# or should I just keep parity between my local workspace and the CI version (would make more sense...)
sys.path.append("../src/")
import foo

class TestFoo(unittest.TestCase):

    def test_foo(self):
        self.assertEqual(foo.foo(),"bar")

if __name__=='__main__':
    unittest.main()