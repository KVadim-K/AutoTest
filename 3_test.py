import pytest
from main_3 import get_github_user

def test_get_github_user(mocker):
    mock_get = mocker.patch('main_3.requests.get')
    mock_get.return_value.status_code = 200
    mock_get.return_value.json.return_value = {
        'login': 'test_user',
        'id': 12345,
        'name': 'Vadim'
    }

    user_data = get_github_user('nizavr')
    assert user_data == {
        'login': 'test_user',
        'id': 12345,
        'name': 'Vadim'
    }
def test_get_github_user_with_error(mocker):
    mock_get = mocker.patch('main_3.requests.get')
    mock_get.return_value.status_code = 500



    user_data = get_github_user('nizavr')
    assert user_data == None

