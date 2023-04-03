"""Country Schema"""

from marshmallow import Schema, fields, validate, EXCLUDE

timezones = ("-1", "0", "1", "2", "3", "4")


class CountrySchema(Schema):
    """model for country objects"""
    __tablename__ = "country"
    id = fields.Str(required=True)
    name = fields.Str(required=True)
    capital = fields.Str(required=True)
    iso_code = fields.Str(required=True)
    date_of_independence = fields.Date(required=True)
    country_code = fields.Str(required=True)
    utc_zone = fields.Str(required=True, validate=validate.OneOf(timezones))
    sub_region = fields.Str(required=True, validate=validate.OneOf(
        ["Northern", "Central", "Western", "Southern", "Eastern"])
    )
    population = fields.Int(required=True)
    admin_division = fields.Str(dump_only=True)
    num_admin_division = fields.Int(required=True)

    class Meta:
        unknown = EXCLUDE
