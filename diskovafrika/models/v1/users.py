"""
User class
"""
from datetime import datetime
from diskovafrika.configs.extensions import db
from sqlalchemy import Enum, func, text
from uuid import uuid4


class User(db.Model):
    """model for users"""
    __tablename__ = "users"
    id = db.Column(db.String(length=50), primary_key=True,
                   default=str(uuid4), unique=True)
    username = db.Column(db.String(length=50), nullable=False, unique=True)
    email = db.Column(db.String(length=50), nullable=False, unique=True)
    password = db.Column(db.String(50))
    gender = db.Column(Enum("Male", "Female"))
    created_at = db.Column(db.DateTime, server_default=func.now())
    updated_at = db.Column(
        db.DateTime,
        server_default=text("CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP")
    )
    # state_id = db.Column(db.Integer, db.ForeignKey('state.id'))
    # TODO In states table
    # users = db.relationship("User", backref='states')

    def __repr__(self):
        return {
            "id": {self.id}, "username": {self.username},
            "email": {self.email}, "gender": {self.gender}
        }
