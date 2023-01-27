from rest_framework import serializers
from .models import MutualAid,Borough


class BoroughSerializer(serializers.ModelSerializer):
    class Meta:
        model=Borough
        fields = ('name')


class MutualaidSerializer(serializers.ModelSerializer):
    class Meta:
        model:MutualAid
        fields=('borough','name','category','website','email')