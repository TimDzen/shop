from marshmallow import Schema, fields


class Product_schema(Schema):
    id = fields.Int()
    name = fields.Str(required=True)
    price = fields.Float(required=True)