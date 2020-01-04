#######################################
#
# Project: 		CareAll
# Company: 		Self Project
# Developer: 	Sheela Bhati
# File:			young_champ.py
#
#######################################

from users import User, CareData

"""
Class Name:			YoungChamp
Purpose:			This is a subclass of User. It holds young users information.
Parent Class:		User
Chile Class:		Not Any
"""
class YoungChamp(User):
	"""
	Name:				__init__
	Purpose:			This function intializes Young folk class object
	"""
	def __init__(self):
		self.salary = 0					# current total salary of young champ.
		self.current_old_caring = 0		# currnt number of old caring, cannot be more than four
		self.list = []					# list of CareData class objects. cannot be more than four
										# each object holds information of old guy, salary, maximum service months
		self.rating_points = 0			# count of rating points
		self.total_cared = 0			# how many user rated 

	"""
	Name:				assign_old
	Purpose:			Api for old folks to assign young guy to themselves for caring
	"""
	def assign_old(self, old_user, month):
		# check if its a valid old user
		if(type(old_user)==YoungChamp):
			print("Invlid Old User")
			return
		# check if old folks is already being cared by any young champ
		if (old_user.current_assigned_young!=None):
			print("\nCan not assign Young Champ " + self.name + " to " + old_user.name)
			print("Young Champ " + old_user.current_assigned_young.name + " is already caring "+ old_user.name)
			return

		# check if young champ already caring four old folks
		if(self.current_old_caring == 4):
			print("\nYoung Champ " + self.name + " already caring four other old folks")
			return

		# increase current caring count for young champ
		self.current_old_caring +=1

		# create a node for "who is caring whom" and append
		self.list.append(CareData(self,old_user,old_user.salary, month))

		# update young champ salary
		self.salary += old_user.salary

		# update old folk info
		old_user.current_assigned_young = self

	"""
	Name:				update_rating
	Purpose:			Internal function updates rating of young champ given by old folk.
	"""
	def update_rating(self,old_user,rating):
		# Check if rating is valid or not
		if(type(rating)==int and rating<=5 and rating>=1):
			# Check if rating is valid or not
			self.rating_points+=rating

			# add user
			self.total_cared +=1

			# display rating on console: Rating = rating_points/total_cared
			print("\nOld folk " + old_user.name + " rated " +  self.name +" " + str(rating))
			print(self.name + "'s current rating is " + str(self.rating_points/self.total_cared))
		else:
			# invalid rating provided
			print("Ignoring invalid rating")

	"""
	Name:				unassign_old
	Purpose:			Old folks ends service of young champ using this API.
	"""
	def unassign_old(self, old_user,rating):
		# check if service requested for old user or not
		if(type(old_user)==YoungChamp):
			print("Invlid Old User")
			return

		# check if the mentioned young user was serving the old folk
		for items in self.list:
			if(items.old_user == old_user):
				print("\nOld folk " + items.old_user.name + " opted to end services of " + self.name)

				# salary update of young champ
				self.salary -= items.salary

				# Update current serving young info to none
				# Old folk is available to care
				old_user.current_assigned_young = None

				# remove and delete current serving data from list
				self.list.remove(items)
				del items

				# update current caring count of young user
				self.current_old_caring -=1

				# update rating of young user given by old user
				self.update_rating(old_user, rating)
				return

		# invalid old user is sent to stop caring
		print("\nYoung Champ " + self.name + " is not serving old folk "+ old_user.name)


	"""
	Name:				show_current_serving
	Purpose:			API to display current serving information of young user on console 
	"""
	def show_current_serving(self):
		if(self.current_old_caring == 0):
			# Young champ is idle
			print("\nYoung Champ " + self.name + " is waiting to care old folk")
			return

		# Display current earning of young champ
		print("\nYoung Champ " + self.name + " is earning " + str(self.salary) + " for serving " +str(self.current_old_caring)+" old folks")

		# Display information to old folks
		index = 1
		for items in self.list: 
			print("\n\t\tOld Folk #" + str(index)+": "+ items.old_user.name )
			index +=1
			print("\t\tAge: "+ str(items.old_user.age) )
			print("\t\tSalary: "+ str(items.salary))

