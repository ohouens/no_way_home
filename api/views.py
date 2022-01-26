from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpRequest, request
from django.http import QueryDict

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

from .models import Joueur

def index(request):
    response = ""
    if request.method == "GET":
        # response += " " + str(HttpRequest.GET)
        tab = request.GET.dict()
        response += " " + str(tab)
        if "add" in tab:
            print("add operation")
            jid = tab["joueur_id"] if "joueur_id" in tab else 0
            shotC = tab["shotCounter"] if "shotCounter" in tab else 0
            stabC = tab["stabCounter"] if "stabCounter" in tab else 0
            deathC = tab["deathCounter"] if "deathCounter" in tab else 0
            deathBSGC = tab["deathByShotGunCounter"] if "deathByShotGunCounter" in tab else 0
            deathBPC = tab["deathByPoisonGunCounter"] if "deathByPoisonGunCounter" in tab else 0
            deathBSC = tab["deathBySuicideCounter"] if "deathBySuicideCounter" in tab else 0
            skipDC = tab["skipDialogCounter"] if "skipDialogCounter" in tab else 0
            dialogC = tab["dialogCounter"] if "dialogCounter" in tab else 0
            interactionC = tab["interactionCounter"] if "interactionCounter" in tab else 0
            phoneCC = tab["phoneCallCounter"] if "phoneCallCounter" in tab else 0
            lootC = tab["lootCounter"] if "lootCounter" in tab else 0
            tradeC = tab["tradeCounter"] if "tradeCounter" in tab else 0
            contactC = tab["contactCounter"] if "contactCounter" in tab else 0
            killerC = tab["killerCounter"] if "killerCounter" in tab else 0
            socializerC = tab["socializerCounter"] if "socializerCounter" in tab else 0
            sprintT = tab["sprintTime"] if "sprintTime" in tab else 0
            zoneT = tab["zoneTime"] if "zoneTime" in tab else 0
            restT = tab["restTime"] if "restTime" in tab else 0
            freezeT = tab["freezeTime"] if "freezeTime" in tab else 0
            label = tab["emotion"] if "emotion" in tab else 0

            j = Joueur(
                joueur_id = jid,
                shotCounter = shotC,
                deathCounter = deathC,
                deathByShotGunCounter = deathBSGC,
                deathByPoisonCounter = deathBPC,
                deathBySuicideCounter = deathBSC,
                skipDialogCounter = skipDC,
                dialogCounter = dialogC,
                interactionCounter = interactionC,
                phoneCallCounter = phoneCC,
                tradeCounter = tradeC,
                lootCounter = lootC,
                contactCounter = contactC,
                killerCounter = killerC,
                socializerCounter = socializerC,
                sprintTime = sprintT,
                zoneTime = zoneT,
                freezeTime = freezeT,
                restTime = restT,
                emotion = label
            )
            j.save()
            print(j.__dict__)
        elif "select" in tab:
            print("select operation")
        else:
            print("nothing to do")
    elif request.method == "POST":
        response += "POOOOOST"
    return HttpResponse(response)
