# -*- coding: utf-8 -*-
"""
Created on Tue Jan 10 14:05:19 2017

@author: Murray
"""

import numpy as np
import random as rd
import matplotlib.pyplot as plt


def collinear_matrix(m): #creates a matrix of size m with every second row is a row of +1
# and every other row is a row of -1
    matrix = [] # creating a basic matrix
    spin_up = np.ones(m) #spin up = +1 (array of +1's)
    spin_down = -np.ones(m) #spin down = -1 (array of -1's)
    i = 0 #The rows start at zero and count up
    while i<m: #creating a while loop
        matrix.append(spin_up) #every second row is spin up
        matrix.append(spin_down) #every second row is spin down
        i = i+2 #every second row is the same (collinear)
    return np.array(matrix) 
#print collinear_matrix(10) # m = 10 so its a square 10 by 10 matrix
#-------------------------------------------------------------

def random_matrix(m): #creates a matrix of size m same as before but 
#randomly assigns a 1 or -1 to each point in the matrix 
    ran_matrix = [] #random matrix
    x = 1.0 #spin up
    y = -1.0 # spin down
    limit = 0.5 # if value is above this it gives a +1 and if value is below it gives a -1
    for i in range(m):
        R=[]
        for j in range(m):
            if rd.random()>limit: #Selects a random number between 0 and 1, when random value > 0.5 we get a +1
                    R.append(x) # x = +1
            else:
                    R.append(y) # when random value is less than 0.5 we get a -1 = y
        ran_matrix.append(R) 
    return np.array(ran_matrix)    #returns the random spin up or spin down matrix
#print random_matrix(10) #printing random matrix
    
#---------------------------------------------------------------------------------------
    
L=10 #L = width of the lattice 

def sweeps(matrix, T):    #function that sweeps through the matrix changing spins if Hamiltonian < 0 when spin is changed
    # or if a random number is < P_flip
    for z in range(100000):     #for z in range(no. of sweeps). This for loop repeats this 'no. of sweeps' times
        i = rd.randint(0, L-1)    #L is matrix size. L = 10 means a 10 by 10 matrix. Starts counting from 0  
        j = rd.randint(0, L-1)    # i is the x coordinates or columns j is the rows or y coordinates   
        matrix1 = matrix[i,j] # defining my matrix
        Boundary=matrix[(i+1)%L,j]+matrix[i,(j+1)%L]+matrix[(i-1)%L,j] + matrix[i, (j-1)%L]  #boundary conditions for sides, top/bottom rows and corners
        Energy_diff=2*matrix1*Boundary       #formula given in slides. Energy is the Hamiltonian
        P_flip = np.exp(-Energy_diff/T) #the probability of the spin flipping
        if Energy_diff < 0:    #If a flip is energy efficient (a flip will end up being less energy) then we flip it     
            matrix1 = -matrix[i,j]     #matrix gets flipped   
        elif rd.random() < P_flip:  # a random number between 0 and 1 is chosen. If it is < P_flip then we flip the spin. If not then we leave it 
            matrix1 = -matrix[i,j] # The spin is flipped if random number is < P_flip
        matrix[i,j]=matrix1 
    return matrix
#print sweeps(collinear_matrix(L), 2000)    
#------------------------------------------------------------------------------------------

#Trying to add up the elements in the matrices to find the magnetisation of each matrix
T=0.1 #T = starting temperature
#print collinear_matrix(L)   #original collinear matrix
#print sweeps(collinear_matrix(L),T)  #updated collinear matrix
list_of_elements=np.array(sweeps(collinear_matrix(L),T)) # makes an array or list out of the matrix elements so they can be added up     
#magnetisation=np.sum(list_of_elements) #adding up all the elements in the array/list = the magnetisation                     
#print magnetisation
 
#Creating a while loop to calculate magnetisations for each matrix as T increases in steps of 0.1
while (T < 6.0): #while loop to find magnetisation of numerous matrices as T increases and plot them
    list_of_elements1=np.array(sweeps(collinear_matrix(L), T)) #makes the elements into an array so they can be added up
    magnetisation1=np.sum((list_of_elements1)/L**2) #magnetisation = the sum of all the elements in a matrix. We divide by L**2 to get our results between 0 and 1
    T = T + 0.1 #T increases in steps of 0.1
    magnetisation2=abs(magnetisation1) # We dont want any negative values of magnetisation so we use the absolute value
    print T # prints the temperature steps
    print magnetisation2 #Prints the magnetisation of different matrices of increasing temperature in steps of 0.1
    plt.scatter(T/3.4, magnetisation2) # magnetisation Vs Temperature
    plt.ylabel('Mean Magnetisation (magnetisation/no. of elements)')
    plt.xlabel('Temperature')
    plt.title('Mean Magnetisation Vs Temperature')
    plt.grid(True)
    plt.show()    
    
#----------------------------------------------------------------------------------------------------------------------------------