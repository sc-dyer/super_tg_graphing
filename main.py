#This is a program to plot the output of SUPER_TG and compare it to
#traverses measured in real samples


from Model import Model
import os
import matplotlib.pyplot as plt
#import numpy as np




fileIn = input('Enter the directory where the SUPER_TG trials are stored: ')
fileIn = fileIn.strip()
fileIn = fileIn.strip('"')


#fileOut = input('Enter the desired directory for the output files to be saved (WARNING: THIS WILL OVERWRITE FILES OF THE SAME NAME, SAVE TO NEW FOLDER IF YOU DONT WANT THIS TO HAPPEN): ')
#fileOut = fileOut.strip()
#fileOut = fileOut.strip('"')


testModel = Model(fileIn, 2, 2)

