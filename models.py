#!/usr/bin/env python
# encoding: utf-8

from datetime import datetime

from mongoengine import (DynamicDocument, DynamicEmbeddedDocument, 
                        EmbeddedDocumentListField, StringField,
                        IntField, BooleanField, DateTimeField)


class TransLation(DynamicEmbeddedDocument):

    name = StringField(max_length=128, unique=True)
    rating = IntField(default=5)
    nominal = StringField(max_length=128, default=u'n.')
    level = StringField(max_length=128, default=u'student')

    def __unicode__(self):
        return self.name

class Word(DynamicDocument):

    name = StringField(max_length=128, unique=True)
    trans = EmbeddedDocumentListField(TransLation)
    blocked = BooleanField(default=False)
    rating = IntField(default=1)
    update_at = DateTimeField(default=datetime.now())

    def __unicode__(self):
        return self.name
