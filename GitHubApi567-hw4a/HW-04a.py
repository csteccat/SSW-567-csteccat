import requests
import json
import unittest

#Function
def GitHub_Repositories(user_id):

    #GitHub repository with user ID
    repository_url = f"https://api.github.com/users/{user_id}/repos"

    #Get request - GitHub API
    response = requests.get(repository_url)

    #Checks for a successful request HTTP status code
    if response.status_code == 200:
        
        #JSON response
        repositories = json.loads(response.text)

        result = []

        #For loop to go through each repo and count commits
        for repo in repositories:

            repo_name = repo["name"]
           
            commit_url = f"https://api.github.com/repos/{user_id}/{repo_name}/commits"
            
            #Another get request to commit API
            commit_response = requests.get(commit_url)

            #Check for successful API request HTTP status code
            if commit_response.status_code == 200:
               
               #Parse JSON into list
                commits = json.loads(commit_response.text)
               
                commit_count = len(commits)
           
            else:
                
                commit_count = 0

            #Append respository 
            result.append({"Repo": repo_name, "Number of commits": commit_count})

        #Return list of repos
        return result
    
    else:
      
        print(f"Error: Failed to retrieve repositories for user '{user_id}'")
       
        return None

#Define user_id to make sure it works
user_id = "csteccat"

result = GitHub_Repositories(user_id)

#Print results
if result is not None:
    
    for repo_info in result:
        
        print(f"Repo: {repo_info['Repo']} Number of commits: {repo_info['Number of commits']}")
else:

    print("Invalid user ID or API error.")

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
