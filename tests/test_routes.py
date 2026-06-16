import pytest
from app import create_app

@pytest.fixture
def app():
    app = create_app()
    app.config.update({
        "TESTING": True,
    })
    yield app

@pytest.fixture
def client(app):
    return app.test_client()

# Test 1: Web Interface loads
def test_index_route(client):
    response = client.get('/')
    assert response.status_code == 200
    assert b"Pipeline Tooling Dashboard" in response.data

# Test 2: Health check endpoint works
def test_health_route(client):
    response = client.get('/health')
    assert response.status_code == 200
    json_data = response.get_json()
    assert json_data['status'] == 'healthy'

# Test 3: Fetching API items works
def test_get_items_route(client):
    response = client.get('/api/items')
    assert response.status_code == 200
    json_data = response.get_json()
    assert json_data['status'] == 'success'
    assert isinstance(json_data['data'], list)

# Test 4: Creating a valid item works
def test_create_item_success(client):
    payload = {"name": "SonarQube", "status": "Active"}
    response = client.post('/api/items', json=payload)
    
    assert response.status_code == 201
    json_data = response.get_json()
    assert json_data['status'] == 'success'
    assert json_data['data']['name'] == 'SonarQube'

# Test 5: Validation rules block malformed items
def test_create_item_bad_request(client):
    payload = {"status": "Isolated"}  # Missing 'name'
    response = client.post('/api/items', json=payload)
    
    assert response.status_code == 400
    json_data = response.get_json()
    assert json_data['status'] == 'error'