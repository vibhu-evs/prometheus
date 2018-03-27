from marshmallow import Schema, fields, ValidationError
from src.models import FeatureRequest

def validate_length(n):
    if len(n) == 0:
        raise ValidationError('Value is required')


def validate_client(val):
    if val not in dict(FeatureRequest.CLIENT_TYPES).keys():
        raise ValidationError('Invalid value')

def validate_product_area(val):
    if val not in dict(FeatureRequest.PRODUCT_TYPES).keys():
        raise ValidationError('Invalid value')


class FeatureSchema(Schema):
    title = fields.String(required=True, validate=validate_length)
    description = fields.String(required=True, validate=validate_length)
    client = fields.String(required=True, validate=validate_client)
    priority = fields.Integer(required=True)
    product_area = fields.String(required=True, validate=validate_product_area)
    target_date = fields.Date(required=True)
