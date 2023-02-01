from django.db import models
#from django_model_mixins import mixins

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

    def __str__(self)->str:
        return self.name



    # def ma_dict(self):
    #     ma_dict={
    #         'id':self.id,
    #         'borough':self.borough,
    #         'name':self.name,
    #         'category':self.category,
    #         'website':self.website,
    #         'email':self.email
    #     }


