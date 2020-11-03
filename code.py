import pandas as pd 
import numpy as np 
from sklearn import linear_model
from sklearn.cross_validation import train_test_split

from sklearn.datasets import load_boston
boston = load_boston()
reg.fit(x_train,y_train)

reg.predict(x_test)
np.mean((reg.predict(x_test) - y_test)**2)
