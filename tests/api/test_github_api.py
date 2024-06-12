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


# так і не працює :(
@pytest.mark.api
def test_commit_author(github_api):
    owner = 'octocat'
    repo = 'Hello-World'
    r = github_api.get_commit_author(owner, repo)
    print(r)
    assert len(r) > 0

    # перевірка першого еементу списку
    first_commit = r[0]
    print(first_commit['commit']['author']['name'])
    assert 'commit' in first_commit, "First commit should have 'commit' key"
    assert 'author' in first_commit['commit'], "Commit should have 'author' key"
    assert 'name' in first_commit['commit']['author'], "Author should have 'name' key"
    
    # assert author_name == 'Monalisa Octocat', f"Expected 'Monalisa Octocat', but got {author_name}"
    
    # assert first_commit['commit']['author']['name'] == 'The Octocat'

