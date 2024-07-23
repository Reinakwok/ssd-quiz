import pytest
from app import app, is_xss_attack, is_sql_injection

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_home_page(client):
    response = client.get('/')
    assert response.status_code == 200
    assert b'Home Page' in response.data

def test_xss_detection():
    assert is_xss_attack('<script>') == True
    assert is_xss_attack('hello') == False

def test_sql_injection_detection():
    assert is_sql_injection('SELECT * FROM users') == True
    assert is_sql_injection('hello') == False

def test_search_valid_input(client):
    response = client.post('/search', data={'search_term': 'hello'})
    assert response.status_code == 200
    assert b'Your search term: hello' in response.data

def test_search_xss_input(client):
    response = client.post('/search', data={'search_term': '<script>alert(1)</script>'})
    assert response.status_code == 302
    assert b'Invalid input: Potential XSS attack detected. Please try again.' in response.data

def test_search_sql_injection_input(client):
    response = client.post('/search', data={'search_term': 'SELECT * FROM users'})
    assert response.status_code == 302
    assert b'Invalid input: Potential SQL injection detected. Please try again.' in response.data
