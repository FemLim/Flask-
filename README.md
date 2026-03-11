# Flask User Manager

Простое веб-приложение для управления пользователями с использованием Flask и SQLite. Реализован как HTML-интерфейс (с Bootstrap), так и REST API для программного доступа.

## 🚀 Функциональность

- **HTML-интерфейс**:
  - Форма для добавления нового пользователя
  - Таблица со списком всех пользователей (с датой регистрации)
  - Кнопка удаления пользователя (с подтверждением)
  - Навигационное меню
- **REST API**:
  - `GET /api/users` – получить всех пользователей в JSON
  - `GET /api/users/<id>` – получить одного пользователя
  - `POST /api/users` – создать нового пользователя (JSON)
  - `PUT /api/users/<id>` – обновить имя пользователя
  - `DELETE /api/users/<id>` – удалить пользователя

## 🛠 Технологиии


- Python 3.14
- Flask
- Flask-SQLAlchemy
- SQLite
- Bootstrap 5
- Jinja2

## 📦 Установка и запуск

1. **Клонируй репозиторий**  
   ```bash
   git clone https://github.com/твой-логин/flask-user-manager.git
   cd flask-user-manager
Создай виртуальное окружение (рекомендуется)

bash
python -m venv venv
source venv/bin/activate   # для Linux/Mac
venv\Scripts\activate      # для Windows
Установи зависимости

bash
pip install -r requirements.txt
Запусти приложение

bash
python app.py
Открой в браузере
Перейди по адресу http://127.0.0.1:5000

📁 Структура проекта
text
flask-user-manager/
├── app.py                 # основной файл приложения
├── requirements.txt       # зависимости
├── users.db               # база данных SQLite (создаётся автоматически)
├── templates/             # HTML-шаблоны
│   ├── base.html
│   ├── form.html
│   └── user.html
└── README.md              # этот файл
🔗 Примеры использования API
Получить всех пользователей

bash
curl http://127.0.0.1:5000/api/users

Создать нового пользователя

bash
curl -X POST -H "Content-Type: application/json" -d "{\"name\": \"Иван\"}" http://127.0.0.1:5000/api/users

Обновить пользователя

bash
curl -X PUT -H "Content-Type: application/json" -d "{\"name\": \"Пётр\"}" http://127.0.0.1:5000/api/users/1

Удалить пользователя

bash
curl -X DELETE http://127.0.0.1:5000/api/users/1


👤 Автор
FemLim – justfemlim@gmai.com – https://github.com/FemLim
