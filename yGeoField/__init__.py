from marshmallow import fields, ValidationError, missing

import geojson

class yGeoField(fields.Field):
  def _deserialize(self, value, attr, data):
    try:
      result = getattr(geojson, value["type"])(value["coordinates"])
      if not result.is_valid:
        raise Exception(result.errors())
      return result
    except Exception as e:
      raise ValidationError('Invalid geojson `%s` `%s`' % (str(value), str(e)))
    
  def _serialize(self, value, attr, obj):
    if value is None:
      return missing
    return  geojson.dumps(value)
