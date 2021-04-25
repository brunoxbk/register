from rest_framework.response import Response

from cashbook.models import Movement
from cashbook.serializers import MovementSerializer

from rest_framework import generics, status


class MovementList(generics.ListCreateAPIView):
    queryset = Movement.objects.all()
    serializer_class = MovementSerializer


class MovementDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Movement.objects.all()
    serializer_class = MovementSerializer