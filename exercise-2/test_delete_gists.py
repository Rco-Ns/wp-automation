import unittest
from module import CreateModule

class Test_DeleteGists(unittest.TestCase):
    print("As a user, I want to delete an existing gist.")
    def test_delete_gists(self):
        test = CreateModule()
        test.setUp()
        test.loginGithub()
        test.findMyGistList()
        test.deleteGists()

    def tearDown(self):
        test = CreateModule()
        test.setUp()
        test.driver.close()

if __name__ == "__main__":
    unittest.main()