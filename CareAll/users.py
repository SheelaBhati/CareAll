#######################################
# Project: 			CareAll
# Company: 			Self Project
# Developer: 		Sheela Bhati
# File:				users.py
#######################################

# Globals

current_user_count = 0 # current_user_count holds count of current users (old and young)

# Classes

"""
Class Name:			User
Purpose:			To create users including old and young peoples
Parent Class:		Not Any
Child Class:		OldFolks, YoungChamp
"""
class User:
	"""
	Name:				__init__
	Purpose:			This function intializes users class object
	"""
	def __init__(self):
		global current_user_count
		current_user_count+=1
		self.id = current_user_count
		self.name = None
		self.age = None
		self.gender = None


	"""
	Name:				update_info
	Purpose:			Update basic information of the users
	"""
	def update_info(self, name, age, gender):
		self.name = name
		self.age = age
		self.gender = gender

"""
Class Name:			CareData
Purpose:			This class contains information of young champ caring old folk
Parent Class:		Not Any
Child Class:		Not Any
"""
class CareData:
	def __init__(self,yound_id, old_user, salary, month):
		self.young_user = self
		self.old_user = old_user
		self.salary = salary
		self.month = month