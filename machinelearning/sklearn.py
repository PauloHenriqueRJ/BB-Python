from sklearn import datasets
import pandas as pd
import numpy as np
import matplotlib.pylot as plt
iris = datasets.load_iris()

print(type(iris))
print(iris.keys())

class 'sklearn.utils.Bunch'>

dict_keys(['data', 'target', 'frame', 'target_names', 'DESCR', 'feature_names', 'filename', 'data_module'])