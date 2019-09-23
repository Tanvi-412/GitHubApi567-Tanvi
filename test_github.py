"""Name: Tanvi Hanamshet
Course: SSW 567
Script:  Test github script
"""


import unittest
from github import github_api


class TestGithub(unittest.TestCase):
   

    def testgithub(self): 
        self.assertEqual(github_api("Tanvi-412"),"Repository Name: 567-HW01, Total number of commits: 2")


if __name__ == '__main__':
    print('Running unit tests')
    unittest.main(exit=False, verbosity=2)


