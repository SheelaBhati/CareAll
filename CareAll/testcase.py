#######################################
#
# Project: 		CareAll
# Company: 		Self Project
# Developer: 	Sheela Bhati
# File:			testcase.py
#
#######################################

from young_champ import YoungChamp
from old_folks import OldFolks

#Driver Program to test the API's

# Creating old folks
OldFolk1 = OldFolks()
OldFolk1.update_info("Suman", 70, "Female")
OldFolk2 = OldFolks()
OldFolk2.update_info("Ramesh", 80, "Male")

# old folks updating there salary
OldFolk1.update_old_salary(200)
OldFolk2.update_old_salary(500)

# Creating young champ
Young1 = YoungChamp()
Young1.update_info("Naman", 20, "Male")

# display current old folk display for young champ
Young1.show_current_serving()

# assigning an old folk to young champ
Young1.assign_old(OldFolk2, 1)
Young1.show_current_serving()

# assigning another old folk
Young1.assign_old(OldFolk1, 1)
Young1.show_current_serving()

# young champ stopping services for an old folk and giving rating
Young1.unassign_old(OldFolk2,4)
Young1.show_current_serving()

# old folk stopping services his young champ and giving rating
OldFolk1.unassign_young(Young1,2)
Young1.show_current_serving()

# old folk assigning again the previous young champ
Young1.assign_old(OldFolk1, 1)

# creating new young champ
Young2 = YoungChamp()
Young2.update_info("Harshit", 22, "Male")

# assign old folk to young champ
Young2.assign_old(OldFolk1, 1)
Young2.show_current_serving()
