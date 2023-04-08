from django.db import models

class beitrag(models.Model):
    titel = models.CharField(max_length=100)
    beitrag = models.CharField(max_length=500)

    def __str__(self) -> str:
        return self.titel
