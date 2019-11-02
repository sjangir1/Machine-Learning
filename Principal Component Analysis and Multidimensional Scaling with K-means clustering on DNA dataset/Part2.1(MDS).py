from Bio import SeqIO
import numpy as np
from numpy import array
from sklearn.preprocessing import LabelEncoder
import matplotlib.pyplot as plt
from sklearn.manifold import MDS
from sklearn.metrics import pairwise_distances
seqList = []
for sequences in SeqIO.parse("DNA.fas", "fasta"):
    seqList.append(list(sequences.seq))
seq = array(seqList)
# print(seq)

label_encoder = LabelEncoder()
integer_encoded = list()
for i in range(len(seq)):
    integer_encoded.append(label_encoder.fit_transform(seq[i]))
# print(integer_encoded)

#  An input distance matrix:- the matrix of pairwise Hamming distances between sequences
X = pairwise_distances(integer_encoded,metric='hamming')
print("\n*********Matrix of pairwise Hamming Distances between Sequences*********")
print(X)
print("Shape of the Original Matrix: ", X.shape, "\n")
embedding = MDS(n_components=2, dissimilarity="precomputed")
X_transformed = embedding.fit_transform(X)
print("Multidimensional Scaling with 2 dimensions")
print(X_transformed)
print("Shape of New matrix after performing MDS on Original Matrix: ", X_transformed.shape)


plt.scatter(X_transformed[:, 0], X_transformed[:, 1])
plt.xlabel('component 1')
plt.ylabel('component 2')
plt.show()

