from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpRequest, request
from django.http import QueryDict

import pandas as pd
import numpy as np
from sklearn.tree import DecisionTreeClassifier # Import Decision Tree Classifier
from sklearn.model_selection import train_test_split # Import train_test_split function
from sklearn import metrics

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
        elif "predict" in tab:
            print("predict operation")
            #jid = tab["joueur_id"] if "joueur_id" in tab else 0
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
            toTest = [shotC, stabC, deathC, deathBSGC, deathBPC, deathBSC, skipDC, dialogC, interactionC, phoneCC, lootC, tradeC, contactC, killerC, socializerC, sprintT, zoneT, restT, freezeT]
            #database
            JoueurDataSet = Joueur.objects
            X = []
            y = []

            print(JoueurDataSet.all())
            print(JoueurDataSet.all()[2].joueur_id)
            for joueur in JoueurDataSet.filter(emotion__gt = 0):
                inter = []
                inter.append(joueur.shotCounter)
                inter.append(joueur.stabCounter)
                inter.append(joueur.deathCounter)
                inter.append(joueur.deathByShotGunCounter)
                inter.append(joueur.deathByPoisonCounter)
                inter.append(joueur.deathBySuicideCounter)
                inter.append(joueur.skipDialogCounter)
                inter.append(joueur.dialogCounter)
                inter.append(joueur.interactionCounter)
                inter.append(joueur.phoneCallCounter)
                inter.append(joueur.lootCounter)
                inter.append(joueur.tradeCounter)
                inter.append(joueur.contactCounter)
                inter.append(joueur.killerCounter)
                inter.append(joueur.socializerCounter)
                inter.append(joueur.sprintTime)
                inter.append(joueur.zoneTime)
                inter.append(joueur.restTime)
                inter.append(joueur.freezeTime)
                X.append(inter)
                y.append([joueur.emotion])
            X = np.array(X)
            y = np.array(y)
            print(X)
            print(y)
            X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3)
            clf = DecisionTreeClassifier()
            clf = clf.fit(X_train, y_train)
            y_pred = clf.predict(X_test)
            print(X_test, y_pred)
            # Model Accuracy, how often is the classifier correct?
            print("Accuracy:", metrics.accuracy_score(y_test, y_pred))
            print("X_to_predict:", toTest)
            result = clf.predict([toTest])
            print("result:", result)
            response = result[0]
        else:
            print("nothing to do")
    elif request.method == "POST":
        response += "POOOOOST"
    return HttpResponse(response)
