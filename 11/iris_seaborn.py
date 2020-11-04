# -*- coding: utf-8 -*-
"""
Created on Wed Nov  4 01:55:43 2020

@author: wilfr
"""

import seaborn as sns
import pandas as pd
from sklearn.datasets import load_iris

iris_dataset = load_iris()
iris_dataframe = pd.DataFrame(iris_dataset['data'], columns = iris_dataset.feature_names)
iris_dataframe['target'] = iris_dataset['target']

sns.pairplot(iris_dataframe, hue = 'target')