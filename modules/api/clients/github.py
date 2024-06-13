import requests


class GitHub:

    def get_user(self, username):
        r = requests.get(f'https://api.github.com/users/{username}')
        body = r.json()

        return body
    
    def search_repo(self, name):
        r = requests.get('http://api.github.com/search/repositories', params={'q':name})
        body = r.json()

        return body

    def get_emojis(self):
        r = requests.get('https://api.github.com/emojis')
        body = r.json()

        return body
    
    def get_commits(self, owner, repo):
        url = f'https://api.github.com/repos/{owner}/{repo}/commits'
        r = requests.get(url)
        r.raise_for_status()
        # body = r.json()
        return r
    
    def get_commit_status_code(self, owner, repo):
        r = self.get_commits(owner, repo)
        return r.status_code
    
    def get_commits_body(self, owner, repo):
        r = self.get_commits(owner, repo)
        return r.json()