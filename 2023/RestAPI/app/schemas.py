from marshmallow import Schema, fields


class ConversorSchema(Schema):
    moeda1 = fields.Str(required=True)
    moeda2 = fields.Str(required=True)
    valor = fields.Str(required=True)
    simbolo = fields.Str(dump_only=True)