from django.db import models
from datetime import date
# Create your models here.
# class User :
class User(models.Model) :
    nom = models.CharField(max_length=50),
    prenom = models.CharField(max_length=50),
    telephone = models.CharField(max_length = 50),
    email = models.EmailField(max_length = 50),
    def __str__(self) :
        return "nom :"+self.nom+" prenom "+self.prenom+" telephone "+self.telephone+" email "+self.email+" "
class Poste(models.Model) :
    image = models.ImageField(blank=True),
    type = models.IntegerField(default=0),
    date = models.DateField(default=date.today)
    users = models.ForeignKey(User ,on_delete=models.CASCADE)
    def __str__(self) :
        return "image "+self.image+" type"+self.type+" date "+self.date+""+self.users
# class Recommandation :
class Recommandation(Poste) :
    text = models.CharField(max_length=255)
    def __str__(self) :
        return "text "+self.text
# class Transport :
class Transport(Poste):
    depart = models.CharField(max_length=255)
    destination = models.CharField(max_length=255)
    heure_dep = models.TimeField()
    nbre_sieges = models.IntegerField()
    contactinfo = models.CharField(max_length=255)
    def __str__(self):
        return "Départ: "+self.depart+" Destination:"+self.destination+" Heure de départ:"+self.heure_dep+" nbre_sieges"+self.nbre_sieges+" contactinfo "+self.contactinfo+""
# class Logement :
class Logement(Poste):
    localisation = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    contactinfo = models.CharField(max_length=255)
    def __str__(self):
        return f"Logement - Localisation: {self.localisation}, Description: {self.description}"     
# class Stage : 
class Stage(Poste):
    typestg = models.IntegerField()
    societe = models.CharField(max_length=255)
    duree = models.IntegerField()
    sujet = models.CharField(max_length=255)
    contactinfo = models.CharField(max_length=255)
    specialite = models.CharField(max_length=255)
    def __str__(self):
        return "Stage - Type:"+ self.typestg +" Société: "+self.societe+" Durée: " +self.duree + " sujet "+self.sujet+" contact info "+self.contactinfo + "specilaiter " +self.specialite    
    
# class Evenement  :
class Evenement(Poste):
    intitule = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    lieu = models.CharField(max_length=255)
    contactinfo = models.CharField(max_length=255)
    def __str__(self):
        return f"Evenement - Intitulé: {self.intitule}, Lieu: {self.lieu} description {self.description} contact info {self.contactinfo}"    
#class EvenClub 
class EvenClub (Evenement)  :
    club = models.CharField(max_length=255)  
    def __str__(self) :
        return "club "+self.club+"" 
# class EvenSocial :
class EvenSocial(Evenement) :
    prix = models.FloatField()
    def __str__(self) :
        return "prix "+str(self.prix)+""     
# class Reaction :
class Reaction(models.Model) :
    comment = models.TextField(max_length=50),
    like = models.BooleanField(default = False),
    users = models.ForeignKey(User ,on_delete=models.CASCADE)
    post = models.ForeignKey(Poste , on_delete=models.CASCADE)
    def __str__(self) :
        return "Commentaire "+self.comment+" like"+self.like+" users "+self.users+""