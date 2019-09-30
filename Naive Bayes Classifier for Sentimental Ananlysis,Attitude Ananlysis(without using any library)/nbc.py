import numpy as np
from collections import Counter, defaultdict

import pandas as pd

from collections import defaultdict
import re
def occurrences(list1):
    no_of_examples = len(list1)
    prob = dict(Counter(list1))
    for key in prob.keys():
        prob[key] = prob[key] / float(no_of_examples)
    return prob


def naive_bayes(training, outcome, new_sample):
    classes = np.unique(outcome)
    rows, cols = np.shape(training)
    likelihoods = {}
    for cls in classes:
        likelihoods[cls] = defaultdict(list)

    class_probabilities = occurrences(outcome)


    for cls in classes:
        row_indices = np.where(outcome == cls)[0]
        subset = training[row_indices, :]
        r, c = np.shape(subset)
        for j in range(0, c):
            likelihoods[cls][j] += list(subset[:, j])

    for cls in classes:
        for j in range(0, cols):
            likelihoods[cls][j] = occurrences(likelihoods[cls][j])

    results = {}
    for cls in classes:
        class_probability = class_probabilities[cls]
        for i in range(0, len(new_sample)):
            relative_values = likelihoods[cls][i]
            if new_sample[i] in relative_values.keys():
                class_probability *= relative_values[new_sample[i]]
            else:
                class_probability *= 0
            results[cls] = class_probability
    return results



if __name__ == "__main__":
    print('-----Feeding Training data-----')
    training = np.asarray(pd.read_csv('S:/AML/AML-Assignment-1/trainnew.csv',sep=','));
    print('-->Done')
    print('-----Feeding the Indicative Attitude of Each Review-----')
    outcome = np.asarray((0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,));
    print('-->Done')
    print('-----Feeding the Test Data for Classification-----')
    new_sample = np.asarray(pd.read_csv('S:/AML/AML-Assignment-1/testnew.csv',sep=','))
    print('-->Done')
for i in range(len(new_sample)):
    z=new_sample[i]
    print('Test_Review[',i,']',naive_bayes(training, outcome, z))