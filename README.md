# 🐍 Flask REST API with MVC Architecture

This is a mini Flask REST API project structured using the MVC (Model-View-Controller) pattern. It supports basic user operations and serves a landing page to confirm the server is running.

## 🚀 Features

- RESTful endpoints for user creation and listing
- MVC architecture for clean separation of concerns
- SQLite database with SQLAlchemy ORM
- Marshmallow for serialization
- CORS support for cross-origin requests
- HTML template rendering for root route


## 📦 Installation

```bash
# Clone the repo
git clone https://github.com/yourusername/flask-api-mvc.git
cd flask_api

# Create virtual environment
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# run app
python run.py

```

## 📬 API Endpoints
– List all users /users
– Create a new user /users

**Sample POST Body**
```json
{
  "name": "Alice Johnson",
  "email": "alice.johnson@example.com"
}
```
## 🛠️ Tech Stack
- Python
- Flask
- SQLAlchemy
- Marshmallow
- SQLite


