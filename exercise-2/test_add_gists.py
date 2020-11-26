import unittest
from module import CreateModule

class Test_AddPublicGists(unittest.TestCase):
    print("As a user, I want to create a public gist.")
    def test_add_gists(self):
        test = CreateModule()
        test.setUp()
        test.loginGithub()
        test.moveToGist()
        test.cickAdd()
        test.addPublic()

    def tearDown(self):
        test = CreateModule()
        test.setUp()
        test.driver.close()

if __name__ == "__main__":
    unittest.main()