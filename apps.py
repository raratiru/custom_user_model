#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.apps import AppConfig


class PeopleConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "key.people"
    label = "people"
