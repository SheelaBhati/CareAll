#######################################
#
# Project: 		CareAll
# Company: 		Self Project
# Developer: 	Sheela Bhati
# File:			old_folks.py
#
#######################################

from users import User

"""
Class Name:			OldFolks
Purpose:			This is a subclass of User. It holds old users information.
Parent Class:		User
Chile Class:		Not Any
"""
class OldFolks(User):
	"""
	Name:				__init__
	Purpose:			This function intializes Old folk class object
	"""
	def __init__ (self):
		self.current_assigned_young = None 	# current assigned young champ
		self.salary = 0						# contains salary offered by old folk
		self.rating_points = 0				# count of rating points
		self.total_cared = 0				# how many user rated 

	"""
	Name:				update_old_salary
	Purpose:			This function modifies salary offred by old guys.
						Using this API old user can modify there salary.
	"""
	def update_old_salary(self,salary):
		self.salary = salary

	"""
	Name:				update_rating
	Purpose:			Internal function updates rating of old folks given by young champ.
	"""
	def update_rating(self,young_user,rating):
		# Check if rating is valid or not
		if(type(rating)==int and rating<=5 and rating>=1):
			# update current rating point
			self.rating_points+=rating

			# add user
			self.total_cared += 1

			# display rating on console: Rating = rating_points/total_cared
			print("Young champ " + young_user.name + " rated " +  self.name +" " + str(rating))
			print(self.name +" current rating is " + str(self.rating_points/self.total_cared))
		else:
			# invalid rating provided
			print("\nIgnoring invalid rating")

	"""
	Name:				unassign_young
	Purpose:			Young champs ends service of old folks using this API.
	"""
	def unassign_young(self, young_user,rating):
		# check if service requested for young user or not
		if(type(young_user)==OldFolks):
			print("Invlid Young User")
			return
		# check if the mentioned young user was serving the old folk
		if(self.current_assigned_young == young_user):
			print("\n"+young_user.name + " opted to stop serices of " + self.name)

			# salary update of young champ
			young_user.salary -= self.salary

			# Update current serving young info to none
			# Old folk is available to care
			self.current_assigned_young = None

			# update current caring count of young user
			young_user.current_old_caring -=1

			# remove and delete current serving data from list
			for items in young_user.list:
				if(items.old_user == self):
					young_user.list.remove(items)
					del items

			# update rating of old folk given by young user
			self.update_rating(young_user, rating)
			return

		# invalid young user is sent to stop caring of old folk
		print("\nYoung Champ " + young_user.name + " is not serving old folk "+ self.name)



