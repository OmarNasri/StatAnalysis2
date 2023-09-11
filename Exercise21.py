import numpy as np 


vector1 = np.array([5,8,7,6,8,4])
vector2 = np.array([1.3,2.1,1.8,1.2,1.4,2.3])
vector3 = np.array(['y','y','n','y','n','n'])

#Combine the vectors into a data matrix with 3 columns and 6 rows. 
data = np.column_stack((vector1,vector2,vector3))
print(data)

#print element at (3,2)
print(data[2,1])

#print the 4th row
print(data[3,:])

#create submatrix of 2 last columns and rows 2-5
submatrix = data[1:5,1:3]
print(submatrix)

#transpose the matrix so that it has 6 columns and 3 rows
transposed = data.transpose()
print(transposed)