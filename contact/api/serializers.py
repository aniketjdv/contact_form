from rest_framework import serializers
from api.models import Contact_Enquriy


class ContactSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model=Contact_Enquriy
        fields='__all__'