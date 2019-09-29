"""Name: Tanvi Hanamshet
Course: SSW 567
Script:  Test github script
"""


import unittest
from unittest import mock
from github import github_api
import github



class TestGithub(unittest.TestCase):
    @mock.patch('github.github_api', side_effect=github_api)
    def test_github_api(self, github_api_function):
        assert github_api("Tanvi-412") == "Repository Name: 567-HW01, Total number of commits: 2"
        result = github.github_api("Tanvi-412")
        print(result)

    def testgithub(self): 
        self.assertEqual(github_api("Tanvi-412"),"Repository Name: 567-HW01, Total number of commits: 2")
        result = github.github_api("Tanvi-412")
        print(result)

        



if __name__ == '__main__':
    print('Running unit tests')
    unittest.main(exit=False, verbosity=2)


