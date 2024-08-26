import pytest
from main import get_weather
from config import API_KEY

def test_get_weather(mocker):
    mock_get = mocker.patch('main.requests.get')  # Таким образом мы заменили функцию на mock-объект, с которым можно работать. Мы можем поменять значение, которое выдается после получения через функцию get.
    mock_get.return_value.status_code = 200  # Создаем мок-ответ для успешного запроса
    mock_get.return_value.json.return_value = {
       'weather': [{'description': 'clear sky'}],
       'main': {'temp': 273.15}
    }

    city = 'London'

    weather_data = get_weather(API_KEY, city)
    assert weather_data == {
        'weather': [{'description': 'clear sky'}],
        'main': {'temp': 273.15}
    }
def test_get_github_user_with_error(mocker):
    mock_get = mocker.patch('main.requests.get')
    mock_get.return_value.status_code = 404
    mock_get.return_value.json.return_value = {
        'message': 'Not Found'
    }
    'API_KEY'
    city = 'London'

    weather_data = get_weather(API_KEY, city)
    assert weather_data is None




