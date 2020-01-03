from rest_framework import serializers
from .models import languages
class languagesserializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model=languages
        fields=('id','url','name','paradigm')
