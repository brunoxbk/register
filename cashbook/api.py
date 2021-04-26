from rest_framework.response import Response

from cashbook.models import Movement
from cashbook.serializers import MovementSerializer

from rest_framework import generics, status


class MovementList(generics.ListCreateAPIView):
    queryset = Movement.objects.all()
    serializer_class = MovementSerializer

    def get_queryset(self, **kwargs):
        return Movement.objects.filter(user=self.request.user)


class MovementDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Movement.objects.all()
    serializer_class = MovementSerializer
