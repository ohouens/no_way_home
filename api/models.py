from django.db import models

# Create your models here.
class Joueur(models.Model):
    #Emotion: {fun:1, frustrating;2, boring:3}
    joueur_id = models.IntegerField(default=0)
    shootCounter = models.IntegerField(default=0)
    deathCounter = models.IntegerField(default=0)
    deathByShotGunCounter = models.IntegerField(default=0)
    deathByPoisonCounter = models.IntegerField(default=0)
    deathBySuicideCounter = models.IntegerField(default=0)
    skipDialogCounter = models.IntegerField(default=0)
    phoneCallCounter = models.IntegerField(default=0)
    contactCounter = models.IntegerField(default=0)
    killerCounter = models.IntegerField(default=0)
    socializerCounter = models.IntegerField(default=0)
    sprintTime = models.IntegerField(default=0)
    zoneTime = models.IntegerField(default=0)
    restTime = models.IntegerField(default=0)
    emotion = models.IntegerField(default=0)
