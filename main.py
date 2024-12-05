# from sklearn.metrics import confusion_matrix
from interpritate import inerpritate
import statistics as st
from math import sqrt


def Get_param(data, true):
    X = st.mean(data)
    D = st.variance(data,X)
    M = st.median(data)
    R = max(data) - min(data)
    print(f"mean = {X:.3f}, variance = {D:.3f}, so = {sqrt(D):.3f}, median = {M:.3f}, razmah = {R:.3f}, mode = {st.mode(data):.3f}")
    #print(confusion_matrix(true,data))

data = inerpritate()
n = len(data[0])
true = [[11]*n, [1]*n,[1]*n,[1]*n,[1]*n,[1]*n,[1]*n,[1]*n,[1]*n,[1]*n,[1]*n,[1]*n]
#print(data[6])
for i in range(len(data)):
    print(i)
    Get_param(data[i],true[i])