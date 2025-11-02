import jwt
import datetime
import time
from werkzeug.security import generate_password_hash, check_password_hash
from app.models.user import User, db
from flask import current_app
from app.utils.errors import AppError
from sqlalchemy.exc import IntegrityError, SQLAlchemyError

# ---------------------------
# REGISTER USER
# ---------------------------
def register_user(data):
    try:
        name = data.get("name")
        email = data.get("email")
        password = data.get("password")

        # Basic validation
        if not name or not email or not password:
            raise AppError("Name, email, and password are required", 400)

        # Check if user already exists
        existing_user = User.query.filter_by(email=email).first()
        if existing_user:
            raise AppError("User with this email already exists", 400)

        # Hash password and save user
        hashed_pw = generate_password_hash(password)
        user = User(name=name, email=email, password=hashed_pw)

        db.session.add(user)
        db.session.commit()

        return user

    except IntegrityError:
        db.session.rollback()
        raise AppError("Email already exists", 400)

    except AppError:
        # Re-raise AppError to be handled globally
        raise

    except Exception as e:
        db.session.rollback()
        current_app.logger.exception("Unexpected error in register_user: %s", e)
        raise AppError("An error occurred while creating the user", 500)


# ---------------------------
# LOGIN USER
# ---------------------------
def login_user(data):
    try:
        email = data.get("email")
        password = data.get("password")

        if not email or not password:
            raise AppError("Email and password are required", 400)

        user = User.query.filter_by(email=email).first()
        if not user or not check_password_hash(user.password, password):
            raise AppError("Invalid email or password", 401)

        # Generate JWT token
        expiration_time = datetime.datetime.now(datetime.UTC) + datetime.timedelta(days=30)
        expiration_timestamp = int(time.mktime(expiration_time.timetuple()))

        token = jwt.encode(
            {"user_id": user.id, "exp": expiration_timestamp},
            current_app.config["SECRET_KEY"],
            algorithm="HS256"
        )

        return token

    except AppError:
        raise

    except jwt.PyJWTError as e:
        current_app.logger.exception("JWT generation failed: %s", e)
        raise AppError("Token generation failed", 500)

    except Exception as e:
        current_app.logger.exception("Unexpected error in login_user: %s", e)
        raise AppError("An unexpected error occurred during login", 500)



