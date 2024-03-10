#!/usr/bin/python3
'''
Module for creating BaseModel class
'''

import uuid
from datetime import datetime
import models

class BaseModel:
	def  __init__(self, *args, **kwargs):
		time_format = "%Y-%m-%dT%H:%M:%S.%f"
		self.id = str(uuid.uuid4())
		self.created_at = datetime.utcnow()
		self.updated_at = datetime.utcnow()

		if kwargs:
			for key, value in kwargs.items():
				if key == "__class__":
					continue
				elif key == "created_at" or key == "updated_at":
					setattr(self, key, datetime.strptime(value, time_format))
				else:
					setattr(self, key, value)

	def save(self):
		'''
		updates the public instance attribute updated_at with the current datetime
		'''
		self.updated_at = datetime.utcnow()


	def to_dict(self):
		'''
		returns a dictionary containing all keys/values of __dict__ of the instance
		'''
		is_dict = self.__dict__.copy()
		is_dict["__class__"] = self.__class__.__name__
		is_dict["created_at"] = self.created_at.isoformat()
		is_dict["updated_at"] = self.updated_at.isoformat()

		return is_dict

	def __str__(self):
		'''
		print: [<class name>] (<self.id>) <self.__dict__>
		'''
		class_name = self.__class__.__name__
		return "[{}] ({}) {}".format(class_name, self.id, self.__dict__)