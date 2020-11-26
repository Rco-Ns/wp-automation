import unittest
from module import CreateModule

class Test_GetMyGists(unittest.TestCase):
    print("As a user, I want to see my list of gists.")
    def test_get_gists(self):
        test = CreateModule()
        test.setUp()
        test.loginGithub()
        test.findMyGistList()

    def tearDown(self):
        test = CreateModule()
        test.setUp()
        test.driver.close()

if __name__ == "__main__":
    unittest.main()