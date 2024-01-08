# -*- coding: utf-8 -*-

"""This file is part of the TPOT library.

TPOT was primarily developed at the University of Pennsylvania by:
    - Randal S. Olson (rso@randalolson.com)
    - Weixuan Fu (weixuanf@upenn.edu)
    - Daniel Angell (dpa34@drexel.edu)
    - and many more generous open source contributors

TPOT is free software: you can redistribute it and/or modify
it under the terms of the GNU Lesser General Public License as
published by the Free Software Foundation, either version 3 of
the License, or (at your option) any later version.

TPOT is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
GNU Lesser General Public License for more details.

You should have received a copy of the GNU Lesser General Public
License along with TPOT. If not, see <http://www.gnu.org/licenses/>.

"""

from .zero_count import ZeroCount
from .combine_dfs import CombineDFs
from .stacking_estimator import StackingEstimator
from .one_hot_encoder import OneHotEncoder, auto_select_categorical_features, _transform_selected
from .feature_transformers import CategoricalSelector, ContinuousSelector
from .feature_set_selector import FeatureSetSelector
try:
    from .nn import PytorchLRClassifier, PytorchMLPClassifier
except (ModuleNotFoundError, ImportError):
    import warnings
    warnings.warn("Warning: optional dependency `torch` is not available. - skipping import of NN models.")

'''
Library Introduction and Licensing: The initial comments explain that TPOT is developed primarily at the University of Pennsylvania by Randal S. Olson and others. It's distributed under the GNU Lesser General Public License (LGPL), version 3. This means TPOT is free software, and you can redistribute and/or modify it under the terms of this license.

Module Imports: The code imports various modules, each of which seems to be a component of TPOT:

ZeroCount, CombineDFs, StackingEstimator, OneHotEncoder, CategoricalSelector, ContinuousSelector, FeatureSetSelector: These are likely custom transformers or estimators for data preprocessing and feature engineering.
auto_select_categorical_features, _transform_selected: Functions for handling categorical features in the dataset.
PytorchLRClassifier, PytorchMLPClassifier: These are neural network models, probably a logistic regression and a multi-layer perceptron classifier, implemented using PyTorch.
Conditional Import and Warning for Optional Dependency: The try-except block is used for importing neural network models (PytorchLRClassifier, PytorchMLPClassifier) that depend on PyTorch (torch). If PyTorch is not installed (ModuleNotFoundError or ImportError), it triggers a warning. This approach is commonly used in Python libraries to handle optional dependencies.

Overall Functionality: TPOT automates the process of building and optimizing machine learning pipelines. It uses genetic programming to optimize a pipeline's structure and parameters, aiming to find the best performing pipeline for a given dataset. The mentioned classes and functions are part of TPOT's toolkit for preprocessing data, feature selection, and model building.

In summary, this code snippet is part of TPOT's implementation, focusing on importing various components for automated machine learning, with an emphasis on handling optional dependencies gracefully.
'''
