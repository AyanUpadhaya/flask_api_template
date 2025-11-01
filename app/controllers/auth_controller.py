import jwt, datetime, time
from werkzeug.security import generate_password_hash,check_password_hash
from app.models.user import User,db
from flask import current_app

def register_user(data):
    hashed_pw = generate_password_hash(data['password'])
    user = User(name=data['name'], email=data['email'], password=hashed_pw)
    db.session.add(user)
    db.session.commit()
    return user

def login_user(data):
    user = User.query.filter_by(email=data['email']).first()
    if user and check_password_hash(user.password, data['password']):
        expiration_time = datetime.datetime.now(datetime.UTC) + datetime.timedelta(days=30)
        expiration_timestamp = int(time.mktime(expiration_time.timetuple()))
        token = jwt.encode({
            'user_id': user.id,
            'exp': expiration_timestamp
        }, current_app.config['SECRET_KEY'], algorithm='HS256')
        return token
    return None



