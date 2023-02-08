from .models import *
from rest_framework import serializers




class NewUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = NewUser
        fields = "__all__"

