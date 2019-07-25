#Class to open and manage the measured garnet traverse
#Must be in a csv file formatted in the following way:
from CompoProfile import CompoProfile, COMPS

class Traverse(CompoProfile):

	def __init__(self, fileName):
		
		CompoProfile.__init__(self)
		
		
		