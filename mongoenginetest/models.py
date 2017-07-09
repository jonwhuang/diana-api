# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from mongoengine import Document, EmbeddedDocument, fields

# Create your models here.

class Test(Document):
  label = fields.StringField(required=True)
