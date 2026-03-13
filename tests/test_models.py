from app import User, db

def test_create_user(client):
	user = User(name='Тестовый Пользователь')
	db.session.add(user)
	db.session.commit()

	assert user.id is not None
	assert user.name == "Тестовый Пользователь"

def test_client_info_endpoint(client):
	response = client.get('/api/client-info')
	assert response.status_code == 200
	data = response.get_json()
	assert 'ip' in data
	assert 'port' in data
	assert 'user_agent' in data
	assert data['ip'] == '127.0.0.1'

def test_get_users_api(client):
	user = User(name="Пользователь API")
	db.session.add(user)
	db.session.commit()

	response = client.get('/api/users')

	assert response.status_code == 200
	assert response.is_json
	data = response.get_json()
	assert isinstance(data, list)
	assert any(u['name'] == 'Пользователь API' for u in data)