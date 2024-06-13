import pytest
from modules.api.clients.github import GitHub


@pytest.mark.api
def test_user_exists(github_api):
    user = github_api.get_user('defunkt')
    assert user['login'] == 'defunkt'


@pytest.mark.api
def test_user_not_exist(github_api):
    r = github_api.get_user('butenkosergii')
    assert r['message'] == 'Not Found'


@pytest.mark.api
def test_repo_can_be_found(github_api):
    r = github_api.search_repo('become-qa-auto')
    print(r)
    assert r['total_count'] == 58
    assert 'become-qa-auto' in r['items'][0]['name']


@pytest.mark.api
def test_repo_cannot_be_found(github_api):
    r = github_api.search_repo('sergiibutenko_repo_non_exist')
    assert r['total_count'] == 0


@pytest.mark.api
def test_repo_with_single_char_be_found(github_api):
    r = github_api.search_repo('s')
    assert r['total_count'] != 0


@pytest.mark.api
def test_emoji_are_present(github_api):
    r = github_api.get_emojis()
    assert len(r) > 0


@pytest.mark.api
def test_emodji_alien(github_api):
    r = github_api.get_emojis()
    assert 'alien' in r


@pytest.mark.api
def test_emodji_zomro(github_api):
    r = github_api.get_emojis()
    assert 'zomro' not in r


# незрозуміла єресь
@pytest.mark.api
def test_commit_author(github_api):
    owner = 'octocat'
    repo = 'Hello-World'
    commits = github_api.get_commits_body(owner, repo)
    assert len(commits) > 0, "Expected non-empty list of commits"

    # перевірка першого елементу списку
    first_commit = commits[0]
    # print(first_commit['commit']['author']['name'])
    assert 'commit' in first_commit, "First commit should have 'commit' key"
    assert 'author' in first_commit['commit'], "Commit should have 'author' key"
    assert 'name' in first_commit['commit']['author'], "Author should have 'name' key"
    author_name = first_commit['commit']['author']['name']
    print(author_name)
    
    assert author_name == 'The Octocat', f"Expected 'Monalisa Octocat', but got {author_name}"
    # assert first_commit['commit']['author']['name'] == 'The Octocat'


@pytest.mark.api
def test_request_is_200(github_api):
    owner = 'octocat'
    repo = 'Hello-World'
    status_code = github_api.get_commit_status_code(owner, repo)
    assert status_code == 200, f'Expected status code 200, but got {status_code}'
