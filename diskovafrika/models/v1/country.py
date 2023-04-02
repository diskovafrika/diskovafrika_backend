"""Country Model"""

from uuid import uuid4
from diskovafrika.configs.extensions import db
from sqlalchemy import Enum


timezones = ("-1", "0", "1", "2", "3", "4")


class Country(db.Model):
    """model for country objects"""
    __tablename__ = "country"
    id = db.Column(
        db.String(length=50), primary_key=True, default=str(uuid4), unique=True)
    name = db.Column(db.String(length=250), nullable=False, unique=True)
    capital = db.Column(db.String(length=250), nullable=False)
    iso_code = db.Column(db.String(4))
    date_of_independence = db.Column(db.Date)
    country_code = db.Column(db.Integer, nullable=False)
    utc_zone = db.Column(Enum(*timezones))
    sub_region = db.Column(Enum(
        "Northern", "Central", "Western", "Southern", "Eastern")
    )
    population = db.Column(db.Integer, nullable=False)
    admin_division = db.Column(db.Integer, db.ForeignKey('admin_division.id'))
    num_admin_division = db.Column(db.Integer)
    # division = db.relationship("Division", backref='div_country')

    # languages = db.relationship("CountryLanguages", backref='country_lang')

    # @staticmethod
    # def get_country_by_id(id=None):
    #     """Get country by id"""
    #     if id is not None:
    #         ctry = Country.query.filter_by(id=id).first()
    #     try:
    #         country = {
    #             "id": ctry.id,
    #             "name": ctry.name,
    #             "capital": ctry.capital,
    #             "date_of_independence": ctry.date_of_independence.strftime("%d-%b-%Y"),
    #             "iso_code": ctry.iso_code,
    #             "admin_div": str(ctry.admin_div),
    #             "country_code": ctry.country_code,
    #             "number of divisions": ctry.num_div
    #         }
    #     except AttributeError:
    #         country = None
    #     return country

    # @staticmethod
    # def get_country_by_iso(name=None):
    #     """Get country by country's name"""
    #     if name is not None:
    #         ctry = Country.query.filter_by(name=name).first()
    #     try:
    #         country = {
    #             "id": ctry.id,
    #             "name": ctry.name,
    #             "capital": ctry.capital,
    #             "date_of_independence": ctry.date_of_independence.strftime("%d-%b-%Y"),
    #             "iso_code": ctry.iso_code,
    #             "admin_div": str(ctry.admin_div),
    #             "country_code": ctry.country_code,
    #             "number of divisions": ctry.num_div
    #         }
    #     except AttributeError:
    #         country = None
    #     return country

    # @staticmethod
    # def all_countries():
    #     """Returns all countries in DB"""
    #     countries = Country.query.order_by(Country.name.desc()).all()
    #     countries = [country.__dict__ for country in countries]
    #     # country = {}
    #     # countris = [ del item["_sa_instance_state"] for item in countries]
    #     for item in countries:
    #         del item["_sa_instance_state"]
    #     # TODO clean-up date-time and Admin-div
    #     return countries
