from marshmallow import Schema, fields


class ConversorSchema(Schema):
    moeda1 = fields.Str(required=True)
    moeda2 = fields.Str(required=True)
    valor = fields.Str(required=True)
    simbolo = fields.Str(dump_only=True)
    
class UserSchema(Schema):
    id = fields.Int(dump_only=True)
    username = fields.Str(required=True)
    password = fields.Str(required=True, load_only=True)


class PlainMoedaShema(Schema):
    moeda = fields.Str(dump_only=True)
    simbolo = fields.Str(dump_only=True)
    valor = fields.Float(dump_only=True)

class MoedaShema(PlainMoedaShema):
    moedas = fields.List(fields.Nested(PlainMoedaShema(), dump_only=True))
