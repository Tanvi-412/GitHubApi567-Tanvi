import unittest

from github import github

# This code implements the unit test functionality
# https://docs.python.org/3/library/unittest.html has a nice description of the framework

class TestTriangles(unittest.TestCase):
    # define multiple sets of tests as functions with names that begin

    def testgithub(self): 
        self.assertEqual(github("Tanvi-412"),"Repository Name: 567-HW01, Total number of commits: 2")


if __name__ == '__main__':
    print('Running unit tests')
    unittest.main(exit=False, verbosity=2)


