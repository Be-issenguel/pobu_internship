from rest_framework import serializers
from apps.subscription.models import Responsible

class ResponsibleSerializer(serializers.ModelSerializer):

    class Meta:
        model = Responsible
        fields = '__all__'
