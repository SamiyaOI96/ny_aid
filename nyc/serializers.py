from rest_framework import serializers
from .models import MutualAid,Borough


class BoroughSerializer(serializers.ModelSerializer):
    class Meta:
        model=Borough
        fields = '__all__'
        
        


class MutualaidSerializer(serializers.ModelSerializer):
    #url = serializers.CharField(source='get_absolute_url', read_only=True)
    borough_name = serializers.CharField(source='borough.name', read_only=True)
    
    # def get_borough_name(self):
    #     return self.borough.name

    class Meta:
        model=MutualAid
        fields=('borough_name','borough','name','category','website','email')
        fields='__all__'
        #read_only_fields=['id','category']



        # def __init__(self,borough,name,category,website,email,created=None):
        #     self.borough=borough
        #     self.name=name
        #     self.category=category
        #     self.website=website
        #     self.email=email

        