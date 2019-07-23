#General class to be extended by the Traverse class and the Model class
#Defines methods that can be used by any garnet composition profile
#Possibly: include method for comparing profiles here?
import matplotlib.pyplot as plt

class CompoProfile:

	def __init__(self):

		#Empty initialization, defines the variables all CompoProfiles should have

		self.x = []
		self.mn = []
		self.mg = []
		self.ca = []
		self.fe = []

	def plotCompo(self, key, clrIn, pltIn):