import unittest
from unittest.mock import patch, Mock
from HW_04a import GitHub_Repositories

class TestGitHubRepositories(unittest.TestCase):

    def test_valid_user(self):
        result = GitHub_Repositories("csteccat")
        self.assertIsNotNone(result)
        self.assertIsInstance(result, list)
        
        for repo_info in result:
            self.assertIsInstance(repo_info, dict)
            self.assertIn("Repo", repo_info)
            self.assertIn("Number of commits", repo_info)
            self.assertIsInstance(repo_info["Repo"], str)
            self.assertIsInstance(repo_info["Number of commits"], int)
            self.assertGreaterEqual(repo_info["Number of commits"], 0)

    def test_invalid_user(self):

        result = GitHub_Repositories("nonexistentuser")
        self.assertIsNone(result)

if __name__ == "__main__":
    
    unittest.main()
