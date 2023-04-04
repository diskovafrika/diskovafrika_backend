import json
from uuid import uuid4
from marshmallow import ValidationError
from sqlalchemy import desc
from diskovafrika.configs.extensions import db
from diskovafrika.models.schema.country import CountrySchema
from diskovafrika.models.v1.admin_divisions import AdminDivision
from diskovafrika.models.v1.country import Country

country_schema = CountrySchema()


class CountryRepo:

    @staticmethod
    def all():
        all = Country.query.order_by("name").all()
        # print(all)
        # serialized_data = json.loads(all)
        serialized_data = json.loads(country_schema.dumps(all, many=True))
        return serialized_data

    @staticmethod
    def division(name):
        if name == 'all':
            country = db.session.query(
                Country.name, AdminDivision.name).join(AdminDivision).all()
        else:
            country = db.session.query(
                Country.name, AdminDivision.name).join(AdminDivision).filter(Country.name.ilike(f"{name}%")).all()
        country_list = [{'country': ctry[0], 'division':ctry[1]}
                        for ctry in country]
        country_dict = {country['country']: country['division']
                        for country in country_list}
        # print(country_dict)
        return country_dict
