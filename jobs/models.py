from django.db import models

#========= Create a Model For Job ========# 
class Jobs (models.Model):
    title = models.CharField(max_length=150)
    designation = models.CharField(max_length=50)

    #========= Set name for admin pannel ========# 
    def __str__(self):
        return self.title

