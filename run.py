from app import create_app, db
from dotenv import load_dotenv
import os
load_dotenv()  # Load variables from .env
app = create_app()

with app.app_context():
    db.create_all()

if __name__ == "__main__":
    app.run(debug=os.getenv('DEBUG_MODE'))