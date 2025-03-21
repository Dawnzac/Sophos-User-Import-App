from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
from .extensions import db  # Import db from extensions

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(150), unique=True, nullable=False)
    password_hash = db.Column(db.String(150), nullable=False)  # Rename to password_hash
    email = db.Column(db.String(150), unique=True, nullable=False)
    group = db.Column(db.String(150), nullable=True)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    def get_id(self):
        return str(self.id)  # Ensure the ID is returned as a string

    def __repr__(self):
        return f'<User {self.username}>'