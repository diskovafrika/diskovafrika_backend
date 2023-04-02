from diskovafrika.configs.extensions import db


class Language(db.Model):
    """model for language objects"""
    __tablename__ = "language"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(length=50), nullable=False, unique=True)
    abbr = db.Column(db.String(length=5), nullable=False, unique=True)


class Currency(db.Model):
    """model for language objects"""
    __tablename__ = "currencies"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(length=50), nullable=False, unique=True)
    short_code = db.Column(db.String(length=5), nullable=False, unique=True)
    symbol = db.Column(db.String(length=5), nullable=True)
