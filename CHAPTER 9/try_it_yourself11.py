
# 9-11. Imported Admin: Start with your work from Exercise 9-8 (page 173). Store
# the classes User, Privileges, and Admin in one module. Create a separate file,
# make an Admin instance, and call show_privileges() to show that everything is
# working correctly.

from Userclass import Admin as ad
cilian = ad('cilian','Murphy',40,'Irelend')
cilian.show_privileges()
