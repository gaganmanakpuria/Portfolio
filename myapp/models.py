from django.db import models

# Create your models here.
class contact(models.Model):
    name= models.CharField(max_length=250)
    email= models.EmailField()
    subject= models.CharField(max_length=250)
    message= models.TextField()

    def __str__(self):
        return self.name

class Hightlight(models.Model):
    hl=models.CharField(max_length=250)
    def __str__(self):
        return self.hl

class Hobbies(models.Model):
    hobby=models.CharField(max_length=250)
    def __str__(self):
        return self.hobby

class project(models.Model):
    name=models.CharField(max_length=250)
    frontend= models.CharField(max_length=250)
    backend = models.CharField(max_length=250)
    discripition= models.TextField()
    def __str__(self):
       return self.name
    

class skills(models.Model):
    skill= models.CharField(max_length=250)
    def __str__(self):
        return self.skill
class about_you(models.Model):
    desc = models.TextField()
    def __str__(self):
        return self.desc
class Personal_info(models.Model):
    date_birth = models.DateField()
    gender_Marital_Status = models.CharField(max_length=250)
    language = models.CharField(max_length=250)
    def __str__(self):
        return self.gender_Marital_Status 
class profile(models.Model):
    img=models.ImageField(upload_to="Profile/")

    