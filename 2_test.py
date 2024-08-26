import pytest
from main_2 import init_db, add_user, get_user
@pytest.fixture  # фикстура - подготовка среды к тестам
def db_conn():
    conn = init_db()
    yield conn # yield возвращает объект соединения conn для дальнейшего использования
    conn.close()
def test_add_or_get_user(db_conn):
    add_user(db_conn, "Sasha", 30)  # добавляем пользователя
    user = get_user(db_conn, "Sasha")  # получаем пользователя и сохраняем его в user
    assert user == (1, "Sasha", 30)  # проверяем, что полученный пользователь соответствует ожидаемому
