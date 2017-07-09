# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from rest_framework_mongoengine import viewsets
from mongoenginetest.serializers import TestSerializer
from mongoenginetest.models import Test

# Create your views here.

class TestViewSet(viewsets.ModelViewSet):
  lookup_field = 'id'
  serializer_class = TestSerializer

  def get_queryset(self):
    return Test.objects.all()
