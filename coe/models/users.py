import mongoengine as me
import datetime
from flask import url_for
from flask_login import UserMixin


class User(me.Document, UserMixin):
    meta = {"collection": "users"}

    first_name = me.StringField(max_length=512)
    last_name = me.StringField(max_length=512)

    username = me.StringField(required=True, unique=True, max_length=64)
    # password = me.StringField(required=True)

    email = me.StringField(required=True, unique=True, max_length=512)
    status = me.StringField(default="active", max_length=64)
    roles = me.ListField(me.StringField(), default=["user"])
    created_date = me.DateTimeField(required=True, default=datetime.datetime.now)
    updated_date = me.DateTimeField(required=True, default=datetime.datetime.now)
    last_login_date = me.DateTimeField(
        required=True, default=datetime.datetime.now, auto_now=True
    )
    created_by = me.ReferenceField("User", dbref=True)
