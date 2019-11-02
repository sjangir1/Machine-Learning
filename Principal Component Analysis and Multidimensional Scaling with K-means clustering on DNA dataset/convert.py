from Bio import SeqIO
from numpy import array
from sklearn.preprocessing import LabelEncoder
seqList = []
# reading fasta file and storing each sequence into list or array
for seq_record in SeqIO.parse("DNA.fas", "fasta"):
    seqList.append(list(seq_record.seq))
seq = array(seqList)
print("The Feature vectors of Characters")
print(seq,"\n")

# Converting feature vector of Characters into feature vectors of Numbers
label_encoder = LabelEncoder()
integer_encoded = list()
for i in range(len(seqList)):
    integer_encoded.append(label_encoder.fit_transform(seqList[i]))
print("The Feature vectors of Numbers")
print(integer_encoded)