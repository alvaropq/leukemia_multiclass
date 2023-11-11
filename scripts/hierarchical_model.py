import numpy as np
import pandas as pd
from sklearn.base import BaseEstimator, ClassifierMixin
from sklearn.utils.validation import check_X_y, check_array, check_is_fitted
from sklearn.utils.multiclass import unique_labels
from sklearn.feature_selection import SelectFromModel

class HierarquicalClassifier(BaseEstimator, ClassifierMixin):

    def __init__(self,hierarchy,clf, params,feature_selection,max_features):
        self.hierarchy = hierarchy
        self.clf = clf
        self.params = params
        self.models = []
        self.model_names = []
        self.classes_ = []
        self.features = []
        self.feature_selection = feature_selection
        self.max_features = max_features

    def fit(self, X, y):
      
      self.models = []
      self.model_names = []
      self.classes_ = []
      self.features = []

      train = X.copy(deep=True)
      train[y.columns] = y.astype('str')

      data = pd.DataFrame.from_dict(self.hierarchy, orient='columns')
      for i in data.columns:
        aux = pd.DataFrame(data[i].notna()).reset_index()
        aux = aux[aux[i] == True]
        for j in aux['index']:
          #print('modelo: '+j)
          #print(data[i].loc[j])
          
          classes = data[i].loc[j]
          new_train = train[train[i].isin(classes)]
          y_ = new_train[i]
          X_ = new_train[X.columns]

          # Check that X and y have correct shape
          # X_, y_ = check_X_y(X_, y_)
          
          self.model_names.append(j)
          self.classes_.append(unique_labels(y_))
          
          if self.feature_selection:
            sel = SelectFromModel(self.clf(**self.params),max_features = self.max_features, threshold='mean')
            sel.fit(X_, y_)
            X_ = X_[list(X_.columns[(sel.get_support())])]
          
          
          clf = self.clf(**self.params)
          clf.fit(X_,y_)
          self.models.append(clf)
          self.features.append(list(X_.columns))
          
        # Return the classifier
      return self

    def predict(self, X):

      # Check if fit has been called
      check_is_fitted(self)

      results = []

      
      for i,row in X.iterrows():
        
        index = self.model_names.index('root')
        features = self.features[index]
  
        X_ = row[features]
        result = self.models[index].predict(pd.DataFrame(np.array(X_).reshape(1, -1),columns = features))

        while(result in self.model_names):
          index = self.model_names.index(result)
          features = self.features[index]
          X_ = row[features]

          result = self.models[index].predict(pd.DataFrame(np.array(X_).reshape(1, -1),columns = features))  
        
        results.extend(result)

      return results
