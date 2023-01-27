from django.db import models

class Borough(models.Model):
    name=models.CharField("Name",max_length=254)
    def __str__(self) -> str:
        return self.name


class MutualAid(models.Model):
    borough=models.ForeignKey(Borough,on_delete=models.CASCADE)
    name=models.CharField("Name",max_length=254)
    category=models.CharField("Category",max_length=254)
    website=models.URLField("Website",max_length=254)
    email=models.EmailField("Email",max_length=254)

    def __str__(self) -> str:
        return self.name



