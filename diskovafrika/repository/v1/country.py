import json
from uuid import uuid4
from marshmallow import ValidationError
from sqlalchemy import desc
from diskovafrika.configs.extensions import db
from diskovafrika.models.schema.country import CountrySchema
from diskovafrika.models.v1.country import Country
