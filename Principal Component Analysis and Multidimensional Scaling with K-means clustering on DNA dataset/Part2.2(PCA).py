from Bio import SeqIO
import numpy as np
from numpy import array
from sklearn.decomposition import PCA
from sklearn.preprocessing import LabelEncoder
import matplotlib.pyplot as plt
seqList = []
for seq_record in SeqIO.parse("DNA.fas", "fasta"):
    seqList.append(list(seq_record.seq))
seq=array(seqList)
# print(seq)
label_encoder = LabelEncoder()
integer_encoded = list()
for i in range(len(seqList)):
    integer_encoded.append(label_encoder.fit_transform(seq[i]))
# print(integer_encoded)

X = np.array(integer_encoded).T
print("\nNumeric feature vectors(transpose)")
print(X)
print("Shape of Above matrix: ", X.shape, "\n")
pca = PCA(n_components=2)
projected = pca.fit_transform(X)
print("Reduced numerical data matrix using PCA")
print(projected)
# print(pca.components_)

print("Shape of above matrix: ", projected.shape)
plt.scatter(projected[:, 0], projected[:, 1])
plt.xlabel('component 1')
plt.ylabel('component 2')
plt.show()
