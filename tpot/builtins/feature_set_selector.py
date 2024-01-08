# Importing necessary libraries
import numpy as np
# numpy is used for numerical operations and array handling in Python.

import pandas as pd
# pandas is a powerful tool for data manipulation and analysis, especially for structured data.

import os, os.path
# These modules allow for interactions with the operating system, including handling file paths.

from sklearn.base import BaseEstimator
# BaseEstimator is a base class from scikit-learn from which all estimators inherit.

try:
    from sklearn.feature_selection._base import SelectorMixin
except ImportError:
    from sklearn.feature_selection.base import SelectorMixin
# SelectorMixin is imported for feature selection utilities in scikit-learn. The try-except block handles potential import errors due to different versions or module structures in sklearn.

# Definition of the FeatureSetSelector class
class FeatureSetSelector(BaseEstimator, SelectorMixin):
    # This class inherits from BaseEstimator and SelectorMixin, indicating it's a custom feature selection estimator for scikit-learn.

    """Select predefined feature subsets."""
    # The docstring explaining the purpose of this class.

    # Property definition for __name__
    @property
    def __name__(self):
        # @property decorator makes the following method accessible as an attribute.
        """Instance name is the same as the class name."""
        # Docstring explaining the property.
        return self.__class__.__name__
        # Returns the name of the class for the instance using this property.

    # Constructor of the class
    def __init__(self, subset_list, sel_subset):
        """Create a FeatureSetSelector object.
        ...
        """
        # Constructor method with a detailed docstring explaining parameters and usage.
        self.subset_list = subset_list
        # Initializing the subset_list attribute.
        self.sel_subset = sel_subset
        # Initializing the sel_subset attribute.

    # fit method definition
    def fit(self, X, y=None):
        """Fit FeatureSetSelector for feature selection
        ...
        """
        # The fit method with a detailed docstring.
        subset_df = pd.read_csv(self.subset_list, header=0, index_col=0)
        # Reading the subset list file into a pandas DataFrame.

        # Processing the sel_subset attribute to determine the subset of features to use. This chunck gives us the self.sel_subset_name attribute, the row indices.
        if isinstance(self.sel_subset, int):
            self.sel_subset_name = subset_df.index[self.sel_subset]
        elif isinstance(self.sel_subset, str):
            self.sel_subset_name = self.sel_subset
        else: # list or tuple
            self.sel_subset_name = []
            for s in self.sel_subset:
                if isinstance(s, int):
                    self.sel_subset_name.append(subset_df.index[s])
                else:
                    self.sel_subset_name.append(s)

        # More processing of selected features
        sel_features = subset_df.loc[self.sel_subset_name, 'Features']
        if not isinstance(sel_features, str):
            sel_features = ";".join(sel_features.tolist())

        sel_uniq_features = set(sel_features.split(';'))

        # Determining the features to select based on the DataFrame or ndarray
        if isinstance(X, pd.DataFrame):
            self.feature_names = list(X.columns.values)
            self.feat_list = sorted(list(set(sel_uniq_features).intersection(set(self.feature_names))))
            self.feat_list_idx = [list(X.columns).index(feat_name) for feat_name in self.feat_list]
        elif isinstance(X, np.ndarray):
            self.feature_names = list(range(X.shape[1]))
            sel_uniq_features = [int(val) for val in sel_uniq_features]
            self.feat_list = sorted(list(set(sel_uniq_features).intersection(set(self.feature_names))))
            self.feat_list_idx = self.feat_list

        # Error handling if no features are found
        if not len(self.feat_list):
            raise ValueError('No feature is found on the subset list!')
        return self

    # transform method definition
    def transform(self, X):
        """Make subset after fit
        ...
        """
        # The transform method with a detailed docstring.
        if isinstance(X, pd.DataFrame):
            X_transformed = X[self.feat_list].values
        elif isinstance(X, np.ndarray):
            X_transformed = X[:, self.feat_list_idx]

        return X_transformed.astype(np.float64)

    # _get_support_mask method definition
    def _get_support_mask(self):
        """
        Get the boolean mask indicating which features are selected
        ...
        """
        # A private method to get a mask of selected features.
        n_features = len(self.feature_names)
        mask = np.zeros(n_features, dtype=bool)
        mask[np.asarray(self.feat_list_idx)] = True

        return mask
        # Returns a boolean array indicating selected features.
