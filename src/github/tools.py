from ..server import mcp
from .client import github_client



#list repositories for the authenticated user
@mcp.tool()
def get_repositories():
    user = github_client.get_user()
    return[
        {
            "name": repo.name,
            "url": repo.html_url,
            "description": repo.description,
            "private": repo.private,
            "stars": repo.stargazers_count
        }
        for repo in user.get_repos()
    ]

#open issues for a given repository
@mcp.tool()
def get_issues(repo_name):
    repo = github_client.get_repo(repo_name)

    return [
        {
            "title": issue.title,
            "url": issue.html_url,
            "state": issue.state,
            "created_at": issue.created_at,
            "updated_at": issue.updated_at
        }
        for issue in repo.get_issues(state="open")
    ]

#create a new issue in a given repository
@mcp.tool()
def create_github_issue(
    repo_name: str,
    title: str,
    body: str = ""
    ):
    repo = github_client.get_repo(repo_name)
    issue = repo.create_issue(
        title=title, 
        body=body
    )
    return issue.html_url

#get pull requests for a given repository
@mcp.tool()
def get_pull_requests(repo_name:str):

    repo = github_client.get_repo(repo_name)

    return [
        {
            "title": pr.title,
            "author": pr.user.login,
            "status": pr.state
        }
        for pr in repo.get_pulls()
    ]

