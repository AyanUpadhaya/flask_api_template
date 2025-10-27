from app import db
from app.models.user import User

def get_all_users():
    return User.query.all()

def create_user(data):
    new_user = User(name=data['name'], email=data['email'])
    db.session.add(new_user)
    db.session.commit()
    return new_user
