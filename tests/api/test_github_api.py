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
    # print(r)
    assert r['total_count'] == 57
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

#так і не працює :(
@pytest.mark.api
def test_commit_author(github_api):
    owner = 'octocat'
    repo = 'Hello-World'
    r = github_api.get_commit_author(owner, repo)
    assert r['name'] == 'Monalisa Octocat'