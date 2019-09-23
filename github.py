import requests
import json

def github_api(id):
    repo = {}
    u_repo = requests.get(f"https://api.github.com/users/{id}/repos")
    output1 = json.loads(u_repo.text)
    for i in output1:
        repository = i["name"]
        commit = requests.get(f"https://api.github.com/repos/{id}/{repository}/commits")
        commit_output = json.loads(commit.text)
        repo[repository] = len(commit_output)
    
    for l,m in repo.items():
        return (f"Repository Name: {l}, Total number of commits: {m}")

if __name__ == '__main__':
    github_api("Tanvi-412")