from rest_framework import generics
from .models import subnetmodel
from .serializers import subnetserializer

class subnetzoneview(generics.ListCreateAPIView):
    queryset = subnetmodel.objects.all()
    serializer_class = subnetserializer
