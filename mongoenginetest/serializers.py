from rest_framework_mongoengine import serializers
from mongoenginetest.models import Test

class TestSerializer(serializers.DocumentSerializer):
  class Meta:
    model = Test
    fields = '__all__'
