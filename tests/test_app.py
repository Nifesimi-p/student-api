import pytest
from app import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    return app.test_client()

def test_healthcheck(client):
    res = client.get('/api/v1/healthcheck')
    assert res.status_code == 200
    assert res.json['status'] == 'ok'
