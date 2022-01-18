from django.shortcuts import render
from django.http import HttpResponse

import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import precision_score, recall_score, accuracy_score
from sklearn.model_selection import train_test_split
from sklearn.ensemble import VotingClassifier, BaggingClassifier
from sklearn.svm import SVC
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import GridSearchCV
from sklearn.preprocessing import StandardScaler

#from .connect import Connect
#from pymongo import MongoClient
#from bson.objectid import ObjectId

# Create your views here.
def index(request):
    response = ""
    #Load, visualize and play with data
    train_data = pd.read_csv("titanic/train.csv")
    # response += str(train_data.head())

    test_data = pd.read_csv("titanic/test.csv")
    # response += str(test_data.head())

    women = train_data.loc[train_data.Sex == 'female']["Survived"]
    rate_women = sum(women)/len(women)
    # response += str("% of women who survived:", rate_women)

    men = train_data.loc[train_data.Sex == "male"]["Survived"]
    rate_men = sum(men)/len(men)
    # response += str("% of men who survived:", rate_men)

    #Upgrade result with ensemble learning
    y = train_data["Survived"]
    features = ["Pclass", "Sex", "SibSp", "Parch"]
    X = pd.get_dummies(train_data[features])
    X_test = pd.get_dummies(test_data[features])
    X_train, X_cross, y_train, y_cross = train_test_split(X, y, test_size=0.30)

    # response += str("")
    # response += str('X train size: ', X_train.shape)
    # response += str('y train size: ', y_train.shape)
    # response += str('X cross size: ', X_cross.shape)
    # response += str('y cross size: ', y_cross.shape)

    #classic random forest model
    # model = RandomForestClassifier(n_estimators=100, max_depth=5)

    #Ensemble learning classifier model
    # rfClf = RandomForestClassifier(n_estimators = 500)
    # svmClf = SVC(probability=True)
    # logClf = LogisticRegression()
    # model = VotingClassifier(estimators=[('rf',rfClf), ('svm',svmClf), ('log',logClf)], voting="soft")

    #Baggin
    model = BaggingClassifier(LogisticRegression(solver='lbfgs'), n_estimators = 500, oob_score = True)

    model.fit(X_train, y_train)
    y_true, y_pred = y_train, model.predict(X_train)
    response += str(model.oob_score_)
    response += str("")+"\n"
    response += str("Metrics on train's set")+"\n"
    response += str('precision on the test set: ') +str(precision_score(y_true, y_pred))+"\n"
    response += str('recall on the test set: ') +str(recall_score(y_true, y_pred))+"\n"
    response += str('accuracy on the test set: ') +str(accuracy_score(y_true, y_pred))+"\n"

    y_true, y_pred = y_cross, model.predict(X_cross)
    response += str("")+"\n"
    response += str("Metrics on cross' set")+"\n"
    response += str('precision on the test set: ') +str(precision_score(y_true, y_pred))+"\n"
    response += str('recall on the test set: ') +str(recall_score(y_true, y_pred))+"\n"
    response += str('accuracy on the test set: ') +str(accuracy_score(y_true, y_pred))+"\n"

    predictions = model.predict(X_test)


    output = pd.DataFrame({"PassengerId":test_data.PassengerId, "Survived":predictions})
    output.to_csv("my_submission_bagging.csv", index=False)
    response += str("Your submission was successfully saved!")
    return HttpResponse(response)
