import json
from uuid import uuid4
from marshmallow import ValidationError
from sqlalchemy import desc
from diskovafrika.configs.extensions import db
from diskovafrika.models.schema.country import CountrySchema
from diskovafrika.models.v1.admin_divisions import AdminDivision
from diskovafrika.models.v1.country import Country
from diskovafrika.utils.utils import error_response

country_schema = CountrySchema()


class CountryRepo:

    @staticmethod
    def all():
        """
        The all function returns a list of all countries in the database.
            It is called by making an HTTP GET request to /api/v2/countries

        :return: A list of dictionaries with the country, capital, iso_code and sub_region

        """
        all = db.session.query(
            Country.name, Country.capital, Country.iso_code, Country.sub_region).join(AdminDivision).all()
        # print(all)
        country_list = [
            {
                'country': ctry[0], 'capital':ctry[1],
                'iso_code': ctry[2], 'sub_region': f"{ctry[3]} Africa"
            } for ctry in all
        ]

        return country_list

    @staticmethod
    def get_country(name=None, div=None):
        """
        The get_country function is used to retrieve a country from the database.
            It takes in two arguments, name and div. If both are provided, it will return all countries that match both criteria.
            If only one argument is provided, it will return all countries that match the given criteria.

        :param name: Filter the countries by name
        :param div: Filter the countries by their capital
        :return: A list of countries that match the query

        """
        if (name is None or name == ""):
            serialized_data = []
            if div and div != "":
                country = db.session.query(
                    Country).filter(Country.capital.ilike(f"{div}%")).all()
                serialized_data = json.loads(
                    country_schema.dumps(country, many=True))
        elif (div is None or div == ""):
            if name and len(name) == 2:
                country = Country.query.filter_by(iso_code=name).first()
                serialized_data = json.loads(country_schema.dumps(country))
            elif name and name != "":
                country = db.session.query(
                    Country).filter(Country.name.ilike(f"{name}%")).all()
                serialized_data = json.loads(
                    country_schema.dumps(country, many=True))
        elif len(div) > 0 and len(name) > 0:
            print("tada")
            country = db.session.query(
                Country).filter(Country.name.ilike(f"{name}%")).filter(Country.capital.ilike(f"{div}%")).all()
            # print(country)
            serialized_data = json.loads(
                country_schema.dumps(country, many=True))
        if serialized_data == [] or serialized_data == {}:
            message = f"Args was not found in country or capitals"
            serialized_data = error_response(message=message, status_code=400)

        return serialized_data

    @staticmethod
    def division(name):
        """
        The division function takes in a country name and returns the number of divisions
            that country has. If no country is specified, it will return all countries with their
            division counts.

        :param name: Filter the countries in the database
        :return: A dictionary of countries and their number of admin divisions

        """
        if name == 'all':
            country = db.session.query(
                Country.name, AdminDivision.name, Country.num_admin_division).join(AdminDivision).all()
        else:
            country = db.session.query(
                Country.name, AdminDivision.name, Country.num_admin_division).join(AdminDivision).filter(Country.name.ilike(f"{name}%")).all()
        country_list = [{'country': ctry[0], 'division_type':ctry[1], 'division_count': ctry[2]}
                        for ctry in country]
        country_dict = {country['country']: f"{country['division_count']} "+country['division_type']
                        for country in country_list}
        return country_dict

    @staticmethod
    def get_country_by_yoi(yoi):
        """
        The get_country_by_yoi function returns a list of countries that have their date of independence in the year specified by the user.
            The function takes one argument, which is an integer representing a year.
            It returns a list of dictionaries containing country names, capitals, dates of independence and sub-regions.

        :param yoi: Filter the results by year of independence
        :return: A list of dictionaries

        """
        country = db.session.query(
            Country.name, Country.capital, Country.date_of_independence, Country.sub_region).join(AdminDivision).filter(Country.date_of_independence.ilike(f"{yoi}%")).all()
        # print(all)
        country_list = [
            {
                'country': ctry[0], 'capital':ctry[1],
                'date_of_independence': ctry[2], 'sub_region': f"{ctry[3]} Africa"
            } for ctry in country
        ]

        return country_list

    @staticmethod
    def get_country_by_region(region):
        """
        The get_country_by_region function returns a list of countries in the specified region.
            The function takes one argument, which is the name of the region.
            It then queries for all countries that have their sub_region field starting with that string and returns them as a list.

        :param region: Filter the countries in a specific region
        :return: A list of dictionaries

        """
        country = db.session.query(
            Country.name, Country.capital, Country.sub_region).filter(Country.sub_region.ilike(f"{region}%")).all()
        country_list = [
            {
                'country': ctry[0], 'capital':ctry[1],
                'sub_region': f"{ctry[2]} Africa"
            } for ctry in country
        ]

        return country_list
