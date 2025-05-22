from rest_framework import viewsets
from apps.subscription.models import Responsible
from .serializers.responsible import ResponsibleSerializer


class ResponsibleViewSet(viewsets.ModelViewSet):
    queryset = Responsible.objects.all()
    serializer_class = ResponsibleSerializer
