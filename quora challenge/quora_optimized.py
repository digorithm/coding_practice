import pandas as pd
import numpy as np

from sklearn.grid_search import GridSearchCV
from sklearn.ensemble import ExtraTreesClassifier

class AnswerClassifier():

    def train(self, raw_data, outputs, rows_quantity, features_quantity):
        
        raw_data = np.delete(raw_data,np.s_[:3],1).astype(np.float)

        raw_data = np.delete(raw_data, np.s_[7:12],1)
        raw_data = np.delete(raw_data, np.s_[19:],1)


        #binarizing labels
        binarizer = lambda val: 0 if val == '-1'  else 1
        y = [binarizer (val) for val in outputs]
        
        # training with a GridSearch in case of searching
        # for beter parameters
        clf = ExtraTreesClassifier(min_samples_split=30, n_estimators=45)
        clf.fit(raw_data, y)
        
        # saving the classify in memory  
        self.clf = clf

    def read_stdin(self):
        """
        this method will read each line of the arguments
        each line is similar to the offline document
        but you have to put each row in an array and work a little
        different from the offline version. after that, do the same
        as the offline training
        """

        first_line = raw_input()
        rows_quantity = int(first_line.split()[0])
        features_quantity = int(first_line.split()[1])
        
        raw_data = np.array([]).reshape(0,25)
        outputs = np.array([]).reshape(0,1)

        for i in xrange(0,rows_quantity):
            row = raw_input().split()
            # if ':' in row, remove it and everything before it
            for idx,feat in enumerate(row):
                if ':' in feat:
                    before,kw,row[idx] = feat.partition(':')
            raw_data = np.vstack([raw_data, row])
            outputs = np.vstack([outputs, raw_data[i][1]])
        
        # send it to training
        self.train(raw_data, outputs, rows_quantity, features_quantity)

    def getQueries(self):
        number_of_rows = int(raw_input())
         
        self.queries = np.array([]).reshape(0,24)
        self.filtered_queries = np.array([]).reshape(0,22)
        self.queries_ids = []

        for i in xrange(0, number_of_rows):
            row = raw_input().split()
            # if ':' in row, remove it and everything before it
            for idx,feat in enumerate(row):
                if ':' in feat:
                    before,kw,row[idx] = feat.partition(':')
            self.queries = np.vstack([self.queries, row])
            self.queries_ids.append(row[0])
        
        self.filtered_queries = np.delete(self.queries, np.s_[:2],1)
        self.filtered_queries = np.delete(self.filtered_queries, np.s_[7:12],1)
        self.filtered_queries = np.delete(self.filtered_queries, np.s_[19:],1)

        # predicting filtered/clean queries 
        for idx,query in enumerate(self.filtered_queries):
            self.predict(query, self.queries_ids[idx])

    def predict(self, query, query_id):
        """
        this method will receive string full of features coming from stdin
        and call the predict method from the trained classifier
        """
        prediction = self.clf.predict(query)
        if prediction == 1:
            print query_id + ' +1'
        else:
            print query_id + ' -1'

if __name__ == '__main__':

    clf = AnswerClassifier()
    clf.read_stdin()
    clf.getQueries()
