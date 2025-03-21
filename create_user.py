# This script creates a new user in the database. It should be run only once to create the initial user.
from app import create_app
from app.models import User
from app import db

app = create_app()
with app.app_context():
    # Create a new user
    username = "admin"
    password = "password123"  # Replace with a secure password
    user = User(username=username, email="admin@example.com", group="admins")  # Add email and group
    user.set_password(password)  # Use set_password to hash the password
    db.session.add(user)
    db.session.commit()
    print(f"User '{username}' created successfully!")