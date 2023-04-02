from datetime import datetime
from uuid import uuid4

from sqlalchemy import func
from diskovafrika.configs.extensions import db


class AdminDivision(db.Model):
    __tablename__ = "admin_division"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(200), nullable=True)
    created_at = db.Column(
        db.DateTime, server_default=func.now(), nullable=False)
    country = db.relationship("Country", backref='country')


class CountryDivision(db.Model):
    __tablename__ = 'divisions'

    id = id = db.Column(
        db.String(length=50), primary_key=True, default=str(uuid4), unique=True)
    country_id = db.Column(
        db.String(length=50), db.ForeignKey('country.id'), nullable=False)
    name = db.Column(db.String(200), nullable=False)
    old_name = db.Column(db.String(200), nullable=True)
    admin_hq = db.Column(db.String(length=250), nullable=True)
    admin_division = db.Column(db.Integer, db.ForeignKey('admin_division.id'))
    num_admin_division = db.Column(db.Integer, nullable=True)
    population = db.Column(db.Integer, nullable=False)
    area = db.Column(db.Float, nullable=False)
    latitude = db.Column(db.Float, nullable=False)
    longitude = db.Column(db.Float, nullable=False)
    created_at = db.Column(db.Date)
