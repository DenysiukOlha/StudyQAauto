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
    
    def get_commit_author(self, owner, repo):
        url = f'https://api.github.com/repos/{owner}/{repo}/commits'
        r = requests.get(url)
        
        # перевірка на успішний статус код
        if r.status_code != 200:
            r.raise_for_status()

        body = r.json()
        return body