from rest_framework import viewsets

from .serializers import DriverSerializer
from .models import Driver


class DriverViewSet(viewsets.ModelViewSet):
    queryset = Driver.objects.all().order_by('name')
    serializer_class = DriverSerializer




    