from app import db
from datetime import datetime
import pytz


# Base Model
class Base(db.Model):
	_id = db.Column(db.Integer, primary_key=True)
	date_created = db.Column(db.DateTime, default=datetime.now(pytz.timezone('Japan')))
	date_modified = db.Column(db.DateTime, default=datetime.now(pytz.timezone('Japan')),
										   onupdate=datetime.now(pytz.timezone('Japan')))
	

# Roles
class Role(Base):
	role = db.Column(db.String(50), nullable=False, unique=True)
	users = db.relationship("User", backref="role")
	def __repr__(self): return f"ID:{self._id} | {self.role}"


# Users
class User(object):
	name = db.Column(db.String(128), nullable=False)
	username = db.Column(db.String(128), nullable=False, unique=True)
	password = db.Column(db.String(128), nullable=False)
	role_id = db.Column(db.Integer, db.ForeignKey('role._id'))
	
	def __init__(self, name, username, password):
		self.name = name
		self.username = username
		self.password = password
	
	def __repr__(self): 
		return f"USer: ID:{self._id} | {self.name}"


