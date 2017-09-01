# -*- coding: utf-8 -*-
import arrow

from . import db


class Users(db.Model):
    """用户"""
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True)
    password = db.Column(db.String(128))
    scope = db.Column(db.String(128), default='')
    date_created = db.Column(
        db.DateTime, default=arrow.now('PRC').datetime.replace(tzinfo=None))
    date_modified = db.Column(
        db.DateTime, default=arrow.now('PRC').datetime.replace(tzinfo=None))
    banned = db.Column(db.Integer, default=0)

    def __init__(self, username, password, scope='', banned=0,
                 date_created=None, date_modified=None):
        self.username = username
        self.password = password
        self.scope = scope
        now = arrow.now('PRC').datetime.replace(tzinfo=None)
        if date_created is None:
            self.date_created = now
        else:
            self.date_created = date_created
        if date_modified is None:
            self.date_modified = now
        else:
            self.date_modified = date_modified
        self.banned = banned

    def __repr__(self):
        return '<Users %r>' % self.id


class Scope(db.Model):
    """权限范围"""
    __tablename__ = 'scope'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True)

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return '<Scope %r>' % self.id

class Kkdd(db.Model):
    """卡口地点"""
    __tablename__ = 'kkdd'
    id = db.Column(db.Integer, primary_key=True)
    kkdd_id = db.Column(db.String(256))
    kkdd_name = db.Column(db.String(256))
    fxbh_list = db.Column(db.String(256))
    ps = db.Column(db.String(256))
    banned = db.Column(db.Integer, default=0)

    def __init__(self, kkdd_id, kkdd_name, fxbh_list, ps, banned=0):
	self.kkdd_id = kkdd_id
	self.kkdd_name = kkdd_name
	self.fxbh_list = fxbh_list
	self.ps = ps
	self.banned = banned

    def __repr__(self):
        return '<Kkdd %r>' % self.id

