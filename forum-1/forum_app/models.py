from django.db import models
from django.contrib.auth.models import User

class beitrag(models.Model):
    titel = models.CharField(max_length=100)
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    beitrag = models.CharField(max_length=500)
    def __str__(self):
        return self.titel + ' | ' + str(self.author)
    
class comment(models.Model):
    beitrag = models.ForeignKey(beitrag, related_name="comments", on_delete=models.CASCADE)
    
    body = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    def __str__(self) ->str:
        return '%s - %s' % (self.beitrag.titel, self.author)

class register(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.user.username
