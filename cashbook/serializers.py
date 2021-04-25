
from cashbook.models import Movement
from rest_framework import serializers


class MovementSerializer(serializers.ModelSerializer):

    class Meta:
        model = Movement
        fields = [
            'id', 'user', 'close', 'kind',
            'date', 'description', 'received_date', 'value']
