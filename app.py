from flask import Flask, render_template, request, url_for, redirect, jsonify
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

#Создание сайта
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

#Модель пользователя
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    date_added = db.Column(db.DateTime, default = datetime.utcnow)

    def __repr__(self):
        return f'<User {self.name}>'

#Создание таблиц 
with app.app_context():
	db.create_all()

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/api/users')
def api_users():
	users = User.query.all()
	#Превращаем список объектов User в список словарей
	users_list = []
	for user in users:
		users_list.append({
			'id': user.id,
			'name': user.name,
			'date_added': user.date_added.strftime('%d-%m-%Y %H:%M')
			})
	return jsonify(users_list)

@app.route('/api/users/<int:id>')
def api_user(id):
	user = User.query.get(id)
	if user is None:
		return jsonify({'error': 'User not found'}), 404
	return jsonify({
		'id': user.id,
		'name': user.name,
		'date_added': user.date_added.strftime('%d-%m-%Y %H:%M')
		})

@app.route('/api/users', methods=['POST'])
def api_create_user():
	data = request.get_json()
	if not data or 'name' not in data:
		return jsonify({'error': 'Name is required'}), 400
	name = data['name'].strip()
	if not name:
		return jsonify({'error': 'Name cannot be empty'}), 400
	user = User(name=name)
	db.session.add(user)
	db.session.commit()
	return jsonify({
		'id': user.id,
		'name': user.name,
		'date_added': user.date_added.strftime('%d-%m-%Y %H:%M')
	}), 201

@app.route('/api/users/<int:id>', methods=['DELETE'])
def api_delete_user(id):
	user = User.query.get(id)
	if user is None:
		return jsonify({'error': 'User not found'}), 404
		db.session.delete(user)
		db.session.commit()
		return jsonify({'result': True})

@app.route('/form', methods = ['GET', 'POST'])
def form():
	if request.method == 'POST':
		username = request.form.get('username', '').strip()
		if not username:
			return render_template('form.html', error = 'Введите имя!')
		new_user = User(name=username)
		db.session.add(new_user)
		db.session.commit()
		return redirect(url_for('users_list'))
	return render_template('form.html')

@app.route('/users')
def users_list():
    all_users = User.query.all()  # получаем всех пользователей из БД
    return render_template('user.html', users = all_users)

@app.route('/api/users/<int:id>', methods=['PUT'])
def api_update_user(id):
	user = User.query.get(id)
	if user is None:
		return jsonify({'error': 'User not found'}), 404
	
	data = request.get_json()
	name = data['name'].strip() 
	if not data or 'name' not in data:
		return jsonify({'error': 'Name if required'}), 400

	user.name = name 
	db.session.commit()
	return jsonify({
		'id': user.id,
		'name': user.name,
		'date_added': user.date_added.strftime('%d-%m-%Y %H:%M')
		})

@app.route('/delete/<int:id>', methods=["POST"])
def delete_user(id):
	user = User.query.get_or_404(id)
	db.session.delete(user)
	db.session.commit()
	return redirect(url_for("users_list"))

@app.route("/info")
def info():
	return 'Это страница информации'

if __name__ == '__main__':
	app.run(debug=True, host='0.0.0.0')