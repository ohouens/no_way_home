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

def index(request):
    reponse = "new thing"
    return HttpResponse(response)
