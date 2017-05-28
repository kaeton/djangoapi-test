#!/usr/bin/env python
# -*- coding: utf-8 -*-
# vim:set fileencoding=utf-8:

from rest_framework import serializers
from .models import User, Entry

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('name', 'mail')

class EntrySerializer(serializers.ModelSerializer):
    author = UserSerializer()
    class Meta:
        model = Entry
        fields = ('id', 'title', 'body', 'created_at', 'status', 'author')
