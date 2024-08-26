import pytest
from DZ3 import get_random_cat_image

def test_get_random_cat_image_success(mocker):
    # Мокируем успешный ответ от API
    mock_get = mocker.patch('requests.get')
    mock_get.return_value.status_code = 200
    mock_get.return_value.json.return_value = [{
        'id': 'abc123',
        'url': 'https://cdn2.thecatapi.com/images/abc123.jpg'
    }]

    # Проверяем, что функция возвращает правильный URL
    url = get_random_cat_image()
    assert url == 'https://cdn2.thecatapi.com/images/abc123.jpg'

def test_get_random_cat_image_failure(mocker):
    # Мокируем неуспешный ответ от API
    mock_get = mocker.patch('requests.get')
    mock_get.return_value.status_code = 404

    # Проверяем, что функция возвращает None
    url = get_random_cat_image()
    assert url is None