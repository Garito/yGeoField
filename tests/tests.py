from unittest import TestCase

from marshmallow import Schema

from yGeoField import yGeoField

class SchemaToTest(Schema):
  geopoint = yGeoField()

class TestGeoField(TestCase):
  def testDumps(self):
    data = {"geopoint": '{"type": "Point", "coordinates": (41.5667, 2.0167)}'}
    model = SchemaToTest()
    data, errors = model.load(data)
    print(data)
    print(errors)
