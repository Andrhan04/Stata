from sklearn.metrics import confusion_matrix
from interpritate import inerpritate
import statistics as st



def Get_param(data, true):
    print(st.mode(data))
    print(st.values(data))
    print(st.median(data))
    print(max(data) - min(data))
    print(confusion_matrix(true,data))
    print(st.mean(data))

data = inerpritate()
for i in data:
    Get_param(i,[])