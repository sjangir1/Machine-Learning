## 1)Convert.py: Script for converting DNA character sequence to DNA numeric sequence
Assign a unique number to distinct characters 

For example: 
  
  ➢ We have a feature vector with [‘A’,’C’,’T’,’G’,’A’,’G’] 
  
  ➢ Now we will assign a unique number to distinct characters let’s say we assign: 
    
    ▪ 0->’A’  
    
    ▪ 1->’C’ 
    
    ▪ 2->’T’ 
    
    ▪ 3->’G’ 
  ➢ We can see that we just have 4 distinct characters in our example feature vector so, we have 4 unique numbers assigned to each distinct character. 
  
  ➢ Following this procedure of encoding our feature vector will now be [0,1,2,3,0,3]. 

Script for this process is named convert.py. It can be found in the code folder. 

## 2)Building a visualization of the DNA data using two methods: 

a) Multidimensional scaling with 2 dimensions. An input distance matrix is the matrix of pairwise Hamming distances between sequences.


b) Principal component analysis. Reducing the numerical data matrix built in 1) to 2 dimensions and ploting sequences using 2 obtained features as coordinates.

➢ After visualization of DNA data using the two methods, Principal component analysis (PCA) produced better results. 

➢ It depends on the Dataset we are using. In our case we used DNA data, which resulted in PCA giving a better visualization. 

➢ It can also depend on the distance metrics we are using.

## 3) Clustering DNA sequences by applying k-means algorithm to 2-dimensional projections of the data obtained in 2).

### K-means on Multidimensional scaling (MDS): 

k=4 (Justification: 4 clusters are perfectly clustering the data by MDS method) 

K value was obtained after experimenting with its value. 

### K-means on Principal component analysis (PCA): 

K=5 (Justification: 5 clusters are perfectly clustering the data by PCA method) 

K value was obtained after experimenting with its value. 
